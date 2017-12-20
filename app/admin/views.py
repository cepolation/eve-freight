from flask import render_template, Blueprint
admin = Blueprint('admin', __name__)

@admin.route('/')
def index():
    return render_template('homepage.html')
