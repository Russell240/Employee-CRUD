# app/__init__.py

# third-party imports
from flask import Flask, config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.config.config import APP_CONFIG

from flask_migrate import Migrate

# local imports
from config import Config

# db variable initialization
app = Flask(__name__)
db = SQLAlchemy()


login_manager = LoginManager()

@app.route('/home')
def helloIndex():
    return 'Hello World from Python Flask!'
@app.route('/home')
def create_app():
    app = Flask(__name__, instance_relative_config=True)
    #app.config.from_object(Config)
    app.config.from_object(APP_CONFIG["development"])
   
    
    db.init_app(app)
     # temporary route
    login_manager.init_app(app) 
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"
    migrate= Migrate(app, db)
    from app import models
    
    return app
    
    