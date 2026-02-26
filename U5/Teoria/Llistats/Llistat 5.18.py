while True:
    tipus_figura = input("Digues una figura \n(T)riangle\n(Q)uadrat\n(R)ectangle: ")
    if tipus_figura.strip() == "":
        print("Tipus de figura no valida")
        continue
    if tipus_figura.upper() in ("T", "Q", "R"):
        break
    else:
        print("Tipus de figura no valida")

match tipus_figura.upper():
    case "T":
        base = float(input("Digues la base: "))
        altura = float(input("Digues la altura: "))
        area = (base * altura) / 2
        print(f"L'area del triangle és: {area}")
    case "Q":
        costat = float(input("Longitut del costat del quadrat: "))
        area = costat ** 2
        print(f"L'area del quadrat és: {area}")
    case "R":
        amplada = float(input("Amplitud del rectangle: "))
        llargada = float(input("Largada del rectangle: "))
        area = amplada * llargada
        print(f"L'area del rectangle és: {area}")
    case _:
        print("Tipus de figura no valida")