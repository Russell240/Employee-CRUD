# run.py

import os

from flask_migrate import current
from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from flask_sqlalchemy import sqlalchemy


config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name='development')
db= SQLAlchemy()

if __name__ == '__main__':

    with create_app().app_context():
        print (create_app().name)
        app.run(host='0.0.0.0',port=8000, debug=True)