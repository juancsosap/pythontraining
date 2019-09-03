#!/usr/bin/env python
# coding: utf-8

# Import the packages required
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR

# load the data from the datasets available in scikit learn
dataset = datasets.load_boston()
print(type(dataset))

# print the data structure information
print(dataset.keys())
print(dataset.data.shape)
print(dataset.feature_names)

# select the x and y data
x = dataset.data[:, np.newaxis, 5]
y = dataset.target
print(x.shape, y.shape)
print(x[0], y[0])

# Split the dataset in training data and testing data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

# Define the algorithm to be used, fit the model and generate a prediction
alg = SVR(kernel='linear', C=1.0, epsilon=0.2)
alg.fit(x_train, y_train)
y_pred = alg.predict(x_test)
print(y_pred.shape)

# Verify the model error based on R²
print('certainty:', alg.score(x_train, y_train) * 100, '%')
print('certainty:', alg.score(x_test, y_test) * 100, '%')

# Graph the test data with the model line
legend = dataset.feature_names[5]
data_test = sorted(zip(x_test, y_pred), key = lambda i : i[0])
plt.scatter(x, y)
plt.plot([i[0] for i in data_test], [i[1] for i in data_test], color='red', linewidth=3)
plt.title('Support Vector Regression')
plt.xlabel(legend)
plt.ylabel('Mean Value')
plt.show()

# Define the algorithm to be used, fit the model and generate a prediction
alg = SVR(kernel='poly', C=1.0, epsilon=0.2, gamma='auto')
alg.fit(x_train, y_train)
y_pred = alg.predict(x_test)
print(y_pred.shape)

# Verify the model error based on R²
print('certainty:', alg.score(x_train, y_train) * 100, '%')
print('certainty:', alg.score(x_test, y_test) * 100, '%')

# Graph the test data with the model line
legend = dataset.feature_names[5]
data_test = sorted(zip(x_test, y_pred), key = lambda i : i[0])
plt.scatter(x, y)
plt.plot([i[0] for i in data_test], [i[1] for i in data_test], color='red', linewidth=3)
plt.title('Support Vector Regression')
plt.xlabel(legend)
plt.ylabel('Mean Value')
plt.show()

# Define the algorithm to be used, fit the model and generate a prediction
alg = SVR(kernel='rbf', C=1.0, epsilon=0.2, gamma='auto')
alg.fit(x_train, y_train)
y_pred = alg.predict(x_test)
print(y_pred.shape)

# Verify the model error based on R²
print('certainty:', alg.score(x_train, y_train) * 100, '%')
print('certainty:', alg.score(x_test, y_test) * 100, '%')

# Graph the test data with the model line
legend = dataset.feature_names[5]
data_test = sorted(zip(x_test, y_pred), key = lambda i : i[0])
plt.scatter(x, y)
plt.plot([i[0] for i in data_test], [i[1] for i in data_test], color='red', linewidth=3)
plt.title('Support Vector Regression')
plt.xlabel(legend)
plt.ylabel('Mean Value')
plt.show()

# Define the algorithm to be used, fit the model and generate a prediction
alg = SVR(kernel='sigmoid', C=1.0, epsilon=0.2, gamma='auto')
alg.fit(x_train, y_train)
y_pred = alg.predict(x_test)
print(y_pred.shape)

# Verify the model error based on R²
print('certainty:', alg.score(x_train, y_train) * 100, '%')
print('certainty:', alg.score(x_test, y_test) * 100, '%')

# Graph the test data with the model line
legend = dataset.feature_names[5]
data_test = sorted(zip(x_test, y_pred), key = lambda i : i[0])
plt.scatter(x, y)
plt.plot([i[0] for i in data_test], [i[1] for i in data_test], color='red', linewidth=3)
plt.title('Support Vector Regression')
plt.xlabel(legend)
plt.ylabel('Mean Value')
plt.show()
