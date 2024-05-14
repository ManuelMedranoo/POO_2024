#concatenar cadenas de caracteres con contenido de variables 

nombre="Manuel Medrano"
especialidad="Area de Desarrollo de SW Multiplataforma"
carrera="Ingeniero en Gestion y Desarrollo de SW"

#1er forma de concatenar
print("Mi nombre es: "+nombre+" estoy en la especialidad de: "+especialidad+" en la carrera de: "+carrera)
print("/n")
#2da forma de concatenar
print("Mi nombre es: ",nombre," estoy en la especialidad de: ",especialidad," en la carrera de: ",carrera)
print("/n")
#3era forma de concatenar es la mas comun en python
print(f"Mi nombre es: {nombre} estoy en la especialidad de: {especialidad} en la carrera de: {carrera}")
#4ta forma de concatenar
print("Mi nombre es:{} estoy en la especialidad de: {}, en la carrera de: {}".format(nombre,especialidad,carrera))
print("/n")
#5ta forma de concatenar 
print('Mi nombre es: '+nombre+' estoy en la especialidad de: '+especialidad+', en la carrera de: '+carrera)
