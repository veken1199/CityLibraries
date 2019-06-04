from flask import Blueprint

import constants
from classes import ApiResponse

cities_blueprint_name = 'cities'
cities_handler_blueprint = Blueprint(cities_blueprint_name, __name__, url_prefix='/cities')


@cities_handler_blueprint.route('', methods=['GET'])
def get_cities():
    return ApiResponse(data=constants.get_cities_names()).send()
