from fastapi import APIRouter
from app.models import WebhookPayload
from app.config import settings
import logging
from datetime import datetime

router = APIRouter()
logger = logging.getLogger("webhook")

WEBHOOK_SECRET = settings.WEBHOOK_SECRET_URL_PART

@router.post(f"/webhook/{WEBHOOK_SECRET}", status_code=200)
async def handle_webhook(
    payload: WebhookPayload
):
    payload.received_at = datetime.utcnow()
    logger.info(f"Webhook received: {payload.event}, time: {payload.received_at}, data: {payload.data}")

    return {"status": "ok", "received": payload.event}
