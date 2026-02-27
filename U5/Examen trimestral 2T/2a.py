print("Benvingut a la prova de Python on em demane de fer un programa que conti vocals i consonants introduits per l'usuari")
contador = 0
while True:
    nom = input("Ingresi un nom (o escriu 'fi' per acabar) ")
    if nom == 'fi':
        break
    contador_vocals = 0
    contador_consonants = 0
    contador_espais = 0
    contador_digits = 0
    contador_signes_puntuacio = 0
    contador_parentesis = 0
    contador_guions = 0
    contador_caracters_especials = 0
    contador_vocals_amb_accents = 0
    contador_vocals_sense_accents = 0
    contador_vocals_amb_diaeresis = 0
    contador_consonants_majuscules = 0
    contador_consonants_minuscules = 0
    contador = 0
    aslletra_anterior = False
    contador_paraules = 1
    for lletra in nom:
        if lletra in ' ,.:;!?)' and aslletra_anterior == True:
            contador_paraules += 1
            aslletra_anterior = False
        if lletra in 'aeiouàáéèíóòúAEIOUÀÁÉÈÍÓÒÚäëïöüÄËÏÖÜ':
            contador_vocals += 1
            aslletra_anterior = True
        if lletra in 'ÀÁÉÈÍÓÒÚàáéèíóòú':
            contador_vocals_amb_accents += 1
            aslletra_anterior = True
        if lletra in 'AEIOUaeiou':
            contador_vocals_sense_accents += 1
            aslletra_anterior = True
        if lletra in 'äëïöüÄËÏÖÜ':
            contador_vocals_amb_diaeresis += 1
            aslletra_anterior = True
        if lletra in 'QWRTYPSDFGHJKLÑZXCVBNMÇqwrtypsdfghjklñzxcvbnmç':
            contador_consonants += 1
            aslletra_anterior = True
        if lletra in 'QWRTYPSDFGHJKLÑZXCVBNMÇ':
            contador_consonants_majuscules += 1
            aslletra_anterior = True
        if lletra in 'qwrtypsdfghjklñzxcvbnmç':
            contador_consonants_minuscules += 1
            aslletra_anterior = True
        if lletra in ' ':
            contador_espais += 1
            lletra_anterior = 0
        if lletra in '0123456789':
            contador_digits += 1
            lletra_anterior = 1
        if lletra in '.,;:!?':
            contador_signes_puntuacio += 1
            lletra_anterior = 0
        if lletra in '()[]{}':
            contador_parentesis += 1
            aslletra_anterior = False
        if lletra in '-_':
            contador_guions += 1
            aslletra_anterior = False
        if lletra in '@#$%&*':
            contador_caracters_especials += 1
            aslletra_anterior = False
        contador += 1
    print(f"El nom '{nom}' conté {contador_vocals} vocals i {contador_consonants} consonants.")
    print(f"En total, conté un total {contador_vocals + contador_consonants} lletres.")
    print(f"També conté:")
    print(f"{contador_espais} espais")
    print(f"{contador_digits} dígits")
    print(f"{contador_signes_puntuacio} signes de puntuació")
    print(f"{contador_parentesis} parèntesis")
    print(f"{contador_guions} guions")
    print(f"{contador_caracters_especials} caràcters especials")
    print(f"{contador_vocals_amb_accents} vocals amb accents")
    print(f"{contador_vocals_sense_accents} vocals sense accents")
    print(f"{contador_vocals_amb_diaeresis} vocals amb dièresi")
    print(f"{contador_consonants_majuscules} consonants majúscules")
    print(f"{contador_consonants_minuscules} consonants minúscules")
    print("-" * 100)
    print(f"Contador total de paraules: {contador_paraules}")
    print(f"Contador total de caracters: {contador}")


print(f"Gràcies per utilitzar {contador} vegades l'ingeniós programa de Python per contar lletres! Fins aviat!")