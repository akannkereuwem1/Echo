from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

# initialize extensions (create objects first so models can import them)
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager(app)
login.login_view = 'login' #'login' is the function name for the login view


db.init_app(app)
migrate.init_app(app, db)

from app import routes, models, errors
