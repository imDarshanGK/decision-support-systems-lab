import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree
import matplotlib.pyplot as plt

# Dataset

data = {
    'Age': [25, 40, 32, 52, 29, 45, 38, 30],
    'Income': [35000, 70000, 45000, 90000, 55000, 85000, 62000, 40000],
    'CreditScore': [650, 780, 720, 810, 690, 790, 740, 680],
    'Employed': [1, 1, 0, 1, 1, 1, 1, 0],
    'Loan': [0, 1, 0, 1, 0, 1, 1, 0]
}

df = pd.DataFrame(data)

# Input and Output

X = df[['Age', 'Income', 'CreditScore', 'Employed']]
y = df['Loan']

# Train Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

# Decision Tree Model

model = DecisionTreeClassifier(criterion='entropy')

model.fit(X_train, y_train)

# Prediction

y_pred = model.predict(X_test)

# Accuracy

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy =", accuracy)

# New Customer Prediction

new_customer = pd.DataFrame(
    [[35, 65000, 750, 1]],
    columns=X.columns
)

prediction = model.predict(new_customer)

if prediction[0] == 1:
    print("Loan Approved")
else:
    print("Loan Rejected")

# Display Tree

plt.figure(figsize=(12, 8))

tree.plot_tree(
    model,
    feature_names=X.columns,
    class_names=["Reject", "Approve"],
    filled=True
)

plt.show()