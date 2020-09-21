from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config_options

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

db = SQLAlchemy()





def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_options[config_name])


    db.init_app(app)
    login_manager.init_app(app)


    #setting config
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


