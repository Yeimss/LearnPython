'''
Leer 8 ciudades colombianas, guardarlas en una lista y mostrar en orden inverso los datos ingresados
'''

ciudades=[]
for i in range(8):
    ciudades.append(input("Ingrese una ciudad colombiana: "))

ciudades.reverse()
print(ciudades)