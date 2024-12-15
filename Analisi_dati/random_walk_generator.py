import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use('dark_background')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)

    ax.plot(rw.x_values, rw.y_values, linewidth=0.5)
    ax.set_aspect('equal')

    plt.show()

    continuare = input("Creare un'altro grafico (s/n): ")
    if continuare == 'n':
        break