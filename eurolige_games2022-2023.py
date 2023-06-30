from bs4  import BeautifulSoup
import requests

# TODO: imposible to read div
web = 'https://www.sofascore.com/real-madrid-olympiacos-bc/bvbsPvb#11274336'

response = requests.get(web)
content = response.text

soup = BeautifulSoup(content, 'lxml')
print(soup)
