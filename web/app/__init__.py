from flask import (
    Flask,
    jsonify,
    make_response
)
from app.helloworld.controller import helloworld_blueprint
from app.catastrophe.controller import main_blueprint

BLUEPRINTS = [
    (helloworld_blueprint, ['/']),
    (main_blueprint, ['/'])
]


def create_app():
    app = Flask(
        __name__,
        static_url_path='',
        static_folder='../static',
        template_folder='../templates'
    )
    # app.config.from_envvar('APPLICATION_SETTINGS')
    for blueprint, prefixes in BLUEPRINTS:
        for prefix in prefixes:
            app.register_blueprint(blueprint, url_prefix=prefix)

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

    return app


app = create_app()
