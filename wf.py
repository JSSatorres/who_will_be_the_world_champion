from year_data import year
from bs4  import BeautifulSoup
import requests

web = 'https://es.wikipedia.org/wiki/Copa_Mundial_de_F%C3%BAtbol_de_2014'

response = requests.get(web)

content = response.text
soup =BeautifulSoup(content, 'lxml')



matches = soup.find_all('table', class_='collapsible autocollapse vevent plainlist')

games = []

# for match in matches:
#     # match.select('tr:nth-child(1) > td:nth-child(2) > a')
#     # print(match)
#     team_links = match.select('tr:nth-child(1) > td:nth-child(2) > a[title^="Selección de fútbol de"]')
#     team_names = [link.text for link in team_links]
#     print(team_names)
#     game = '-'.join(team_names)
#     print(game)
#     print('------------------')
#     games.append(game)
#     print(games)

#     print('-------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-----------')
for i in range(0, len(matches), 2):
    match1 = matches[i]
    match2 = matches[i+1]

    team_links1 = match1.select('tr:nth-child(1) > td:nth-child(2) > a[title^="Selección de fútbol de"]')
    team_names1 = [link.text for link in team_links1]

    team_links2 = match2.select('tr:nth-child(1) > td:nth-child(2) > a[title^="Selección de fútbol de"]')
    team_names2 = [link.text for link in team_links2]

    game = f"{team_names1[0]}-{team_names2[0]}"
    games.append(game)
    # games += [(game)]
print(games)   
    # score_cells = match.select('td[align="right"] > div > b')
    # scores = [cell.text for cell in score_cells]
    
# print(games)

# print (soup)
# matches = soup.select("#collapsibleTable0 > tbody > tr:nth-child(1)")
# for match in matches:
#     print(match)
#collapsibleTable0 > tbody > tr:nth-child(1)


#collapsibleTable6 > tbody > tr:nth-child(1) > td:nth-child(2) > a