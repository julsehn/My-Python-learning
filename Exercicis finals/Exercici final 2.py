num_usuari = int(input("Ingrese el seu numero: "))
binari = ""

if num_usuari == 0:
    binari = "0"
else:
    for _ in range(64):
        if num_usuari == 0:
            break
        residu = num_usuari % 2
        binari = str(residu) + binari
        num_usuari = num_usuari // 2

print(f"El numero en binari es: {binari}")