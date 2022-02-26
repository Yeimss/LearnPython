nivelAgua=float(input("Digite la cantidad de agua de la represa: "))

if nivelAgua < 200:
    print("No tenemos aguita")
elif nivelAgua < 450:
    print("Todo bien, todo correcto")
else:
    print("Ojito que nos desbordamos")