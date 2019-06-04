class LibraryResultItem(dict):
    def __init__(self, title="", author="", link="", publisher="", query_url=""):
        dict.__init__(self, title=title, author=author, link=link, publisher=publisher, query_url=query_url)
        self.title = title
        self.author = author
        self.link = link

        if not self.author:
            self.author = publisher

        if not self.link:
            self.link = query_url


class LibraryResult(dict):
    def __init__(self, university_name="", library_result_items=[]):
        dict.__init__(self, university_name=university_name, library_result_items=library_result_items)
        self.university_name = university_name
        self.data = library_result_items
