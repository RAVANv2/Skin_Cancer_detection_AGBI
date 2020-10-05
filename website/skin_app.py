from flask import Flask,render_template,request,session
import requests
import os
from flask import Flask, flash, redirect, url_for
from werkzeug.utils import secure_filename
from PIL import Image
import numpy as np
from datetime import datetime
from werkzeug.utils import secure_filename


# from flask_mysqldb import MySQL

import warnings
warnings.filterwarnings("ignore")

import logging
FORMAT = '%(asctime)-15s [%(levelname)s] [%(filename)s:%(lineno)s]: %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO, filename="skin_app.out")
logger = logging.getLogger(__name__)

# skin_app =  Flask(__name__,  static_folder='static')
skin_app = Flask(__name__, static_url_path='/static')
skin_app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

skin_app.config['MYSQL_HOST'] = 'localhost'
skin_app.config['MYSQL_USER'] = 'root'
skin_app.config['MYSQL_PASSWORD'] = 'password'
skin_app.config['MYSQL_DB'] = 'skin_db'

# mysql = MySQL(skin_app)

from config import get_config
conf = get_config()
UPLOAD_FOLDER=conf.data_path
ALLOWED_EXTENSIONS = {'png', 'jpeg', 'jpg'}
skin_app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@skin_app.route('/')
def home():
    logger.info("loading home page")
    return render_template('index.html')

@skin_app.route('/services')
def services():
    logger.info("loading services page")
    return render_template('services.html')

@skin_app.route('/gallery')
def gallery():
    logger.info("loading gallery page")
    return render_template('gallery.html')


@skin_app.route('/blog')
def blog():
    logger.info("loading blog page")
    return render_template('blog.html')


@skin_app.route('/faq')
def faq():
    logger.info("loading faq page")
    return render_template('faq.html')

@skin_app.route('/contact')
def contact():
    logger.info("loading contact page")
    return render_template('contact.html')

@skin_app.route('/doctors')
def doctors():
    logger.info("loading doctors page")
    return render_template('doctors.html')


@skin_app.route('/private_index')
def private_index():
    logger.info("loading private_index page")
    return render_template('private_index.html')


@skin_app.route('/signup')
def signup():
    logger.info("loading signup page")
    return render_template('signup.html')

@skin_app.route('/check_reg_cred', methods=['GET', 'POST'])
def check_reg_cred():
    logger.info("checking signup credentials")
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['pass']
        try:
            logger.info("making DB connection for signup")
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO user(username, password) VALUES (%s, %s)", (username, password))
            # mysql.connection.commit()
            cur.close()
        except:
            logger.info("Unable to connect DB for signup")
            message = "Unable to register you, please make sure your username is unique and you have entered password"
            return render_template('login.html',message=message)

        message ="Sucess, Proceed to use Special services"
        return render_template('login.html',message=message)###

@skin_app.route('/login')
def login():
    logger.info("loading login page")
    return render_template('login.html')

@skin_app.route('/check_cred', methods=['GET', 'POST'])
def check_cred():
    logger.info("checking login credentials")
    if request.method == 'POST' and 'uname' in request.form and 'pass' in request.form:
        username = request.form['uname']
        password = request.form['pass']
        try:
            logger.info("trying to conenect the DB")
            cursor = mysql.connection.cursor()
            logger.info("Connectino successfull")

            logger.info("making db Query")
            cursor.execute('SELECT * FROM user WHERE username = %s AND password = %s', (username, password,))
            logger.info("Query Sucess full")

            global user_list

            logger.info("fetching user list")
            user_list = cursor.fetchone()
            logger.info("fetching done")

            logger.info(" commit cursor")
            # mysql.connection.commit()
            cursor.close()
            logger.info("close cursor")
        except:
            logger.info("Bad credentials, fail login attemp")
            return render_template('login.html')

        # print(user_list,"user fetched")
        if user_list:
            session['loggedin'] = True
            session['username'] = user_list[0]
            logger.info("SucessFull Login")
            return redirect(url_for('private_index')) ################################################## successfull
        else:
            logger.info("No such user exists, bad login attemp")
            return render_template('login.html')

    else:
        logger.info("got the 'GET' request for login")

@skin_app.route('/logout')
def logout():
# Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('username', None)
    # Redirect to login page
    return redirect(url_for('home'))

@skin_app.route('/pred', methods=['GET', 'POST'])
def pred():
    return render_template('pred.html')

@skin_app.route('/upload_image', methods=['GET', 'POST'])
def upload_image():
  if 'loggedin' in session:
     img_file = request.files['img_file']
     # img_filename = secure_filename(img_file.filename)
     file = session['username']
     img_file.save(os.path.join(skin_app.config['UPLOAD_FOLDER'], str(file)+'.png'))
     loc = os.path.join(skin_app.config['UPLOAD_FOLDER'], str(file)+'.png')
     # print(loc)
     root = os.getcwd()
     part_1 = "{\'src\':\'"
     image = root+'/'+loc
     part_3 = "'}\n'"

     payload = part_1+image+part_3

     strr = payload.replace("\'", "\"")

     url = "http://0.0.0.0:6000/"

     payload = "{\"src\":\"/home/bhrt/Documents/Skin_Cancer_detection_AGBI/website/test_images/bharat.png\"}\n"
     headers = {
       'Content-Type': 'application/json'
     }

     response = requests.request("POST", url, headers=headers, data = payload)

     answer = response.json()
     cancer_class = answer['class']

     pred_index = answer['pred_idx']
     pred_index = pred_index[7:-1]
     pred_index = int(pred_index)

     prob = answer['probability']
     prob = prob[8:-2]
     prob = prob.split(",")

     thres = 0.3
     if float(prob[pred_index]) > float(0.3):
         pro = float(prob[pred_index])
         per = 100 - pro
         not_per = pro
         cancer_class = "This is your predicted probability for " + cancer_class
         message = "Please see a doctor ASAP"
     else:
         per = 0
         not_per = 100
         cancer_class = "No cancer detected for this skin type"
         message = "Congratulations you're safe"

     # print(cancer_class)
     print(per,"per")
     print(not_per,"not_per")

     return render_template('map.html',per=per,not_per=not_per,cancer_class=cancer_class,message=message)
  else:
      return redirect(url_for('login'))


@skin_app.route('/map', methods=['GET', 'POST'])
def map():
  if 'loggedin' in session:
     return render_template('map.html')
  else:
      return redirect(url_for('login'))


@skin_app.route('/chat', methods=['GET', 'POST'])
def chat():
  if 'loggedin' in session:
     return render_template('chat.html')
  else:
      return redirect(url_for('login'))

def callbot(userText):
    url = "https://paidqnabot3.azurewebsites.net/qnamaker/knowledgebases/192e9b82-3d48-4fa2-82c4-587e1ba22351/generateAnswer"

    # payload = "\n{\"question\":\"+str(userText)+\"}\n"
    part_1 = "\n{\'question\':\'"
    var = userText
    part_3 = "'}\n'"
    payload = part_1+var+part_3
    headers = {
      'Authorization': 'EndpointKey b5ba0699-4c25-416d-8dc9-7448f6e87eb4',
      'Content-Type': 'application/json',
      }

    response = requests.request("POST", url, headers=headers, data = payload)
    return response.json()

@skin_app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    try:
        answer_dict = callbot(userText)
        return str(answer_dict['answers'][0]['answer'])
    except :
        return "sorry i dont have idea about that"


@skin_app.route('/forum', methods=['GET', 'POST'])
def forum():
 if 'loggedin' in session:
    return render_template('forum.html')
 else:
     return redirect(url_for('login'))



if __name__ == '__main__':
    skin_app.run(host='0.0.0.0',port=7007,debug=True)
