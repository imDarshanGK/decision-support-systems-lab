# Experiment No. 10
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
        "Login Problem",
        "Product Damage",
        "Payment Failure",
        "Delivery Delay",
        "Product Damage",
        "Login Problem"
    ],
    "Product": [
        "Mobile App",
        "Subscription",
        "Web Portal",
        "Laptop",
        "Mobile App",
        "Laptop",
        "Mobile App",
        "Web Portal"
    ],
    "Priority": [
        "High", "High", "Medium", "High",
        "Medium", "Low", "Medium", "High"
    ],
    "Customer_Type": [
        "Regular", "Premium", "Regular", "Premium",
        "Regular", "Regular", "Premium", "Premium"
    ],
    "Solution": [
        "Reset password and verify account",
        "Retry payment and verify payment details",
        "Reset password and clear browser cache",
        "Replace damaged product",
        "Verify card details and retry payment",
        "Track shipment and inform customer",
        "Initiate product replacement",
        "Reset password and verify account"
    ]
}

df = pd.DataFrame(data)

print("=" * 65)
print("CASE-BASED REASONING FOR CUSTOMER SUPPORT")
print("=" * 65)

print("\nHistorical Customer Support Cases:")
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

# Step 3: Define a New Customer Case
new_case = {
    "Issue_Type": "Login Problem",
    "Product": "Web Portal",
    "Priority": "High",
    "Customer_Type": "Premium"
}

print("\nNew Customer Complaint:")
for key, value in new_case.items():
    print(f"{key}: {value}")

# Step 4: Encode the New Case
new_case_encoded = []

for column in features:
    value = encoders[column].transform([new_case[column]])[0]
    new_case_encoded.append(value)

new_case_vector = np.array(new_case_encoded).reshape(1, -1)

# Step 5: Calculate Euclidean Distance
distances = euclidean_distances(X, new_case_vector).flatten()
df["Distance"] = distances

# Step 6: Convert Distance into Similarity Score
df["Similarity"] = 1 / (1 + df["Distance"])

# Step 7: Retrieve the Most Similar Historical Case
best_index = df["Similarity"].idxmax()
best_case = df.loc[best_index]

print("\nSimilarity Results:")
print(
    df[
        features + ["Distance", "Similarity"]
    ].round({"Distance": 3, "Similarity": 3}).to_string(index=False)
)

# Step 8: Display Retrieved Case and Recommended Solution
print("\nMost Similar Historical Case:")
for column in features:
    print(f"{column}: {best_case[column]}")

print(f"Distance: {best_case['Distance']:.3f}")
print(f"Similarity Score: {best_case['Similarity']:.3f}")
print(f"Recommended Solution: {best_case['Solution']}")

# Step 9: Demonstrate the CBR Cycle
print("\nCBR Cycle:")
print("1. Retrieve: Found the most similar historical case.")
print("2. Reuse: Recommended the solution from that case.")
print("3. Revise: A support agent can verify and modify the solution.")
print("4. Retain: After resolution, the updated case can be stored")
print("   for future customer-support recommendations.")

print("\nExperiment completed successfully.")