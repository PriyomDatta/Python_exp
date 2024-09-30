#Problem: The data are complex but our assumption is Y = A*(X1) + B*(X2) + C*(X3) + D
#         Our aim is to find A,B,C,D
#Author: Priyom Datta

import pandas as pd
import numpy as np

#load excel file
file_path = '../Data/Data_001.xlsx'
df = pd.read_excel(file_path)

#Extract the columns
X = df.iloc[:, 11:14].values #three columns as independent var col: L,M,N
y = df.iloc[:, 14].values    #column as dependent var col: O

#print(X)
#print(y)  

#Add a column of ones to X to account for the intercept term in linear regression model
X = np.append(np.ones((X.shape[0],1)),X, axis = 1)
#print(X)

# Compute the coefficient using equation

coefficients = np.linalg.inv(X. T @ X) @ X.T @ y
intercept = coefficients[0]
x1_slope = coefficients[1]
x2_slope = coefficients[2]
x3_slope = coefficients[3]

print('Intercept: ' , intercept)
print('X1 slope: ' , x1_slope)
print('x2 slope: ' , x2_slope)
print('x3 slope: ' , x3_slope)