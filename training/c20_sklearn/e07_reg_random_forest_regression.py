#!/usr/bin/env python
# coding: utf-8

# Import the packages required
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# load the data from the datasets available in scikit learn
dataset = datasets.load_boston()
print(type(dataset))

# print the data structure information
print(dataset.keys())
print(dataset.data.shape)
print(dataset.feature_names)
print(dataset.DESCR)

# Define the algorithm to be used
alg = RandomForestRegressor(n_estimators=300, max_depth=5)

# Graph the importance of the features in the prediction
alg.fit(dataset.data, dataset.target)
features = dataset.data.shape[1]
plt.barh(range(features), alg.feature_importances_)
plt.yticks(np.arange(features), dataset.feature_names)
plt.xlabel('Features Importance')
plt.ylabel('Features')
plt.show()

# select the x and y data
x = dataset.data[:, [5,12]]
y = dataset.target
print(x.shape, y.shape)
print(x[0], y[0])

# plot the information
legends = dataset.feature_names[[5, 12]]
num_graphs = len(legends)

figure, plots = plt.subplots(1, num_graphs, figsize=(2.5*num_graphs, 2.5))
figure.suptitle('Random Forest Regression', y=1.02)

for g in range(num_graphs):
    plots[g].scatter(x[:,g], y)
    plots[g].set_xlabel(legends[g])
    if g != 0 : plots[g].set_yticklabels([])
    plots[0].set_ylabel('Mean Value')

plt.tight_layout(pad=1)
plt.show()

# Split the dataset in training data and testing data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

# Fit the model using the algorithm
alg.fit(x_train, y_train)

# Generate a prediction over the test data using the model
y_pred = alg.predict(x_test)
print(y_pred.shape)

# Graph the test data with the model line
figure, plots = plt.subplots(1, num_graphs, figsize=(2.5*num_graphs, 2.5))
figure.suptitle('Random Forest Regression', y=1.02)

for g in range(num_graphs):
    data_test = sorted(zip(x_test[:, g], y_pred), key = lambda i : i[0])

    plots[g].scatter(x[:,g], y)
    plots[g].plot([i[0] for i in data_test], [i[1] for i in data_test], color='red', linewidth=3)
    plots[g].set_xlabel(legends[g])
    if g != 0 : plots[g].set_yticklabels([])
    plots[0].set_ylabel('Mean Value')

plt.tight_layout(pad=1)
plt.show()

# Verify the model error based on R²
print('certainty:', alg.score(x_train, y_train) * 100, '%')
print('certainty:', alg.score(x_test, y_test) * 100, '%')
