import os
from funciones import solicitarNumeros,calculadora,EspereTecla,raiz,calraiz
opcion=True
while opcion:
    os.system("cls")
    print("\n\t..:: CALCULADORA BÁSICA ::.. \n 1.- Suma \n 2.- Resta \n 3.- Multiplicacion \n 4.- División \n 5.- Potencia \n 6.- Raiz \n 7.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()
    
    if opcion in ("SUMA","1","+","RESTA","2","-","MULTIPLICACION","3","*","DIVISION","4","/","POTENCIA","**","5"):
        n1,n2=solicitarNumeros()
        print(calculadora(n1,n2,opcion))
        EspereTecla()
    elif opcion in ("Raiz","6"):
        n11=raiz()
        print(calraiz(n1,opcion))
        EspereTecla()
    else:
        opcion=False
        print("Gracias por utilizar el sistema ...")    