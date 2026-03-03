numero_usr = 1
suma = 0
suma_nums = ""
while numero_usr >= 0:
    numero_usr = int(input("Ingrese un número (0 para salir): "))
    if numero_usr != 0:
        print(f"El número ingresado es: {numero_usr}")
    suma += numero_usr
    suma_nums += str(suma) + " + "
print(f"La suma total de los números ingresados es: {suma}")
print(f"La suma de los números ingresados es: {suma_nums[:-3]} = {suma}")