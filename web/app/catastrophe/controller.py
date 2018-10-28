import os
import json
from flask import (
    Blueprint,
    render_template,
    url_for
)
from util import read_config, read_data

main_blueprint = Blueprint(
    'catastrophe',
    __name__,
    template_folder='html'
)

APP_ROOT = os.path.dirname(os.path.abspath(__file__)) 
DATA_PATH = os.path.join(APP_ROOT, 'data')


@main_blueprint.route('/', methods=['GET'])
def index():
	config_path = os.path.join(DATA_PATH, 'config.json')
	config = read_config(config_path)
	return render_template('graph.html', config=json.dumps(config))


@main_blueprint.route('/jsonurl', methods=['GET'])
def jsonurl():
    object_path = os.path.join(DATA_PATH, 'objects.json')
    data, errors = read_data(object_path)
    result = {}
    result['data'] = data
    result['errors'] = errors
    return json.dumps(result)
