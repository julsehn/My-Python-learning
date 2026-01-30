suma = 0
comptador = 0
numero = float(input("Introdueix un número (0 per acabar): "))

while numero != 0:
    suma += numero
    comptador += 1
    numero = float(input("Introdueix un número (0 per acabar): "))

if comptador != 0:
    mitjana = suma / comptador
    print("La mitjana és:", mitjana)
else:
    print("No s'han introduït números.")