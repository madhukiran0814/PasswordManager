import logging
import random
import smtplib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from cryptography.fernet import Fernet
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from bson.objectid import ObjectId
from modules.databases.mongo import mongo_conn
from modules.manager.services.constants import *
from modules.app.config import settings
pm_db = mongo_conn['pm_db']

logging = logging.getLogger('logger')


# User registration Function
async def register_user(user_data: dict):
    collection = pm_db["users"]
    # Insert user into MongoDB
    if user_data['pin_type'] == "common":
        user_data["pin"] = password_options_[random.randrange(0, len(password_options_)-1)]
    user_data["date_of_birth"] = str(user_data["date_of_birth"])
    result = collection.insert_one(user_data)
    return result.inserted_id


def generate_key():
    return Fernet.generate_key()


def encrypt_password(message, key):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode('utf-8'))
    return encrypted_message


def decrypt_password(encrypted_message, key):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode('utf-8')
    return decrypted_message


def encrypt_password_client(password, token):
    # Convert password and token to bytes
    password_bytes = password.encode('utf-8')
    token_bytes = token.encode('utf-8')
    cipher = AES.new(token_bytes, AES.MODE_ECB)
    padded_password = pad(password_bytes, 16)
    encrypted_password = cipher.encrypt(padded_password)
    return encrypted_password


def decrypt_password_client(encrypted_password, token):
    # Convert the token to bytes
    token_bytes = token.encode('utf-8')
    cipher = AES.new(token_bytes, AES.MODE_ECB)
    decrypted_password = cipher.decrypt(encrypted_password)
    unpad_pass = unpad(decrypted_password, 16)
    return unpad_pass.decode('utf-8')


async def store_password(pwd_data: dict):
    collection = pm_db["passwords"]
    # Insert password into MongoDB
    if pwd_data['client_key']:
        if len(pwd_data['key']) < 16:
            pwd_data['key'] += 'z'*(16 - len(pwd_data['key']))
        pwd_data['password'] = encrypt_password_client(pwd_data['password'], pwd_data['key'])
        pwd_data['key'] = False
    else:
        key = generate_key()
        pwd_data['key'] = key
        pwd_data['password'] = encrypt_password(pwd_data['password'], key)
    result = collection.insert_one(pwd_data)
    return result.inserted_id


def validate_pin(pwd_type, saved_pwd, cur_pwd, date_of_birth):
    if pwd_type == 'common':
        obj = {}
        now = datetime.now()
        obj['hour'] = str(now.strftime("%I"))
        obj['min'] = str(now.strftime("%M"))
        obj['hour24'] = str(now.hour)
        obj['year'] = date_of_birth.split('-')[0]
        obj['month'] = date_of_birth.split('-')[1]
        obj['day'] = date_of_birth.split('-')[-1]
        pwd_str1 = ''
        pwd_str2 = ''
        for st in saved_pwd.split(','):
            if st == 'hour':
                pwd_str1 += obj['hour']
                pwd_str2 += obj['hour24']
            else:
                pwd_str1 += obj.get(st)
                pwd_str2 += obj.get(st)
        return cur_pwd in [pwd_str2, pwd_str1]
    else:
        return saved_pwd == cur_pwd


async def get_password(pwd_data: dict):
    usr_collection = pm_db["users"]
    pwd_connection = pm_db["passwords"]
    record = usr_collection.find_one({"_id": ObjectId(pwd_data['user_id'])})
    if not record.get('is_active'):
        return {"status_code": 403, "details": "Account locked, Please reset the pin"}
    if not validate_pin(record['pin_type'], record['pin'], pwd_data['pin'], record['date_of_birth']):
        return {"status_code": 400, "details": "Authentication failed, Wrong Pin"}
    pwd_record = pwd_connection.find_one({"_id": ObjectId(pwd_data['password_id'])})
    if pwd_data['client_key'].lower() == 'false':
        password = decrypt_password(pwd_record.get('password'), pwd_record.get('key'))
    else:
        try:
            key = pwd_data['client_key']
            if len(key) < 16:
                key += 'z'*(16 - len(key))
            password = decrypt_password_client(pwd_record.get('password'), key)
        except ValueError as e:
            return {"status_code": 400, "details": "Wrong API Key"}
    return {"status_code": 200, "details": "Password fetched successfully", "password": password}


def get_all_passwords(user_id):
    pwd_connection = pm_db["passwords"]
    records = pwd_connection.find({"user_id": user_id}, {"user_id": 0, "key": 0, "password": 0})
    all_records = []
    for record in records:
        record["_id"] = str(record["_id"])
        all_records.append(record)
    if all_records:
        return {"status_code": 200, "details": "Passwords fetched successfully", "passwords": all_records}
    return {"status_code": 200, "details": "No passwords found", "passwords": []}


def generate_otp():
    """Generates a random OTP of the specified length."""
    otp = random.randint(1000, 9999)
    return otp


def send_mail(email_address, template, name="user", pin="None", sequence=None):
    """Sends the generated OTP to the specified email address."""
    smtp_server = settings.SMTP_SERVER   # Replace with the SMTP server address
    smtp_port = settings.SMTP_PORT  # Replace with the SMTP server port
    sender_email = settings.SMTP_MAIL
    sender_password = settings.SMTP_PASSWORD
    otp = False
    subject = "Security Pin"
    message_template = ""
    if template == "otp_message_template":
        otp = generate_otp()
        subject = "Your OTP"
        message_template = otp_message_template.format(otp)
    elif template == "reset_pin_custom_template":
        message_template = reset_pin_custom_template.format(name, pin)
    elif template == 'reset_pin_common_template':
        message_template = reset_pin_common_template.format(name, sequence, pin)
    try:
        # Create a multipart message and set the headers manually
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = email_address
        msg["Subject"] = subject

        # Attach the HTML message to the email
        msg.attach(MIMEText(message_template, "html"))
        try:
            # Connect to the SMTP server and send the email
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.send_message(msg)
                logging.info(f"OTP has been sent to {email_address}")
                if otp:
                    return {"status_code": 200, "details": "OTP sent successfull", "otp": otp}
                return {"status_code": 200, "details": "Mail successfully sent"}
        except Exception as e:
            logging.info('exception while sending OTP', e)
            return {"status_code": 400, "details": "Authentication Error for mail"}
    except Exception as e:
        logging.info(f"An error occurred while sending the OTP: {str(e)}")
        return {"status_code": 500, "details": "Internal Server Error"}


def create_temp_pin(sequence):
    obj = {
        "min": "30",
        "hour": "01",
        "day": "08",
        "year": "2002",
        "month": "05",
        "hour24": "13"
    }
    pwd_str1 = ""
    pwd_str2 = ""
    for st in sequence.split(','):
        if st == 'hour':
            pwd_str1 += obj['hour']
            pwd_str2 += obj['hour24']
        else:
            pwd_str1 += obj.get(st)
            pwd_str2 += obj.get(st)
    return pwd_str1+" , "+pwd_str2


def login(email):
    usr_collection = pm_db["users"]
    record = usr_collection.find_one({"email": email})
    if record:
        return send_mail(email, template="otp_message_template")
    else:
        return {"status_code": 400, "details": "User doesn't exist"}


def send_pin(user_id):
    usr_collection = pm_db["users"]
    record = usr_collection.find_one({"_id": ObjectId(user_id)})
    pin_type = record.get('pin_type')
    sequence = record.get('pin')
    if pin_type == 'common':
        pin = create_temp_pin(sequence)
        return send_mail(record.get('email'), 'reset_pin_common_template', record.get('first_name'), pin, sequence)
    else:
        return send_mail(record.get('email'), 'reset_pin_custom_template', record.get('first_name'), sequence)


def update_password(pwd_data: dict):
    try:
        collection = pm_db["passwords"]
        usr_collection = pm_db['users']
        record = usr_collection.find_one({"_id": ObjectId(pwd_data['user_id'])})
        if not validate_pin(record['pin_type'], record['pin'], pwd_data['pin'], record['date_of_birth']):
            return {"status_code": 400, "details": "Authentication failed, Wrong Pin"}
        # Insert password into MongoDB
        if pwd_data['client_key'].lower() != 'false':
            if len(pwd_data['client_key']) < 16:
                pwd_data['client_key'] += 'z'*(16 - len(pwd_data['client_key']))
            new_password = encrypt_password_client(pwd_data['password'], pwd_data['client_key'])
            new_key = False
        else:
            new_key = generate_key()
            new_password = encrypt_password(pwd_data['password'], new_key)
        query = {"_id": ObjectId(pwd_data['password_id'])}
        update = {"$set": {"password": new_password, "key": new_key}}
        collection.update_one(query, update)
        return {"status_code": 200, "details": "Successfully Updated"}
    except Exception as e:
        return {"status_code": 402, "details": "Unable to Process"}
        logging.error("error : %s", e)


def delete_one_password(pwd_id):
    collection = pm_db["passwords"]
    collection.delete_one({"_id": ObjectId(pwd_id)})
    return {"status_code": 200, "details": "Successfully deleted"}


def delete_user(user_id):
    collection = pm_db["users"]
    pwd_collection = pm_db["passwords"]
    collection.delete_one({"_id": ObjectId(user_id)})
    pwd_collection.delete_many({"user_id": user_id})
    return {"status_code": 200, "details": "Successfully deleted"}