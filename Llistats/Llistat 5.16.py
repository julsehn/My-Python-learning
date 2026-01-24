while True:
    try:
        nota = float(input("Dona'm la teva nota de l'u al deu: "))
    except ValueError:
        print("No és un número, torna-ho a intentar.")
        continue
    if 1 <= nota <= 10:
        break
    else:
        print("Número fora de rang (1-10), torna-ho a intentar.")
if 9 <= nota <= 10:
    nota_alfanumerica = "Excel·lent"
elif nota >= 7:
    nota_alfanumerica = "Notable"
elif nota >= 6:
    nota_alfanumerica = "Bé"
elif nota >= 5:
    nota_alfanumerica = "Suficient"
elif nota < 5:
    nota_alfanumerica = "Suspens"

print("La teva alfanumèrica és: ", nota_alfanumerica)