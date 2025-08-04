from fastapi import APIRouter, Request
from telegram import Update as TgUpdate, Bot
from app.config import settings
import logging
import json
from datetime import datetime

router = APIRouter()
logger = logging.getLogger("webhook")
BOT_TOKEN = settings.TELEGRAM_BOT_TOKEN  # додаєш у .env
bot = Bot(token=BOT_TOKEN)

WEBHOOK_SECRET = settings.WEBHOOK_SECRET_URL_PART

@router.post(f"/webhook/{WEBHOOK_SECRET}", status_code=200)
async def handle_webhook(request: Request):
    body_bytes = await request.body()
    body_dict = json.loads(body_bytes)

    # Telegram Update з python-telegram-bot
    update = TgUpdate.de_json(body_dict, bot=None)  # bot=None, бо не потрібен для парсингу

    received_at = datetime.utcnow()
    logger.info(f"Telegram webhook received at {received_at.isoformat()}")
    logger.info(f"Update ID: {update.update_id}")


    if update.message and update.message.text:
        chat_id = update.message.chat.id
        user_message = update.message.text
        logger.info(f"Message text: {user_message}")
        logger.info(f"BOT_TOKEN: {BOT_TOKEN}")
        
        # Відправка відповіді
        bot.send_message(chat_id=chat_id, text=f"You said: {user_message}")

    return {"status": "ok"}
