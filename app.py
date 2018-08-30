from flask import Flask
from flask_cors import CORS
from request_manager import RequestsManager
import json

app = Flask(__name__)
CORS(app)

@app.route('/query/<query>', methods=['GET', 'OPTIONS'])
def find_book(query):
    request_manager = RequestsManager()
    return json.dumps(request_manager.init_thread_pool(query))

@app.route('/log')
def log():
    return 'log'

if __name__ == '__main__':
    app.run(port=8082)
