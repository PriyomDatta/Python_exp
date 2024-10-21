import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))

def update(frame):
    scale = 0 + 1.5 * np.sin(frame / 10.0)
    ax.clear()
    ax.plot_surface(scale * x, scale * y, scale * z, color='b',alpha = 0.2)
    ax.plot_surface(scale * x * 1.5, scale * y * 1.5, scale * z, color='r',alpha = 0.2)
    ax.plot_surface(scale * x, scale * y * 1.5, scale * z * 1.5, color='g',alpha = 0.2)
    ax.plot_surface(scale * x * 1.5, scale * y, scale * z * 1.5, color='y',alpha = 0.2)
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)
    ax.set_title("Growing and Shrinking Sphere")
    return ax,

ani = FuncAnimation(fig, update, frames=100, interval=50)

# Save animation as .gif
writer = PillowWriter(fps=15)
ani.save("output/growing_shrinking_sphere_004.gif", writer=writer)

plt.show()
