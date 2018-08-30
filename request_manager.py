from threading import Thread
import engine_mapper
from queue import Queue


class RequestsManager():
    def __init__(self):
        self.results = []
        self.thread_pool = []

    def init_thread_pool(self, keyword):
        for library_name, crawler in engine_mapper.engine_map.items():
            thread = Thread(target=crawler, args=[keyword, self.results])
            self.thread_pool.append(thread)
            thread.start()

        for thread in self.thread_pool:
            thread.join()

        return self.results

