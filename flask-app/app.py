import os

from flask import Flask
from flask_cors import CORS
from module.solver.controller.solver_controller import solver


def create_app():
    flask_app = Flask(__name__, instance_relative_config=True)
    try:
        os.makedirs(flask_app.instance_path)
    except OSError:
        pass

    flask_app.register_blueprint(solver)
    return flask_app


app = create_app()
CORS(app)
