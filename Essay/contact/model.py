import reflex as rx
from sqlmodel import Field
from datetime import datetime, timezone

import sqlalchemy

def get_utc_now() -> datetime:
    return datetime.now(timezone.utc)

class ContactDataModel(rx.Model, table=True):
    first_name: str
    last_name: str | None = None
    email: str | None = None
    text: str
    created_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'server_default': sqlalchemy.func.now()
        }
    )