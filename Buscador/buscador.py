import os

GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
HEADER = '\033[95m'
IMPORTANT = '\33[35m'
NOTICE = '\033[33m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
RED = '\033[91m'
END = '\033[0m'
UNDERLINE = '\033[4m'
LOGGING = '\33[34m'

def buscar_archivos(directorio, extension):
    archivos_encontrados = []
    for raiz, directorios, archivos in os.walk(directorio):
        for archivo in archivos:
            if archivo.endswith(extension):
                archivos_encontrados.append(os.path.join(raiz, archivo))
    return archivos_encontrados

# Ejemplo de uso
directorio_a_buscar = input("Directorio a buscar: ") # /ruta/al/directorio/a/buscar  Ruta al directorio a buscar
extension_a_buscar = input("Extension: ") # .pdf  Extension

archivos_encontrados = buscar_archivos(directorio_a_buscar, extension_a_buscar)

for archivo in archivos_encontrados:
    print(archivo)