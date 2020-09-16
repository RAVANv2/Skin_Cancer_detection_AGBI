import requests
from flask_restful import Resource, Api
from model import *
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from support import base64_to_image,id_generator
# from recognize import pred

import warnings
warnings.filterwarnings("ignore")

import logging

FORMAT = '%(asctime)-15s [%(levelname)s] [%(filename)s:%(lineno)s]: %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO, filename="malonoma_app.out")
logger = logging.getLogger(__name__)

'''Creating malonoma_app instance'''
malonoma_app = Flask(__name__)
# CORS(malonoma_app)
# malonoma_app.config['DEBUG'] = True
# malonoma_app.config['JSON_SORT_KEYS'] = False

# Creating api instance
# api = Api(malonoma_app)
@malonoma_app.route('/pred_malonoma', methods=['POST','GET'])
def pred_malonoma():
    if request.method == 'GET':
        return jsonify({'messege':'Make post method for prediction'})
    else:
        logger.info("getting json request")
        try:
            logger.info("getting base64 of image")
            user_id_to_test= request.json['user_id_to_test']
            image_for_test = request.json['image_for_test']

            try:
                data_dir = base64_to_image(user_id_to_test, image_for_test, 'test')
                path = data_dir
                print(path)
                logger.info("reading image")
                read = lambda imname: np.asarray(Image.open(imname).convert("RGB"))
                img = [read(path)]
                img_arr = np.array(img[0],dtype='uint8')
                img_arr = img_arr/255.0
                img_arr = resnet.resize_image(img_arr,(224,224))
                new_img = np.resize(img_arr,(1,)+(224, 224, 3))
                logger.info("passing image to model")
            except:
                return jsonify({ "errorcode": -1, "result": "Unable to Read base 64 image" })

            pred = resnet.model(new_img)
            logger.info("getting the prob of malonoma")
            prob = pred.numpy()[0]
            logger.info("returning the prob of malonoma as json")
            return jsonify({ "errorcode": 0, "value": str(prob), "result": "success" })
        except:
            return jsonify({ "errorcode": -1, "result": "Eror in Resnet Model" })

# api.add_resource(prediction,'/')



if __name__ == '__main__':
    malonoma_app.run(host='0.0.0.0', port=5005, debug=True)
