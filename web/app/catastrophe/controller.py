from flask import (
    Blueprint,
    render_template
)

main_blueprint = Blueprint(
    'catastrophe',
    __name__,
    template_folder='html'
)


@main_blueprint.route('/', methods=['GET'])
def index():
    return render_template('index.html')

