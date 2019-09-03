#!/usr/bin/env python
# coding: utf-8

# Import the packages required
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model, metrics
from sklearn.model_selection import train_test_split

# load the data from the datasets available in scikit learn
dataset = datasets.load_breast_cancer()
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
columns = 5
lines = num_graphs//columns

figure, plots = plt.subplots(lines, columns, figsize=(2.5*columns, 2.5*lines))
figure.suptitle('Linear Regression', y=1.02)

y_cat = [categories[i] for i in y]

for g in range(num_graphs):
    idr, idc = g//columns, g%columns

    plots[idr][idc].scatter(x[:,g], y_cat)
    plots[idr][idc].set_xlabel(legends[g])
    if idc != 0 : plots[idr][idc].set_yticklabels([])

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
print(y_pred[:10])
print(y_test[:10])

# Graph the test data with the model line
figure, plots = plt.subplots(lines, columns, figsize=(2.5*columns, 2.5*lines))
figure.suptitle('Linear Regression', y=1.02)

for g in range(num_graphs):
    idr, idc = g//columns, g%columns
    data_test = sorted(zip(x_test[:,g], y_pred), key = lambda i : i[0])

    plots[idr][idc].scatter(x[:,g], y)
    plots[idr][idc].plot([i[0] for i in data_test], [i[1] for i in data_test], color='red', linewidth=3)
    plots[idr][idc].set_xlabel(legends[g])
    if idc != 0 : plots[idr][idc].set_yticklabels([])
    
plt.tight_layout(pad=1)
plt.show()

# Map the predicted linear values to discrete values
y_pred_round = np.round(y_pred).astype(int)
print(y_pred_round[:10])
print(np.unique(y_pred_round))

# Fix the values outside te valid classes
min_y, max_y = np.min(y_train), np.max(y_train)
fixer = lambda i : min_y if i < min_y else max_y if i > max_y else i
y_pred_fix = np.array([i for i in map(fixer, y_pred_round)])
print(y_pred_fix[:10])
print(np.unique(y_pred_fix))

# Graph the test data with the model line
figure, plots = plt.subplots(lines, columns, figsize=(2.5*columns, 2.5*lines))
figure.suptitle('Linear Regression', y=1.02)

y_pred_cat = [categories[i] for i in y_pred_fix]

for g in range(num_graphs):
    idr, idc = g//columns, g%columns
    data_test = sorted(zip(x_test[:,g], y_pred_cat), key = lambda i : i[0])

    plots[idr][idc].scatter(x[:,g], y_cat)
    plots[idr][idc].plot([i[0] for i in data_test], [i[1] for i in data_test], color='red', linewidth=3)
    plots[idr][idc].set_xlabel(legends[g])
    if idc != 0 : plots[idr][idc].set_yticklabels([])
    
plt.tight_layout(pad=1)
plt.show()

# Validate, using the confusion matrix
matrix = metrics.confusion_matrix(y_test, y_pred_fix)
print(matrix)

# Calculate the metrics
precision = metrics.precision_score(y_test, y_pred_fix)
print('Precision :', precision * 100, '%')
accuracy = metrics.accuracy_score(y_test, y_pred_fix)
print('Accuracy  :', accuracy * 100, '%')
recall = metrics.recall_score(y_test, y_pred_fix)
print('Recall    :', recall * 100, '%')
f1 = metrics.f1_score(y_test, y_pred_fix)
print('F1        :', f1 * 100, '%')
roc_auc = metrics.roc_auc_score(y_test, y_pred_fix)
print('ROC/AUC   :', roc_auc * 100, '%')

# Verify the model error based on R²
print('certainty:', alg.score(x_train, y_train) * 100, '%')
print('certainty:', alg.score(x_test, y_test) * 100, '%')
