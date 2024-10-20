#Animating a gif 

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter

fig = plt.figure()
l, = plt.plot([], [], 'k--')

plt.xlim(-5,5)
plt.ylim(-5,5)

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Sin plot')

def func(x):
    return 3*np.sin(x)
    
metadata = dict(title='Movie',artist='Nobody')
writer = PillowWriter(fps = 15,metadata=metadata)

xlist = []
ylist = []

with writer.saving(fig, "output/sinWave_001.gif", 100):
    for xval in np.linspace(-5,5,100):
        xlist.append(xval)
        ylist.append(func(xval))
        
        l.set_data(xlist,ylist)
        
        writer.grab_frame()
