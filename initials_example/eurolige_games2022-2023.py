from bs4  import BeautifulSoup
import requests

# TODO: imposible to read div
web = ''

from year_data import years
from bs4  import BeautifulSoup
import requests
import pandas as pd

quarter= [0,1,2,3]
    # web = f'https://www.livescore.in/es/partido/v35dSz8d/#/resumen-del-partido/punto-a-punto/{quarter}'

def get_all_matches():    
    web = 'https://www.livescore.in/es/partido/v35dSz8d/#/resumen-del-partido/punto-a-punto/0'

    response = requests.get(web)

    content = response.text
    soup =BeautifulSoup(content, 'lxml')

    quarters_score = soup.find_all('div', class_='matchHistoryRow')
    print(quarters_score)

    for quarter_score in quarters_score:
        scores_by_points = soup.find_all('div', class_='matchHistoryRow__score')
         
        primer_div = scores_by_points[0]
        segundo_div = scores_by_points[1]

        print(primer_div.text)
        print(segundo_div.text)
           
    

#     home = []
#     score = []
#     away = []

#     for match in matches:
#         local_team = match.select('tr:nth-child(1) > td:nth-child(2) > a[title^="Selección de fútbol de"]')
#         home.append(local_team[0].text if local_team else "")
        
#         scoreMatch = match.select('tr:nth-child(1) > td:nth-child(3) > div > b')
#         score.append(scoreMatch[0].text if score else "")
        
#         visitor_team = match.select('tr:nth-child(1) > td:nth-child(4) > a[title^="Selección de fútbol de"]')
#         away.append(visitor_team[0].text if visitor_team else "")

#     dict_football= {'home':home,'score':score,'away':away}
#     df_matches = pd.DataFrame(dict_football)
#     df_matches['year']= year  
#     return df_matches 

# fifa = [get_all_matches(year) for year in years ] 
# df_fifa = pd.concat(fifa, ignore_index=True)
# df_fifa.to_csv('fifa_worldcup_historical_data.csv', index=False)