#Animating a mp4

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter
plt.rcParams['animation.ffmpeg_path'] = 'C:\\ffmpeg\\bin\\ffmpeg.exe' #need path for ffmpeg.exe

fig = plt.figure()
l, = plt.plot([], [], 'k--')
l2, = plt.plot([], [], 'm-')

plt.xlim(-5,5)
plt.ylim(-5,5)

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Sin plot')

def func(x):
    return 3*np.sin(x)
    
def func2(x):
    return 3*np.cos(x)
    
metadata = dict(title='Movie',artist='Nobody')
writer = FFMpegWriter(fps = 15,metadata=metadata)

xlist = []
ylist = []
ylist2 = []

with writer.saving(fig, "output/sinWave_002.mp4", 100):
    for xval in np.linspace(-5,5,100):
        xlist.append(xval)
        ylist.append(func(xval))
        ylist2.append(func2(xval))
        
        l.set_data(xlist,ylist)
        l2.set_data(xlist,ylist2)
        
        writer.grab_frame()
