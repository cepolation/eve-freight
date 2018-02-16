from flask import render_template, Blueprint
from flask import current_app as app
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('homepage.html')

@main.route('contracts/')
def contracts():
    esi_app = app.config['esi_app']
    op = esi_app.op['get_corporations_corporation_id_contracts'](
        corporation_id=app.config['CORPORATION_ID']
    )
    contracts = app.config['esi_client'].request(op)

    show_data = []
    for contract in contracts.data:
        if app.config['CORPORATION_ID'] != contract['assignee_id']:
            continue

        op = esi_app.op['get_characters_character_id'](
            character_id=contract['issuer_id']
        )
        issuer = app.config['esi_client'].request(op).data['name']
        iss_time = contract['date_issued']
        exp_time = contract['date_expired']
        volume = str(contract['volume']) + " m3"
        show_data.append((issuer, iss_time, exp_time, volume))

    op = esi_app.op['get_corporations_corporation_id'](
        corporation_id=app.config['CORPORATION_ID']
    )
    corp = app.config['esi_client'].request(op).data['name']
    print(contracts)
    print(contracts.data)
    return render_template('main.html', data=show_data, corp=corp)
