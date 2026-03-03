numero_usr_int = 1
suma = 0
suma_nums = ""
while numero_usr_int != 0:
    numero_usr_int = int(input("Introdueixi un nombre (0 per sortir): "))
    if numero_usr_int != 0:
        print(f"El nombre introduït és: {numero_usr_int}")
    suma += numero_usr_int
    suma_nums += str(numero_usr_int) + " + "
print(f"La suma total dels nombres introduïts és: {suma}")
print(f"La suma dels nombres introduïts és: {suma_nums[:-7]} = {suma}")