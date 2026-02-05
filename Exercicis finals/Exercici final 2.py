num_usuari = int(input("Ingrese el seu numero: "))
xifres = 0
print(num_usuari)
numero = 0
final = ""

for hell in str(num_usuari):
  final += str(int(hell) % 2)

print(final)