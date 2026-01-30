suma = 0
comptador = 0
num_max = float('-inf')
num_min = float('inf')
numero = float(input("Introdueix un número (0 per acabar): "))

while numero != 0:
    if numero > 0:
        if numero < num_min:
            num_min = numero
        elif numero > num_max:
            num_max = numero
    suma += numero
    comptador += 1
    numero = float(input("Introdueix un número (0 per acabar): "))

if comptador != 0:
    mitjana = suma / comptador
    print("La mitjana és:", mitjana)
    print("El nombre major és", num_max)
    print("I el nombre menor és", num_min)
else:
    print("No s'han introduït números.")