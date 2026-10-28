# ============================================================
# EXPERIMENT NO. 11
# BASIC INTELLIGENT DECISION SUPPORT SYSTEM USING ML
# Dataset: loan_approval_dataset(1).csv
# Platform: Google Colab
# ============================================================

import os
import pandas as pd
import numpy as np

from google.colab import files
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# ------------------------------------------------------------
# STEP 1: LOAD THE ACTUAL DATASET
# ------------------------------------------------------------

print("=" * 60)
print(" INTELLIGENT DSS - LOAN APPROVAL PREDICTION")
print("=" * 60)

file_path = "/content/loan_approval_dataset(1).csv"

if not os.path.exists(file_path):
    print("\nPlease upload your loan approval CSV dataset.")
    uploaded = files.upload()

    csv_files = [
        name for name in uploaded
        if name.lower().endswith(".csv")
    ]

    if not csv_files:
        raise ValueError("No CSV file uploaded. Please upload the dataset.")

    file_path = csv_files[0]

df = pd.read_csv(file_path)

# Remove unwanted spaces from column names and text values
df.columns = df.columns.str.strip()

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

print("\nDataset loaded successfully!")
print("Dataset shape:", df.shape)

print("\nFirst 5 records:")
display(df.head())

print("\nColumn names:")
print(df.columns.tolist())

# ------------------------------------------------------------
# STEP 2: CHECK AND PREPROCESS THE DATA
# ------------------------------------------------------------

print("\nMissing values before preprocessing:")
print(df.isnull().sum())

# Remove duplicate records
df = df.drop_duplicates().copy()

# Remove rows where the target is missing
df = df.dropna(subset=["loan_status"]).copy()

# Remove ID column because it is not a predictive feature
if "loan_id" in df.columns:
    df = df.drop(columns=["loan_id"])

# Separate features and target
target = "loan_status"

X = df.drop(columns=[target])
y = df[target]

# Fill missing feature values
numeric_cols = X.select_dtypes(include=np.number).columns.tolist()
categorical_cols = X.select_dtypes(
    exclude=np.number
).columns.tolist()

for col in numeric_cols:
    X[col] = X[col].fillna(X[col].median())

for col in categorical_cols:
    X[col] = X[col].fillna(
        X[col].mode()[0] if not X[col].mode().empty else "Unknown"
    )

print("\nDataset after preprocessing:")
print("Number of records:", len(X))
print("Number of features:", X.shape[1])
print("\nTarget class distribution:")
print(y.value_counts())

# ------------------------------------------------------------
# STEP 3: ENCODE CATEGORICAL VARIABLES
# ------------------------------------------------------------

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_cols
        )
    ],
    remainder="passthrough"
)

# ------------------------------------------------------------
# STEP 4: SPLIT INTO TRAINING AND TESTING DATA
# ------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

# ------------------------------------------------------------
# STEP 5: CREATE AND TRAIN THE DECISION TREE MODEL
# ------------------------------------------------------------

model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "classifier",
            DecisionTreeClassifier(
                criterion="entropy",
                max_depth=3,
                random_state=42
            )
        )
    ]
)

model.fit(X_train, y_train)

print("\nDecision Tree model trained successfully!")

# ------------------------------------------------------------
# STEP 6: EVALUATE THE MODEL
# ------------------------------------------------------------

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\n" + "=" * 60)
print(" MODEL EVALUATION")
print("=" * 60)

print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

labels = model.named_steps["classifier"].classes_

print("\nConfusion Matrix:")
print("Class order:", list(labels))
print(confusion_matrix(y_test, y_pred, labels=labels))

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        labels=labels,
        zero_division=0
    )
)

# ------------------------------------------------------------
# STEP 7: ENTER A NEW CUSTOMER'S DETAILS
# ------------------------------------------------------------

# Example values based on the dataset's feature columns.
# Modify these values to test another customer.

new_customer = pd.DataFrame([{
    "no_of_dependents": 2,
    "education": "Graduate",
    "self_employed": "No",
    "income_annum": 7000000,
    "loan_amount": 15000000,
    "loan_term": 10,
    "cibil_score": 750,
    "residential_assets_value": 5000000,
    "commercial_assets_value": 3000000,
    "luxury_assets_value": 10000000,
    "bank_asset_value": 4000000
}])

# Ensure the new customer's columns match the training features
new_customer = new_customer.reindex(columns=X.columns)

print("\nNew customer details:")
display(new_customer)

# ------------------------------------------------------------
# STEP 8: PREDICT THE LOAN DECISION
# ------------------------------------------------------------

prediction = model.predict(new_customer)[0]
probabilities = model.predict_proba(new_customer)[0]

print("\n" + "=" * 60)
print(" NEW CUSTOMER LOAN DECISION")
print("=" * 60)

print("Predicted Loan Status:", str(prediction).upper())

print("\nPrediction Probabilities:")
for label, probability in zip(labels, probabilities):
    print(f"{label}: {probability * 100:.2f}%")

# ------------------------------------------------------------
# STEP 9: GENERATE DSS RECOMMENDATION
# ------------------------------------------------------------

print("\n" + "=" * 60)
print(" DECISION SUPPORT RECOMMENDATION")
print("=" * 60)

if str(prediction).strip().lower() == "approved":
    print(
        "Recommendation: The customer may be considered "
        "for loan approval based on the trained model."
    )
else:
    print(
        "Recommendation: The customer may require "
        "additional assessment before a loan decision."
    )

print(
    "\nNote: This is an educational DSS demonstration. "
    "The prediction is not a real lending decision."
)

print("\nExperiment completed successfully!")