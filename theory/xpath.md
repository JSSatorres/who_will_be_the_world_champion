## Resumen de XPath con ejemplos de selectores, operadores y rutas

1. Selector de etiqueta:
   - Utiliza el nombre de la etiqueta para seleccionar elementos específicos. Por ejemplo:

    ```xpath
     //div
     ``` 
     seleccionará todos los elementos `div` en el documento.

2. Selector de atributo:
   - Utiliza el símbolo `@` seguido del nombre del atributo para seleccionar elementos basados en un atributo específico. Por ejemplo: 

   ```xpath
     //input[@type="text"]
  ``` 
     seleccionará todos los elementos `input` con el atributo `type` establecido en "text".

3. Selector de posición:
   - Utiliza corchetes y un número para seleccionar elementos en una posición específica. Por ejemplo: 

   ```xpath
     (//div)[3]
    ``` 
     seleccionará el tercer elemento `div` en el documento.

4. Combinación de selectores:
   - Puedes combinar diferentes selectores utilizando operadores lógicos para refinar aún más tu selección.
   - El operador `or` se utiliza para seleccionar elementos que cumplen con cualquiera de los selectores. Por ejemplo: 

   ```xpath
     //input[@type="text" or @type="password"]
    ```
      seleccionará todos los elementos `input` con el atributo `type` establecido en "text" o "password".
   - El operador `and` se utiliza para seleccionar elementos que cumplen con varios selectores. Por ejemplo:

    ```xpath
     //input[@type="text" and @name="username"]
     ``` 

     seleccionará todos los elementos `input` con el atributo `type` establecido en "text" y el atributo `name` establecido en "username".

5. Uso del contenido de texto:
   - Puedes utilizar el método `text()` para seleccionar elementos basados en su contenido de texto. Por ejemplo:

    ```xpath
     //p[text()="Hola"]
     ``` 

     seleccionará todos los elementos de párrafo que contengan la palabra "Hola".

6. Rutas relativas y rutas absolutas:
   - Las rutas relativas comienzan con un elemento específico en el documento y siguen una jerarquía descendente. Por ejemplo:

    ```xpath
     //div/span
     ``` 

     seleccionará todos los elementos `span` que están dentro de un elemento `div`, en cualquier nivel de profundidad.

   - Las rutas absolutas comienzan desde la raíz del documento con dos barras (`//`) o con una sola barra (`/`). Por ejemplo:

    ```xpath
     /html/body/div
     ``` 
     
     seleccionará el elemento `div` que es hijo directo del elemento `body`, que a su vez es hijo directo del elemento `html`.

Estos son solo algunos ejemplos básicos de cómo actuar con XPath y utilizar diferentes selectores, operadores y rutas. Puedes combinarlos y ajustarlos según tus necesidades para seleccionar elementos específicos en documentos HTML o XML.