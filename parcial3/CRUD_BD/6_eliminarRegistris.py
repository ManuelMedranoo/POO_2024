from conexionBD import *

try:
    micursor=conexion.cursor()
    sql="delete from clientes WHERE id=1"

    micursor.execute(sql)
    #Es necesario ejecutar
    conexion.commit()

except:
    print(f"Ocurrió un error por favor vuelva inentar más tarde...")
else:
    print("Registros Eliminado con éxito")