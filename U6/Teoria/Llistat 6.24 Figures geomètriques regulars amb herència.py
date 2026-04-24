import math
class FiguraGeometrica:
    def __init__(self,nom):
        self.nom = nom
    @property
    def area(self):
        pass
    def perimetre(self):
        pass
class FiguraGeometricaRegular(FiguraGeometrica):
    def __init__(self, nom, nombre_costats, longitud_costat):
        super().__init__(nom)
        self.nombre_costats = nombre_costats
        self.longitud_costat = longitud_costat
    @property
    def area(self):
        import math
        return (self.nombre_costats * (self.longitud_costat ** 2)) / (4 * math.tan(math.pi / self.nombre_costats))
    def perimetre(self):
        return self.nombre_costats * self.longitud_costat
class TriangleEquilater(FiguraGeometricaRegular):
    def __init__(self, longitud_costat):
        super().__init__("Triangle Equilater", 3, longitud_costat)
    @property
    def area(self):
        import math
        return (math.sqrt(3) / 4) * (self.longitud_costat ** 2)
class Quadrat(FiguraGeometricaRegular):
    def __init__(self, longitud_costat):
        super().__init__("Quadrat", 4, longitud_costat)
    @property
    def area(self):
        return self.longitud_costat ** 2
class PentagonRegular(FiguraGeometricaRegular):
    def __init__(self, longitud_costat):
        super().__init__("Pentagon Regular", 5, longitud_costat)
    @property
    def area(self):
        return (self.nombre_costats * (self.longitud_costat ** 2)) / (4 * math.tan(math.pi / self.nombre_costats))
class HexagonRegular(FiguraGeometricaRegular):
    def __init__(self, longitud_costat):
        super().__init__("Hexagon Regular", 6, longitud_costat)
    @property
    def area(self):
        return (3 * math.sqrt(3) / 2) * (self.longitud_costat ** 2)


triangle = TriangleEquilater(6)
print(f"{triangle.nom}: Area = {triangle.area:.2f}, Perímetre = {triangle.perimetre():.2f}")
quadrat = Quadrat(5)
print(f"{quadrat.nom}: Area = {quadrat.area:.2f}, Perímetre = {quadrat.perimetre():.2f}")
pentagon = PentagonRegular(4)
print(f"{pentagon.nom}: Area = {pentagon.area:.2f}, Perímetre = {pentagon.perimetre():.2f}")
hexagon = HexagonRegular(3)
print(f"{hexagon.nom}: Area = {hexagon.area:.2f}, Perímetre = {hexagon.perimetre():.2f}")