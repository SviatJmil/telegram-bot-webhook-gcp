from fastapi import FastAPI
from app.webhook_router import router
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

app = FastAPI(title="Webhook FastAPI Server")

app.include_router(router)
