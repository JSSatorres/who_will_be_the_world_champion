from year_data import year
from bs4  import BeautifulSoup
import requests

web = 'https://en.wikipedia.org/wiki/2014_FIFA_World_Cup'

response = requests.get(web)

response.text



