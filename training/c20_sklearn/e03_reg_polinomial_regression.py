#!/usr/bin/env python
# coding: utf-8

# Import the packages required
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

# load the data from the datasets available in scikit learn
dataset = datasets.load_boston()
print(type(dataset))

# print the data structure information
print(dataset.keys())
print(dataset.data.shape)
print(dataset.feature_names)
print(dataset.DESCR)

# select the x and y data
x = dataset.data[:, np.newaxis, 5]
y = dataset.target
print(x.shape, y.shape)
print(x[0], y[0])

# plot the information
legend = dataset.feature_names[5]

plt.scatter(x, y)
plt.title('Polynomial Linear Regression')
plt.xlabel(legend)
plt.ylabel('Mean Value')
plt.show()

# Split the dataset in training data and testing data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)
print(x_train[0])

# Transform the data from polinomial to Lineal
poly = PolynomialFeatures(degree = 2)
x_train_poly = poly.fit_transform(x_train)
x_test_poly = poly.fit_transform(x_test)
print(x_train_poly.shape, x_test_poly.shape)
print(x_train_poly[0])

# Define the algorithm to be used, fit the model
alg = linear_model.LinearRegression()
alg.fit(x_train_poly, y_train)

# Generate a prediction over the test data using the model
y_pred = alg.predict(x_test_poly)
print(y_pred.shape)

# Graph the test data with the model line
data_test = sorted(zip(x_test, y_pred), key = lambda i : i[0])
plt.scatter(x, y)
plt.plot([i[0] for i in data_test], [i[1] for i in data_test], color='red', linewidth=3)
plt.title('Polynomial Linear Regression')
plt.xlabel(legend)
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
print('certainty:', alg.score(x_test_poly, y_test) * 100, '%')
