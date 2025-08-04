from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime

class WebhookPayload(BaseModel):
    event: str
    data: Dict
    received_at: Optional[datetime] = None
