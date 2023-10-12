from smb.SMBConnection import SMBConnection

# Crea una conexión SMB
conn = SMBConnection('Sebastian', 'python 444', 'nube', 'WORKGROUP', use_ntlm_v2=True)

# Conecta con el servidor
if conn.connect('10.10.10.1', 445):
    # Si la conexión es exitosa, imprime un mensaje
    print("Conexión exitosa")

    # Obtiene la lista de archivos y directorios en una carpeta del servidor
    files = conn.listPath('Respaldo', '')

    # Imprime la lista de archivos y directorios
    for file in files:
        print(file.filename)

    # Cierra la conexión
    conn.close()
else:
    # Si la conexión falla, imprime un mensaje
    print("Error al conectar al servidor")
