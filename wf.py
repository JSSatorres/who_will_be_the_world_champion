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
    local_team = match.select('tr:nth-child(1) > td:nth-child(2) > a[title^="Selección de fútbol de"]')
    local_team_text = local_team[0].text if local_team else ""
    
    score = match.select('tr:nth-child(1) > td:nth-child(3) > div > b')
    score_text = score[0].text if score else ""
    
    visitor_team = match.select('tr:nth-child(1) > td:nth-child(4) > a[title^="Selección de fútbol de"]')
    visitor_team_text = visitor_team[0].text if visitor_team else ""
    
    game = f"{local_team_text}-{visitor_team_text}-{score_text}"
    games.append(game)
    # games += [(game)]
print(games)   
