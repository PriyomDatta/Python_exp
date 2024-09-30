import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,500, 1000)
y1 = np.square(x)
y2 = np.sin(x*np.pi*2/360)
y3 = np.cos(x*np.pi*2/360)
y4 = np.power(x,3)

# Create the plot
plt.plot(x, y1)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('square Plot')

# Show the plot
plt.show()

#create another plot
plt.plot(x,y4, 'r--') #colour , circle ponints , dash line would be 'ro--'

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Cube Plot')
# Show the plot
plt.show()

#create plot
plt.plot(x,y2,'b-',label = 'sin(x)')
plt.plot(x,y3,'g--',label = 'cos(x)')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Multiple Plot')
plt.legend()
plt.savefig('../Data/sincos.jpg')
plt.show()

y5 = np.tan(x*np.pi*2/360)
y6 = np.sinh(x*np.pi*2/360)
y7 = np.cosh(x*np.pi*2/360)