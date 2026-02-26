print("Benvingut a la prova de Python on em demane de fer un programa que conti vocals i consonants introduits per l'usuari")
contador = 0
while True:
    nom = input("Ingresi un nom (o escriu 'fi' per acabar) ")
    if nom == 'fi':
        break
    contador_vocals = 0
    contador_consonants = 0
    for lletra in nom:
        if lletra in 'aeiouàáéèíóòúAEIOUÀÁÉÈÍÓÒÚäëïöüÄËÏÖÜ':
            contador_vocals += 1
        if lletra in 'QWRTYPSDFGHJKLÑZXCVBNMÇqwrtypsdfghjklñzxcvbnmç':
            contador_consonants += 1
    print(f"El nom '{nom}' conté {contador_vocals} vocals i {contador_consonants} consonants.")
    print(f"En total, conté un total {contador_vocals + contador_consonants} lletres.")
    contador += 1

print(f"Gràcies per utilitzar {contador} vegades l'ingeniós programa de Python per contar lletres! Fins aviat!")