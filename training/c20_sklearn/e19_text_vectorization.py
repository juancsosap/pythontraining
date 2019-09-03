#!/usr/bin/env python
# coding: utf-8

# Import the packages required
from sklearn import datasets, model_selection, linear_model
from sklearn.feature_extraction.text import CountVectorizer

# load the data from the datasets available in scikit learn
dataset = datasets.fetch_20newsgroups(subset='train')
print(type(dataset))

# print the data structure information
print(dataset.keys())
print(dataset.target_names)
print(dataset.DESCR)

# select the features and labels from the data
x = dataset.data
y = dataset.target
print(x[0])
print('target:', y[0])

# Define the Tokenization algorithm to be used and fit the model
vector = CountVectorizer()
vector.fit(x)

# Verify the vocabulary learned
print(vector.vocabulary_)

# Transform the data to token list
tokens = vector.transform(dataset.data)
print(tokens.shape)
print(type(tokens))
print(tokens)

# Split the dataset in training data and testing data
x_train, x_test, y_train, y_test = model_selection.train_test_split(tokens, y, test_size=0.2)
print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

# Define the algorithm to be used and fit the model
alg = linear_model.LogisticRegression(solver = 'liblinear', multi_class='auto')
alg.fit(x_train, y_train)

# Verify the model error based on R²
print('certainty:', alg.score(x_train, y_train) * 100, '%')
print('certainty:', alg.score(x_test, y_test) * 100, '%')
