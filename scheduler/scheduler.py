import sched
import time
import subprocess

# Función que ejecutará tu script de Selenium
def ejecutar_script():
    # Ruta al intérprete de Python y tu script de Selenium
    ruta_python = "C:/ruta/a/tu/python"
    ruta_script = "D:/ruta/a/tu/script.py"

    # Ejecutar el script usando subprocess
    subprocess.run([ruta_python, ruta_script])

# Crear un objeto de la clase sched.scheduler
programador = sched.scheduler(time.time, time.sleep)

# Calcula el tiempo hasta las 10:00 AM
hora_ejecucion = time.mktime(time.strptime("10:00:00", "%H:%M:%S"))

# Programa la ejecución de tu script a las 10:00 AM
programador.enterabs(hora_ejecucion, 1, ejecutar_script, ())

# Inicia el programa
programador.run()