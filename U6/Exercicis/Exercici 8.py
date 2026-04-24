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
class TriangleNoRegular(FiguraGeometrica):
    def __init__(self, nom, costat1, costat2, costat3):
        super().__init__(nom)
        self.costat1 = costat1
        self.costat2 = costat2
        self.costat3 = costat3
    @property
    def area(self):
        s = (self.costat1 + self.costat2 + self.costat3) / 2
        return math.sqrt(s * (s - self.costat1) * (s - self.costat2) * (s - self.costat3))
    def perimetre(self):
        return self.costat1 + self.costat2 + self.costat3
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
class HeptagonRegular(FiguraGeometricaRegular):
    def __init__(self, longitud_costat):
        super().__init__("Heptagon Regular", 7, longitud_costat)
    @property
    def area(self):
        return (self.nombre_costats * (self.longitud_costat ** 2)) / (4 * math.tan(math.pi / self.nombre_costats))
class OctagonRegular(FiguraGeometricaRegular):
    def __init__(self, longitud_costat):
        super().__init__("Octagon Regular", 8, longitud_costat)
    @property
    def area(self):
        return 2 * (1 + math.sqrt(2)) * (self.longitud_costat ** 2)


triangle = TriangleEquilater(6)
print(f"{triangle.nom}: Area = {triangle.area:.2f}, Perímetre = {triangle.perimetre():.2f}")
triangle_no_regular = TriangleNoRegular("Triangle No Regular", 3, 4, 5)
print(f"{triangle_no_regular.nom}: Area = {triangle_no_regular.area:.2f}, Perímetre = {triangle_no_regular.perimetre():.2f}")
quadrat = Quadrat(5)
print(f"{quadrat.nom}: Area = {quadrat.area:.2f}, Perímetre = {quadrat.perimetre():.2f}")
pentagon = PentagonRegular(4)
print(f"{pentagon.nom}: Area = {pentagon.area:.2f}, Perímetre = {pentagon.perimetre():.2f}")
hexagon = HexagonRegular(3)
print(f"{hexagon.nom}: Area = {hexagon.area:.2f}, Perímetre = {hexagon.perimetre():.2f}")
heptagon = HeptagonRegular(2)
print(f"{heptagon.nom}: Area = {heptagon.area:.2f}, Perímetre = {heptagon.perimetre():.2f}")
octagon = OctagonRegular(1)
print(f"{octagon.nom}: Area = {octagon.area:.2f}, Perímetre = {octagon.perimetre():.2f}")
