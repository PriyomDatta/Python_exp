import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

plt.rcParams['animation.ffmpeg_path'] = 'C:\\ffmpeg\\bin\\ffmpeg.exe' #need path for ffmpeg.exe


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

surf = ax.plot_surface(x, y, z, cmap='viridis')

def update(frame):
    ax.clear()
    z = np.sin(np.sqrt(x**2 + y**2) + frame / 10.0)
    ax.plot_surface(x, y, z, cmap='viridis')
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_zlim(-1, 1)
    ax.set_title("3D Animated Sine Wave")

ani = FuncAnimation(fig, update, frames=100, interval=50)

# Save animation as .mp4
metadata = dict(title='3D Sine Wave', artist='Python')
writer = FFMpegWriter(fps=15, metadata=metadata)
ani.save("output/3d_wave_003.mp4", writer=writer)

plt.show()
