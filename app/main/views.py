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
    print(contracts)
    print(contracts.data)
    return render_template('main.html')
