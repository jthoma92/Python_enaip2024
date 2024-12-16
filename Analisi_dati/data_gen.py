import matplotlib.pyplot as plt
from random_walk import RandomWalk

# max_number_calculation = 1000

#list comprehension per creare le liste dei valori
# input_values = [x for x in range(1,max_number_calculation+1)]
# squares = [x**2 for x in range(1,max_number_calculation+1)]

# plt.style.use('seaborn-v0_8-notebook')
# fig, ax = plt.subplots()
#ax.plot(input_values, squares, linewidth = 3)
# ax.scatter(input_values, squares, s=2)
# ax.scatter(input_values, squares, color = 'red', s=10)
# ax.scatter(input_values, squares, c = squares, cmap = plt.cm.Blues, s = 10)

#impostare nome del grafico e assi
# ax.set_title("Numeri quadrati", fontsize=24)
# ax.set_xlabel("Valore", fontsize=14)
# ax.set_ylabel("Il quadrato del numero", fontsize=14)


#impostare il formato dei segni
# ax.tick_params(labelsize = 14)
# ax.ticklabel_format(style = 'plain')

#impostare la gamma per gli assi
#ax.axis([0,max_number_calculation+100, 0, 1_100_000])

#aggiornamento per randomwalk:
rw = RandomWalk(10000)
rw.fill_walk()

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15, cmap='plasma')
ax.set_aspect('equal')
print(rw.x_values,rw.y_values)
plt.show()