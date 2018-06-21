#!/user/bin/python3

import numpy
#import sklearn
from sklearn.datasets import load_iris
from sklearn import tree

#loading all data
iris=load_iris()

#printing features name
print(iris.feature_names)

#target names
print(iris.target_names)

#training data
print(iris.data)

#target data means flower data
print(iris.target)

x=[0,50,100]
only_target_training=numpy.delete(iris.target,x)
print(only_target_training)
print(only_target_training.size)


#testing target
test_target=iris.target[x]
print("only_test_target:")
print(test_target)

#training data value after deleting
only_data_training=numpy.delete(iris.data,x)
print(only_data_training)

#target data value after deleting
only_target_training=numpy.delete(iris.target,x) 
print(only_target_training)

#testing target
test_target=iris.target[x]
test_data=iris.data[x]
print(test_target)
print(test_data)

#calling algo
clf=tree.DecisionTreeClassifier()
trained=clf.fit(only_data_training,only_data_training)
output=trained.predict(test_data)
print(output)


