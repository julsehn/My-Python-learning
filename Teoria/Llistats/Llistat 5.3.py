print('Com et dius?')
nom = input() #input sense paràmetres
cognom = input(nom + ', quin és el teu cognom?')
#input amb text associat
print('Tant de gust de conèixer-te ' + nom + ' ' + cognom)
edat = input('Quants anys tens? ')
edatFutura = int(edat) + 8
print('{} {}, dins de 8 anys tindràs {}'.format(nom, cognom, edatFutura))