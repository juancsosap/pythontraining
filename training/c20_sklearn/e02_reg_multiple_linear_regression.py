#!/usr/bin/env python
# coding: utf-8

# Import the packages required
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split

# load the data from the datasets available in scikit learn
dataset = datasets.load_boston()
print(type(dataset))

# print the data structure information
print(dataset.keys())
print(dataset.data.shape)
print(dataset.feature_names)
print(dataset.DESCR)

# select the x and y data
x = dataset.data[:, [5, 6, 7, 12]]
y = dataset.target
print(x.shape, y.shape)
print(x[0], y[0])

# plot the information
legends = dataset.feature_names[[5, 6, 7, 12]]
num_graphs = len(legends)
columns = 2
lines = num_graphs//columns

figure, plots = plt.subplots(lines, columns, figsize=(2.5*columns, 2.5*lines))
figure.suptitle('Multiple Linear Regression', y=1.02)

for g in range(num_graphs):
    idr, idc = g//columns, g%columns

    plots[idr][idc].scatter(x[:,g], y)
    plots[idr][idc].set_xlabel(legends[g])
    if idc != 0 : plots[idr][idc].set_yticklabels([])
    plots[idr][0].set_ylabel('Mean Value')

plt.tight_layout(pad=1)
plt.show()

# Split the dataset in training data and testing data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

# Define the algorithm to be used, fit the model
alg = linear_model.LinearRegression()
alg.fit(x_train, y_train)

# Generate a prediction over the test data using the model
y_pred = alg.predict(x_test)
print(y_pred.shape)

# Graph the test data with the model line
figure, plots = plt.subplots(lines, columns, figsize=(2.5*columns, 2.5*lines))
figure.suptitle('Multiple Linear Regression', y=1.02)

for g in range(num_graphs):
    idr, idc = g//columns, g%columns

    data_test = sorted(zip(x_test[:,g], y_pred), key = lambda i : i[0])
    
    plots[idr][idc].scatter(x[:,g], y)
    plots[idr][idc].plot([i[0] for i in data_test], [i[1] for i in data_test], color='red', linewidth=3)
    plots[idr][idc].set_xlabel(legends[g])
    if idc != 0 : plots[idr][idc].set_yticklabels([])
    plots[idr][0].set_ylabel('Mean Value')

plt.tight_layout(pad=1)
plt.show()

# Obtain the parameters ai for this model
a0 = alg.intercept_
print('a0:', a0)
a = alg.coef_
print('ai:', a)
print('y =', a0, '+', a[0], '* x1 +', a[1], '* x2 +', a[2], '* x3')

# Verify the model error based on R²
print('certainty:', alg.score(x_train, y_train) * 100, '%')
print('certainty:', alg.score(x_test, y_test) * 100, '%')
