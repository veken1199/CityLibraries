from datetime import datetime, timedelta

import short_url
from sqlalchemy import Column, Integer, String, DateTime, desc

import constants
from database import db


class ImageModel(db.Model):
    __tablename__ = 'image_repo'
    __bind_key__ = 'image_repository'  # the db name this table will exist

    id = Column(Integer, primary_key=True)
    storage_full_dir = Column(String, nullable=False)
    image_filename = Column(String, unique=True, nullable=False)
    image_short_url = Column(String, default="", unique=True)
    title = Column(String, nullable=False)
    description = Column(String, default="")
    added_on = Column(DateTime, nullable=False, default=datetime.utcnow)


    def self_assign_short_url(self):
        """
        Function to assign a calling object/record with a short url
        based on it own record id. It will return short url
        :return: str : short url
        """
        self.image_short_url = short_url.encode_url(self.id)
        return self.image_short_url

    @staticmethod
    def get_row_id_for_short_url(url):
        """
        Small function to get the id from a short url, if the short url
        is not correct, short_url will throw error and we will have to
        catch and return -1
        :param url:
        :return: int
        """
        try:
            return short_url.decode_url(url)
        except:
            return -1

    @staticmethod
    def get_all_images(page):
        expiry_date = datetime.utcnow() - timedelta(weeks=1)
        records = ImageModel.query \
            .filter(ImageModel.added_on > expiry_date) \
            .order_by(desc(ImageModel.added_on)) \
            .paginate(page=page, error_out=False, max_per_page=constants.IMAGE_PAGE_SIZE)
        return records.items, records.next_num, records.pages

    def create_posted_on_property(self):
        """
        Function that adds a new property on the record to hold the
        date this record was created. The function will basically parse
        the date value from self.addedon column
        :return:
        """
        self.posted_on = self.added_on.date


    @staticmethod
    def get_image_by_id(id):
        return ImageModel.query.filter(ImageModel.id == id) \
            .first()
