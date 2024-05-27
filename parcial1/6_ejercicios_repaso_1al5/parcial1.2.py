
kwh=int(input("Ingrese la cantidad de kwh: "))
if kwh<=150:
    print("Tarifa basica")
    tarifa=(kwh*0.987)
    iva=(0.16*tarifa)+tarifa+12.56
    print(f"Total a pagar por el recibo es {iva}")
elif kwh>150:
    print("Tarifa Intermedaria")
    tarifa2=(kwh*1.203)
    iva1=(0.16*tarifa2)+tarifa2+12.56
    print(f"Total a pagar por el recibo es {iva1}")
