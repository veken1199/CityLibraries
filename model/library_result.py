class LibraryResult(dict):
    title = "Unknown"
    author = "Unknown"
    other = []

    def __init__(self, title, author, **kwargs):
        self.title = title
        self.author = author
        self.other = kwargs
