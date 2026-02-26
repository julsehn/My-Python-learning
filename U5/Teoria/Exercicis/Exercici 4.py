numero_inicial = int(input("Digue'm el numero inicial: "))
numero_final = int(input("Digue'm el numero final: "))
suma_total = 0

for numero in range(numero_inicial, numero_final + 1):
    if numero % 7 != 0:
        suma_total += numero

print("La suma total és:", suma_total)