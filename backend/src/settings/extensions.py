from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_httpauth import HTTPBasicAuth

db = SQLAlchemy()
migrate = Migrate()
auth_basic = HTTPBasicAuth()
