from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = "Мой первый проект"
    db_user: str
    db_password: str
    db_host: str
    db_port: str = "5432"
    db_name: str

    class Config:
        env_file = ".env"


settings = Settings()
