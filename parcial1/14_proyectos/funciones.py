
peliculas=[]
def InsertarPeliculas():
        nombre=input("Ingrese el nombre de la pelicula: ") 
        peliculas.append(nombre)
        print("La pelicula fue agregada con exito!")

def EliminarPeliculas():
      nombre=input("Ingrese el nombre de la pelicula: ")
      if nombre in peliculas:
            respuesta=input("Esta seguro de borrar esta pelicula? (SI/NO)").upper()
            if respuesta=="SI":
                  posicion=peliculas.index(nombre)
                  peliculas.pop(posicion)
                  print("La pelicula se ha eliminado correctamente")
            elif respuesta=="NO":
                  print(f"Para volver al menu principal")
      else:
            print("La pelicula no se encuentra en la lista")   

def Consultar():
      print(f"Las peliculas disponibles son: {peliculas}")

def Actualizar():
      nombre=input("Ingrese el nombre de la pelicula: ")
      if nombre in peliculas:
            posicion=peliculas.index(nombre)
            nuevo_nombre=input("Ingrese el nuevo nombre de la pelicula: ")
            peliculas[posicion]=nuevo_nombre
            print("La pelicula fue cambiada con exito")
      else:
            print("La pelicula no se encuentra en la lista")       

def EspereTecla():
    print("Oprima cuaquier tecla para continuar");
    input();

#Ejercicio calculadora 
#Funciones Calculadoras
def solicitarNumeros():
      n1=int(input("Numero # 1:"))
      n2=int(input("Numero # 2:"))
      return n1,n2

def calculadora(n1,n2,opcion):
      if opcion=="1" or opcion=="+" or opcion=="SUMA":
            
            return f"{n1}+{n2}={n1+n2}"
      elif opcion=="2" or opcion=="-" or opcion=="RESTA":
            
            return f"{n1}-{n2}={n1-n2}"
      elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
            
            return f"{n1}*{n2}={n1*n2}"
      elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
  
            return f"{n1}/{n2}={n1/n2}"
      elif opcion=="5" or opcion== "**" or opcion=="POTENCIA":
            
            return f"{n1}**{n2}={n1**n2}"

def raiz():
    n11=int(input("Numero # 1:"))

def calraiz(n11,opcion):    
      return f"{n11}"