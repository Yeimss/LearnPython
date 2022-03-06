'''
Codificar un programa que presente un menú de 4 opciones y reciba un numero 
natural  para realizar las siguientes operaciones:
	
	0: Salida
	1: Encuentre si el número es múltiplo de 2
	2: Encuentre la raíz cuadrada del número
   	3: Sume 100 al número ingresado
 	4: Eleve a la 2 el número ingresado
'''
import math
def menu():
    return int(input("\n\n--------- MENU ----------\n"+
    "0: Salida\n"+
	"1: Encuentre si el número es múltiplo de 2\n"+
	"2: Encuentre la raíz cuadrada del número\n"+
   	"3: Sume 100 al número ingresado\n"+
 	"4: Eleve a la 2 el número ingresado\n"+
    "Digite la opcion que desea: "))

flag=None
while flag!=0:
    opcion=menu()
    if opcion==1:
        numero=int(input("Ingrese un numero para saber si es multiplo de 2: "))
        if numero%2==0:
            print(f"Efectivamente, el {numero} es multiplo de 2 😎")
        else:
            print("No es multiplo del 2 .-.")
    elif opcion==2:
        numero=int(input("Ingrese un numero para saber su raiz cuadrada: "))
        print(f"La raiz cuadrada de {numero} es: {math.sqrt(numero)}")
    elif opcion==3:
        numero=int(input("Ingrese un numero para sumarle 100: "))
        print(f"{numero}+100= {numero+100}")
    elif opcion==4:
        numero=int(input("Ingrese un numero para elevarlo al cuadrado: "))
        print(f"{numero}^2= {math.pow(numero,2)}")
    elif opcion==0:
        flag=0
        break
    else:
        print("Opcion incorrecta ._., ingrese otro numero")

    