class Exemple:
    def __init__(self):
        self.atribut_amb_guio = "Atribut amb guió"
        self.__atribut_amb_dos_guions = "Atribut amb dos guions"
    
    def metode_exemple(self):
        print(self.atribut_amb_guio)
        print(self.__atribut_amb_dos_guions)
    
exemple = Exemple()
exemple.metode_exemple()

print(exemple.atribut_amb_guio)
print(exemple.__atribut_amb_dos_guions)