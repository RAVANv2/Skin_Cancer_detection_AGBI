from pprint import pprint
import requests

API_KEY = 'lw6NYBgWACpAwePIGFpd-cjmu1hBeAPvPG_KF5NpEVg'
Lat,Long = 27.023803599999997,74.21793260000001
query = 'skin + hospital'

ans = requests.get(f'https://discover.search.hereapi.com/v1/discover?at={Lat},{Long}&q={query}&lang=en-US&apiKey={API_KEY}')

pprint(ans.json())