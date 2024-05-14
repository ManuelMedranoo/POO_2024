"""
Comentario de varias lineas
Nota: A la hora de concatenar cadenas no es posible incluir en 
algunas ocaciones contenido de variables que no sean de tipo str

"""

#comentario de una linea 

#concatenar un srt con srt 


texto="soy una cadena de texto"
numero=23
numero_str=str(numero)

#concatenar un int con srt
print("El numero :"+numero_str)

print("El numero: "+str(numero))

#concatenar un str con int

n1='23'
n2=33

suma=int(n1)+n2

print("El numero: "+str(suma))

#concatenar un float con str

n1='23'
n2=33.0

suma=int(n1)+n2

print("El numero: "+str(suma))
print(f"El numero:{suma}")

#Concatenar un float y float con float

n1='23.34'
n2='33.99'

suma=float(n1)+float(n2)

print(f"El numero es {suma}")