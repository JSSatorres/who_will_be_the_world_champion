# who_will_be_the_world_champion

 la biblioteca lxml, que es necesaria para analizar y extraer datos de HTML en pandas.
https://devhints.io/xpath
 ```python
pip install lxml  
```
Selenium tiene una documentación sobre
cuales eventos dentro del DOM podemos esperarexplícitamente. En esta
documentación encontrarás también como puedes definir tus propios eventos
personalizados

https://selenium-python.readthedocs.io/waits.html

title_is
title_contains
presence_of_element_located
visibility_of_element_located
visibility_of
presence_of_all_elements_located
text_to_be_present_in_element
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable
staleness_of
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be
alert_is_present

Beautiful Soup es una biblioteca de Python diseñada para analizar y extraer datos de documentos HTML y XML de una manera sencilla y eficiente. Proporciona herramientas poderosas para navegar y buscar elementos en una estructura de árbol, lo que permite a los desarrolladores extraer información específica de páginas web de manera programática.

Al usar Beautiful Soup, puedes realizar las siguientes tareas:

Análisis de documentos HTML/XML: Beautiful Soup analiza el código fuente HTML/XML y crea una estructura de árbol, lo que facilita la extracción de datos. Puedes pasarle el contenido HTML/XML de una página web y obtener un objeto BeautifulSoup que representa la estructura del documento.

Navegación en el árbol: Una vez que tienes un objeto BeautifulSoup, puedes navegar por la estructura de árbol utilizando métodos y atributos proporcionados por la biblioteca. Puedes acceder a los elementos padre, hijos y hermanos, y realizar búsquedas específicas basadas en etiquetas, atributos y contenido de texto.

Búsqueda de elementos: Beautiful Soup ofrece métodos de búsqueda flexibles para encontrar elementos específicos en un documento. Puedes buscar elementos por nombre de etiqueta, atributos, contenido de texto y más. Esto es especialmente útil cuando quieres extraer datos específicos de una página web.

Extracción de datos: Una vez que has encontrado los elementos deseados, Beautiful Soup te permite extraer datos de ellos. Puedes acceder a los atributos de los elementos, obtener su contenido de texto o incluso navegar a través de los elementos hijos y extraer información más detallada.

En resumen, Beautiful Soup es una herramienta invaluable para aquellos que deseen extraer datos de páginas web de forma programática. Proporciona una API fácil de usar que simplifica el análisis y la extracción de información de documentos HTML/XML, ahorrando tiempo y esfuerzo en el desarrollo de aplicaciones web y tareas de raspado de datos.