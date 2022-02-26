#soy un comentario
'''
soy un comentario de bloque
'''

nombreUsuario="Chente Fernandez"

#--------concatenar con f print----------
print(f"Su nombre es: {nombreUsuario}")


#-------tipos de variables---------------

edadUsuario=23              #int/entero
estatura=1.72               #double/decimal
esHinchaDelMejor=True       #Booleano
nombre="Juan"               #string


n1=int(input("ingrese un numero: "))
n2=int(input("ingrese un numero: "))
suma=n1+n2
print(f"la suma entre {n1} y {n2} es: {suma}")

if n1<0:
    print(f"{n1} es un numero negativo")
else:
    print(f"{n1} es un numero positivo")


nivelAgua=float(input("Digite la cantidad de agua de la represa: "))
print(f"El nivel de agua es: {nivelAgua}")

print("soy un cambio para agregarlo al Git")