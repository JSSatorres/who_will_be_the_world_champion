from year_data import year
from bs4  import BeautifulSoup
import requests

web = 'https://es.wikipedia.org/wiki/Copa_Mundial_de_F%C3%BAtbol_de_2014'

response = requests.get(web)

content = response.text
soup =BeautifulSoup(content, 'lxml')

# matches = soup.find_all('table', class_='collapsible autocollapse vevent plainlist')
# for match in matches:
#     print(match)

matches = soup.select("tbody > tr > td ")
for match in matches:
    print(match)
#collapsibleTable0 > tbody > tr:nth-child(1)
