from pydantic import BaseSettings

class Settings(BaseSettings):
    HOST:str = 'http://127.0.0.1:8000'
    DETA_PROJECT_KEY:str = Field(..., env='DETA_PROJECT_KEY')
    DETA_BASE_NAME:str = 'links'


setting = Settings()
