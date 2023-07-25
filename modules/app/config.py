# -*- coding: utf-8 -*-
from pydantic import BaseSettings


class Settings(BaseSettings):
    """ Global Variables in order to use anywhere in app"""
    PROJECT_NAME: str
    PROJECT_VERSION: float
    PROJECT_TERMS_OF_SERVICE: str
    X_API_KEY: str
    MONGO_URL: str
    SMTP_SERVER: str
    SMTP_PORT: int
    SMTP_MAIL: str
    SMTP_PASSWORD: str

    class Config:
        """ Assigned by taking the values from .env file in local"""
        case_sensitive = True
        env_file = ".env"


settings = Settings()
