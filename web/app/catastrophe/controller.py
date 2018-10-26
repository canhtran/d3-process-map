import os
from flask import (
    Blueprint,
    render_template,
    url_for
)
from util import read_config

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
	object_path = os.path.join(DATA_PATH, 'objects.json')
	config = read_config(config_path, object_path)
	print(config)
	return render_template('graph.html')

