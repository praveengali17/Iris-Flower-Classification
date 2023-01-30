# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13BNnBT7D5CYGRdyfeibnI7Hp6zWMDBrl
"""



from sklearn.datasets import load_iris
iris = load_iris()
#print(iris.feature_names)
#print(iris.target_names)
#print(iris.data[0])
#print(iris.target[0])
#for i in range(len(iris.target)):
#  print("Example %d: label %s , feature %s"%(i,iris.target[i],iris.data[i]))

test_idx = [0,50,100]

#training data
train_target = np.delete(iris.target,test_idx)
train_data = np.delete(iris.data,test_idx,axis = 0)

test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data,train_target)

print(test_target)
print(clf.predict(test_data))

print(test_data[1],test_target[1])
print(iris.feature_names,iris.target_names)