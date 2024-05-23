contador=0
promedio=0
promedio2=0
paciente="si"
while paciente== "si":
    nombre=str(input("Nombre del paciente: "))
    tipo=str(input("Tipo de sangre: "))
    for mediciones in range(3):
        precion1=float(input("la presion numero SIS fue: "))
        precion2=float(input("la presion numero DIA fue: "))

        promedio += precion1
        promedio2 += precion2
    precionfi=float(input("Presion arterial final es : "))
    promedio /=3
    promedio2 /= 3
    
    precionul=(promedio+precionfi)/2
    print(F"El promedio de las presiones arteriales es: {promedio}")  
    print(f"la presion arterial final es: {precionul}")
    if promedio<=120 and precionfi<=80:
        print("Presenta una presion normal")
    contador+=1      
    paciente=input("Deseas agregar otro paciente:").upper
print(f"EL total de pacientes es: {contador}") 