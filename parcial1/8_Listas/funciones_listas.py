paises=["Mexico","USA","Brasil","China"]
numeros=[100,80,3.1416,75]
varios=["UTD",True,100,0.100]
#ordenar listas
print(paises)
paises.sort()
print(paises)

print(numeros)
numeros.sort()
print(numeros)

# print(varios)
# varios.sort()
# print(varios)

#agregar elementos a la lista
print(numeros)
numeros.append(100)
print(numeros)
numeros.insert(len(numeros),200)
print(numeros)

#Remover elementos 
print(numeros)
numeros.remove(100)
print(numeros)
numeros.pop(2)
print(numeros)
#dar la vuelta a los elementos de una lista
print(varios)
varios.reverse()
print(varios)
#buscar un valor un dato dentro de una lista
encontro="Brasil" in paises
print(encontro)
#Vaciar o borrar el contenido de una lista
print(paises)
paises.clear()
print(paises)
#unir listas
print(varios)
varios.extend(numeros)
print(varios)