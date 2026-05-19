from datetime import datetime

from src.settings.extensions import db


class WebhookEvent(db.Model):

    __tablename__ = "webhook_events"

    id = db.Column(db.Integer, primary_key=True)

    source = db.Column(
        db.String(50)
    )

    event_type = db.Column(
        db.String(100)
    )

    payload = db.Column(
        db.JSON
    )

    processed = db.Column(
        db.Boolean,
        default=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )