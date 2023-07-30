import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert



opts = Options()
opts.add_argument("user-agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
# opts.add_argument("--headless") #ocultar el navegador

driver = webdriver.Chrome( 
	service=Service('./chromedriver.exe'),
	options=opts
)
web = 'https://www.888sport.es/'
# web2 = 'https://www.bet365.es/#/HO/'
driver.get(web)
sleep(10)


# # Intentamos rechazar la alerta de notificaciones si está presente
# try:
# 	WebDriverWait(driver, 10).until(EC.alert_is_present())
# 	alert = Alert(driver)
# 	print("Alerta encontrada")
# 	# Rechazar la alerta
# 	alert.dismiss()
# except:
# 	pass
  
# aceptamos las cookies
try:
	cookies_alert = driver.find_element(By.XPATH, '//button[@id="onetrust-accept-btn-handler"]')
	# Si se encuentra el mensaje, haz clic en el botón "Rechazar"
	if cookies_alert.is_displayed():
			cookies_alert.click()
except NoSuchElementException:
	pass
# 

# wait = WebDriverWait(driver, 10)
# Odd = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@class="bb-sport-event__selection"]'))) 

# score = wait.until(EC.frame_to_be_available_and_switch_to_it)

# for team in teams:
#   print(team.text)

# print(Odd.text)
# print(visit_team.text)
# titles = driver.find_elements(By.XPATH,'//div[@data-testid="listing-card-title"]')
# for title in titles:


  
