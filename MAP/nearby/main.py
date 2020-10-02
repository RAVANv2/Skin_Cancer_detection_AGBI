import requests
from pprint import pprint
from flask_cors import CORS
from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True
app.config['JSON_SORT_KEYS'] = False


@app.route('/', methods=['Get','POST'])
def homepage():
    '''Get Location with Your IP Address'''
    url = 'http://ipinfo.io/json'
    data = requests.get(url).json()
    city = data['city'].lower().strip()
    region = data['region'].lower().strip()
    Lat = data['loc'].split(',')[0]
    Long = data['loc'].split(',')[1]

    '''Get skin hospital according to region'''
    API_KEY = 'lw6NYBgWACpAwePIGFpd-cjmu1hBeAPvPG_KF5NpEVg'
    query = 'skin + hospital'
    ans = requests.get(f'https://discover.search.hereapi.com/v1/discover?at={Lat},{Long}&q={query}&lang=en-US&apiKey={API_KEY}').json()

    location = []

    for response_dict in ans['items']:
        state = response_dict['address']['state'].lower().strip()
        state_city = response_dict['address']['city'].lower().strip()
        # print(state,state_city)
        
        nearby = dict()

        if state == region:
            nearby['address'] = response_dict['address']['label']
            nearby['name'] = response_dict['title']
            nearby['position'] = [response_dict['position']['lat'],response_dict['position']['lng']]  # Lat, Long
            location.append(nearby)

    return render_template('index.html', nearby=location)




if __name__=='__main__':
    app.run(host='0.0.0.0', port=7000)