from flask import render_template, Blueprint, redirect, request
from flask import current_app as app
from app.utils.list import *
eve = Blueprint('eve', __name__)

@eve.route('/')
def index():
    return redirect(app.config['ESI_REDIRECT_URL'])
@eve.route('/callback')
def callback():
    code = request.args.get('code')
    token = request.args.get('state')
    print(code)
    print(token)
    esi_response = app.config['esi_security'].auth(code)
    user = app.config['esi_security'].verify()
    app.config['user'] = user
    print(app.config['user'])
    print(user)
    return redirect('/')



