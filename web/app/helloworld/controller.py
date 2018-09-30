from flask import (
    Blueprint,
    render_template
)

helloworld_blueprint = Blueprint(
    'helloworld',
    __name__,
    template_folder="html"
)


@helloworld_blueprint.route('/hello_world', methods=['GET'])
def helloword():
    return render_template("helloworld.html")
