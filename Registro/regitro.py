import os.path
import time

def log_edit(file_path):
    if not os.path.exists(file_path):
        print(f"El archivo {file_path} no existe.")
        return

    # Obtiene la fecha y hora actual
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # Obtiene la fecha y hora de la última modificación del archivo
    mod_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime(file_path)))

    # Escribe el registro en un archivo de texto
    with open("registro.log", "a") as log_file:
        log_file.write(f"El archivo {file_path} fue editado el {mod_time} ({current_time})\n")

# Ejemplo de uso
log_edit("D:\Programacion\Python\Sandboxed\sandbox.py")
log_edit("D:\Programacion\Python\Sandboxed\setup.sh")