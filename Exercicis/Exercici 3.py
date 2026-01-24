numero = input("Un número si us plau: ")
suma_digits = 0
for ch in numero:
    if ch.isdigit():
        suma_digits += int(ch)

print("La suma de dígits és:", suma_digits)