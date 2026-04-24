class MaquinaExprendedora:
    def __init__(self):
        self.tipus_de_veguda = "cafè"
        self.preu = 1.50
        self.quantitat = 10
        self.vendes_totals = 0
        self.import_introduit = 0

    def introduir_diner(self, import_introduit):
        """Introdueix diners a la màquina."""
        self.import_introduit += import_introduit
    
    def seleccionar_beguda(self):
        """Seleccionar una veguda"""
        if self.quantitat == 0:
            return "Ho sento, no hi ha més begudes disponibles."
        if self.import_introduit < self.preu:
            return f"Ho sento, el preu del {self.tipus_de_veguda} és {self.preu} euros."
        self.import_introduit -= self.preu
        self.quantitat -= 1
        self.vendes_totals += self.preu
        return "Gaudeixi de la veguda!"
    
    def obtenir_vendes_totals(self):
        """Obtenir les vendes totals de la màquina."""
        return self.vendes_totals
    
    def recarregar(self, quantitat):
        """Recarregar la màquina amb una quantitat específica de begudes."""
        self.quantitat += quantitat
    
    def menu_usuari(self):
        while True:
            print("\nBenvingut a la màquina expenedora!")
            print("1. Introduir diners")
            print("2. Seleccionar beguda")
            print("3. Sortir")
            opcio = input("Selecciona una opció: ")
            
            if opcio == "1":
                try:
                    import_introduit = float(input("Introdueix l'import en euros: "))
                except ValueError:
                    print("Cal introduir un nombre vàlid amb coma. Torna-ho a provar.")
                    continue

                if import_introduit <= 0:
                    print("L'import introduït ha de ser positiu. Si us plau, introdueix un import vàlid.")
                    continue

                self.introduir_diner(import_introduit)
                print(f"Has introduït {import_introduit} euros.")
            elif opcio == "2":
                resultat = self.seleccionar_beguda()
                print(resultat)
            elif opcio == "3":
                print("Gràcies per utilitzar la màquina expenedora. Fins aviat!")
                break
            else:
                print("Opció no vàlida. Si us plau, selecciona una opció vàlida.")
    
    def menu_administrador(self):
        while True:
            print("\nMenú d'administrador")
            print("1. Recarregar la màquina")
            print("2. Veure vendes totals")
            print("3. Sortir")
            opcio = input("Selecciona una opció: ")
            
            if opcio == "1":
                try:
                    quantitat = int(input("Introdueix la quantitat de begudes a recarregar: "))
                except ValueError:
                    print("Cal introduir un nombre enter vàlid. Torna-ho a provar.")
                    continue

                if quantitat <= 0:
                    print("La quantitat ha de ser positiva. Introdueix un valor vàlid.")
                    continue

                self.recarregar(quantitat)
                print(f"La màquina ha estat recarregada amb {quantitat} begudes.")
            elif opcio == "2":
                vendes_totals = self.obtenir_vendes_totals()
                print(f"Les vendes totals de la màquina són: {vendes_totals} euros.")
            elif opcio == "3":
                print("Sortint del menú d'administrador. Fins aviat!")
                break
            else:
                print("Opció no vàlida. Si us plau, selecciona una opció vàlida.")
    
    @staticmethod
    def menu_principal():
        maquina = MaquinaExprendedora()
        while True:
            print("\nMenú principal")
            print("1. Usuari")
            print("2. Administrador")
            print("3. Sortir")
            opcio = input("Selecciona una opció: ")
            
            if opcio == "1":
                maquina.menu_usuari()
            elif opcio == "2":
                maquina.menu_administrador()
            elif opcio == "3":
                print("Gràcies per utilitzar la màquina expenedora. Fins aviat!")
                break
            else:
                print("Opció no vàlida. Si us plau, selecciona una opció vàlida.")


if __name__ == "__main__":
    MaquinaExprendedora.menu_principal()