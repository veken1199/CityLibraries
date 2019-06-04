from flask import Blueprint, app

from classes import ApiResponse

app_blueprint_name = 'app'
app_handler_blueprint = Blueprint(app_blueprint_name, __name__, url_prefix='/', static_folder='static')


@app_handler_blueprint.route(' ', methods=["GET"])
def root():
    return app_handler_blueprint.send_static_file('index.html')

@app_handler_blueprint.errorhandler(404)
def exception_handler(e):
    return ApiResponse(message="We can't find what you are looking for", status_code=404).send()

@app_handler_blueprint.errorhandler(500)
def exception_handler(e):
    return ApiResponse(message="Something went wrong!", status_code=500).send()
