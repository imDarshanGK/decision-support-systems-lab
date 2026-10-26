# ============================================================
# EXPERIMENT NO. 11
# Implement a Basic Intelligent DSS Using Machine Learning
# ============================================================

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# Step 1: Create the Dataset
data = {
    "Age": [25, 32, 45, 29, 41, 52, 27, 36, 48, 30,
            39, 26, 43, 34, 50],

    "Income": [35000, 60000, 85000, 42000, 75000,
               90000, 38000, 65000, 70000, 45000,
               58000, 32000, 82000, 55000, 95000],

    "Credit_Score": [620, 720, 780, 650, 740, 800, 610,
                     710, 730, 640, 690, 600, 760, 680, 810],

    "Loan_Amount": [15000, 20000, 30000, 18000, 25000,
                    40000, 12000, 22000, 28000, 16000,
                    20000, 10000, 30000, 18000, 45000],

    "Debt": [8000, 5000, 4000, 12000, 7000, 6000, 9000,
             6000, 8000, 10000, 7000, 7000, 5000, 9000, 5000],

    "Employment": [
        "Salaried", "Salaried", "Salaried", "Self-Employed",
        "Salaried", "Self-Employed", "Salaried", "Salaried",
        "Self-Employed", "Self-Employed", "Salaried",
        "Salaried", "Salaried", "Self-Employed", "Salaried"
    ],

    "Loan_Decision": [
        "Rejected", "Approved", "Approved", "Rejected",
        "Approved", "Approved", "Rejected", "Approved",
        "Approved", "Rejected", "Approved", "Rejected",
        "Approved", "Rejected", "Approved"
    ]
}

df = pd.DataFrame(data)

print("=" * 60)
print("INTELLIGENT DSS - LOAN DECISION")
print("=" * 60)

print("\nHistorical Customer Dataset:")
print(df.to_string(index=False))

# Step 2: Check Missing Values and Data Types
print("\nMissing Values:")
print(df.isnull().sum())

print("\nDataset Data Types:")
print(df.dtypes)

# Step 3: Encode Categorical Variables
df["Employment"] = df["Employment"].map({
    "Salaried": 0,
    "Self-Employed": 1
})

df["Loan_Decision"] = df["Loan_Decision"].map({
    "Rejected": 0,
    "Approved": 1
})

# Step 4: Separate Features and Target
features = [
    "Age",
    "Income",
    "Credit_Score",
    "Loan_Amount",
    "Debt",
    "Employment"
]

X = df[features]
y = df["Loan_Decision"]

# Step 5: Split Dataset into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y
)

print("\nTraining Samples:", len(X_train))
print("Testing Samples:", len(X_test))

# Step 6: Create and Train Decision Tree Classifier
model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)

model.fit(X_train, y_train)

print("\nDecision Tree model trained successfully.")

# Step 7: Predict Test Outcomes
y_pred = model.predict(X_test)

# Step 8: Evaluate the Model
accuracy = accuracy_score(y_test, y_pred)

print(f"\nModel Accuracy: {accuracy:.2%}")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred, labels=[0, 1]))

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        labels=[0, 1],
        target_names=["Rejected", "Approved"],
        zero_division=0
    )
)

# Step 9: Define a New Customer
new_customer = pd.DataFrame([{
    "Age": 35,
    "Income": 65000,
    "Credit_Score": 720,
    "Loan_Amount": 20000,
    "Debt": 5000,
    "Employment": 0
}])

print("\nNew Customer Details:")
print(new_customer.to_string(index=False))

# Step 10: Predict the New Customer's Decision
prediction = model.predict(new_customer)[0]
probabilities = model.predict_proba(new_customer)[0]

class_index = list(model.classes_).index(prediction)
confidence = probabilities[class_index]

decision = "Approved" if prediction == 1 else "Rejected"

print("\nPredicted Loan Decision:", decision)
print(f"Model Confidence: {confidence:.2%}")

print("\nClass Probabilities:")
for class_label, probability in zip(
    model.classes_, probabilities
):
    label = "Approved" if class_label == 1 else "Rejected"
    print(f"{label}: {probability:.2%}")

# Step 11: Decision-Support Recommendation
print("\nDecision-Support Recommendation:")

if decision == "Approved":
    print("The model predicts approval.")
    print("Verify the customer's financial details before deciding.")
else:
    print("The model predicts rejection.")
    print("Review the customer's financial details and eligibility.")

print("\nNote: This is an educational model, not a real lending decision.")
print("\nExperiment completed successfully.")