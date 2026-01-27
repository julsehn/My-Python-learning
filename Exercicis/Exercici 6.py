vocals = "aeiou"

for vocal1 in vocals:
    for vocal2 in vocals:
        for vocal3 in vocals:
            combine = vocal1 + vocal2 + vocal3
            if not (vocal1 == vocal2 == vocal3):
                print(combine)