import mysql.connector

#Conexion con la BD de MySQL
try:
    conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password=''
)
    
    #Crear un objeto de tipo cursor para ejecutar SQL
    micursor=conexion.cursor()

    sql="create database bd_python"

    micursor.execute(sql)

except Exception as e:
    print(f"Error: {e}")
    print(f"Tipo de error: {type(e)._name_}")
    print(f"Ocurrio un error, porfavor vuelvalo a intentar más tarde...")
else: 
    print(f"Se creo la BDe exitosamente")
    micursor.execute("Show databases")
    for x in micursor:
        print(x)


