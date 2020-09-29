sudo apt update && \
sudo apt-get upgrade && \
pip3 install django && \
python3 -m pip install Pillow && \
pip3 install gunicorn && \
python3 manage.py migrate

# sudo ../django/bin/python3 manage.py runserver 0.0.0.0:80