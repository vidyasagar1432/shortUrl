from pydantic import BaseSettings

class Settings(BaseSettings):
    HOST:str = 'http://127.0.0.1:8000'
    DETA_PROJECT_KEY:str
    DETA_BASE_NAME:str = 'links'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

setting = Settings(_env_file='.env')