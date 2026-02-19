import time

print("€                      Banc dels milions                       €")
print("€                                                              €")
print("€        Benvingut al banc dels milions, on si necessita       €")
print("€            uns calerets, només cal que ens truqui!           €")
print("")
print("")
diners = int(input("        Introdueixi la quantitat de diners que necessita:      "))
while diners < 0:
    print("                       No pots demanar una quantitat negativa de diners!       ")
    diners = int(input("        Introdueixi la quantitat de diners que necessita:       "))
while diners > 9999999:
    print("        No pots demanar més de 9.999.999 €!       ")
    diners = int(input("        Introdueixi la quantitat de diners que necessita:      "))
restant = diners
taxa = float(input("       Introdueix la taxa d'interes anual que vols pagar:       "))
while taxa < 0:
    print("       No pots introduir una taxa d'interes negativa!       ")
    taxa = float(input("       Introdueix la taxa d'interes anual que vols pagar:       "))
taxa = taxa / 100

anys = int(input("     Introdueix el nombre d'anys que necesites el prestec:     "))
while anys < 0:
    print("     No pots introduir un nombre d'anys negatiu!     ")
    anys = int(input("     Introdueix el nombre d'anys que necesites el prestec:     "))
time.sleep(1)
any = 0
print("€" + "─" * 62 + "€")
print("€" + " " * 13 + "D'acord, es així serà el teu prestec:" + " " * 12 + "€")
print("€" + "─" * 62 + "€")
print("€ Any │ Capital/any │ Interès/any │ Total/any │ Capital restant€")
print("€" + "─" * 62 + "€")
pagar_cada_any = diners / anys
interes_anual_fix = diners * taxa
restant = diners
pagar_total = 0
while restant > 0:
    any += 1
    pago_total_aquest_any = pagar_cada_any + interes_anual_fix
    pagar_total += pago_total_aquest_any
    restant -= pagar_cada_any
    print(f"€ {any:>2}  │ {pagar_cada_any:>10.2f}  │ {interes_anual_fix:>10.2f}  │ {pago_total_aquest_any:>8.2f}  │ {restant:>13.2f} €")
print("€" + "─" * 62 + "€")
print(f"€ {anys:>2}  │ {diners:>10.2f}  │ {interes_anual_fix * anys:>10.2f}  │ {pagar_total:>8.2f}  │ {restant:>13.2f} €")
print("")
print("            Gracies per confiar en el banc dels milions!           ")
