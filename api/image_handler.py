import os

from flask import Blueprint, request, send_file
from werkzeug.utils import secure_filename

from classes import ApiResponse, ImageUrlCacheManager
from database import ImageModel, db
from helpers import generate_secret_filename_for, is_allowed_file_extension, \
    generate_todays_date_folder
from .schema import ImageSchema
import constants

image_blueprint_name = 'image handler'
image_handler_blueprint = Blueprint(image_blueprint_name, __name__, url_prefix='/image')


@image_handler_blueprint.route('/upload', methods=['POST'])
def handle_image_uploading():
    if not request.files or not request.files['file']:
        return ApiResponse(message="File is missing", has_error=True).send()

    if not request.form['title'] or len(request.form['title']) > constants.IMAGE_TITLE_MAX_LENGTH:
        return ApiResponse(message="Title is invalid", has_error=True).send()

    if request.form['description'] and len(request.form['description']) > constants.IMAGE_DESCRIPTION_MAX_LENGTH:
        return ApiResponse(message="Description is invalid", has_error=True).send()

    # read the file and prepare a filename
    file = request.files['file']
    filename = request.files['file'].filename
    if not is_allowed_file_extension(filename):
        return ApiResponse(message="File type is not supported", has_error= True).send()

    # generate today's folder such as folder '12-2-2012'
    storage_full_dir = generate_todays_date_folder()

    filename = secure_filename(file.filename)
    secret_filename = generate_secret_filename_for(filename)
    image_complete_path = os.path.join(storage_full_dir, secret_filename)
    file.save(image_complete_path)

    image_record = ImageModel(title=request.form['title'],
                              description=request.form['description'],
                              image_filename=secret_filename,
                              storage_full_dir=storage_full_dir)

    db.session.add(image_record)
    db.session.commit()

    # we do refresh to update image_record with ID from the db
    db.session.refresh(image_record)
    short_url = image_record.self_assign_short_url()
    db.session.add(image_record)
    db.session.commit()

    image_full_url = _generate_image_url(short_url)
    return ApiResponse(message='Image uploaded: URL => {}'.format(image_full_url)).send()


@image_handler_blueprint.route('/<int:page>', methods=['GET'])
def get_images(page=0):
    images, next_page_num, total_page_nums = ImageModel.get_all_images(page)

    # Cache the image short_url as key and full image path as value
    # for faster image retrieves and less db calls
    for image in images:
        image.image_url = _generate_image_url(image.image_short_url)
        ImageUrlCacheManager.cache_image_short_url(image)
        image.create_posted_on_property()

    images = ImageSchema(many=True).dump(images).data
    return ApiResponse(data=images, total_page_nums=total_page_nums).send()


@image_handler_blueprint.route('/load/<path:short_url>', methods=["GET"])
def load_image(short_url):
    image_full_path = ImageUrlCacheManager.get_image_full_path(short_url)
    if not image_full_path:
        # We need to get the path from the db and cache it
        # Get the id of the image from short_url
        id = ImageModel.get_row_id_for_short_url(short_url)
        image = ImageModel.get_image_by_id(id)
        if image:
            ImageUrlCacheManager.cache_image_short_url(image)
            image_full_path = os.path.join(image.storage_full_dir, image.image_filename)
        else:
            return ApiResponse(message="Image not found", has_error=True).send()

    if os.path.isfile(image_full_path):
        return send_file(image_full_path)
    return ApiResponse(message="Image not found", has_error=True).send()


def _generate_image_url(image_short_url):
    """
    Helper function to create complete url for an image short url
    :param image_short_url:
    :return: str: url
    """
    return request.host_url + 'image/load/' + image_short_url
