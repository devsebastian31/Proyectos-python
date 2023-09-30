import os
import shutil

# Definir la ruta a escanear
ruta_escaneo = 'D:\Programacion\Python\Antivirus\Prueba'

# Definir la lista de extensiones de archivos maliciosos
extensiones_maliciosas = ['.exe', '.dll', '.vbs', '.bat']

# Recorrer todos los archivos en la ruta de escaneo
for foldername, subfolders, filenames in os.walk(ruta_escaneo):
    for filename in filenames:
        # Verificar si la extensión del archivo es maliciosa
        if any(ext in filename for ext in extensiones_maliciosas):
            archivo_malicioso = os.path.join(foldername, filename)
            print(f"Archivo malicioso encontrado: {archivo_malicioso}")
            # Eliminar el archivo malicioso
            try:
                os.remove(archivo_malicioso)
                print(f"Archivo malicioso eliminado: {archivo_malicioso}")
            except:
                print(f"No se pudo eliminar el archivo: {archivo_malicioso}")