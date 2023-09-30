import os

def es_malicioso(archivo):
    if "archivo3.txt" in archivo:
        return True
    else:
        return False
for raiz, carpetas, archivos in os.walk("D:/Programacion/Python/Antivirus/Prueba"):
    for archivo in archivos:
        ruta_completa = os.path.join(raiz, archivo)
        if es_malicioso(archivo):
            print(f"El archivo {ruta_completa} es malicioso")
            # Aquí puedes agregar código para eliminar el archivo
os.remove(ruta_completa)