# Ejemplos de Condiciones de expected_conditions

## EC.presence_of_element_located(locator)

Espera a que un elemento esté presente en la página.

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

elemento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "mi-elemento")))
```

## EC.visibility_of_element_located(locator)

Espera a que un elemento esté visible en la página.

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

elemento = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='mi-clase']")))
```




## EC.invisibility_of_element_located(locator)

Espera a que un elemento no esté visible en la página.

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='mi-clase']")))
```

## EC.element_to_be_clickable(locator)

Espera a que un elemento sea clickeable.

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

elemento = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='mi-boton']")))
```

## EC.text_to_be_present_in_element(locator, text)

Espera a que el texto especificado esté presente en el elemento ubicado por el locator.

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "saludo"), "Bienvenido"))
```

## EC.title_contains(title)

Espera a que el título de la página contenga el texto especificado.

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WebDriverWait(driver, 10).until(EC.title_contains("Selenium"))
```

## EC.element_to_be_selected(element)

Espera a que el elemento especificado esté seleccionado (por ejemplo, un elemento <input> de tipo checkbox o radio).

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

checkbox = driver.find_element(By.ID, "mi-checkbox")
WebDriverWait(driver, 10).until(EC.element_to_be_selected(checkbox))
```

## EC.alert_is_present()

Espera a que aparezca una alerta (cuadro de diálogo) en la página.

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WebDriverWait(driver, 10).until(EC.alert_is_present())
```