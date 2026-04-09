class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat
    
    def __add__(self, altraPersona):
        nom = self.nom + " " + altraPersona.nom
        edat = self.edat + altraPersona.edat
        return Persona(nom, edat)
    def __str__(self):
        return f"{self.nom} té {self.edat} anys."
    
persona1 = Persona("Joan", 30)
persona2 = Persona("Maria", 25)
persona3 = persona1 + persona2
print(persona3)