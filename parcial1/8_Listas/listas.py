
"""
list(Array)
son colecciones o conjunto de datos/valores bajo
un mismo nombre para acceder a los valores se hace
con un indice numerico

nota: sus valores si son modificables

la lista es una colecion ordenda y modificable permite miembros
duplicados

"""


# Ejemplo 1 crear una lista con valores numericos enteros e imprimir lista

numeros=[23,34]
print(numeros)

# recorer la lista con un for
for i in numeros:
    print(i)

# recorer la lista con un while
i=0
while i<len(numeros):
    print(numeros[i])
    i+=1

# crear una lista de palabras posterior mente ingresar una palabra para buscar la concidencia en la lista e indicar si aparece la pa
# palabra y en que posicion en caso contrario indicar una sola vez si no la encontro

palabras=("hola","2024","10,23","True")
print(palabras) 
noloencontro=True
palabra_buscar=input("ingrese la palabra a buscar: ")
for i in palabras:
    if palabra_buscar==i:
        print(f"Enconte la palabra {palabra_buscar}, en la posicion {palabras.index(i)}")
        noloencontro=False

if noloencontro:
  print(f"No se encontro la palabra dentro de la lista")

i=0
while i<len(palabras):
   if palabra_buscar==palabras[1]:
        print(f"Enconte la palabra {palabra_buscar}, en la posicion {palabras.index(i)}")
        noloencontro=False
if noloencontro:
  print(f"No se encontro la palabra dentro de la lista")


# ejemplo 3 crear una listae multilinea o multidimensional (matriz) para crear una agenda telefonica
agenda=[
["carlos",6181234567], 
["Fernando",6182334567],
["Juan polainas",6182332345],
]
print(agenda)

for i in agenda:
    print(f"{agenda.index(i)+1}.-{i}")


  