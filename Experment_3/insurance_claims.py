# Decision Support Systems Laboratory
# Experiment No. 3
#
# Analyze and Simulate Different Decision Table Modifications
# in Real-World Applications

import pandas as pd

# Decision Table - Version 1
# Basic Decision Table

decision_table = pd.DataFrame({
    "Policy_Active": ["Yes", "Yes", "Yes", "No"],
    "Claim_Covered": ["Yes", "Yes", "No", "-"],
    "Documents_Complete": ["Yes", "No", "Yes", "-"],
    "Within_Limit": ["Yes", "Yes", "Yes", "-"],
    "Decision": [
        "Approve Claim",
        "Manual Review",
        "Reject Claim",
        "Reject Claim"
    ]
})

print("\n==============================================")
print("BASIC DECISION TABLE")
print("==============================================")
print(decision_table.to_string(index=False))

# Function to simulate the Decision Table

def insurance_decision(
    policy_active,
    claim_covered,
    documents_complete,
    within_limit
):

    # Rule 1
    if (policy_active == "Yes" and
        claim_covered == "Yes" and
        documents_complete == "Yes" and
        within_limit == "Yes"):

        return "Approve Claim"

    # Rule 2
    elif (policy_active == "Yes" and
          claim_covered == "Yes" and
          documents_complete == "No"):

        return "Manual Review"

    # Rule 3
    elif (policy_active == "Yes" and
          claim_covered == "No"):

        return "Reject Claim"

    # Rule 4 - Modified rule using Don't-Care condition
    elif policy_active == "No":

        return "Reject Claim"

    # Other cases
    else:

        return "Manual Review"

# Test Cases

customers = pd.DataFrame({
    "Customer_ID": [
        "C001",
        "C002",
        "C003",
        "C004",
        "C005",
        "C006"
    ],

    "Policy_Active": [
        "Yes",
        "Yes",
        "Yes",
        "No",
        "Yes",
        "Yes"
    ],

    "Claim_Covered": [
        "Yes",
        "Yes",
        "No",
        "Yes",
        "Yes",
        "No"
    ],

    "Documents_Complete": [
        "Yes",
        "No",
        "Yes",
        "No",
        "Yes",
        "Yes"
    ],

    "Within_Limit": [
        "Yes",
        "Yes",
        "Yes",
        "Yes",
        "No",
        "Yes"
    ]
})

# Apply Decision Table

customers["Decision"] = customers.apply(
    lambda row: insurance_decision(
        row["Policy_Active"],
        row["Claim_Covered"],
        row["Documents_Complete"],
        row["Within_Limit"]
    ),
    axis=1
)

# Display Results

print("\n==============================================")
print("SIMULATION RESULTS")
print("==============================================")
print(customers.to_string(index=False))

# Decision Summary

print("\n==============================================")
print("DECISION SUMMARY")
print("==============================================")

summary = customers["Decision"].value_counts()

print(summary)

# Modified Decision Table

modified_table = pd.DataFrame({
    "Policy Active": ["No", "Yes", "Yes", "Yes"],
    "Claim Covered": ["-", "No", "Yes", "Yes"],
    "Documents Complete": ["-", "-", "No", "Yes"],
    "Within Limit": ["-", "-", "-", "Yes"],
    "Action": [
        "Reject Claim",
        "Reject Claim",
        "Manual Review",
        "Approve Claim"
    ]
})

print("\n==============================================")
print("MODIFIED DECISION TABLE")
print("==============================================")

print(modified_table.to_string(index=False))