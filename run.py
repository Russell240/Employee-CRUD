# run.py

import os
from config import Config
from flask import Flask
from app import models 
from flask_sqlalchemy import SQLAlchemy


from app import create_app
app=Flask(__name__)
db = SQLAlchemy()

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name='development')

if __name__ == '__main__':
    from app import create_app 
    with create_app().app_context():
        db.init_app(app)
    app.run(host='0.0.0.0',port=8000, debug=True)