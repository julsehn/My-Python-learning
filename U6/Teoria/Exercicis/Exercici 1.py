import random
print("generador de numero de loteria que mai es repeteixen")
numeros = []
for i in range(6):
    temp_num = random.randint(1, 49)
    while temp_num in numeros:
        temp_num = random.randint(1, 49)
    numeros.append(temp_num)
    print(temp_num)
