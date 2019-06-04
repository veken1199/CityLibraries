import os
from classes import ImmutableMap

CITIES = ImmutableMap({"MTL": "MTL"})

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_REPOSITORY_PATH = os.path.join(ROOT_DIR, 'image_repository')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
IMAGE_PAGE_SIZE = 3
FILENAME_SECRET_LENGTH = 24
REDIS_HOST = '192.168.99.100'
REDIS_CACHE_TIMEOUT = 0
TITLE_BLACKLISTS = [
    'Please log in to see this content from Scopus®',
    'Reference',
    'index.'
]
CRAWLER_CACHE_DURATION_IN_DAYS = 1 #day

PASS_CODE = 200  # OK
HAS_ERROR_CODE = 422  # Unprocessible Entity


def get_cities_names():
    """ in python 3, dict.values return dict.values() type instead of
     regular list type. This dict.values() is not json serializable"""
    return list(CITIES.values())


def get_default_city_name():
    return CITIES.MTL
