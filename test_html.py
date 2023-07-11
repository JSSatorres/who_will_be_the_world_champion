import requests
from bs4 import BeautifulSoup


# Realizar la solicitud HTTP
url = 'https://www.livescore.in/es/baloncesto/europa/euroliga/#/8dahPi08/table/overall'
response = requests.get(url)


html = response.content


soup = BeautifulSoup(html, 'html.parser')

# Seleccionar el elemento utilizando el selector CSS
elemento = soup.select_one('#g_3_WG03yMyc > div.event__participant.event__participant--home')

# Extraer el contenido del elemento
contenido = elemento.text.strip()

# Imprimir el contenido
print(contenido)
