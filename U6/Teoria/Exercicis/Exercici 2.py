import matplotlib.pyplot as plt

equips = ['Equip A', 'Equip B', 'Equip C', 'Equip D', 'Equip E', 'Equip F']
punts = [78, 72, 69, 65, 62, 60]

plt.bar(equips, punts, color='blue')
plt.title('Punts dels primers sis classificats')
plt.xlabel('Equips')
plt.ylabel('Punts')
plt.show()