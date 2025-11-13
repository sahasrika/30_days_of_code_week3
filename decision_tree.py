from sklearn import tree
from sklearn.datasets import load_iris

iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)

pred = clf.predict([[5.1, 3.5, 1.4, 0.2]])
print(f"Predicted class: {iris.target_names[pred][0]}")
