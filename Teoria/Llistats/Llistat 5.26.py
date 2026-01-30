import random

numero = random.randint(1, 10)
endevinat = False
intents = 0

print("Endevina el numero de 1 al 10 per guanyar la loteria")
while not endevinat:
    entrada = input("Digues-me un numero (0-100): ")
    try:
        numJugador = int(entrada)
    except ValueError:
        print("Valor no vàlid. Introdueix un nombre enter.")
        continue

    if numJugador < 0 or numJugador > 10:
        print("Número fora de rang (0-10). Intenta-ho de nou.")
        continue
    intents += 1
    if numJugador == numero:
        print("Enhorabona, l'has encertat en", intents, "intents")
        endevinat = True
    elif numJugador > numero:
        print("El número és menor que el teu")
    else:
        print("El número és més gran que el teu")