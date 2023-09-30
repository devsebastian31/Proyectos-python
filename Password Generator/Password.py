import string
import random

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

lower = "abcdefghijklmnñopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ "
numbers = "0123456789"
symbols = "[]{}()*;/,._-!$%?@#"

all = lower + upper + numbers + symbols # Combinación
length =  15

characters = string.ascii_letters + string.digits + string.punctuation

# Generar la contraseña aleatoria
password = ''.join(random.choice(characters) for i in range(16))

# Guardar la contraseña en un archivo key
with open('clave.key', 'w') as file:
    file.write(password)

print(f"La contraseña generada es: {password}")
print("Se ha guardado la contraseña en el archivo clave.key")