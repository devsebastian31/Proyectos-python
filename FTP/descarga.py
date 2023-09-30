import ftplib

FTP_HOST = "ftp.dlptest.com"
FTP_USER = "dlpuser@dlptest.com"
FTP_PASS = "SzMf7rTE4pCrf9dV286GuNe4N"

# conectarse al servidor FTP
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
# forzar la codificación UTF-8
ftp.encoding = "utf-8"
# el nombre del archivo que desea descargar del servidor FTP
filename = "some_file.txt"
with open(filename, "wb") as file:
    # use el comando RETR de FTP para descargar el archivo
    ftp.retrbinary(f"RETR {filename}", file.write)

# salir y cerrar la conexión
ftp.quit()