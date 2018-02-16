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

    context = {'contracts': []}
    tot_volume = 0
    for contract in contracts.data:
        if app.config['CORPORATION_ID'] != contract['assignee_id']:
            continue
        if contract['status'] != 'outstanding':
            continue
        if contract['type'] != 'courier':
            continue

        op = esi_app.op['get_characters_character_id'](
            character_id=contract['issuer_id']
        )
        issuer = app.config['esi_client'].request(op).data['name']
        iss_time = contract['date_issued']
        exp_time = contract['date_expired']
        volume = str(contract['volume']) + " m3"
        tot_volume += float(contract['volume'])
        context['contracts'].append((issuer, iss_time, exp_time, volume, contract['type'], contract['status']))

    context['progress'] = str(round(tot_volume / 3400, 2))

    op = esi_app.op['get_corporations_corporation_id'](
        corporation_id=app.config['CORPORATION_ID']
    )
    context['corp'] = app.config['esi_client'].request(op).data['name']
    print(contracts)
    print(contracts.data)
    return render_template('main.html', **context)
