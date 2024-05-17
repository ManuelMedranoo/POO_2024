#existe una condicion llama "if"
#la cual evalua una condicion para encontrar el valor "true" y si se cumple
#la condicion se ejecuta la linea o lineas de codigo


#Ejemplo 1 if simple
color=input("Ingrese un color: ")

if color=="rojo":
    print("Soy el color rojo")
    
#Ejemplo 2 if compuesto
    color=input("Ingrese un color: ")

if color=="rojo":
    print("Soy el color rojo")
else:
    print("No soy el color rojo")

    #Ejemplo 3 if anidado
    color=input("Ingrese un color: ")

if color=="rojo":
    print("Soy el color rojo")
    if color=="rojo":
     print("No soy el color rojo")
else:
    print("No soy el color rojo soy otra cosa")

        #Ejemplo 4 if y elif
    color=input("Ingrese un color: ")

if color=="rojo":
    print("Soy el color rojo")
elif color=="amarillo":
    print("soy el color amarillo")
elif color=="Azul":
    print("soy el color azuel")
elif color=="morado":
    print("soy el color morado")
else:
    print("No soy ningun de los anteriores")

    #Crear un programa que solicite el numero de la semana 
    #e imprima en pantalla el dia que le corresponde

    dia=int(input("Ingrese un numero: "))
    if dia=="1":
        print("Domingo")
    elif dia=="2":
        print("Lunes")
    elif dia=="3":
        print("martes")
    elif dia=="4":
        print("Miercoles")
    elif dia=="5":
        print("Jueves")
    elif dia=="6":
        print("viernes")
    elif dia=="7":
        print("Sabado")
    else:
        print("Este numero no corresponde a ningun dia")
    