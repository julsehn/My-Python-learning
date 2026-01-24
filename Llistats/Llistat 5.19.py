text = input("Introdueix el teu text: ")
comptador = 0

for lletra in text:
    if lletra == "a" or lletra == "A":
        comptador += 1

print("He trobat", comptador, "vegadoes la lletra a/A.")