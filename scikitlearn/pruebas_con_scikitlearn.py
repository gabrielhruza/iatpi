from sklearn.datasets import load_iris
from sklearn import tree
import graphviz

iris = load_iris()

clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)

print(clf)

dot_data = tree.export_graphviz(clf, out_file=None)

graph = graphviz.Source(dot_data)
graph.render("iris")