from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    root_directory: str='examples'
    host: str='localhost'
    port: int=8501
    
    # model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


config = Settings()