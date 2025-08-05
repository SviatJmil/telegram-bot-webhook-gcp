from fastapi import APIRouter, Request
from telegram import Update as TgUpdate, Bot
from app.config import settings
import logging
import json
from app.utils import fetch_html, extract_titles

router = APIRouter()
logger = logging.getLogger("webhook")
BOT_TOKEN = settings.TELEGRAM_BOT_TOKEN  # додаєш у .env
bot = Bot(token=BOT_TOKEN)

WEBHOOK_SECRET = settings.WEBHOOK_SECRET_URL_PART

prev_message = ''

@router.post(f"/webhook/{WEBHOOK_SECRET}", status_code=200)
async def handle_webhook(request: Request):
    body_bytes = await request.body()
    body_dict = json.loads(body_bytes)

    # Telegram Update з python-telegram-bot
    update = TgUpdate.de_json(body_dict, bot=None)  # bot=None, бо не потрібен для парсингу

    if update.message and update.message.text:
        chat_id = update.message.chat.id
        user_message = update.message.text

        if user_message and user_message.lower() == 'ping':
            global prev_message
            if prev_message and prev_message.lower() == 'ping':
                prev_message = user_message
                await bot.send_message(chat_id=chat_id, text=f"pong.. pong, bro")
                return {"status": "ok"}
            
            prev_message = user_message
            await bot.send_message(chat_id=chat_id, text=f"pong")
            return {"status": "ok"}

        message = ''

        url = "https://www.aljazeera.com/news"
        html = fetch_html(url)
        titles = extract_titles(html)

        message += "The Latest aljazeera News: \n"
        for i, title in enumerate(titles, 1):
            message += f"{i}. {title}\n"

        url = "https://www.nytimes.com/section/world"
        html = fetch_html(url)
        titles = extract_titles(html)

        message += "\nThe Latest nytimes News: \n"
        for i, title in enumerate(titles, 1):
            message += f"{i}. {title}\n"
        
        # Відправка відповіді
        await bot.send_message(chat_id=chat_id, text=f"You said: {message}")

    return {"status": "ok"}
