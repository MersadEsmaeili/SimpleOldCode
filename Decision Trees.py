import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


#YOU SHOULD PROVIDE data.csv and requirements


# Load data
data = pd.read_csv('data.csv')

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(data[['x1', 'x2']], data['y'], test_size=0.2, random_state=0)

# Train model
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)

# Predict on test set
y_pred = clf.predict(X_test)

# Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)
