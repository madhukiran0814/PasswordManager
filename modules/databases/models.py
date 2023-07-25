from datetime import date
from pydantic import BaseModel, validator
from typing import Optional


# User model
class User(BaseModel):
    first_name: str
    last_name: Optional[str]
    email: str
    date_of_birth: date
    pin_type: str
    pin: Optional[str] = False
    is_active: Optional[bool] = True

    @validator("pin_type")
    def validate_password_type(cls, pin_type):
        if pin_type not in ["common", "custom"]:
            raise ValueError("Invalid pin_type")
        return pin_type


class Password(BaseModel):
    user_id: str
    name: str
    description: Optional[str] = ""
    password: str
    client_key: bool = False
    key: Optional[str] = False


class ShowPassword(BaseModel):
    user_id: str
    password_id: str
    pin: str
    client_key: Optional[str] = False


class UpdatePassword(BaseModel):
    user_id: str
    password_id: str
    pin: str
    password: str
    client_key: Optional[str] = False