from Calculadora import Calculadora

n1=int(input("numero 1: "))
n2=int(input("numero 2: "))

calculadora=Calculadora(n1,n2)

def menu():
    return int(input(
        """
        Opciones: 
        1. Sumar
        2. Restar
        3. Multiplicar
        4. Dividir
        5. salir
        """
    ))

bandera=True

while bandera:
    opcion=menu()
    if opcion==1:
        print(f"{calculadora.numero1}+{calculadora.numero2}={calculadora.suma()}")
    elif opcion==2:
        print(f"{calculadora.numero1}-{calculadora.numero2}={calculadora.resta()}")
    elif opcion==3:
        print(f"{calculadora.numero1}*{calculadora.numero2}={calculadora.multiplicacion()}")
    elif opcion==4:
        print(f"{calculadora.numero1}/{calculadora.numero2}={calculadora.division()}")
    elif opcion==5:
        bandera=False
    else:
        print("Opcion incorrecta")

