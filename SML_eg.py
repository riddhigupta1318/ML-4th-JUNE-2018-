#!/usr/bin/python3
from sklearn import tree
#features about APPLE=0 and ORANGE=1

data=[[100,0],[130,0],[135,1],[150,1]]

output=["APPLE","APPLE","ORANGE","ORANGE"]

#decision tree algorithm call
trained_algo=tree.DecisionTreeClassifier()

#train the data
trained_data=trained_algo.fit(data,output)

#now testing phase
predict_1=trained_algo.predict([[100,1]])
predict_2=trained_algo.predict([[145,1]])

#printing the output
print(predict_1)
print(predict_2)
