# import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import re
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC #expected_conditions
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.alert import Alert


opts = Options()
opts.add_argument("user-agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
# opts.add_argument("--headless") #ocultar el navegador

driver = webdriver.Chrome( 
	service=Service('./chromedriver.exe'),
	options=opts
)
web = 'https://betway.es/es/sports/ctl/soccer'
driver.get(web)
sleep(10)


wait = WebDriverWait(driver, 10)
onlive_matchs = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="oneLineEventItem"]'))) 

# Listas para almacenar los nombres de los equipos
team_names_home = []
team_names_away = []

for match in onlive_matchs:
    # Buscar los nombres de los equipos en cada elemento de partido
    team_name_home = match.find_element(By.XPATH, './/div[@class="teamNameHome teamName"]')
    team_name_away = match.find_element(By.XPATH, './/div[@class="teamNameAway teamName"]')
    
    # Agregar los nombres a las listas
    team_names_home.append(re.sub(r'\-', '', team_name_home.text.strip()).rstrip()) 
    team_names_away.append(team_name_away.text)


data = {'Equipo Local': team_names_home, 'Equipo Visitante': team_names_away}
df = pd.DataFrame(data)

print(df)
  
