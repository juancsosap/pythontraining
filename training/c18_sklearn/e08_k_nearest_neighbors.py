# SciKit Learn must be installed
# pip install sklearn

# Import the packages required
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, precision_score, f1_score, \
                            accuracy_score, recall_score, roc_auc_score

# load the data from the datasets available in scikit learn
cancer = datasets.load_breast_cancer()

# print the data structure information
print(cancer.keys())
print(cancer.DESCR)
print(cancer.data.shape)
print(cancer.feature_names)

# select the x and y data
x = cancer.data
print(x.shape)
y = cancer.target
print(y.shape)

# Split the dataset in training data and testing data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

# Define the algorithm to be used
alg = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)

# Fit the model
alg.fit(x_train, y_train)

# Verify the prediction model using the test data 
y_pred = alg.predict(x_test)
print(y_pred.shape)

# Validate, using the confusion matrix
matrix = confusion_matrix(y_test, y_pred)
print(matrix)

# Calculate the metrics
precision = precision_score(y_test, y_pred)
print(precision * 100, '% \t Precision')
accuracy = accuracy_score(y_test, y_pred)
print(accuracy * 100, '% \t Accuracy')
recall = recall_score(y_test, y_pred)
print(recall * 100, '% \t Recall')
f1 = f1_score(y_test, y_pred)
print(f1 * 100, '% \t F1')
roc_auc = roc_auc_score(y_test, y_pred)
print(roc_auc * 100, '% \t ROC-AUC')
