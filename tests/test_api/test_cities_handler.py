from tests import BaseTestCase
from constants import get_cities_names

class CitiesHandlerTest(BaseTestCase):
    def test_get_cities_request(self):

        res = self.client.get('/cities')
        self.assert200(res)
        self.assertEqual(get_cities_names(), res.json['data'])
