import pandas as pd
import requests
from bs4 import BeautifulSoup

req = requests.get('https://guildstats.eu/bosses?monsterName=&world=Dibra&rook=0')
if req.status_code == 200:
    print('Requisição bem sucedida!')
    content = req.content
