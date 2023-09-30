import mysql.connector

# Establecer la conexión con la base de datos
cnx = mysql.connector.connect(
    user='mouredev_read',
    password='mouredev_pass',
    host='mysql-5707.dinaserver.com',
    database='moure_test'
)

# Crear un cursor para ejecutar consultas SQL
cursor = cnx.cursor()

# Ejecutar una consulta
consulta = "SELECT * FROM `challenges`"
cursor.execute(consulta)

# Obtener los resultados de la consulta
resultados = cursor.fetchall()

# Recorrer los resultados e imprimirlos
for fila in resultados:
    print(fila)

# Cerrar el cursor y la conexión
cursor.close()
cnx.close()