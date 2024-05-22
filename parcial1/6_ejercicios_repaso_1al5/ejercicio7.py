#Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario
numero=int(input("Ingresa un numero: "))
numero2=int(input("ingresa un numero nuevamente: "))
for i in range(numero,numero2):
  if i%2==1:
    print(f"Los numeros inpares son: {i}")
