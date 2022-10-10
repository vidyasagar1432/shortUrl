from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    HOST:str = 'https://bitly.deta.dev'
    DETA_PROJECT_KEY:str = Field(..., env='DETA_PROJECT_KEY')
    DETA_BASE_NAME:str = 'links'


setting = Settings()
