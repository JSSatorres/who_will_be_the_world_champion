import random
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

opts = Options()
opts.add_argument("user-agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
opts.add_argument("--headless") #ocultar el navegador

driver = webdriver.Chrome( 
	service=Service('./chromedriver.exe'),
	options=opts
)

web = 'https://www.airbnb.es/'
driver.get(web)
sleep(3)

titles = driver.find_elements(By.XPATH,'//div[@data-testid="listing-card-title"]')
for title in titles:
	print(title.text)


  
