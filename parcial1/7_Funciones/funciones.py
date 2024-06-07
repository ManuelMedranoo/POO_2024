"""
Una función es un conjunto de instrucciones
agrupadas bajo un nombre en particular como un 
programa más pequeño que cumple una función
específica . La función se puede reutilizar con 
el simple hecho de invocarla es decir mandarla 
llamar 

"""
#sintaxis
# def nombre de mi funcion(parametros):
#     bloque o conjunto de instrucciones 
    
#     nombre de mi funcion(parametros)
# las funciones pueden ser de 4 tipos 
# 1.- funcion que no recibe parametros y no regresa valor
# 2.- Funcion que no recibe parametros y regresa valor

 #funcion que no recibe parametros y no regresa valor
# def sumaNumeros1():
#     n1=int(input("Numero # 1:"))
#     n2=int(input("Numero # 2:"))
#     suma=n1+n2
#     print(f"{n1}+{n2}={suma}")
#     print(f"{n1}+{n2}={suma}")


# 2.- Funcion que no recibe parametros y regresa valor    
# def sumaNumeros2():
#     n1=int(input("Numero # 1:"))
#     n2=int(input("Numero # 2:"))
#     suma=n1+n2
#     return f"{n1}+{n2}={suma}"
    
# print(sumaNumeros2())

 #funcion que  recibe parametros y no regresa valor
def sumaNumeros3(n1,n2):
   
    suma=n1+n2
    print(f"{n1}+{n2}={suma}")


# n1=int(input("Numero # 1:"))
# n2=int(input("Numero # 2:"))
# sumaNumeros3(n1,n2)


 #funcion que  recibe parametros y  regresa valor
# def sumaNumeros4(n1,n2):
   
#     suma=n1+n2
#     return f"{n1}+{n2}={suma}"


# n1=int(input("Numero # 1:"))
# n2=int(input("Numero # 2:"))
# print(sumaNumeros4(n1,n2))

#crear un programa que solicite a traves de una funcion la siguiente 
#informacion Nombre del Paciente Edad Estatura Tipo de sangre Utilizar lo 4 tipos de funciones 