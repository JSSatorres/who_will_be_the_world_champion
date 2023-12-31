from year_data import years
from bs4  import BeautifulSoup
import requests
import pandas as pd

def get_all_matches(year):    
    web = f'https://es.wikipedia.org/wiki/Copa_Mundial_de_F%C3%BAtbol_de_{year}'

    response = requests.get(web)

    content = response.text
    soup =BeautifulSoup(content, 'lxml')

    matches = soup.find_all('table', class_='collapsible autocollapse vevent plainlist')

    home = []
    score = []
    away = []

    for match in matches:
        local_team = match.select('tr:nth-child(1) > td:nth-child(2) > a[title^="Selección de fútbol de"]')
        home.append(local_team[0].text if local_team else "")
        
        scoreMatch = match.select('tr:nth-child(1) > td:nth-child(3) > div > b')
        score.append(scoreMatch[0].text if score else "")
        
        visitor_team = match.select('tr:nth-child(1) > td:nth-child(4) > a[title^="Selección de fútbol de"]')
        away.append(visitor_team[0].text if visitor_team else "")

    dict_football= {'home':home,'score':score,'away':away}
    df_matches = pd.DataFrame(dict_football)
    df_matches['year']= year  
    return df_matches 

fifa = [get_all_matches(year) for year in years ] 
df_fifa = pd.concat(fifa, ignore_index=True)
# extraer en excel el contenido extraído
df_fifa.to_csv('fifa_worldcup_historical_data.csv', index=False)