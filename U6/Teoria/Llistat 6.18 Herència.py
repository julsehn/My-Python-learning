class Vehicle:
    def __init__(self, marca, model, preu):
        self.marca = marca
        self.model = model
        self.preu = preu

class Cotxe(Vehicle):
    def __init__ (self, marca, model, preu, portes):
        super().__init__(marca, model, preu)
        self.portes = portes
    def __str__(self):
        return f"{self.marca} {self.model} amb {self.portes} portes i preu de {self.preu} euros."

class Moto(Vehicle):
    def __init__(self, marca, model, preu, cilindrada):
        super().__init__(marca, model, preu)
        self.cilindrada = cilindrada
    def __str__(self):
        return f"{self.marca} {self.model} amb {self.cilindrada} cm³ de cilindrada i preu de {self.preu} euros."

cotxe1 = Cotxe("Toyota", "Corolla", 20000, 4)
moto1 = Moto("Honda", "CBR500R", 7000, 500)

print(cotxe1)
print(moto1)