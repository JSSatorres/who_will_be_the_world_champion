import pandas as pd
from string import ascii_uppercase as alfabeto
import pickle

all_tables = pd.read_html('https://web.archive.org/web/20221115040351/https://en.wikipedia.org/wiki/2022_FIFA_World_Cup')


# print(all_tables[19].columns[1] = 'Team')
dict_tables = {} 

# for in con range(primera posicion, ultima poscion, intervalo)
for letter, i in  zip(alfabeto, range(12,68,7)):
  df = all_tables[i]
  df.rename(columns={df.columns[1]:'Team'},inplace=True)
  df.pop('Qualification')
  dict_tables[f'Grupo {letter}'] = df
  # print(dict_tables['Grupo {letter}'])
  # print('\n') 

with open('dict_table', 'wb') as output:
     pickle.dump(dict_tables,output)