import pandas as pd
import requests
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from creds import *

from requests.auth import HTTPBasicAuth
basic = HTTPBasicAuth(nyc_api_key, nyc_api_secret)
r = requests.get('https://data.cityofnewyork.us/resource/s7yh-frbm.json?$limit=497727', auth=basic)
df = pd.read_json(r.text)
df.to_csv("data/nycMilestones.csv",index=False) 