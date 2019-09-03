#!/usr/bin/env python
# coding: utf-8

# Import the packages required
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# load the data from the datasets available in scikit learn
dataset = datasets.load_iris()
print(type(dataset))

# print the data structure information
print(dataset.keys())
print(dataset.data.shape)
print(dataset.feature_names)
print(dataset.target_names)
print(dataset.DESCR)

# select the x and y data
x = dataset.data
y = dataset.target
print(x.shape, y.shape)
print(x[0], y[0])

# plot the information
legends = dataset.feature_names
categories = dataset.target_names
num_graphs = len(legends)

figure, plots = plt.subplots(1, num_graphs, figsize=(2.5*num_graphs, 2.5))
figure.suptitle('Logistic Regression', y=1.02)

y_cat = [categories[i] for i in y]

for g in range(num_graphs):
    plots[g].scatter(x[:,g], y_cat)
    plots[g].set_xlabel(legends[g])
    if g != 0 : plots[g].set_yticklabels([])

plt.tight_layout(pad=1)
plt.show()

# Split the dataset in training data and testing data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

# Scale the data to unify them
scaler = StandardScaler()
x_train_scale = scaler.fit_transform(x_train)
x_test_scale = scaler.fit_transform(x_test)

# Define the algorithm to be used, fit the model
alg = LogisticRegression(solver = 'lbfgs', multi_class='auto')
alg.fit(x_train_scale, y_train)

# Generate a prediction over the test data using the model
y_pred = alg.predict(x_test_scale)
print(y_pred.shape)
print(y_pred[:10])

# Graph the test data with the model line
figure, plots = plt.subplots(1, num_graphs, figsize=(2.5*num_graphs, 2.5))
figure.suptitle('Logistic Regression', y=1.02)

y_pred_cat = [categories[i] for i in y_pred]

for g in range(num_graphs):
    data_test = sorted(zip(x_test[:,g], y_pred_cat), key = lambda i : i[0])

    plots[g].scatter(x[:,g], y_cat)
    plots[g].plot([i[0] for i in data_test], [i[1] for i in data_test], color='red', linewidth=3)
    plots[g].set_xlabel(legends[g])
    if g != 0 : plots[g].set_yticklabels([])
    
plt.tight_layout(pad=1)
plt.show()

# Validate, using the confusion matrix
matrix = metrics.confusion_matrix(y_test, y_pred)
print(matrix)

# Verify the model error based on R²
print('certainty:', alg.score(x_train, y_train) * 100, '%')
print('certainty:', alg.score(x_test, y_test) * 100, '%')
