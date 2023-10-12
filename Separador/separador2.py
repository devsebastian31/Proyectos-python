import os
import shutil
import time

# directorio que contiene los archivos a ordenar
directorio = 'D:\Descargas\word'

while True:
    # obtener una lista de archivos en el directorio
    archivos = os.listdir(directorio)
    
    # ordenar la lista de archivos por fecha de modificación (de más antiguo a más nuevo)
    archivos.sort(key=lambda x: os.path.getmtime(os.path.join(directorio, x)))
    
    # mover los archivos ordenados a una carpeta llamada "ordenados"
    for archivo in archivos:
        shutil.move(os.path.join(directorio, archivo), os.path.join(directorio, 'ordenados', archivo))
    
    # dormir el programa durante 10 segundos antes de volver a ordenar los archivos
    time.sleep(10)