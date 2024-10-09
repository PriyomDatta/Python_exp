# Exploring different features of Ridge(Linear Model)
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

# Create the Ridge model set alpha as 1
reg_Ridge1 = linear_model.Ridge(alpha = 1)
# Fit the model using the training data
reg_Ridge1.fit(X_train, y_train)

# Create the Ridge model set alpha as 0
reg_Ridge2 = linear_model.Ridge(alpha = 0)
# Fit the model using the training data
reg_Ridge2.fit(X_train, y_train)

# Create the Ridge model set solver as ‘cholesky’
reg_Ridge3 = linear_model.Ridge(solver='cholesky')
# Fit the model using the training data
reg_Ridge3.fit(X_train, y_train)

# Create the Ridge model set solver as ‘sparse_cg’
reg_Ridge4 = linear_model.Ridge(solver='sparse_cg')
# Fit the model using the training data
reg_Ridge4.fit(X_train, y_train)

# Print the coefficients
print("Coefficients linear reg:", reg.coef_)
print("Coefficients linear reg:", reg.intercept_)

print("Coefficients Ridge reg(alpha 1):", reg_Ridge1.coef_)
print("Coefficients Ridge reg(alpha 1):", reg_Ridge1.intercept_)

print("Coefficients Ridge reg(alpha 0):", reg_Ridge2.coef_)
print("Coefficients Ridge reg(alpha 0):", reg_Ridge2.intercept_)

print("Coefficients Ridge reg(cholesky):", reg_Ridge3.coef_)
print("Coefficients Ridge reg(cholesky):", reg_Ridge3.intercept_)

print("Coefficients Ridge reg(sparse_cg):", reg_Ridge4.coef_)
print("Coefficients Ridge reg(sparse_cg):", reg_Ridge4.intercept_)
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

y2 = x1*reg_Ridge1.coef_ + reg_Ridge1.intercept_
plt.plot(x1,y2,'--',label = 'calculated_Ridge_Alpha1',color = 'orange')

y3 = x1*reg_Ridge2.coef_ + reg_Ridge2.intercept_
plt.plot(x1,y3,'--',label = 'calculated_Ridge_Alpha0',color = 'magenta')

y4 = x1*reg_Ridge3.coef_ + reg_Ridge3.intercept_
plt.plot(x1,y4,'--',label = 'calculated_Ridge_cholesky',color = 'green')

y5 = x1*reg_Ridge4.coef_ + reg_Ridge4.intercept_
plt.plot(x1,y5,'--',label = 'calculated_Ridge_sparse_cg',color = 'yellow')

plt.legend(loc = 'lower right')
plt.savefig('../Images/Img_004_2D.png')
plt.show()
