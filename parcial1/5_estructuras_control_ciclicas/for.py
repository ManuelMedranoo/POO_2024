#Ciclo for es una estructura iterativa que se ejecuta X veces

#sintaxis
#--For--Variable in elemento iterable (lista, rango,etc):
# bloque de instrucciones 

# Ejemplo 1 crear un programa que se imprima en pantalla 5 veces
#el @

for contador in range(1,6):
 print("@")
 print()
#Crear un programa que imprima los numeros del 1 al 5 y los sume y al final imprima la suma 

suma=0
for contador in range (1,6):
    print(contador)
    suma+=contador 

print(f"La suma es: {suma}")

#Ejemplo 3 crear un programa que imprima la tabla de multiplicar que el usuario desee 

tabla=int(input("Ingrese un numero para calcular su tabla de multiplicar: "))


multi=0

for i in range(1,11):
    multi=i*tabla
    print(f"tabla X {i} = {multi}")
