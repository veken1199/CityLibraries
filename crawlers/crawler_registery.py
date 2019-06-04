from constants import get_default_city_name


class CrawlerRegistry(object):
    """
    Simple class that contains map attribute to hold city names as key and
    an array of crawlers as value.
    """
    _crawlers_registry = {}
    _self = None

    @classmethod
    def get_instance(cls):
        if not CrawlerRegistry._self:
            CrawlerRegistry._self = CrawlerRegistry.__new__(cls)
        return CrawlerRegistry._self

    def get_crawlers_registry(self):
        return self._crawlers_registry

    def insert_city_crawler(self, city, crawler_func):
        if not self._crawlers_registry.get(city):
            self._crawlers_registry[city] = []
        self._crawlers_registry.get(city).append(crawler_func)

    def get_crawlers_for_city(self, city):
        if not city:
            city = get_default_city_name()
        crawlers = self._crawlers_registry.get(city)
        return crawlers


def register_crawler_decorator(city):
    def wrapper(func):
        crawler_registry = CrawlerRegistry.get_instance()
        crawler_registry.insert_city_crawler(city, func)
        return func
    return wrapper

