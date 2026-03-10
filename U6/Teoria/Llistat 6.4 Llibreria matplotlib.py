import matplotlib.pyplot as plt

mesos = ['Gener', 'Febrer', 'Març', 'Abril', 'Maig', 'Juny']
vendes = [100, 120, 90, 110, 80, 130]

plt.bar(mesos, vendes, color='blue')
plt.title('Vendes mensuals')
plt.xlabel('Mesos')
plt.ylabel('Vendes')
plt.show()