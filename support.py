import os
import base64
import random
import string
import logging
import subprocess
from PIL import Image
from pathlib import Path
from io import BytesIO

BASE_DIR = os.curdir
test_storage = os.path.join(BASE_DIR, 'test')

logger = logging.getLogger(__name__)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    """
    this will generate random name
    :param size:
    :param chars:
    :return:
    """
    return ''.join(random.choice(chars) for _ in range(size))

def base64_to_image(user_id, base64_string, image_for='test', extension='.png'):
    """
    this will convert the base64 string to image
    :param extension: extension of image
    :param user_id: user_id to enroll
    :param base64_string: base64 encoded image string
    :param image_for: train/test
    :return: filename of the writtened file
    """

    if image_for == 'test':
        if user_id:
            filename = os.path.join(test_storage, user_id + '.png')
        else:
            filename = os.path.join(test_storage, id_generator() + '.png')

        try:
            # img_data = base64.b64decode(base64_string)
            im = Image.open(BytesIO(base64.b64decode(base64_string)))

            im.save(filename, 'png')
            # with open(filename, 'wb') as f:
            #     print(img_data)
            #     f.write(img_data)
        except:
            logger.exception("Bad base64 string provided")

        logger.info("test data saved: '{}'".format(str(filename)))
        return filename
