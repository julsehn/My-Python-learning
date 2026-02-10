import time
contador_dies = 0
dia = 0
mes = 1
any = 2026

for i in range(1, 365):
    contador_dies += 1
    dia += 1
    print(f"{dia}/{mes}/{any}")
    if mes == 1:
        for i in range(1, 32):
            time.sleep(0.002)
            if dia == 31:
                dia = 0
                mes += 1
                time.sleep(0.002)
    if mes == 2:
        for i in range(1, 29):
            time.sleep(0.002)
            if dia == 28:
                dia = 0
                mes += 1
                time.sleep(0.002)
    if mes == 3:
        for i in range(1, 32):
            time.sleep(0.002)
            if dia == 31:
                dia = 0
                mes += 1
                time.sleep(0.002)
    if mes == 4:
        for i in range(1, 31):
            time.sleep(0.002)
            if dia == 30:
                dia = 0
                mes += 1
                time.sleep(0.002)
    if mes == 5:
        for i in range(1, 32):
            time.sleep(0.002)
            if dia == 31:
                dia = 0
                mes += 1
                time.sleep(0.002)
    if mes == 6:
        for i in range(1, 31):
            time.sleep(0.002)
            if dia == 30:
                dia = 0
                mes += 1
                time.sleep(0.002)
    if mes == 7:
        for i in range(1, 32):
            time.sleep(0.002)
            if dia == 31:
                dia = 0
                mes += 1
                time.sleep(0.002)
    if mes == 8:
        for i in range(1, 32):
            time.sleep(0.002)
            if dia == 31:
                dia = 0
                mes += 1
                time.sleep(0.002)
    if mes == 9:
        for i in range(1, 31):
            time.sleep(0.002)
            if dia == 30:
                dia = 0
                mes += 1
                time.sleep(0.002)
    if mes == 10:
        for i in range(1, 32):
            time.sleep(0.002)
            if dia == 31:
                dia = 0
                mes += 1
                time.sleep(0.002)
    if mes == 11:
        for i in range(1, 31):
            time.sleep(0.002)
            if dia == 30:
                dia = 0
                mes += 1
                time.sleep(0.002)
    if mes == 12:
        for i in range(1, 32):
            time.sleep(0.002)
            if dia == 31:
                dia = 0
                mes = 1
                any += 1
                time.sleep(0.002)