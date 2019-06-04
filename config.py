import logging
from logging.config import dictConfig


class BaseConfig(object):
    DEBUG = True
    TESTING = False

    MAX_CONTENT_LENGTH = 4 * 1024 * 1024  # 4mb

    # SQLAlchemy setup
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data_repository/app.db'
    SQLALCHEMY_BINDS = {'image_repository': 'sqlite:///data_repository/image_repository.db'}
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # Session secret keys
    SECRET_KEY = 'ae24a87634bf4d749bef9d089cfcb79140d47727'
    SESSION_TYPE = 'sqlalchemy'
    SESSION_USE_SIGNER = True

    from logging.config import dictConfig

    logging_config = dict(
        version=1,
        formatters={
            'f': {'format':
                      '%(asctime)s %(name)-6s [%(filename)s:%(lineno)d]-2s %(levelname)-6s %(message)s'}
        },
        handlers={
            'h': {'class': 'logging.StreamHandler',
                  'formatter': 'f',
                  'level': logging.INFO}
        },
        root={
            'handlers': ['h'],
            'level': logging.INFO,
        },
    )

    dictConfig(logging_config)


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True

    # SQLAlchemy setup
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data_repository/test_app.db'
    SQLALCHEMY_BINDS = {'image_repository': 'sqlite:///data_repository/test_image_repository.db'}
