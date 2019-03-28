"""Display random walk visualisation."""
import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolor='none', s=5)
    plt.show()

    keep_running = input("Generate new chart? (y/n): ")
    if keep_running == "n":
        break
