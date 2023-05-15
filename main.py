import requests
from bs4 import BeautifulSoup
from bs2json import BS2Json

import json
 
page = requests.get('https://www.imdb.com/chart/top/') # Getting page HTML through request
soup = BeautifulSoup(page.content, 'html.parser') # Parsing content using beautifulsoup
 
links = soup.select("table tbody tr td.titleColumn a") # Selecting all of the anchors with titles
first10 = links[:10] # Keep only the first 10 anchors
data = []
for x in first10:
    data.append(x.text)
    print(x.text)
print(data)

doc = {"data": data}

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(doc, f, ensure_ascii=False, indent=4)

