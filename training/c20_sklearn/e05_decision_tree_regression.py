# SciKit Learn must be installed
# pip install sklearn

# Import the packages required
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

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
plt.title('Decision Tree Regression')
plt.xlabel('Rooms Number')
plt.ylabel('Mean Value')
plt.show()

# Split the dataset in training data and testing data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

# Define the algorithm to be used
alg = DecisionTreeRegressor(max_depth = 5)

# Fit the model
alg.fit(x_train, y_train)

# Verify the prediction model using the test data 
y_pred = alg.predict(x_test)
print(y_pred.shape)

# Preparing the values to the model graph
x_grid = np.arange(min(x_test), max(x_test), 0.1)
x_grid = x_grid.reshape((len(x_grid), 1))
y_grid = alg.predict(x_grid)

# Graph the test data with the regretion line
plt.scatter(x_test, y_test)
plt.plot(x_grid, y_grid, color='red', linewidth=3)
plt.title('Decision Tree Regression')
plt.xlabel('Rooms Number')
plt.ylabel('Mean Value')
plt.show()

# Verify the model error based on R²
print('certainty:', alg.score(x_train, y_train) * 100, '%')
