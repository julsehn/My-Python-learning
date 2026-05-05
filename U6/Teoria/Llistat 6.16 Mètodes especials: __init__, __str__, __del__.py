class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat

    def __str__(self):
        return f"{self.nom} té {self.edat} anys."

    def __del__(self):
        print(f"{self.nom} ha mort.")

p1 = Persona("Joan", 30)
p1 = None

p2 = Persona("Maria", 25)
print(p2)