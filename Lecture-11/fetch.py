from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime

url = 'https://www.bbc.com/'

response = requests.get(url)
data = response.text

soup = BeautifulSoup(data)
text = soup.find_all('h2')

news = [t.text for t in soup.find_all('h2', {'class': 'sc-87075214-3 eywmDE'})]

f = open(str(datetime.now()) + '.txt', 'w')
f.write('\n'.join(news))
f.close()