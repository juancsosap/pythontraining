#!/usr/bin/env python
# coding: utf-8

# Import the packages required
from sklearn import datasets, model_selection, neural_network

# load the data from the datasets available in scikit learn
dataset = datasets.load_iris()
print(type(dataset))

# select the features and labels from the data
features = dataset.data
labels = dataset.target

# Split the dataset in training data and testing data
f_train, f_test, l_train, l_test = model_selection.train_test_split(features, labels, test_size=0.2)
print(f_train.shape, l_train.shape)
print(f_test.shape, l_test.shape)

# Define the algorithm to be used, fit the model
net = neural_network.MLPClassifier(max_iter=1000, hidden_layer_sizes=(10, 10))
net.fit(f_train, l_train)

# Verify the model error based on R²
print('certainty:', net.score(f_train,l_train) * 100, '%')
print('certainty:', net.score(f_test, l_test) * 100, '%')
