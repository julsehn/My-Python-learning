while True:
    mes_numero = input("En quin mes vols fer la reserva?: \n(1) Gener\n(2) Febrer\n(3) Març\n(4) Abril\n(5) Maig\n(6) Juny\n(7) Juliol\n(8) Agost\n(9) Setembre\n(10) Octubre\n(11) Novembre\n(12) Desembre\n")
    if mes_numero.strip() == "":
        print("Mes no valid")
        continue
    if "12" >= mes_numero >= "01":
        break
    else:
        print("Mes incorrecte")
match mes_numero:
    case "1":
        mes = "Gener"
    case "2":
        mes = "Febrer"
    case "3":
        mes = "Març"
    case "4":
        mes = "Abril"
    case "5":
        mes = "Maig"
    case "6":
        mes = "Juny"
    case "7":
        mes = "Juliol"
    case "8":
        mes = "Agost"
    case "9":
        mes = "Setembre"
    case "10":
        mes = "Octubre"
    case "11":
        mes = "Novembre"
    case "12":
        mes = "Desembre"
    case _:
        mes = "Mes incorrecte"

print(f'Has seleccionat el mes de {mes}.')
while True:
    dia = input("Quin dia del mes vols fer la reserva?")
    if dia.strip() == "":
        print("Dia no valid")
        continue
    if mes == "Febrer":
        if "28" >= dia >= "01":
            break
    if mes in ("Gener", "Març", "Maig", "Juliol", "Agost", "Octubre", "Desembre"):
        if "31" >= dia >= "01":
            break
    if mes in ("Abril", "Juny", "Setembre", "Novembre"):
        if "30" >= dia >= "01":
            break
    print("Dia incorrecte")

print(f'Has seleccionat el dia {dia} de {mes}.')
while True:
    hora = input("A quina hora vols fer la reserva? (Format 24h)")
    if hora.strip() == "":
        print("Hora no valida")
        continue
    if "23" >= hora >= "00":
        break
    else:
        print("Hora incorrecte")
hora = input("A quina hora vols fer la reserva? (Format 24h)")

print(f'Has seleccionat les {hora}h del dia {dia} de {mes}.')
print(f'La teva reserva s\'ha realitzat per al dia {dia} de {mes} a les {hora}h. Gràcies!')