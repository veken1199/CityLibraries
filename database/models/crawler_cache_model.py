import logging
from datetime import datetime, timedelta

from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint
from sqlalchemy_utils import JSONType

from constants import CRAWLER_CACHE_DURATION_IN_DAYS
from database import db

logger = logging.getLogger()


class CrawlerCacheModel(db.Model):
    __tablename__ = 'crawler_cache'

    id = Column(Integer, primary_key=True)
    query_term = Column(String, nullable=False)
    city = Column(String, nullable=False)
    content = Column(JSONType, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    # __table_args__ value must be a tuple, dict, or None
    __table_args__ = (UniqueConstraint('query_term', 'city', name='_query_city_uc'),)

    def is_out_dated(self):
        expiry_date = datetime.utcnow() - timedelta(days=CRAWLER_CACHE_DURATION_IN_DAYS)
        return self.timestamp < expiry_date

    @staticmethod
    def get_cache_crawlers_record_for(query, city):
        cached_response = CrawlerCacheModel.query.filter(CrawlerCacheModel.query_term == query) \
            .filter(CrawlerCacheModel.city == city) \
            .first()
        return cached_response

    @staticmethod
    def crawler_cache_decorator(handler):
        def wrapper(*args, **kwargs):
            # args and kwargs are the params passed in the handler
            try:
                query = args[0]
                city = args[1]
                cached_response = CrawlerCacheModel.get_cache_crawlers_record_for(query, city)
                if not cached_response or cached_response.is_out_dated():
                    response = handler(*args, **kwargs)
                    if not cached_response:
                        # it means this is the first time we see this query and city
                        cached_response = CrawlerCacheModel(query_term=query, content=response, city=city)
                    else:
                        # it means the row is out dated, we only need to update the content
                        cached_response.content = response

                    db.session.add(cached_response)
                    db.session.commit()
                    return response

                return cached_response.content

            except Exception as e:
                logger.warning('Error in the cache: {}'.format(e))

            # return the handler in case the caching system failed
            return handler(*args, **kwargs)

        return wrapper
