from year_data import year
from bs4  import BeautifulSoup
import requests

web = 'https://es.wikipedia.org/wiki/Copa_Mundial_de_F%C3%BAtbol_de_2014'

response = requests.get(web)

content = response.text
soup =BeautifulSoup(content, 'lxml')



matches = soup.find_all('table', class_='collapsible autocollapse vevent plainlist')

games = []

for match in matches:
    # match.select('tr:nth-child(1) > td:nth-child(2) > a')
    # print(match)
    team_links = match.select('tr:nth-child(1) > td:nth-child(2) > a[title^="Selección de fútbol de"]')
    team_names = [link.text for link in team_links]
    game = '-'.join(team_names)
    games.append(game)
    # games += [(game)]
    
    # score_cells = match.select('td[align="right"] > div > b')
    # scores = [cell.text for cell in score_cells]
    
print(games)

# print (soup)
# matches = soup.select("#collapsibleTable0 > tbody > tr:nth-child(1)")
# for match in matches:
#     print(match)
#collapsibleTable0 > tbody > tr:nth-child(1)


#collapsibleTable6 > tbody > tr:nth-child(1) > td:nth-child(2) > a