from datetime import datetime

from src.settings.extensions import db


class AplisRequest(db.Model):

    __tablename__ = "aplis_requests"

    id = db.Column(db.Integer, primary_key=True)

    shift_order_id = db.Column(
        db.Integer,
        db.ForeignKey("shift_orders.id"),
        nullable=False
    )

    aplis_request_code = db.Column(
        db.String(100),
        unique=True
    )

    status = db.Column(
        db.String(50),
        default="SENT"
    )

    response_payload = db.Column(
        db.JSON
    )

    pdf_base64 = db.Column(
        db.Text
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    shift_order = db.relationship(
        "ShiftOrder",
        backref="aplis_requests"
    )