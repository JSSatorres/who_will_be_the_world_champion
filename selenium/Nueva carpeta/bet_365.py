import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #expected_conditions



opts = Options()
opts.add_argument("user-agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
# opts.add_argument("--headless") #ocultar el navegador

driver = webdriver.Chrome( 
	service=Service('./chromedriver.exe'),
	options=opts
)
web = 'https://www.bet365.es/#/HO/'
# web2 = 'https://www.bet365.es/#/HO/'
driver.get(web)
sleep(3)

wait = WebDriverWait(driver, 120)
Odd = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@class="fh-ParticipantFixtureOdd_Odds"]'))) 

# score = wait.until(EC.frame_to_be_available_and_switch_to_it)

# for team in teams:
#   print(team.text)

# print(Odd.text)
# print(visit_team.text)
# titles = driver.find_elements(By.XPATH,'//div[@data-testid="listing-card-title"]')
# for title in titles:


  
