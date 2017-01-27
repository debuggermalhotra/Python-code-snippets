# I have used Iris data set in this program. Checkout https://en.wikipedia.org/wiki/Iris_flower_data_set for more
from sklearn.datasets import load_iris
from sklearn import tree
import numpy as np
iris = load_iris()

# 1st part:
'''print(iris.feature_names) #will print the featurs
print(iris.target_names)  #will print the targets(flowers)
print(iris.data[0])  #data at index 1
print(iris.target[0])
for i in range(1,10):
    print ("Example %d: label: %s features: %s" % (i, iris.target[i],iris.data[i]))'''

#2nd part:

test_idx=[0,50,100]

    #training data:
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

    #testing data:
test_target=iris.target[test_idx]
test_data = iris.data[test_idx]

#training data
clf=tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

#using tree to classify our testing data
print(test_target)

#using the tree to predict a lbel for another flower
print(clf.predict(test_data))