# run.py

import os
from config import Config

from app import create_app

config_name = os.environ.get('FLASK_APP')
app = create_app()

if __name__ == '__main__':
    app.run()