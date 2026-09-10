from pprint import pprint
import requests
r = requests.get('https://api.open-meteo.com/v1/forecast')
pprint(r.json) 