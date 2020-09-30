from pprint import pprint
import requests

API_KEY = 'lw6NYBgWACpAwePIGFpd-cjmu1hBeAPvPG_KF5NpEVg'
Lat,Long = 27.023803599999997,74.21793260000001
query = 'skin + hospital'

ans = requests.get(f'https://discover.search.hereapi.com/v1/discover?at={Lat},{Long}&q={query}&lang=en-US&apiKey={API_KEY}').json()

region = 'Rajasthan'
region = region.lower()

location = []

for response_dict in ans['items']:
    state = response_dict['address']['state'].lower()
    
    nearby = dict()

    if state == region:
        nearby['address'] = response_dict['address']['label']
        nearby['name'] = response_dict['title']
        nearby['position'] = [response_dict['position']['lat'],response_dict['position']['lng']]  # Lat, Long
        location.append(nearby)

pprint(location)

# pprint(ans['items'])