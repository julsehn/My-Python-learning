iva = 0.21

def calcular_preu(base, impost=iva):
    return base + (base * impost)

print(calcular_preu(float(input("Introdueix el preu base: "))))
print(calcular_preu(float(input("Introdueix el preu base: ")), float(input("Introdueix el percentatge d'impost (en format decimal): "))))