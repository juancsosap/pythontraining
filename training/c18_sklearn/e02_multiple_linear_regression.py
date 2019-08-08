# y = a0 + a1*x1 + a2*x2 + ... + an*xn
# where a0 is the intersection with the y axis
# and the rest ai are the slope asociated with
# each xi axis

# to messure the error could be used the MSE
# or mean square error
# r^2 = 1 - ESS / TSS

# SciKit Learn must be installed
# pip install sklearn

# Import the packages required
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split

# load the data from the datasets available in scikit learn
boston = datasets.load_boston()

# print the data structure information
print(boston.keys())
print(boston.DESCR)
print(boston.data.shape)
print(boston.feature_names)

# select the x and y data
x = boston.data[:, 5:8]
print(x)
y = boston.target
print(y)

# plot the information
plt.scatter(x[:,0], y)
plt.title('Multiple Linear Regression')
plt.xlabel('Rooms Number')
plt.ylabel('Mean Value')
plt.show()

plt.scatter(x[:,1], y)
plt.title('Multiple Linear Regression')
plt.xlabel('Age')
plt.ylabel('Mean Value')
plt.show()

plt.scatter(x[:,2], y)
plt.title('Multiple Linear Regression')
plt.xlabel('Distance')
plt.ylabel('Mean Value')
plt.show()

# Split the dataset in training data and testing data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

# Define the algorithm to be used
alg = linear_model.LinearRegression()

# Fit the model
alg.fit(x_train, y_train)

# Verify the prediction model using the test data 
y_pred = alg.predict(x_test)
print(y_pred.shape)

# Graph the test data with the regretion line
plt.scatter(x[:,0], y)
plt.plot(x_test[:,0], y_pred, color='red', linewidth=3)
plt.title('Multiple Linear Regression')
plt.xlabel('Rooms Number')
plt.ylabel('Mean Value')
plt.show()

plt.scatter(x[:,1], y)
plt.plot(x_test[:,1], y_pred, color='red', linewidth=3)
plt.title('Multiple Linear Regression')
plt.xlabel('Age')
plt.ylabel('Mean Value')
plt.show()

plt.scatter(x[:,2], y)
plt.plot(x_test[:,2], y_pred, color='red', linewidth=3)
plt.title('Multiple Linear Regression')
plt.xlabel('Distance')
plt.ylabel('Mean Value')
plt.show()

# Obtain the parameters ai for this model
a0 = alg.intercept_
print('a0:', a0)
a = alg.coef_
print('ai:', a)
print('y =', a0, '+', a[0], '* x1 +', a[1], '* x2 +', a[2], '* x3')

# Verify the model error based on R²
print('certainty:', alg.score(x_train, y_train) * 100, '%')
