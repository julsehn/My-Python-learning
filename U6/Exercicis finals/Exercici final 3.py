import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_encapcalament():
    print("+" + "-" * 62 + "+")
    print("|" + "".center(62) + "|")
    print("|" + "CAIXER AUTOMÀTIC".center(62) + "|")
    print("|" + "".center(62) + "|")
    print("+" + "-" * 62 + "+")
    print()


def solicitar_float(prompt, min_value=0.1, max_value=None):
    while True:
        try:
            valor = float(input(prompt))
        except ValueError:
            print("  Error: introdueix un nombre vàlid.")
            continue

        if min_value is not None and valor < min_value:
            print(f"  Error: el valor ha de ser com a mínim {min_value}.")
            continue
        if max_value is not None and valor > max_value:
            print(f"  Error: el valor ha de ser com a màxim {max_value}.")
            continue

        return valor


def mostrar_menu():
    print("+" + "-" * 62 + "+")
    print("|" + " SELECCIONA UNA OPCIÓ ".center(62) + "|")
    print("+" + "-" * 62 + "+")
    print("| 1 - Extreure diners".ljust(62) + "|")
    print("| 2 - Ingressar diners".ljust(62) + "|")
    print("| 3 - Comprovar saldo".ljust(62) + "|")
    print("| 4 - Sol·licitar préstec".ljust(62) + "|")
    print("| 0 - Sortir".ljust(62) + "|")
    print("+" + "-" * 62 + "+")


def extraure_diners(saldo_actual):
    clear_screen()
    mostrar_encapcalament()
    print("+" + "-" * 62 + "+")
    print("|" + " EXTREURE DINERS ".center(62) + "|")
    print("+" + "-" * 62 + "+")
    quantitat = solicitar_float("  Quantitat a treure: ", min_value=0.01)
    if quantitat > saldo_actual:
        print("  No hi ha suficient saldo per fer aquesta operació.")
        print(f"  Saldo disponible: {saldo_actual:.2f} €")
        return saldo_actual

    saldo_actual -= quantitat
    print(f"  Operació realitzada. Has retirat {quantitat:.2f} €.")
    print(f"  Saldo restant: {saldo_actual:.2f} €")
    pause()
    return saldo_actual


def ingressar_diners(saldo_actual):
    clear_screen()
    mostrar_encapcalament()
    print("+" + "-" * 62 + "+")
    print("|" + " INGRESSAR DINERS ".center(62) + "|")
    print("+" + "-" * 62 + "+")
    quantitat = solicitar_float("  Quantitat a ingressar: ", min_value=0.01)
    saldo_actual += quantitat
    print(f"  Operació realitzada. Has ingressat {quantitat:.2f} €.")
    print(f"  Nou saldo: {saldo_actual:.2f} €")
    pause()
    return saldo_actual


def comprovar_saldo(saldo_actual):
    clear_screen()
    mostrar_encapcalament()
    print("+" + "-" * 62 + "+")
    print("|" + " SALDO DISPONIBLE ".center(62) + "|")
    print("+" + "-" * 62 + "+")
    print(f"  Saldo actual: {saldo_actual:.2f} €")
    pause()


def pause():
    input("\nPrem qualsevol tecla per tornar al menú...")


def solicitar_prestec(saldo_actual):
    clear_screen()
    mostrar_encapcalament()
    print("+" + "-" * 62 + "+")
    print("|" + " SOL·LICITUD DE PRÉSTEC ".center(62) + "|")
    print("+" + "-" * 62 + "+")

    principal = solicitar_float("  Quantitat del préstec: ", min_value=1.0, max_value=9999999.0)
    taxa_percent = solicitar_float("  Taxa d'interès anual (%): ", min_value=0.0)
    anys = int(solicitar_float("  Durada del préstec (anys): ", min_value=1.0))

    taxa = taxa_percent / 100
    capital_restant = principal
    pagament_capital = principal / anys
    interes_anual_fix = principal * taxa
    pagar_total = 0.0

    print()
    print("+" + "-" * 62 + "+")
    print("|" + " AMORTITZACIÓ DEL PRÉSTEC ".center(62) + "|")
    print("+" + "-" * 62 + "+")
    print("  Any | Capital/any | Interès/any | Total/any | Capital restant")
    print("  " + "-" * 58)

    for any_num in range(1, anys + 1):
        pagament_any = pagament_capital + interes_anual_fix
        pagar_total += pagament_any
        capital_restant -= pagament_capital
        if capital_restant < 0:
            capital_restant = 0.0

        print(f"  {any_num:>3} | {pagament_capital:>11.2f} | {interes_anual_fix:>11.2f} | {pagament_any:>10.2f} | {capital_restant:>14.2f}")

    print("  " + "-" * 58)
    print(f"  Total pagat: {pagar_total:.2f} €")
    print(f"  Préstec concedit: {principal:.2f} €")
    print(f"  Taxa aplicada: {taxa_percent:.2f} %")

    saldo_actual += principal
    print(f"  El préstec s'ha afegit al teu saldo. Nou saldo: {saldo_actual:.2f} €")
    pause()
    return saldo_actual


def main():
    saldo = 0.0

    while True:
        clear_screen()
        mostrar_encapcalament()
        print("Benvingut al caixer automàtic. Pots utilitzar les opcions del menú per gestionar el teu compte.")
        print()
        mostrar_menu()
        opcio = input("Selecciona una opció: ").strip()

        if opcio == "1":
            saldo = extraure_diners(saldo)
        elif opcio == "2":
            saldo = ingressar_diners(saldo)
        elif opcio == "3":
            comprovar_saldo(saldo)
        elif opcio == "4":
            saldo = solicitar_prestec(saldo)
        elif opcio == "0":
            print()
            print("Gràcies per utilitzar el caixer automàtic. Fins aviat!")
            break
        else:
            print("  Opció no vàlida. Torna-ho a intentar.")

if __name__ == "__main__":
    main()