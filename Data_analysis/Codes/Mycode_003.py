#Model is y=ax+b(2x+7)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model

file_path = '../Data/Data_003.xlsx'
sheet_name = 'Linear_1'

df = pd.read_excel(file_path, sheet_name=sheet_name)

# Separate features and target variable
X = df[['X1']]
y = df['Data']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)  # ,random_state=42

# Create the linear regression model
reg = linear_model.LinearRegression()

# Fit the model using the training data
reg.fit(X_train, y_train)

# Print the coefficients
print("Coefficients:", reg.coef_)
print("Coefficients:", reg.intercept_)

#-------------------Plotting-------------------#
import matplotlib.pyplot as plt
import numpy as np

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.plot(X_train,y_train,'bo',label = 'Training Data')
plt.plot(X_test,y_test,'r^',label = 'Test Data')

x1 = np.linspace(0,12,100)
y1 = x1*reg.coef_ + reg.intercept_
plt.plot(x1,y1,'--',label = 'calculated',color = 'black')

plt.legend(loc = 'lower right')
plt.savefig('../Images/Img_003_2D.png')
plt.show()


#############################################################################################################################
#Now model is y= a0+a1*x1+a2*x2(7+2*x1+3*x2)
file_path = '../Data/Data_003.xlsx'
sheet_name = 'Linear_2'

df = pd.read_excel(file_path, sheet_name=sheet_name)

# Separate features and target variable
X = df[['X1','X2']]
y = df['Data']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)  # ,random_state=42

# Create the linear regression model
reg = linear_model.LinearRegression()

# Fit the model using the training data
reg.fit(X_train, y_train)

# Print the coefficients
print("Coefficients:", reg.coef_)
print("Coefficients:", reg.intercept_)
#--------------------3D Plotting--------------------
from mpl_toolkits.mplot3d import Axes3D

#Create a figure
fig = plt.figure()
ax =fig.add_subplot(111, projection = '3d')

tra_X = X_train[['X1']]
tra_y = X_train[['X2']]
tra_z = y_train

# Plot data
ax.scatter(tra_X, tra_y, tra_z, color = 'blue',label = 'Train data')
ax.set_title('3D Scatter Plot')

test_X = X_test[['X1']]
test_y = X_test[['X2']]
test_z = y_test

# Plot data
ax.scatter(test_X, test_y, test_z, color = 'red',label = 'Test data')
ax.set_title('3D Scatter Plot')

# Generate data
x = np.linspace(0,11, 100)
y = np.linspace(0,11, 100)
x, y = np.meshgrid(x, y)
z = reg.intercept_ + reg.coef_[0]*x + reg.coef_[1]*y

# Plot the surface
ax.plot_surface(x, y, z, cmap='coolwarm',alpha = 0.5,label = 'Predicted Surface') #viridis, plasma, inferno, magma,coolwarm, bwr, seismic,tab10, tab20, Set1

# Add labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.legend(loc = 'upper left')
plt.savefig('../Images/Img_003_3D.png')
plt.show()