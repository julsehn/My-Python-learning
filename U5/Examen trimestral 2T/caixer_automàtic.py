import random
import time

def programa_prestec(prestec_diners):
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





print("Benvingut al caixer automàtic!")
saldo = random.randint(500, 10000)
print(f"El seu saldo actual és de {saldo} euros.")
key = input("Introdueixi la seva clau de seguretat: ")
if key == "1234":
    print("Clau correcta. Accés concedit.")
    while True:
        print("\nQuina operació desitja realitzar?")
        print("1. Consultar saldo")
        print("2. Retirar diners")
        print("3. Ingressar diners")
        print("4. Sortir")
        opcio = input("Introdueixi el número de l'operació: ")
        
        if opcio == "1":
            print(f"El seu saldo actual és de {saldo} euros.")
        
        elif opcio == "2":
            quantitat = int(input("Introdueixi la quantitat a retirar: "))
            if quantitat > saldo:
                print("Fons insuficients. Operació cancel·lada.")
                prestec = input("Voleu fer un prestec per cobrir la quantitat? (s/n): ")
                if prestec == "s":
                    
            else:
                saldo -= quantitat
                print(f"Ha retirat {quantitat} euros. El seu nou saldo és de {saldo} euros.")
        
        elif opcio == "3":
            quantitat = int(input("Introdueixi la quantitat a ingressar: "))
            saldo += quantitat
            print(f"Ha ingressat {quantitat} euros. El seu nou saldo és de {saldo} euros.")
        
        elif opcio == "4":
            print("Gràcies per utilitzar el caixer automàtic. Fins aviat!")
            break
        
        else:
            print("Opció no vàlida. Si us plau, intenti-ho de nou.")
