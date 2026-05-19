from datetime import datetime

from src.settings.extensions import db


class IntegrationLog(db.Model):

    __tablename__ = "integration_logs"

    id = db.Column(db.Integer, primary_key=True)

    system = db.Column(
        db.String(50)
    )

    action = db.Column(
        db.String(100)
    )

    status = db.Column(
        db.String(50)
    )

    message = db.Column(
        db.Text
    )

    payload = db.Column(
        db.JSON
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )