'''
Construir un programa que reciba el tamaño de una lista y la llene con números entregados por el usuario
'''

tamaño=int(input("Ingrese la cantidad numeros que desea agregar: "))
numeros=[]

for i in range(tamaño):
    numeros.append(int(input("Ingrese un numero: ")))

print(numeros)