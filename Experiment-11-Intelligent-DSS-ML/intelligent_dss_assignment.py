# Experiment No. 11 - Assignment
# Intelligent DSS Using Machine Learning

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Step 1: Create Customer Dataset
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

print("=" * 65)
print("INTELLIGENT DSS - MODEL COMPARISON ASSIGNMENT")
print("=" * 65)

# Step 2: Encode Categorical Variables
df["Employment"] = df["Employment"].map({
    "Salaried": 0,
    "Self-Employed": 1
})

df["Loan_Decision"] = df["Loan_Decision"].map({
    "Rejected": 0,
    "Approved": 1
})

# Step 3: Separate Features and Target
features = [
    "Age", "Income", "Credit_Score",
    "Loan_Amount", "Debt", "Employment"
]

X = df[features]
y = df["Loan_Decision"]

# Step 4: Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y
)

print("\nTraining Samples:", len(X_train))
print("Testing Samples:", len(X_test))

# Step 5: Create Two Models
models = {
    "Decision Tree": DecisionTreeClassifier(
        criterion="gini", max_depth=3, random_state=42
    ),
    "Random Forest": RandomForestClassifier(
        n_estimators=100, random_state=42
    )
}

results = {}

# Step 6: Train and Evaluate Models
for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    results[name] = accuracy

    print(f"\n{name}")
    print(f"Accuracy: {accuracy:.2%}")
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, predictions, labels=[0, 1]))
    print("Classification Report:")
    print(classification_report(
        y_test,
        predictions,
        labels=[0, 1],
        target_names=["Rejected", "Approved"],
        zero_division=0
    ))

# Step 7: Select the Model with Higher Test Accuracy
best_name = max(results, key=results.get)
best_model = models[best_name]

print("\nModel Comparison:")
for name, accuracy in results.items():
    print(f"{name}: {accuracy:.2%}")

print(f"\nSelected Model: {best_name}")
print("Selection is based on test accuracy for this lab demonstration.")

# Step 8: Predict a New Customer's Decision
new_customer = pd.DataFrame([{
    "Age": 35,
    "Income": 65000,
    "Credit_Score": 720,
    "Loan_Amount": 20000,
    "Debt": 5000,
    "Employment": 0
}])

prediction = best_model.predict(new_customer)[0]
probabilities = best_model.predict_proba(new_customer)[0]
class_index = list(best_model.classes_).index(prediction)

decision = "Approved" if prediction == 1 else "Rejected"
confidence = probabilities[class_index]

print("\nNew Customer Details:")
print(new_customer.to_string(index=False))
print("\nPredicted Loan Decision:", decision)
print(f"Model Confidence: {confidence:.2%}")

print("\nDecision-Support Recommendation:")
if decision == "Approved":
    print("The model predicts approval. Verify financial details before deciding.")
else:
    print("The model predicts rejection. Review financial details and eligibility.")

print("\nNote: This is an educational model, not a real lending decision.")
print("\nAssignment completed successfully.")