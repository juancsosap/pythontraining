#!/usr/bin/env python
# coding: utf-8

# Import the packages required
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
import joblib

# load the data from the datasets available in scikit learn
dataset = datasets.load_boston()
print(type(dataset))

# select the x and y data
x = dataset.data[:, np.newaxis, 5]
y = dataset.target
print(x.shape, y.shape)
print(x[0], y[0])

# Split the dataset in training data and testing data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

# Define the algorithm to be used, fit the model
alg = linear_model.LinearRegression()
alg.fit(x_train, y_train)

# Save a persistency of the fit model in a file
joblib.dump(alg, 'linear_regression.model')

# Load a persistence fit model from a file
lr = joblib.load('linear_regression.model')

# Generate a prediction over the test data using the model
y_pred = lr.predict(x_test)
print(y_pred.shape)


# In[ ]:


# Graph the test data with the model line
legend = dataset.feature_names[5]
data_test = sorted(zip(x_test, y_pred), key = lambda i : i[0])
plt.scatter(x_test, y_test)
plt.plot([i[0] for i in data_test], [i[1] for i in data_test], color='red', linewidth=3)
plt.title('Simple Linear Regression')
plt.xlabel(legend)
plt.ylabel('Mean Value')
plt.show()


# In[ ]:


# Verify the model error based on R²
print('certainty:', alg.score(x_train, y_train) * 100, '%')
print('certainty:', alg.score(x_test, y_test) * 100, '%')

