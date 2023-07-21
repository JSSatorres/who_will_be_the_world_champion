import random
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

opts = Options()
opts.add_argument("user-agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")

webdriver.Chrome(
	service=Service('./chromedriver'),
	options=opts
)

# driver_path = 'D:\programacion\python\who_will_be_champion\selenium' 
# service = Service(executable_path=driver_path)

# driver = webdriver.Chrome(service=service)
# # driver = webdriver.Chrome(ChromeDriverManager().install())

# # Abrir la página web

# # web1='https://www.sofascore.com/tournament/basketball/international/euroleague/138#42914'
# web = 'https://as.com//'
# # web = 'https://www.olx.pt/bebes-criancas/relaxar-e-dormir/'
# driver.get(web)

# # todos los elementos
# articles = driver.find_elements(by='xpath',value=".//article[contains(@class, 's s--h')]")
# # print(article)
# # wait = WebDriverWait(driver, 10) 
# for article in articles:    
#   title = article.find_element(by='xpath',value=".//a[contains(@class, 's__tl')]")
#   # title = coche.find_element_by_xpath('.//*[@id="515250869"]/a/div/div/div[2]/div[1]/h6')
#   print(title)  

input("Presiona una tecla para cerrar el navegador...")

# Cerrar el navegador
# driver.quit()