"""
OBJETIVO: 
    - Resultado de un cuarto de un partido de baloncesto punto a punto
CREADO POR: JUAN SANCHEZ
ULTIMA VEZ EDITADO: 26 DE JUNIO 2023
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # pip install webdriver-manager

opts = Options()
opts.add_argument("user-agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")

driver = webdriver.Chrome( 
	service=Service('./chromedriver.exe'),
	options=opts
)

for i in range(4):
  web = f'https://www.livescore.in/es/partido/v35dSz8d/#/resumen-del-partido/punto-a-punto/{i}'
  driver.get(web)

  # opts.add_argument("--headless") #ocultar el navegador

  # Me doy cuenta que la pagina carga el formulario dinamicamente luego de que la carga incial ha sido completada
  # Por eso tengo que esperar que aparezca 
  input_user = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='matchHistoryRowWrapper']")))


  # Espero a que aparezcan los resultados
  scores = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="matchHistoryRow__scoreBox "]')))

  # Imprimo el texto de los resultados
  for score in scores:
    print(score.text)

driver.quit()