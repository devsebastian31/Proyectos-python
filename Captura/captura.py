import pyautogui
import time
import os
import psutil

# Crea una carpeta para guardar las capturas
carpeta = 'capturas'
if not os.path.exists(carpeta):
    os.mkdir(carpeta)

# Define el intervalo de tiempo entre cada captura
intervalo_captura = 5  # segundos

# Toma las capturas y guárdalas en la carpeta hasta que la PC se apague
while psutil.Process().pid != 1:
    # Define el nombre del archivo de la captura
    nombre_archivo = f'captura{time.time()}.png'

    # Toma la captura y guárdala en la carpeta
    screenshot = pyautogui.screenshot()
    screenshot.save(os.path.join(carpeta, nombre_archivo))

    # Espera el intervalo de tiempo antes de tomar la siguiente captura
    time.sleep(intervalo_captura)