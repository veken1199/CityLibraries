import logging
from flask import Flask
from api import cities_handler_blueprint, query_handler_blueprint, image_handler_blueprint
from database import db
from classes import ImageUrlCacheManager, ApiResponse

def create_app(config='config.BaseConfig'):
    app = Flask(__name__, static_url_path='')
    app.config.from_object(config)
    app.app_context().push()

    ImageUrlCacheManager.initiate()

    app.register_blueprint(image_handler_blueprint)
    app.register_blueprint(cities_handler_blueprint)
    app.register_blueprint(query_handler_blueprint)

    db.init_app(app)
    db.create_all()
    return app, db

app, _ = create_app()

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.errorhandler(404)
def exception_handler(e):
    return ApiResponse(message="We can't find what you are looking for", status_code=404).send()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
