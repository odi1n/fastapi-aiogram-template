from pydantic import BaseSettings, validator


class Settings(BaseSettings):
    # Setting project
    DEBUG = True

    SECRET_KEY: str
    ALGORITHM = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES = 30  # через сколько истекает токен

    ADMIN = 1459259424

    TIMEZONE = "Asia/Samarkand"

    # DB Connect
    DB_URL: str

    # Bot
    BOT_TOKEN: str
    # Link service. example: ngrok
    HOST: str

    WEBHOOK_PATH: str = None
    WEBHOOK_URL: str = None

    @validator("WEBHOOK_PATH")
    def weebhook_path(cls, v, values: dict) -> str:
        return f"/bot/{values.get('BOT_TOKEN')}"

    @validator("WEBHOOK_URL")
    def weebhook_url(cls, v, values: dict) -> str:
        return f'{values.get("HOST")}/api{values.get("WEBHOOK_PATH")}'

settings = Settings(_env_file=".env")

TORTOISE_ORM = {
    "connections": {"default": settings.DB_URL},
    "apps": {
        "models": {
            "models": ["app.db.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
