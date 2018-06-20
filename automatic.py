#!/user/bin/python3
import sklearn
from sklearn.datasets import load_iris

#loading iris data set
iris=load_iris()

#now splitting into test and train data sets 
from sklearn.model_selection import train_test_split
x,y,z,a=train_test_split(iris.data,iris.target,test_size=0.1)
''' x=train_iris {all features value containing 90%}
    y=remaining test iris{10% of features}
    z=train_target{all labels of containing 90% of iris.target}
    a=test_target{remaing 10% of iris.target}'''
print("value of x:")
print(x)
print("value of y:")
print(x)
print("value of z:")
print(z)
print("value of a:")
print(a)

#calling algo
from sklearn import tree
dsclf=tree.DecisionTreeClassifier()

#now training data with decision
trained=dsclf.fit(x,z)

#time for prediction
output=trained.predict(y)
print(output)

#acutal output 
print("Acutal output:")
print(z)

#now calculating accuracy
from sklearn.metrics import accuracy_score 

check_pct=accuracy_score(a,output) 
print("accuracy:")
print(check_pct)

result_x=[]
result_x.append(check_pct)
print(result_x)



