import requests
from bs4 import BeautifulSoup


# Realizar la solicitud HTTP
url = 'https://www.sofascore.com/real-madrid-olympiacos-bc/bvbsPvb#11274336'
response = requests.get(url)

content = response.text
soup =BeautifulSoup(content, 'lxml')

div = soup.find('div', class_='sc-hLBbgP sc-eDvSVe iWJGpI KyGQG')

# Extraer el contenido del span dentro del div
span = div.find('span', class_='sc-bqWxrE cYwlbu')
contenido = span.text

# Imprimir el contenido extraído
print(contenido)

# # Seleccionar el elemento utilizando el selector CSS
# scores = soup.find_all('span', class_='cYwlbu')

# # Obtener el texto de cada elemento span y hacer un print
# text_list = []
# for score in scores:
#     text_list.append(score.text)

# # Imprimir cada elemento de la lista
# for text in text_list:
#     print(text)

