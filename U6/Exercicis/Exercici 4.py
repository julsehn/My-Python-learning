import importlib.util
import sys
ruta_biblioteca = "U6/Teoria/Llistat 6.21 Class Fracció.py"

spec = importlib.util.spec_from_file_location("Fraccio", ruta_biblioteca)
modul_fraccio = importlib.util.module_from_spec(spec)
spec.loader.exec_module(modul_fraccio)
Fraccio = modul_fraccio.Fraccio

q1_numerador = int(input("Introdueix el numerador de la primera fracció: "))
q1_denominador = int(input("Introdueix el denominador de la primera fracció: "))
q1 = Fraccio(q1_numerador, q1_denominador)

q2_numerador = int(input("Introdueix el numerador de la segona fracció: "))
q2_denominador = int(input("Introdueix el denominador de la segona fracció: "))
q2 = Fraccio(q2_numerador, q2_denominador)

if q1.valor_real() == q2.valor_real():
    print(f"Les fraccions {q1} i {q2} són equivalents.")
else:
    print(f"Les fraccions {q1} i {q2} no són equivalents.")