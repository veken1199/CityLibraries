from flask import Blueprint, request

from classes import ApiResponse
from classes import ThreadsManager
from crawlers import CrawlerRegistry
from database import CrawlerCacheModel
from constants import get_default_city_name

query_blueprint_name = 'query'
query_handler_blueprint = Blueprint(query_blueprint_name, __name__, url_prefix='/query')


@query_handler_blueprint.route('', methods=['GET'])
def handle_query():
    query = request.args.get('query')
    city = request.args.get('city')

    if not query or len(query) > 100:
        return ApiResponse(message="Query is invalid", has_error=True).send()

    if not city:
        city = get_default_city_name()

    query_response = _process_query(query, city)
    return ApiResponse(data=query_response).send()


@CrawlerCacheModel.crawler_cache_decorator
def _process_query(query, city):
    thread_manager = ThreadsManager()
    crawler_registry = CrawlerRegistry.get_instance()
    crawlers = crawler_registry.get_crawlers_for_city(city)
    response = thread_manager.init_thread_pool(query, crawlers)
    return response
