try:
    x = 10 / 0
except:
    print("No es divisible")

try:
    x = int(input("Introdueix un número: "))
except:
    print("Has d'introduir un numero valid")

try:
    a = int(input("Introdueix un número: "))
    b = int(input("Introdueix un altre número: "))
    resultat = a / b
    print(resultat)

except ValueError:
    print("Has un valors numerics valids.")
except ZeroDivisionError:
    print("No es pot dividir entre zero.")

except Exception as e:
    print("S'ha poduït una excepció:", e)