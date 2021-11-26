import json

from flask import Blueprint, request
from http import HTTPStatus
from module.solver.service.solver_service import SolverService

solver = Blueprint('solver', __name__)

solverService = SolverService()


@solver.route('/recognize', methods=['POST'])
def recognize():
    data_url = request.json['data_url']
    img = solverService.data_url_to_cv2_img(data_url)
    segments = solverService.segment(img)
    pred = []
    for segment in segments:
        pred.append(solverService.recognize(segment))
    return json.dumps({"recognition": pred}), HTTPStatus.OK, {'ContentType': 'application/json'}
