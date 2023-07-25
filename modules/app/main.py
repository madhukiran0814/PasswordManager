from logging.config import dictConfig
from modules.app.log_config import log_config
from fastapi import Depends
from modules.app.application import get_application, authenticate
from modules.manager.v1 import router

dictConfig(log_config)
app = get_application()


app.include_router(router, prefix='/api', tags=["Api's"]
                   , dependencies=[Depends(authenticate)]
                   )
