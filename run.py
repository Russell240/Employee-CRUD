# run.py

import os
from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import create_app


config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name='development')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000, debug=True)