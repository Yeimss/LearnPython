""" Construir un programa que reciba el tamaño de una lista  y la llene con múltiplos de 7 """

tamaño=int(input("Ingrese la cantidad de multiplos del 7 que desea conocer: "))
multiplos=[]

for i in range(0, tamaño):
    multiplos.append((i+1)*7)

print(multiplos)

