import pandas as pd
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree

# 1. Dataset

data = {
    'Age': [25, 40, 32, 52, 29, 45, 38, 30],
    'Income': [35000, 70000, 45000, 90000, 55000, 85000, 62000, 40000],
    'CreditScore': [650, 780, 720, 810, 690, 790, 740, 680],
    'Employed': [1, 1, 0, 1, 1, 1, 1, 0],
    'Loan': [0, 1, 0, 1, 0, 1, 1, 0]
}


# Convert dictionary into DataFrame
df = pd.DataFrame(data)

print("Dataset:")
print(df)

# 2. Input and Output

X = df[['Age', 'Income', 'CreditScore', 'Employed']]
y = df['Loan']


# 3. Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

print("\nTraining data:")
print(X_train)

print("\nTesting data:")
print(X_test)

# 4. Create Decision Tree

model = DecisionTreeClassifier(
    criterion='entropy',
    random_state=42
)

# 5. Train Model

model.fit(X_train, y_train)

# 6. Prediction on Test Data

y_pred = model.predict(X_test)

print("\nActual values:")
print(y_test.values)

print("\nPredicted values:")
print(y_pred)

# 7. Accuracy

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy =", accuracy)


# 8. New Customer Prediction

new_customer = pd.DataFrame(
    [[35, 65000, 750, 1]],
    columns=X.columns
)

prediction = model.predict(new_customer)


if prediction[0] == 1:
    print("\nLoan Approved")
else:
    print("\nLoan Rejected")

# 9. Display Decision Tree

plt.figure(figsize=(12, 8))

tree.plot_tree(
    model,
    feature_names=X.columns,
    class_names=["Reject", "Approve"],
    filled=True
)

plt.title("Loan Approval Decision Tree")
plt.show()