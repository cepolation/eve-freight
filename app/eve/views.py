from flask import render_template, Blueprint, redirect, request
from flask import current_app as app
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

    esi_app = app.config['esi_app']
    op = esi_app.op['get_characters_character_id'](
        character_id=user['CharacterID']
    )
    data = app.config['esi_client'].request(op)
    app.config['CORPORATION_ID'] = data.data['corporation_id']
    print(app.config['user'])
    print(user)
    return redirect('/')



