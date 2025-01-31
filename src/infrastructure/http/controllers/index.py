from flask import Blueprint, jsonify, request
from core.services.example_service import ExampleService

routes = Blueprint('routes', __name__)

@routes.route('/example', methods=['GET'])
def get_example():
    service = ExampleService()
    result = service.get_example()
    return jsonify(result), 200
