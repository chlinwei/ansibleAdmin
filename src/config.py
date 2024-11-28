import os 
from pydantic_settings import BaseSettings
from pydantic import BaseModel
class LoggerSetting(BaseModel):
    LOG_DIR:str = "./logs"
    LOG_LEVEL:str = "DEBUG"

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    # FRONTEND_HOST: str = "http://localhost:5173"

    PROJECT_NAME: str = "ansibleAdmin"
    DATA_DIR:str = "."
    loggerSetting:LoggerSetting  = LoggerSetting()
    @property
    def DB_URL(self) -> str:
        return f"sqlite:///{self.DATA_DIR}/sql_app.db"
    PORT:int = 8080



settings = Settings()  # type: ignore