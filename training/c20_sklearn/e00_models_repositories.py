#!/usr/bin/env python
# coding: utf-8

# Import the packages required
from sklearn import datasets
from sklearn import linear_model, svm, tree, ensemble, neighbors, neural_network, cluster
from sklearn import preprocessing, decomposition

# ## Regression Data

dsfs = [datasets.load_boston, datasets.load_diabetes]

for dsf in dsfs:

    # load the data from the datasets available in scikit learn
    dataset = dsf()

    # print the data structure information
    print('* Dataset Type:',type(dataset))
    print('* Dataset Content:',dataset.keys())
    print('* Data Shape:',dataset.data.shape)
    print('* Feature Names:',dataset.feature_names)
    print('* Data:',dataset.data[0])
    print('* Target:',dataset.target[0])
    print('* Dataset Description:\n',dataset.DESCR)

# ## Classification Data

dsfs = [datasets.load_iris, datasets.load_breast_cancer,
        datasets.load_linnerud, datasets.load_wine]

for dsf in dsfs:

    # load the data from the datasets available in scikit learn
    dataset = dsf()

    # print the data structure information
    print('* Dataset Type:',type(dataset))
    print('* Dataset Content:',dataset.keys())
    print('* Data Shape:',dataset.data.shape)
    print('* Feature Names:',dataset.feature_names)
    print('* Target Names:',dataset.target_names)
    print('* Data:',dataset.data[0])
    print('* Target:',dataset.target[0])
    print('* Dataset Description:\n',dataset.DESCR)

# ## Image Processing Data

# load the data from the datasets available in scikit learn
dataset = datasets.load_digits()

# print the data structure information
print('* Dataset Type:',type(dataset))
print('* Dataset Content:',dataset.keys())
print('* Data Shape:',dataset.data.shape)
print('* Target Names:',dataset.target_names)
print('* Data:',dataset.data[0])
print('* Target:',dataset.target[0])
print('* Dataset Description:\n',dataset.DESCR)

# ## Models
packages = [linear_model, svm, tree, ensemble, neighbors, 
            cluster, neural_network, preprocessing, decomposition]

for package in packages:
    print([item for item in dir(package) if item[0].isupper()])
