import ftplib
import os
from datetime import datetime

FTP_HOST = "ftp.ed.ac.uk"
FTP_USER = "anonymous"
FTP_PASS = ""
# FTP_HOST = "192.168.1.1"
# FTP_USER = "admin"
# FTP_PASS = "586290929699"

# algunas funciones de utilidad que vamos a necesitar
def get_size_format(n, suffix="B"):
    # convierte bytes a formato escalado (por ejemplo, KB, MB, etc.)
    for unit in ["", "K", "M", "G", "T", "P"]:
        if n < 1024:
            return f"{n:.2f}{unit}{suffix}"
        n /= 1024


def get_datetime_format(date_time):
    # convertir a objeto de fecha y hora
    date_time = datetime.strptime(date_time, "%Y%m%d%H%M%S")
    # convertir a una cadena de fecha y hora legible por humanos
    return date_time.strftime("%Y/%m/%d %H:%M:%S")


# inicializar sesión FTP
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
# forzar la codificación UTF-8
ftp.encoding = "utf-8"
# imprimir el mensaje de bienvenida
print(ftp.getwelcome())
# cambie el directorio de trabajo actual a la carpeta 'pub' y la subcarpeta 'maps'
ftp.cwd("pub/maps")

# LISTA de un directorio
print("*"*50, "LIST", "*"*50)
ftp.dir()

# Comando NLST
print("*"*50, "NLST", "*"*50)
print("{:20} {}".format("File Name", "File Size"))
for file_name in ftp.nlst():
    file_size = "N/A"
    try:
        ftp.cwd(file_name)
    except Exception as e:
        ftp.voidcmd("TYPE I")
        file_size = get_size_format(ftp.size(file_name))
    print(f"{file_name:20} {file_size}")


print("*"*50, "MLSD", "*"*50)
# utilizando el comando MLSD
print("{:30} {:19} {:6} {:5} {:4} {:4} {:4} {}".format("File Name", "Last Modified", "Size",
                                                    "Perm","Type", "GRP", "MODE", "OWNER"))
for file_data in ftp.mlsd():
    # extraer datos devueltos
    file_name, meta = file_data
    # es decir, directorio, archivo o enlace, etc.
    file_type = meta.get("type")
    if file_type == "file":
        # si es un archivo, cambie el tipo de transferencia de datos a IMAGEN/binario
        ftp.voidcmd("TYPE I")
        # obtener el tamaño del archivo en bytes
        file_size = ftp.size(file_name)
        # convertirlo a un formato legible por humanos (es decir, en 'KB', 'MB', etc.)
        file_size = get_size_format(file_size)
    else:
        # no es un archivo, puede ser un directorio u otros tipos
        file_size = "N/A"
    # fecha de la última modificación del archivo
    last_modified = get_datetime_format(meta.get("modify"))
    # file permissions
    permission = meta.get("perm")
    
    # obtener la identificación única del archivo
    unique_id = meta.get("unique")
    # grupo de usuario
    unix_group = meta.get("unix.group")
    # modo archivo, permisos unix
    unix_mode = meta.get("unix.mode")
    # Dueño del archivo
    unix_owner = meta.get("unix.owner")
    # imprimir todo
    print(f"{file_name:30} {last_modified:19} {file_size:7} {permission:5} {file_type:4} {unix_group:4} {unix_mode:4} {unix_owner}")


# salir y cerrar la conexión
ftp.quit()