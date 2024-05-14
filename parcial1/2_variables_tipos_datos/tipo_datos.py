#Los tipos de datos mas comunes en python son:
#primitivos o primario
# int "Entero"
# float "real"
# bool "logico"

# Estructurados
# str "cadena"
# list "lista"
# tuple
# dict "como un objeto"

#variables
entero=80
real=3.1416
caracter='@'
logico=False

#Ejemplo de estructurados 
palabra="hola"
lista=[10,20,30,40]
lista2=["hola",'true','@',30,1.8]
tupla=("Hola","como","estas?")
diccinario={
    "nombre":"Daniel",
    "apellidos":"Contreras Ramirez",
    "especialidad":"TI",
    "Edad":20
}
#Mostrar los tipos de datos
print(type(entero))
print(type(real))
print(type(caracter))
print(type(logico))
print(type(palabra))
print(type(lista))
print(type(lista2))
print(type(tupla))
print(type(diccinario))