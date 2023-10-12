import os
import time
import datetime

def modificar_fecha_carpeta(ruta_carpeta, nueva_fecha):
    # Convierte la nueva fecha en formato de tiempo
    nueva_fecha_tiempo = time.mktime(nueva_fecha.timetuple())

    # Modifica la fecha de creación de la carpeta o archivo
    os.utime(ruta_carpeta, (nueva_fecha_tiempo, nueva_fecha_tiempo))
    print("Fecha de creación modificada con éxito.")

# Ruta de la carpeta o archivo que deseas modificar
#ruta = 'R:\\Nube\\Copia de Seguridad Completa\\Carpeta'
ruta = 'D:\Descargas\Carpeta'

# Nueva fecha de creación (ejemplo: 1 de enero de 2023 a las 12:00 PM)
nueva_fecha = datetime.datetime(2023, 6, 4, 22, 19)

# Llama a la función para modificar la fecha de creación
modificar_fecha_carpeta(ruta, nueva_fecha)
