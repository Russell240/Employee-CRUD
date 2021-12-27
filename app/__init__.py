# app/__init__.py

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
# local imports
from config import app_config
import mysql.connector

# db variable initialization
app = Flask(__name__)
db = SQLAlchemy()

login_manager = LoginManager()

@app.route('/home')
def helloIndex():
    return 'Hello World from Python Flask!'
@app.route('/l')
def create_app(config_name='development'):
    app = Flask(__name__, instance_relative_config=True)
    #app.config.from_object(Config)
    app.config.from_object(["development"])
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://flahe:password@ 127.00.1:59536/employees'
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('..\config.py')
    
     # temporary route
    login_manager.init_app(app) 
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"
    migrate= Migrate(app, db)
    db.init_app(app)
    from app import models
    
    """ from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')"""

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    
    return app
    
    