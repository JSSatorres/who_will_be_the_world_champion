from selenium import webdriver

url = "https://www.sofascore.com/ldlc-asvel-lyon-villeurbanne-olympiacos-bc/bvbsLvb#10500287"

# Configurar el driver de Selenium (en este caso, se utiliza Chrome)
driver = webdriver.Chrome("path/al/chromedriver")  # Reemplaza "path/al/chromedriver" con la ubicación de tu chromedriver

# Acceder a la página
driver.get(url)

# Obtener el contenido HTML de la página cargada
html_content = driver.page_source

# Aquí puedes analizar o extraer la información relevante del HTML utilizando técnicas como regex, BeautifulSoup, etc.

# Por ejemplo, puedes buscar el contenido de los elementos <span> con la clase "sc-bqWxrE" y "cYwlbu"
import re

pattern = r'<span class="sc-bqWxrE cYwlbu">([^<]+)</span>'
matches = re.findall(pattern, html_content)

for match in matches:
    data = {'score': match}
    print(data)

# Cerrar el driver de Selenium
driver.quit()