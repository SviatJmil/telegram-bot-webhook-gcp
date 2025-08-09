from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Локально завантажує .env (продакшен ігнорує, якщо нема .env)
load_dotenv()

class Settings(BaseSettings):
    APP_NAME: str = "Telegram Bot Webhook Server"
    WEBHOOK_SECRET_URL_PART: str
    TELEGRAM_BOT_TOKEN: str
    #GOOGLE_APPLICATION_CREDENTIALS: str
    
    class Config:
        env_file = ".env"  # .env файл буде використовуватись локально, у проді змінні з ENV

settings = Settings()
