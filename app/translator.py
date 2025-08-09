from google.cloud import translate_v2 as translate
import asyncio
import logging
# from app.config import settings
# from google.oauth2 import service_account
# import os

logger = logging.getLogger("webhook")

# SERVICE_ACCOUNT_FILE = settings.GOOGLE_APPLICATION_CREDENTIALS
# SCOPES = ["https://www.googleapis.com/auth/cloud-translation"]

# if SERVICE_ACCOUNT_FILE and os.path.exists(SERVICE_ACCOUNT_FILE):
#     credentials = service_account.Credentials.from_service_account_file(
#         SERVICE_ACCOUNT_FILE, scopes=SCOPES
#     )
#     client = translate.Client(credentials=credentials)
# else:
client = translate.Client()

async def translate_text_async(text: str, target_lang: str = "uk") -> str:
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, translate_text, text, target_lang)

def translate_text(text: str, target_lang: str = "uk") -> str:
    try:
        result = client.translate(text, target_language=target_lang)
        return result.get("translatedText", text)
    except Exception as e:
        logger.error(f"Translation failed: {e}", exc_info=True)
        return text
