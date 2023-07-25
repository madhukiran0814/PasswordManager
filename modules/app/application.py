from fastapi import FastAPI, Header, HTTPException
from modules.app.config import settings
from fastapi.middleware.cors import CORSMiddleware


def get_application():

    """Returns the Fatsapi Object with specific configuration [CORS Enabled]"""

    _app = FastAPI(
        title=settings.PROJECT_NAME,
        description="Password Manager Backend API's",
        version=settings.PROJECT_VERSION,
        terms_of_service="https://www.password_manager.com/terms-and-conditions/",
        openapi_url="/api/v1/openapi.json",
        swagger_ui_parameters={"defaultModelsExpandDepth": -1}
    )

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:8000", "https://localhost:8000",
                        "http://localhost", "https://localhost"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


def authenticate(x_api_key: str = Header(default=None)):
    """ To Aunthenticate the individual recieved request"""
    if not x_api_key or x_api_key != settings.X_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
