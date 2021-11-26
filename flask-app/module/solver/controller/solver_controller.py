import json

from flask import Blueprint
from http import HTTPStatus

solver = Blueprint('solver', __name__)


@solver.route('/', methods=['GET'])
def account_profile():
    return json.dumps('Test'), HTTPStatus.OK, {'ContentType': 'application/json'}
