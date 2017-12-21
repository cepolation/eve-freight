from flask import render_template, Blueprint
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('homepage.html')

@main.route('contracts/')
def contracts():
    return render_template('main.html')
