from flask import Flask
from .settings.config import Config
from .settings.extensions import db, migrate, auth_basic

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    auth = auth_basic()

    try:
        from .routes import register_routes
        register_routes(app)
        
        
        # Import models
        from src.models.aplis_request_model import AplisRequest
        from src.models.shift_order_model import ShiftOrder
        from src.models.audit_log_model import AuditLog
        from src.models.webhook_event_model import WebhookEvent
        from src.models.integration_log_model import IntegrationLog
        
    except Exception:
        pass

    return app
