from Cliente import Cliente
from Cuenta import Cuenta

nombre=input("Nombre: ")
apellido=input("Apellido: ")
cedula=input("Cedula: ")
numero_cuenta=input("Numero de cuenta: ")
saldo=float(input("Saldo: "))
cliente=Cliente(nombre, apellido, cedula)
cuenta=Cuenta(cedula,numero_cuenta,saldo)

def menu():
    return int(input(
        """
        1. consultar saldo
        2. retirar dinero
        3. ingresar dinero
        4. salir
        """
    ))

def retirar(retirar):
    total=cuenta.get_saldo()-retirar
    cuenta.set_saldo(total)

def ingresar(ingresar):
    total=cuenta.get_saldo()+ingresar
    cuenta.set_saldo(total)

salir=False
while not salir:
    opcion=menu()
    if opcion==1:
        print(f"Su saldo es: {cuenta.get_saldo()}")
    elif opcion==2:
        r=float(input("Cuanto dinero desea retirar: "))
        retirar(r)
    elif opcion==3:
        i=float(input("Cuanto dinero desea ingresar: "))
        ingresar(i)
    elif opcion==4:
        salir=1
    else:
        print("Opcion incorrecta. >.<")
    