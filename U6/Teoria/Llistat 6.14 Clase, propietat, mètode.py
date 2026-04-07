class Persona:
    nom = "Robert"
    edat = 35

    def incrementar_edat(self):
        self.edat += 1

p1 = Persona()
print(p1.nom, p1.edat)
p1.incrementar_edat()
print(p1.nom, p1.edat)