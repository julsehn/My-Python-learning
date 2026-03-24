def salutacio(hora):
    if hora >=6 and hora < 12:
        print("Bon dia!")
    elif hora >= 12 and hora < 20:
        print("Bona tarda!")
    else:
        print("Bona nit!")

salutacio(8)
salutacio(15)
salutacio(22)