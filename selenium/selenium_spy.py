import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Instalar y configurar el controlador de Chrome
 # Ruta absoluta del controlador
driver_path = 'D:\programacion\python\who_will_be_champion\selenium' 
service = Service(executable_path=driver_path)

driver = webdriver.Chrome(service=service)
# driver = webdriver.Chrome(ChromeDriverManager().install())

# Abrir la página web

# web1='https://www.sofascore.com/tournament/basketball/international/euroleague/138#42914'
web = 'https://www.olx.pt/bebes-criancas/relaxar-e-dormir/'
driver.get(web)

# todos los elementos
carricoches_bebe = driver.find_elements(by='xpath',value='//*[@id="647203475"]')
print(carricoches_bebe)

# for coche in carricoches_bebe:    
#   title = coche.find_element_by_xpath('.//*[@id="515250869"]/a/div/div/div[2]/div[1]/h6')
#   # title = coche.find_element_by_xpath('.//*[@id="515250869"]/a/div/div/div[2]/div[1]/h6')
#   print(title)  

input("Presiona una tecla para cerrar el navegador...")

# Cerrar el navegador
driver.quit()