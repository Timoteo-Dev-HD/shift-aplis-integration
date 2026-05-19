from datetime import datetime

from src.settings.extensions import db

class ShiftOrder(db.Model):

    __tablename__ = "shift_orders"

    id = db.Column(db.Integer, primary_key=True)

    shift_order_id = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    patient_name = db.Column(
        db.String(255),
        nullable=False
    )

    patient_document = db.Column(
        db.String(50)
    )

    doctor_name = db.Column(
        db.String(255)
    )

    insurance_name = db.Column(
        db.String(255)
    )

    status = db.Column(
        db.String(50),
        default="PENDING"
    )

    raw_payload = db.Column(
        db.JSON
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )