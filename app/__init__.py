from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config_options

loginManager = LoginManager()
loginManager.session_protection = 'strong'
loginManager.login_view = 'auth.login'

db = SQLAlchemy()





def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_options[config_name])


    db.init_app(app)
    loginManager.init_app(app)



    return app


