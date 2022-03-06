"""
Leer 20 números enteros y guardar en una lista, después permitir 
que el usuario busque un número y si este se encuentra en la lista 
indicar con un mensaje que el resultado es exitoso

"""

from ast import Break


print("------------Vamos a ingresar 20 numeros a una lista------------")
numeros=[]
for i in range(20):
    numeros.append(int(input("Ingrese un numero: ")))

print("----------Ahora vamos a buscar un numero en la lista----------")

intento=True
adivine=False
while intento:
    respuesta=int(input("Desea intentar adivinar un numero?\n1.Sí.\n2.No.\n"))
    if respuesta==1:
        numeroAdivinado=int(input("Ingrese un numero para ver si está en la lista: "))
        if numeroAdivinado in numeros:
            adivine=True
            break
        else:
            print(f"el numero {numeroAdivinado} no se encuentra en la lista")
    elif respuesta==2:
        intento=False
        break
    else:
        print("respuesta invalida, intente de nuevo\n\n")


if adivine:
    print("Felicidades, encontraste un numero de la lista")
if not adivine:
    print("Más suerte a la proxima")
    

