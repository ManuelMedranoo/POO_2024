from conexionBD import *

try:
    micursor=conexion.cursor()
    sql="update clientes set direccion='Col. del utd' where id=1"

    micursor.execute(sql) 
    #Es necesario ejecutar
    conexion.commit()

except:
    print(f"Ocurrió un error por favor vuelva inentar más tarde...")
else:
    print("Registros Actualizado con éxito")