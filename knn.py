#!/user/bin/python3

#getting data
from sklearn.datasets import load_iris 

#to check % accuracy
from sklearn.metrics import accuracy_score

#to split into tesr and train datasets
from sklearn.model_selection import train_test_split 

#for k nearest neighbors algorithm 
from sklearn.neighbors import KNeighborsClassifier

#for decision tree algo 
from sklearn import tree 

#loading iris data 
iris=load_iris()

#now splitting data in target and train datasets
x,y,z,a=train_test_split(iris.data,iris.target,test_size=0.1)

'''
x=train_iris
y=test_iris
z=train_target
a=test_target'''


#calling decision tree classifier 
clf=tree.DecisionTreeClassifier()

#calling KNN classifier
knnclf=KNeighborsClassifier(n_neighbors=2) # here 2 indicates the value of K

#now train data with decision tree 
trained_DT=clf.fit(x,z)

#now trained data with knn 
trained_KNN=knnclf.fit(x,z)

#original output 
print("original output:",a)


#now prediction with DT
output_DT=trained_DT.predict(y)
print("predicted output with DT:",output_DT)

#now prediction with KNN 
output_KNN=trained_KNN.predict(y)
print("predicted output with KNN:",output_KNN)

#checking % of accuracy with DT
check_percentage_DT=accuracy_score(a,output_DT)
print("% of accuracy with DT:",check_percentage_DT)

#checking % of accuracy with KNN 
check_percentage_KNN=accuracy_score(a,output_KNN)
print("% of accuracy with KNN:",check_percentage_KNN)
