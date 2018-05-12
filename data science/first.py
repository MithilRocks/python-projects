from sklearn import tree

x = [[1,2,3],[2,3,4],[5,3,2],[4,5,6],[12,2,89],[24,22,10],[2,6,4],[6,7,56]]
y = ['a','b','d','a','a','b','c','b']

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

prediction = clf.predict([[24,22,12]])

print(prediction)