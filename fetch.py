from bs4 import BeautifulSoup
import requests
import re

url = 'https://www.bbc.com/'

response = requests.get(url)
data = response.text

soup = BeautifulSoup(data)
text = soup.find_all('h2')

news = [t.text for t in soup.find_all('h2')]
