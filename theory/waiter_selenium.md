## Resumen de Esperas (Waits) en Selenium con ejemplos

En Selenium, las esperas (waits) son utilizadas para sincronizar la interacción con los elementos de una página web, asegurándose de que estén disponibles antes de realizar acciones sobre ellos. Los tipos de esperas más comunes son:

1. Espera explícita (`Explicit Wait`):
   - Se utiliza para esperar hasta que se cumpla una determinada condición antes de continuar con la ejecución del código.
   - Ejemplo: Esperar hasta que un elemento esté visible antes de hacer clic en él. 
   
   ```python
     from selenium.webdriver.common.by import By
     from selenium.webdriver.support.ui import WebDriverWait
     from selenium.webdriver.support import expected_conditions as EC

     # Crear una instancia de WebDriverWait
     wait = WebDriverWait(driver, 10)  # Esperar hasta 10 segundos

     # Esperar hasta que el elemento esté visible
     element = wait.until(EC.visibility_of_element_located((By.ID, 'myElement')))

     # Realizar acciones sobre el elemento
     element.click()
     ```

2. Espera implícita (`Implicit Wait`):
   - Se establece un tiempo máximo para esperar que los elementos estén disponibles antes de lanzar una excepción.
   - Ejemplo: Configurar una espera implícita de 5 segundos. ```python
     driver.implicitly_wait(5)  # Esperar hasta 5 segundos

     # Realizar acciones sobre los elementos de la página
     ```

3. Espera de tiempo de carga de página (`Page Load Wait`):
   - Se espera a que la página se cargue completamente antes de continuar con las siguientes acciones.
   - Ejemplo: Esperar hasta que la página se cargue completamente. ```python
     driver.set_page_load_timeout(10)  # Esperar hasta 10 segundos para que se cargue la página

     # Realizar acciones después de que la página se haya cargado completamente
     ```

Estos son solo algunos ejemplos básicos de los tipos de esperas en Selenium y cómo se pueden utilizar. Puedes ajustar los tiempos y las condiciones según tus necesidades para una interacción más robusta con los elementos de la página web.