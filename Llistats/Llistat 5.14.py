numero1 = int(input("Dige'm un numero"))
numero2 = int(input("Dige'm un altre numero"))
if numero1 > numero2:
    major = numero1
    minor = numero2
    print(f"El número major és: {major}, mentres que el número menor és: {minor}")
elif numero2 > numero1:
    major = numero2
    minor = numero1
    print(f"El número major és: {major}, mentres que el número menor és: {minor}")
else:
    major = numero1
    minor = numero2
    print(f"Els números són iguals: {major} i {minor}")