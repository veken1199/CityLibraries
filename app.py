from flask import Flask
from request_manager import RequestsManager
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    request_manager = RequestsManager()
    return json.dumps(request_manager.init_thread_pool('calculus'))

@app.route('/log')
def log():
    return 'log'

if __name__ == '__main__':
    app.run(port=8082)
