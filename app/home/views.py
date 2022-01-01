from flask import Blueprint, render_template
from flask_login import login_required


from . import home

# http://127.0.0.1/index
@home.route('/index')
def homepage():
    """
    Render the homepage template on the /l route
    """
    return render_template('home/index.html', title="Welcome")

@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Dashboard")
