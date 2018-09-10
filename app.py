from flask import Flask,send_from_directory
from flask_cors import CORS
from request_manager import RequestsManager
import json

app = Flask(__name__)
app = Flask(__name__, static_url_path='')
CORS(app)

@app.route('/js/<path:path>')
def serve_js_files(path):
    return send_from_directory('dust', path)

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/query/<query>', methods=['GET', 'OPTIONS'])
def find_book(query):
    request_manager = RequestsManager()
    return json.dumps(request_manager.init_thread_pool(query))

@app.route('/log')
def log():
    return 'log'


if __name__ == '__main__':
    app.run(port=8082)
