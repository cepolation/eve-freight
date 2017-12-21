from flask import render_template, Blueprint, redirect
from flask import current_app as app
eve = Blueprint('eve', __name__)

@eve.route('/')
def index():
    return redirect(app.config['ESI_REDIRECT_URL'])
