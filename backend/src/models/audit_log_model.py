from datetime import datetime

from src.settings.extensions import db


class AuditLog(db.Model):

    __tablename__ = "audit_logs"

    id = db.Column(db.Integer, primary_key=True)

    user = db.Column(
        db.String(255)
    )

    action = db.Column(
        db.String(255)
    )

    description = db.Column(
        db.Text
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )