from functools import wraps
import json


def jsonify_response_decorator(route):
    @wraps(route)
    def wrapper(*args, **kwargs):
        resp, status_code = route(*args, **kwargs)
        return json.dumps(resp), status_code
    return wrapper
