import requests
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import numpy as np 
from fastai import *
from fastai.vision import open_image, ImageList
from fastai.callbacks.hooks import load_learner 
import warnings
warnings.filterwarnings('ignore')


from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['DEGUB'] = True
app.config['JSON_SORT_KEYS'] = False

api = Api(app)

Path = './fast_model'
class CustomImageItemList(ImageList):
    def custom_label(self,df, **kwargs)->'LabelList':
        """Custom Labels from path"""
        file_names=np.vectorize(lambda files: str(files).split('/')[-1][:-4])
        get_labels=lambda x: df.loc[x,'lesion']
        #self.items is an np array of PosixPath objects with each image path
        labels= get_labels(file_names(self.items))
        y = CategoryList(items=labels)
        res = self._label_list(x=self,y=y)
        return res

''' Loading model from hard disk'''
learner = load_learner(Path)
print('Model loaded')

class prediction(Resource):
    def get(self):
        return jsonify({'message':'Make post request for prediction'})

    def post(self):
        data = request.get_json()
        path = data['src']
        img = open_image(path)
        pred_class,pred_idx,outputs = learner.predict(img)
        return jsonify({'class':str(pred_class),'pred_idx':str(pred_idx), 'probability':str(outputs)})

api.add_resource(prediction,'/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6000, debug=True)
