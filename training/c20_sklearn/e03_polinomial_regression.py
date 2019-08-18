# SciKit Learn must be installed
# pip install sklearn

# Import the packages required
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

# load the data from the datasets available in scikit learn
boston = datasets.load_boston()

# print the data structure information
print(boston.keys())
print(boston.DESCR)
print(boston.data.shape)
print(boston.feature_names)

# select the x and y data
x = boston.data[:, np.newaxis, 5]
print(x.shape)
y = boston.target
print(y.shape)

# plot the information
plt.scatter(x, y)
plt.title('Polynomial Linear Regression')
plt.xlabel('Rooms Number')
plt.ylabel('Mean Value')
plt.show()

# Split the dataset in training data and testing data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)
print(x_train[0])

# Transform the data from polinomial to Lineal
poly = PolynomialFeatures(degree = 2)
x_train_poly = poly.fit_transform(x_train)
x_test_poly = poly.fit_transform(x_test)
print(x_train_poly.shape)
print(x_test_poly.shape)
print(x_train_poly[0])

# Define the algorithm to be used
alg = linear_model.LinearRegression()

# Fit the model
alg.fit(x_train_poly, y_train)

# Verify the prediction model using the test data 
y_pred = alg.predict(x_test_poly)
print(y_pred.shape)

# Graph the test data with the regretion line
plt.scatter(x_test, y_test)
plt.plot(x_test, y_pred, color='red', linewidth=3)
plt.title('Polynomial Linear Regression')
plt.xlabel('Rooms Number')
plt.ylabel('Mean Value')
plt.show()

# Obtain the parameters ai for this model
a0 = alg.intercept_
print('a0:', a0)
a = alg.coef_
print('ai:', a)
print('y =', a0 + a[0], '+', a[1], '* x +', a[2], '* x^2')

# Verify the model error based on R²
print('certainty:', alg.score(x_train_poly, y_train) * 100, '%')
