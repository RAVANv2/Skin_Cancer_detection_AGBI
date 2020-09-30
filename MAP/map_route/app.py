import requests
from flask import Flask, render_template, request, redirect, flash, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True
app.config['JSON_SORT_KEYS'] = False

@app.route('/',methods=['GET','POST'])
def homepage():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)