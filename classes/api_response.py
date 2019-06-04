import constants
import json

class ApiResponse:
    """
    Class the represents our api response to the client request
    """

    def __init__(self, data=[], message='Successful request', has_error=False, status_code=None, **kwargs):
        self.data = data
        self.message = message
        self.has_error = has_error
        self.status_code = status_code
        self.__dict__.update(kwargs)

    def send(self):
        status = self._get_status_code()
        return json.dumps(self.__dict__), status, {'Content-Type': 'application/json'}

    def _get_status_code(self):
        if not self.status_code:
            self.status_code = constants.HAS_ERROR_CODE if self.has_error \
                else constants.PASS_CODE
        return self.status_code


