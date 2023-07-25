from fastapi import FastAPI, APIRouter, HTTPException
from modules.manager.services.services import *
from modules.databases.models import *

# API router
router = APIRouter()


@router.post("/send-otp", status_code=200)
async def send_otp(email_json: dict):
    # Convert user object to dictionary
    otp_dic = send_mail(email_json.get('email'), template="otp_message_template")
    if otp_dic.get('status_code') != 200:
        raise HTTPException(status_code=otp_dic.get('status_code'), detail=otp_dic.get('details'))
    # Return the success json
    return otp_dic


@router.post("/get-passwords", status_code=200)
async def get_passwords(user_json: dict):
    # Convert user object to dictionary
    pass_dic = get_all_passwords(user_json.get('user_id'))
    return pass_dic


@router.post("/show-password", status_code=200)
async def show_pwd(password: ShowPassword):
    # Convert user object to dictionary
    password_data = password.dict()
    pwd_dic = await get_password(password_data)
    if pwd_dic.get('status_code') != 200:
        raise HTTPException(status_code=pwd_dic.get('status_code'), detail=pwd_dic.get('details'))
    # Return the success json
    return pwd_dic


@router.post("/store-password", status_code=200)
async def show_password(password: Password):
    try:
        # Convert user object to dictionary
        password_data = password.dict()
        pwd_id = await store_password(password_data)
        # Return the inserted user ID
        return {"message": "Password stored successfully", "password_id": str(pwd_id)}
    except Exception as e:
        logging.error("error while processing record %s", e)
        raise HTTPException(status_code=500, detail="Internal server error") from e


@router.post("/register", status_code=201)
async def register(user: User):
    try:
        # Convert user object to dictionary
        user_data = user.dict()
        reg_id = await register_user(user_data)
        # Return the inserted user ID
        return {"message": "User registered successfully", "user_id": str(reg_id)}
    except Exception as e:
        logging.error("error while processing record %s", e)
        raise HTTPException(status_code=500, detail="Internal server error") from e


@router.post("/reset-pin", status_code=201)
async def reset_pin(user_id: dict):
    try:
        # Convert user object to dictionary
        mail_dic = send_pin(user_id.get('user_id'))
        # Return the inserted user ID
        if mail_dic.get('status_code') != 200:
            raise HTTPException(status_code=mail_dic.get('status_code'), detail=mail_dic.get('details'))
        # Return the success json
        return mail_dic
    except Exception as e:
        logging.error("error while processing request %s", e)
        raise HTTPException(status_code=500, detail="Internal server error") from e


@router.post("/update-password", status_code=201)
async def update_one_password(pass_data: UpdatePassword):
    # Convert user object to dictionary
    pass_data = pass_data.dict()
    # Return the inserted user ID
    new_password = update_password(pass_data)
    if new_password.get('status_code') != 200:
        raise HTTPException(status_code=new_password.get('status_code'), detail=new_password.get('details'))
    # Return the success json
    return new_password


@router.post('/login', status_code=200)
async def login_user(email_dic: dict):
    login_dic = login(email_dic.get('email'))
    if login_dic.get('status_code') != 200:
        raise HTTPException(status_code=login_dic.get('status_code'), detail=login_dic.get('details'))
    return login_dic


@router.delete("/delete-password", status_code=200)
async def delete_password(pwd_json: dict):
    # Convert user object to dictionary
    pass_dic = delete_one_password(pwd_json.get('password_id'))
    return pass_dic


@router.delete("/delete-user", status_code=200)
async def delete_account(user_json: dict):
    # Convert user object to dictionary
    user_dic = delete_user(user_json.get('user_id'))
    return user_dic
