# Experiment No. 12
# Intelligent Decision Support System Using Classification
# Application: Credit Risk Assessment

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# Step 1: Create the Credit-Risk Dataset
data = {
    "Age": [25, 32, 41, 29, 45, 36, 27, 52, 39, 31,
            48, 26, 43, 35, 50, 30, 37, 42, 28, 46],

    "Income": [35000, 60000, 85000, 42000, 95000,
               70000, 30000, 110000, 78000, 50000,
               100000, 32000, 90000, 65000, 105000,
               45000, 72000, 88000, 38000, 92000],

    "CreditScore": [610, 690, 760, 630, 790, 720, 590,
                    810, 750, 670, 800, 600, 770, 710,
                    820, 640, 730, 780, 620, 795],

    "LoanAmount": [15000, 20000, 25000, 18000, 30000,
                   25000, 12000, 40000, 28000, 18000,
                   35000, 14000, 30000, 22000, 38000,
                   17000, 26000, 29000, 15000, 32000],

    "Debt": [8000, 5000, 4000, 10000, 3000, 6000, 12000,
             2000, 4500, 7000, 2500, 9000, 3500, 5500,
             2000, 8500, 5000, 3000, 11000, 2800],

    "PreviousDefault": [
        "Yes", "No", "No", "Yes", "No",
        "No", "Yes", "No", "No", "No",
        "No", "Yes", "No", "No", "No",
        "Yes", "No", "No", "Yes", "No"
    ],

    "Risk": [
        "High", "Medium", "Low", "High", "Low",
        "Low", "High", "Low", "Low", "Medium",
        "Low", "High", "Low", "Medium", "Low",
        "High", "Low", "Low", "High", "Low"
    ]
}

df = pd.DataFrame(data)

print("=" * 60)
print("INTELLIGENT DSS - CREDIT RISK ASSESSMENT")
print("=" * 60)

# Step 2: Explore Dataset
print("\nFirst Five Records:")
print(df.head())

print("\nDataset Dimensions:", df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe())

print("\nRisk Category Distribution:")
print(df["Risk"].value_counts())

# Step 3: Encode Categorical Variables
default_encoder = LabelEncoder()
risk_encoder = LabelEncoder()

df["PreviousDefault"] = default_encoder.fit_transform(
    df["PreviousDefault"]
)

df["Risk"] = risk_encoder.fit_transform(df["Risk"])

print("\nEncoded Dataset:")
print(df.head())

# Step 4: Define Features and Target
features = [
    "Age",
    "Income",
    "CreditScore",
    "LoanAmount",
    "Debt",
    "PreviousDefault"
]

X = df[features]
y = df["Risk"]

# Step 5: Split Dataset into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Samples:", len(X_train))
print("Testing Samples:", len(X_test))

# Step 6: Create and Train Decision Tree
model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=4,
    random_state=42
)

model.fit(X_train, y_train)

print("\nDecision Tree trained successfully.")

# Step 7: Predict Test Data
y_pred = model.predict(X_test)

# Step 8: Evaluate Model
accuracy = accuracy_score(y_test, y_pred)

print(f"\nModel Accuracy: {accuracy:.2%}")

risk_labels = risk_encoder.inverse_transform(
    np.arange(len(risk_encoder.classes_))
)

print("\nRisk Categories:", list(risk_labels))

print("\nConfusion Matrix:")
print(confusion_matrix(
    y_test,
    y_pred,
    labels=np.arange(len(risk_encoder.classes_))
))

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    labels=np.arange(len(risk_encoder.classes_)),
    target_names=list(risk_labels),
    zero_division=0
))

# Step 9: Enter a New Applicant
new_applicant = pd.DataFrame([{
    "Age": 34,
    "Income": 55000,
    "CreditScore": 680,
    "LoanAmount": 20000,
    "Debt": 7000,
    "PreviousDefault": default_encoder.transform(["No"])[0]
}])

print("\nNew Applicant Details:")
print(new_applicant.to_string(index=False))

# Step 10: Predict Credit Risk
predicted_risk_code = model.predict(new_applicant)[0]

predicted_risk = risk_encoder.inverse_transform(
    [predicted_risk_code]
)[0]

probabilities = model.predict_proba(new_applicant)[0]

class_index = list(model.classes_).index(predicted_risk_code)
confidence = probabilities[class_index]

print("\nPredicted Credit Risk:", predicted_risk)
print(f"Model Confidence: {confidence:.2%}")

print("\nRisk Category Probabilities:")
for code, probability in zip(model.classes_, probabilities):
    category = risk_encoder.inverse_transform([code])[0]
    print(f"{category}: {probability:.2%}")

# Step 11: Decision-Support Recommendation
print("\nDecision-Support Recommendation:")

if predicted_risk == "Low":
    print("The model predicts LOW credit risk.")
    print("The application may proceed to further eligibility checks.")
elif predicted_risk == "Medium":
    print("The model predicts MEDIUM credit risk.")
    print("Review income, existing debt, and repayment capacity.")
else:
    print("The model predicts HIGH credit risk.")
    print("Conduct additional risk assessment before making a decision.")

print("\nNote: This educational model does not make a final lending decision.")
print("\nExperiment completed successfully.")