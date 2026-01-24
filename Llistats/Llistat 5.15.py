numero1 = int(input('Primer número: '))
numero2 = int(input('Segon número: '))
numero3 = int(input('Tercer número: '))

if numero1 > numero2:
    if numero1 > numero3:
        major = numero1
    else:
        major = numero3
else:
    if numero2 > numero3:
        major = numero2
    else:
        major = numero3

print('El número major és: ', major)