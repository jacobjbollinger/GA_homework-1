import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from __future__ import division

iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target
