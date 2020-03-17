import pandas as pd
import requests
from bs4 import BeautifulSoup

req = requests.get('https://guildstats.eu/bosses?monsterName=&world=Dibra&rook=0')
if req.status_code == 200:
    print('Requisição bem sucedida!')
    content = req.content

soup = BeautifulSoup(content, 'html.parser')
table = soup.find(name='table')

df = pd.read_html(str(table))[0]

df.columns = df.columns.get_level_values(0)

df.rename(columns={'#':'#', 'Boss name':'Boss name', 'Image':'Image', 'Yesterday':'Boss Death (Yesterday)',
                  'Overall (since 21 Feb 2015)':'Player Death (Yesterday)','Last seen':'Boss Death (Total)',
                  'Unnamed: 6_level_0':'Player Death (Total)', 'Unnamed: 7_level_0':'Last Seen'}, inplace=True)



df.drop(columns=['#','Image', 'Player Death (Yesterday)', 'Boss Death (Total)', 'Player Death (Total)'],inplace=True)
df.drop([0,1],inplace=True)
df[:10]
print(df)