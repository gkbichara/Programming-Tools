from bs4 import BeautifulSoup
import requests
import re

url = 'https://www.bbc.com/'

response = requests.get(url)
data = response.text

# features = "html.parser" written to avoid warning message
soup = BeautifulSoup(data, features = "html.parser")
text = soup.find_all('h2')

news = [t.text for t in soup.find_all('h2')]
