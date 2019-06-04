import os
import constants
import logging
from werkzeug.contrib.cache import RedisCache, SimpleCache

logger = logging.getLogger()

class CacheManager:
    """
    Base caching manager class that can be extended in the future
    by other types of cache managers in order to provide
    custom caching functionality
    """
    cache = None

    @classmethod
    def initiate(cls):
        """
        Method to decide which caching client is available at the moment.
        It first tries with cache_client, if It fails, it will use SimpleCache
        """
        if not cls.cache:
            try:
                cls.cache = RedisCache(host=constants.REDIS_HOST)
                cls.cache.get("test")
                logger.info(msg="We are using Redis for Caching")
            except:
                cls.cache = SimpleCache()
                logger.info(msg='We are using SimpleCache for Caching')
        return cls.cache


class ImageUrlCacheManager(CacheManager):
    """
    Special type of Cache manager that will be responsible for caching
    image_short_url and image_full_path either on Redis on SimpleCache
    """

    @classmethod
    def cache_image_short_url(cls, image_record):
        """
        Helper function to cache image's short_url and image full_path.
        Image short_url is cached as key, and image full path is cached as value
        :param image_record:
        :return: None
        """
        try:
            cls.cache.set(image_record.image_short_url,
                          os.path.join(image_record.storage_full_dir, image_record.image_filename))
        except Exception as e:
            logger.warning('Value was not cached: '.format(e))

    @classmethod
    def get_image_full_path(cls, image_short_url):
        """
        Helper function to get image full path. It will return None if the
        value was not found or in case the cache failed
        :param image_short_url:
        :return: Object or None
        """
        try:
            return cls.cache.get(image_short_url)
        except Exception as e:
            logger.warning('Cached value was not retrieved :'.format(e))
            return None

