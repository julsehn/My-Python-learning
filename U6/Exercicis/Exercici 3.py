def calcular_area_triangle(base, altura):
    return (base * altura) / 2
def calcular_area_quadrat(costat):
    return costat * costat
def calcular_area_cercle(radi):
    return 3.1416 * (radi ** 2)

tipus_figura = input("Introdueix el tipus de figura \n(T)triangle, \n(Q)quadrat, \n(C)cercle): ")

match tipus_figura:
    case "T":
        print(calcular_area_triangle(float(input("Introdueix la base del triangle: ")), float(input("Introdueix l'altura del triangle: "))))
    case "Q":
        print(calcular_area_quadrat(float(input("Introdueix el costat del quadrat: "))))
    case "C":
        print(calcular_area_cercle(float(input("Introdueix el radi del cercle: "))))