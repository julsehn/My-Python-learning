seguir = True
i = k = 0

while seguir:
    i += 2
    for j in range(i):
        k = i + j
        if k > 7:
            seguir = False

print(k)