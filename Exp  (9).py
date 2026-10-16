from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y
)
knn = KNeighborsClassifier(n_neighbors=5)
dtree = DecisionTreeClassifier(max_depth=3, random_state=42)
knn.fit(X_train, y_train)
dtree.fit(X_train, y_train)
pred_knn = knn.predict(X_test)
pred_tree = dtree.predict(X_test)
print("k-NN accuracy:", accuracy_score(y_test, pred_knn))
print(confusion_matrix(y_test, pred_knn))
print("Decision Tree accuracy:", accuracy_score(y_test, pred_tree))
print(confusion_matrix(y_test, pred_tree))
