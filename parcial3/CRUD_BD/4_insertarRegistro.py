from conexionBD import*

try:
    micursor=conexion.cursor()
    sql="INSERT INTO clientes (id, nombre, direccion) Values (NULL, 'Jose Gonzalez', 'col Palmas', '1232333333');"
    micursor.execute(sql)
    
    conexion.commit()
except:
    print(f"Ocurrio un error")
else:
    print("El registro se inserto correctamente")    

