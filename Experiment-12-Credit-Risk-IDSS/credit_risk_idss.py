# ============================================================
# EXPERIMENT NO. 12
# INTELLIGENT DECISION SUPPORT SYSTEM USING CLASSIFICATION
# Application: Loan Approval Prediction
# Dataset: loan_approval_dataset(2).csv
# Platform: Google Colab
# ============================================================

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from google.colab import files
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

# ------------------------------------------------------------
# STEP 1: LOAD THE ACTUAL CSV DATASET
# ------------------------------------------------------------

print("=" * 60)
print(" INTELLIGENT DSS - LOAN APPROVAL PREDICTION")
print("=" * 60)

file_path = "/content/loan_approval_dataset(2).csv"

if not os.path.exists(file_path):
    print("\nUpload your loan approval dataset:")
    uploaded = files.upload()

    csv_files = [
        name for name in uploaded
        if name.lower().endswith(".csv")
    ]

    if not csv_files:
        raise ValueError("Please upload a valid CSV file.")

    file_path = csv_files[0]

df = pd.read_csv(file_path)

# Remove leading/trailing spaces in column names
df.columns = df.columns.str.strip()

# Remove extra spaces from text columns
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

print("\nDataset loaded successfully!")
print("Dataset dimensions:", df.shape)

print("\nFirst five records:")
display(df.head())

print("\nColumn names:")
print(df.columns.tolist())

# ------------------------------------------------------------
# STEP 2: EXPLORE THE DATASET
# ------------------------------------------------------------

print("\nDataset information:")
df.info()

print("\nMissing values:")
print(df.isnull().sum())

print("\nStatistical summary:")
display(df.describe(include="all").T)

# ------------------------------------------------------------
# STEP 3: PREPROCESS THE DATA
# ------------------------------------------------------------

# Remove duplicate records
df = df.drop_duplicates().copy()

# Target column in the actual dataset
target = "loan_status"

if target not in df.columns:
    raise ValueError(
        "Target column 'loan_status' was not found. "
        "Please verify the uploaded dataset."
    )

# Remove records without a known target
df = df.dropna(subset=[target]).copy()

# Remove ID column: it is not a meaningful predictor
if "loan_id" in df.columns:
    df = df.drop(columns=["loan_id"])

# Separate input features and target
X = df.drop(columns=[target])
y = df[target].astype(str).str.strip()

# Fill missing numeric and categorical values
numeric_cols = X.select_dtypes(include=np.number).columns.tolist()
categorical_cols = X.select_dtypes(
    exclude=np.number
).columns.tolist()

for col in numeric_cols:
    X[col] = X[col].fillna(X[col].median())

for col in categorical_cols:
    mode = X[col].mode()
    X[col] = X[col].fillna(
        mode.iloc[0] if not mode.empty else "Unknown"
    )

print("\nPreprocessing completed.")
print("Number of records:", len(X))
print("Number of input features:", X.shape[1])

print("\nLoan status distribution:")
print(y.value_counts())

# ------------------------------------------------------------
# STEP 4: ENCODE CATEGORICAL FEATURES
# ------------------------------------------------------------

# OneHotEncoder handles Graduate/Not Graduate and Yes/No.
# The encoder is fitted only on training data through the pipeline.

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
# STEP 5: SPLIT INTO TRAINING AND TESTING DATA
# ------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

# ------------------------------------------------------------
# STEP 6: CREATE AND TRAIN DECISION TREE CLASSIFIER
# ------------------------------------------------------------

model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "classifier",
            DecisionTreeClassifier(
                criterion="entropy",
                max_depth=4,
                random_state=42
            )
        )
    ]
)

model.fit(X_train, y_train)

print("\nDecision Tree model trained successfully!")

# ------------------------------------------------------------
# STEP 7: PREDICT TEST DATA
# ------------------------------------------------------------

y_pred = model.predict(X_test)

# ------------------------------------------------------------
# STEP 8: EVALUATE THE MODEL
# ------------------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)
labels = model.named_steps["classifier"].classes_

print("\n" + "=" * 60)
print(" MODEL EVALUATION")
print("=" * 60)

print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

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

# Plot the confusion matrix
ConfusionMatrixDisplay.from_predictions(
    y_test,
    y_pred,
    labels=labels,
    display_labels=labels,
    cmap="Blues",
    values_format="d"
)

plt.title("Loan Approval - Confusion Matrix")
plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# STEP 9: TEST A NEW LOAN APPLICANT
# ------------------------------------------------------------

# Example applicant. Values are illustrative and can be changed.
# All feature names match the actual CSV dataset.

new_applicant = pd.DataFrame([{
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

# Match the dataset's exact feature order
new_applicant = new_applicant.reindex(columns=X.columns)

print("\n" + "=" * 60)
print(" NEW APPLICANT DETAILS")
print("=" * 60)

display(new_applicant)

# ------------------------------------------------------------
# STEP 10: PREDICT LOAN STATUS AND PROBABILITY
# ------------------------------------------------------------

prediction = model.predict(new_applicant)[0]
probabilities = model.predict_proba(new_applicant)[0]

print("\nPredicted Loan Status:", str(prediction).upper())

print("\nPrediction probabilities:")
for label, probability in zip(labels, probabilities):
    print(f"{label}: {probability * 100:.2f}%")

# ------------------------------------------------------------
# STEP 11: DECISION SUPPORT RECOMMENDATION
# ------------------------------------------------------------

print("\n" + "=" * 60)
print(" DECISION SUPPORT RECOMMENDATION")
print("=" * 60)

if str(prediction).strip().lower() == "approved":
    recommendation = (
        "The applicant may be considered for approval, "
        "subject to verification and applicable lending policies."
    )
else:
    recommendation = (
        "The applicant requires further review of the "
        "application and relevant financial information."
    )

print("Recommendation:", recommendation)

print(
    "\nNote: This is an educational decision-support system. "
    "It assists human review and must not be used as the sole "
    "basis for an actual lending decision."
)

print("\nExperiment No. 12 completed successfully!")
