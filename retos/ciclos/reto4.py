'''
Pedir 20 números y contar cuantos de los ingresados fueron negativos
'''

print("Vamos a ingresar 20 numero y a descubrir cuantos de los ingresados fueron negativos")
contadorNegativos=0
numeros=[]
for i in range(20):
    n=int(input("\nIngrese un numero: "))
    numeros.append(n)
    if n<0:
        contadorNegativos+=1

print("los numeros ingresados fueron: ")
print(numeros)

print(f"La cantidad de numero negativos fueron: {contadorNegativos}")