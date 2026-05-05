import random
from colorama import init, Fore, Style

init()

GREEN = Fore.GREEN + "Correcte" + Style.RESET_ALL
YELLOW = Fore.YELLOW + "Present" + Style.RESET_ALL
RED = Fore.RED + "Absent" + Style.RESET_ALL
RESET = "\033[0m"

class LINGO:
    def __init__(self, paraula):
        self.paraula = paraula.upper()
        self.paraules_possibles = ['porta', 'arbre', 'llibre', 'taula', 'gos', 'gat', 'sol', 'mar', 'casa', 'lluna', 'flor', 'riu', 'munt', 'vent', 'foc', 'aigua', 'terra', 'cel', 'llum', 'nit']
        self.max_intents = 6
        self.intents = 0

    def verificar_endevinada(self, endevinada):
        endevinada = endevinada.upper()
        retroalimentacio = []
        llista_paraula = list(self.paraula)
        llista_endevinada = list(endevinada)
        
        for i in range(len(endevinada)):
            if endevinada[i] == self.paraula[i]:
                retroalimentacio.append("correcte ")
                llista_paraula[i] = None
                llista_endevinada[i] = None
            else:
                retroalimentacio.append(None)
        
        for i in range(len(endevinada)):
            if retroalimentacio[i] is None:
                if endevinada[i] in llista_paraula:
                    retroalimentacio[i] = "present "
                    llista_paraula[llista_paraula.index(endevinada[i])] = None
                else:
                    retroalimentacio[i] = "absent "
        
        return retroalimentacio

    def endevinalla(self):
        print(f"La paraula té {len(self.paraula)} lletres. Tens {self.max_intents} intents.")
        while self.intents < self.max_intents:
            endevinada = input("Endevina la paraula: ").strip()
            if len(endevinada) != len(self.paraula):
                print(f"La paraula ha de tenir {len(self.paraula)} lletres.")
                continue
            if endevinada.upper() == self.paraula:
                print(f"Felicitats! Has endevinat la paraula '{self.paraula}'!")
                return True
            
            retroalimentacio = self.verificar_endevinada(endevinada)
            print("Retroalimentació:")
            for i, estat in enumerate(retroalimentacio):
                if estat == "correcte":
                    print(f"{GREEN} Lletra {i+1}: {endevinada[i]} - Correcte{RESET}")
                elif estat == "present":
                    print(f"{YELLOW} Lletra {i+1}: {endevinada[i]} - Present{RESET}")
                else:
                    print(f"{RED} Lletra {i+1}: {endevinada[i]} - Absent{RESET}")
            
            self.intents += 1
            print(f"Intents restants: {self.max_intents - self.intents}")
        
        print(f"Has perdut! La paraula correcta era '{self.paraula}'.")
        return False

if __name__ == "__main__":
    paraules_possibles = ['porta', 'arbre', 'llibre', 'taula', 'gos', 'gat', 'sol', 'mar', 'casa', 'lluna', 'flor', 'riu', 'munt', 'vent', 'foc', 'aigua', 'terra', 'cel', 'llum', 'nit']
    paraula_per_endevinar = random.choice(paraules_possibles).upper()
    joc = LINGO(paraula_per_endevinar)
    joc.endevinalla()