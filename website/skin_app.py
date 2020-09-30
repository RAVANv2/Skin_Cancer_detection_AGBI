from flask import Flask,render_template,request,session
import requests
import os
from flask import Flask, flash, redirect, url_for
from werkzeug.utils import secure_filename
from PIL import Image
import numpy as np
from datetime import datetime


from flask_mysqldb import MySQL

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

mysql = MySQL(skin_app)

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

        message ="Sucess, Proceed to use Intelli-Parser"
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
    return redirect(url_for('login'))

@skin_app.route('/pred', methods=['GET', 'POST'])
def pred():
 if 'loggedin' in session:
    return render_template('pred.html')
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

@skin_app.route('/forum', methods=['GET', 'POST'])
def forum():
 if 'loggedin' in session:
    return render_template('forum.html')
 else:
     return redirect(url_for('login'))



if __name__ == '__main__':
    skin_app.run(host='0.0.0.0',port=7007,debug=True)
