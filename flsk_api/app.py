import requests
from flask_restful import Resource, Api
from model import *
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS

'''Creating app instance'''
app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True
app.config['JSON_SORT_KEYS'] = False

# Creating api instance
api = Api(app)

class prediction(Resource):

    def get(self):
        return jsonify({'messege':'Make post method for prediction'})
    
    def post(self):
        data = request.get_json()
        path = data['src']
        read = lambda imname: np.asarray(Image.open(imname).convert("RGB"))
        img = [read(path)]
        img_arr = np.array(img[0],dtype='uint8')
        img_arr = img_arr/255.0
        img_arr = resnet.resize_image(img_arr,(224,224))
        new_img = np.resize(img_arr,(1,)+(224, 224, 3))
        pred = resnet.model(new_img)
        prob = pred.numpy()[0]
        return jsonify({'value':str(prob)})

api.add_resource(prediction,'/')

if __name__ == '__main__':
    app.run()


