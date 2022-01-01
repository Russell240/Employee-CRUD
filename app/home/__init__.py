from flask import Blueprint
from flask import Flask

app = Flask(__name__)
home = Blueprint('home', __name__ , template_folder='../templates')

from . import views

