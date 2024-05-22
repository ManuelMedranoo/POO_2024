#Crear un programa que solicite la calificacion de 15 alumnos e imprimir en pantalla cuantos aproboron y cuantos no aprobaron
contador=0
contador1=0
for i in range(1,16):
    calificacion=float(input("Ingrese la calificacion: "))
    if calificacion>=8:
        contador+=1
    else:
        contador1+=1

print(f"Total de alumnos aprobado:{contador}")
print (f"Total de alumnos reprobados:{contador1} ")
