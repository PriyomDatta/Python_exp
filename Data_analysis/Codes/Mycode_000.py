#Problem: In Data_000.xlsx y=3*(x1)+4*(x2)+ 15 and on D column we added some random values with y
#         Our aim is using x1,x2 and D colunm find out the values of 3,4,15
#         Will plot the data
#Author: Priyom Datta

import pandas as pd
import numpy as np

#load excel file
file_path = '../Data/Data_000.xlsx'
df = pd.read_excel(file_path)

#Extract the columns
X = df.iloc[:, :2].values #first two columns as independent var.
y = df.iloc[:, 3].values  #third column as dependent var

#print(X)
#print(y)  Some changes was observed

#Add a column of ones to X to account for the intercept
X = np.hstack([np.ones((X.shape[0],1)),X])

# Compute the coefficient using equation

coefficients = np.linalg.inv(X. T @ X) @ X.T @ y
intercept = coefficients[0]
x1_slope = coefficients[1]
x2_slope = coefficients[2]

print('Intercept: ' , intercept)
print('X1 slope: ' , x1_slope)
print('x2 slope: ' , x2_slope)

#-----------------------------Plotting------------------------------
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig =plt.figure()
ax = fig.add_subplot(111, projection ='3d')

#plot discrete points
array1 = X[:, 1]
array2 = X[:, 2]

ax.scatter(array1 , array2 , y , c="blue",marker = 'o')

#plot surface
# Generate data
a = np.linspace(0,60,200)
b = np.linspace(0,60,200)
a, b = np.meshgrid(a,b)
z = coefficients[0] + coefficients[1]*a + coefficients[2]*b

ax.plot_surface(a, b, z, cmap='coolwarm',alpha = 0.5)

# Add labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.savefig('../Images/Img_000.png')
plt.show()