import matplotlib.pyplot as plt
import numpy as np
import random

x_values = []
y_values = []

fig, ax = plt.subplots()
scat = ax.scatter(x_values, y_values, color='black')

try:
    for _ in range(1000):
        x_values.append(random.randint(0, 100))
        y_values.append(random.randint(0, 100))

        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        scat.set_offsets(np.c_[x_values, y_values])
        plt.pause(0.001)
except KeyboardInterrupt:
    plt.close(fig)

plt.show()

#kill the terminal to stop animation. try 'ctr+c'