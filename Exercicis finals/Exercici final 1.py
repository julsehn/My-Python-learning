text_usuari = input("Digues: ")
comptador = 1

for lletra in text_usuari:
    if lletra == " ":
        comptador += 1

if comptador == 1:
    print(f"El text {text_usuari} conte: {comptador} paraula")
else:
    print(f"El text {text_usuari} conte: {comptador} paraules")