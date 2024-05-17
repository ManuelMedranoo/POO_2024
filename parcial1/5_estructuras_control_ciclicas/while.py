#el Ciclo while es una estructura iterativa que se ejecuta X veces siempre y cuando la condicion se cumpla y se 
#seguira ejecutando como sea true la condicion

#sintaxis
#--while--condicion:
# bloque de instrucciones 

# Ejemplo 1 crear un programa que se imprima en pantalla 5 veces
#el @

contador=1

while contador<=5:
    print("@")
    contador+=1

# #Crear un programa que imprima los numeros del 1 al 5 y los sume y al final imprima la suma 
contador=1
suma=0
while contador<=10:
     print(contador)
     suma+=contador
     contador+=1
      
print(f"la suma es: {suma}")


# #Ejemplo 3 crear un programa que imprima la tabla de multiplicar que el usuario desee 

tabla=int(input("Ingrese un numero para calcular su tabla de multiplicar: "))

i=1
multi=0

while i<=10:
     multi=i*tabla
     print(f"{tabla} X {i} = {multi}")
     i+=1