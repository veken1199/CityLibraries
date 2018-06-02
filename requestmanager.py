from threading import Thread
from queue import Queue

class RequestsManager():
    def __init__(self, url_list):
        self.results = {}
        self.thread_pool_size = len(url_list)
        self.url_list = url_list

    def init_thread_pool(self, keyword):
        thread = Thread()
