# Experiment No. 10 - Assignment
# Case-Based Reasoning for Customer Support

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics.pairwise import euclidean_distances

# Step 1: Create Historical Customer Support Cases
data = {
    "Issue_Type": [
        "Login Problem",
        "Payment Failure",
        "Delivery Delay",
        "Product Damage",
        "Login Problem",
        "Payment Failure",
        "Delivery Delay",
        "Product Damage",
        "Login Problem",
        "Payment Failure"
    ],
    "Product": [
        "Mobile App", "Subscription", "Laptop", "Laptop",
        "Web Portal", "Mobile App", "Mobile App", "Mobile App",
        "Mobile App", "Subscription"
    ],
    "Priority": [
        "High", "High", "Medium", "High", "Medium",
        "Low", "Low", "Medium", "High", "Medium"
    ],
    "Customer_Type": [
        "Regular", "Premium", "Regular", "Premium", "Premium",
        "Regular", "Regular", "Premium", "Premium", "Regular"
    ],
    "Solution": [
        "Reset password and verify account",
        "Retry payment and verify payment details",
        "Track shipment and inform customer",
        "Replace damaged product",
        "Reset password and clear browser cache",
        "Verify card details and retry payment",
        "Check shipment status and update customer",
        "Initiate product replacement",
        "Reset password and enable account access",
        "Verify billing details and retry payment"
    ]
}

df = pd.DataFrame(data)

print("=" * 70)
print("CASE-BASED REASONING - CUSTOMER SUPPORT ASSIGNMENT")
print("=" * 70)

print("\nHistorical Cases:")
print(df.to_string(index=False))

# Step 2: Encode Categorical Attributes
features = ["Issue_Type", "Product", "Priority", "Customer_Type"]
encoders = {}

for column in features:
    encoder = LabelEncoder()
    df[column + "_Encoded"] = encoder.fit_transform(df[column])
    encoders[column] = encoder

encoded_features = [column + "_Encoded" for column in features]
X = df[encoded_features].values

# Step 3: Define a New Customer Complaint
new_case = {
    "Issue_Type": "Payment Failure",
    "Product": "Subscription",
    "Priority": "High",
    "Customer_Type": "Premium"
}

print("\nNew Customer Complaint:")
for key, value in new_case.items():
    print(f"{key}: {value}")

# Step 4: Encode the New Complaint
new_case_encoded = []

for column in features:
    value = encoders[column].transform([new_case[column]])[0]
    new_case_encoded.append(value)

new_case_vector = np.array(new_case_encoded).reshape(1, -1)

# Step 5: Calculate Euclidean Distance
distances = euclidean_distances(X, new_case_vector).flatten()
df["Distance"] = distances

# Step 6: Calculate Similarity Scores
df["Similarity"] = 1 / (1 + df["Distance"])

# Step 7: Retrieve the Top 3 Similar Cases
top_cases = df.sort_values(
    by="Similarity", ascending=False
).head(3).copy()

print("\nTop 3 Similar Historical Cases:")
print(
    top_cases[
        features + ["Distance", "Similarity", "Solution"]
    ].round({"Distance": 3, "Similarity": 3}).to_string(index=False)
)

# Step 8: Recommend the Best Matching Solution
best_case = top_cases.iloc[0]

print("\nRecommended Solution:")
print(best_case["Solution"])
print(f"Similarity Score: {best_case['Similarity']:.3f}")

# Step 9: Demonstrate the CBR Cycle
print("\nCBR Cycle:")
print("1. Retrieve: Retrieve the three most similar cases.")
print("2. Reuse: Recommend the solution from the closest case.")
print("3. Revise: A support agent checks and adjusts the solution.")
print("4. Retain: Store the resolved case for future use.")

print("\nAssignment completed successfully.")