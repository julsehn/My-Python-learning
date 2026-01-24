n = int(input('Introdueix un numero positiu: '))
producte = 1

for i in range(1, n + 1):
    producte *= i

print("El producte dels", n, "primers nombres és:", producte)
