from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)



db = SQLAlchemy()
migrate = Migrate()

db.init_app(app)
migrate.init_app(app, db)

csrf = CSRFProtect(app)

CORS(app)

from app import views