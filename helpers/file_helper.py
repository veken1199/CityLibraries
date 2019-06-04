import os
from datetime import datetime

import constants


def is_allowed_file_extension(filename):
    """
    Function used to check if the file extension is one of the allowed extensions
    :param filename:str
    :return: boolean
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in constants.ALLOWED_EXTENSIONS


def generate_secret_filename_for(filename):
    """
    Function allows us to create a secret and append it to the original file name
    to make it unique
    :param filename:
    :return: str: New filename
    """
    secret = os.urandom(constants.FILENAME_SECRET_LENGTH).hex()
    return secret + filename


def generate_todays_date_folder():
    """
    Function to check and create if does not exist a folder of today's date
    and returns today's date folder directory
    :return: str
    """
    todays_date = datetime.today().date()

    todays_date_folder_dir = os.path.join(constants.IMAGE_REPOSITORY_PATH, str(todays_date))
    if not os.path.isdir(todays_date_folder_dir):
        os.mkdir(todays_date_folder_dir)
    return todays_date_folder_dir
