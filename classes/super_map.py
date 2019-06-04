import logging

logger = logging.getLogger()

class Map(dict):
    """
        This is a helper class that extends dict
        in order to allow us access dict attribute using dot . operator
    """
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class ImmutableMap(dict):
    """
        This is a helper class that extends dict
        in order to allow us access dict attribute using dot . operator
        plus it deactivates set and delete operations
    """
    __getattr__ = dict.get

    def __setattr__(self, key, value):
        logger.warning('Set function is not supported in ImmutableMap')

    def __delattr__(self, item):
        logger.warning('Del function is not supported in ImmutableMap')