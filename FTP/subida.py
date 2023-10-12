import ftplib

# Credenciales del servidor FTP
FTP_HOST = "ftp.dlptest.com"
FTP_USER = "dlpuser@dlptest.com"
FTP_PASS = "SzMf7rTE4pCrf9dV286GuNe4N"

# conectarse al servidor FTP
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
# forzar la codificación UTF-8
ftp.encoding = "utf-8"
# nombre de archivo local que desea cargar
filename = "some_file.txt"
with open(filename, "rb") as file:
    # use el comando STOR de FTP para cargar el archivo
    ftp.storbinary(f"STOR {filename}", file)
# lista de archivos y directorios actuales
ftp.dir()
# salir y cerrar la conexión
ftp.quit()