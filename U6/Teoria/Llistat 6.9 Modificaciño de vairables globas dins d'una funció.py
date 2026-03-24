x = 10

def funcio():
    global x
    x = 50

print("Valor de x abans de la funció:", x)
funcio()
print("Valor de x després de la funció:", x)