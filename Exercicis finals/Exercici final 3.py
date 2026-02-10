numero_usuari = int(input("Dige'm un numero per a que te'ls converteixi a primers fins al numero: "))
numero_primer = 0

for i in range(2, numero_usuari):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            numero_primer = i
            print(numero_primer)