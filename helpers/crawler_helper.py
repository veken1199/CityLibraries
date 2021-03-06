import constants


def is_valid_book(title="", author=""):
    """
    Helper function to check if the title of a book is one of the blacklisted
    and if both title and author are empty
    titles
    :param title:
    :param author
    :return: boolean
    """
    if title in constants.TITLE_BLACKLISTS:
        return False
    if not title and not author:
        return False
    else:
        return True
