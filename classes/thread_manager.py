from threading import Thread

class ThreadsManager:
    def __init__(self):
        self.results = []
        self.thread_pool = []

    def init_thread_pool(self, query, crawlers):
        """
        Method to create threads and assign crawlers to each
        of the threads. Each thread then will start processing
        the query and once all the threads join, the results will
        be returned
        :param query:
        :param crawlers:
        :return: data:[LibraryResult] => results from the crawlers
        """
        for crawler in crawlers:
            thread = Thread(target=crawler, args=[query, self.results])
            self.thread_pool.append(thread)
            thread.start()

        for thread in self.thread_pool:
            thread.join()

        return self.results

