class Fraccio:
    def __init__(self, numerador=0, denominador=1):
        self.numerador = numerador
        self.denominador = denominador
    def __str__(self):
        return f"{self.numerador}/{self.denominador}"
    def __add__(self, altra_fracció):
        num = self.numerador * altra_fracció.denominador + altra_fracció.numerador * self.denominador
        den = self.denominador * altra_fracció.denominador
        return Fraccio(num, den)
    def __sub__(self, altra_fracció):
        num = self.numerador * altra_fracció.denominador - altra_fracció.numerador * self.denominador
        den = self.denominador * altra_fracció.denominador
        return Fraccio(num, den)
    def __mul__(self, altra_fracció):
        num = self.numerador * altra_fracció.numerador
        den = self.denominador * altra_fracció.denominador
        return Fraccio(num, den)
    def __truediv__(self, altra_fracció):
        num = self.numerador * altra_fracció.denominador
        den = self.denominador * altra_fracció.numerador
        return Fraccio(num, den)
    def simplificar(self):
        divisor = self.mcd(self.numerador, self.denominador)
        self.numerador //= divisor
        self.denominador //= divisor
    def valor_real(self):
        return self.numerador / self.denominador
    def invertir(self):
        self.numerador, self.denominador = self.denominador, self.numerador
    
    @staticmethod
    def mcd(a, b):
        while b == 0:
            return a
        return Fraccio.mcd(b, a % b)