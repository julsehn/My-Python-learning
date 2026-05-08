llista1 = ["taronja", "platan", "pera", "poma", "kiwi"]
print(llista1)
print(llista1[0])

try:
    element = llista1[6]
    print(element)
except IndexError:
    print("L'índex està fora dels límits de la llista.")

llista1[2] = "maduixa"
print(llista1)
print(llista1[-1])
print(llista1[-2])
print(llista1[-len(llista1)])