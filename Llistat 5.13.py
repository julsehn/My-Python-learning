PreuEnt = 8
edat = int(input('Digues la teva edat: '))
if edat < PreuEnt or edat > 65:
    PreuEnt = 8 * 0.7
print(f"El preu de l'entrada es: {PreuEnt}€")