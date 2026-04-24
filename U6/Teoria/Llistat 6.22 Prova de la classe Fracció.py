import importlib.util
import sys
ruta_biblioteca = "U6/Teoria/Llistat 6.21 Class Fracció.py"

spec = importlib.util.spec_from_file_location("Fraccio", ruta_biblioteca)
modul_fraccio = importlib.util.module_from_spec(spec)
spec.loader.exec_module(modul_fraccio)
Fraccio = modul_fraccio.Fraccio

q1 = Fraccio(1, 2)
q2 = Fraccio(3, 4)

q_suma = q1 + q2
q_resta = q1 - q2

print(f"La suma de {q1} i {q2} és {q_suma}")
print(f"La resta de {q1} i {q2} és {q_resta}")

q_producte = q1 * q2
q_divisio = q1 / q2

print(f"El producte de {q1} i {q2} és {q_producte}")
print(f"La divisió de {q1} i {q2} és {q_divisio}")

q_invertit = q1.invertir()
print(f"L'invers de {q1} és {q_invertit}")

q_simplificada = Fraccio(8, 14)
q_simplificada.simplificar()

print(f"La fracció {Fraccio(8, 14)} la seva simplificació és {q_simplificada}")

q_valor_real = Fraccio(3, 5)
valor_real = q_valor_real.valor_real()
print(f"El valor real de {q_valor_real} és {valor_real}")