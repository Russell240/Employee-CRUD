# app/__init__.py

# third-party imports
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
# local imports
from config import app_config
import mysql.connector

# db variable initialization
app = Flask(__name__ ,template_folder='../templates' ,static_folder='../static')
db = SQLAlchemy()

login_manager = LoginManager()

@app.route('/home')
def helloIndex():
    return render_template('home/index.html')
@app.route('/index')
def create_app(config_name='development'):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(["development"])
    app.config['FLASK_ENV'] = 'development'
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://flahe:password@ 127.00.1:59536/employees'
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('C:\\development\\technifist\\Employee CRUD\config.py')
    
   
    
     # temporary route
    login_manager.init_app(app) 
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"
    migrate= Migrate(app, db)
    db.init_app(app)
    Bootstrap(app)
    from app import models
    
    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
 
    @app.errorhandler(403)
    def forbidden(error):
        return render_template('errors/403.html', title='Forbidden'), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html', title='Page Not Found'), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('errors/500.html', title='Server Error'), 500

    return app
    
    