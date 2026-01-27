numero = int(input("Ingrese un numero: "))
es_primer = True
if numero < 2:
    es_primer = False

for i in range(2, numero):
    if numero % i == 0:
        es_primer = False
        break

if es_primer:
    print(numero, "és primer")
else:
    print(numero, "no és primer")