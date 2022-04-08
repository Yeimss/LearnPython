'''
Construir un programa que reciba números enteros y los sume
mientras estos sean positivos, si se digita un número 
negativo el programa debe terminar
'''
sumatoria=0
i=True
while i:
    numero=int(input("Digite un numero para sumarlo: "))
    if(numero>=0):
        sumatoria+=numero
    else:
        i=False

print(f"La suma de todos los numeros ingresados es: {sumatoria}")