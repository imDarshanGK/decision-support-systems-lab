import pandas as pd

# Function for Loan Decision

def loan_decision(credit_score, income, employed, existing_loan):

    if credit_score >= 750 and income >= 50000 and employed == "Yes" and existing_loan == "No":
        return "Approve Loan"

    elif credit_score >= 750 and employed == "Yes":
        return "Manual Review"

    elif income >= 50000 and employed == "Yes":
        return "Manual Review"

    elif credit_score >= 750 and income >= 50000:
        return "Manual Review"

    else:
        return "Reject Loan"

# Sample Customer Records

customers = pd.DataFrame({
    "Customer": [1, 2, 3, 4, 5],
    "Credit Score": [780, 760, 690, 720, 810],
    "Income": [65000, 45000, 70000, 30000, 90000],
    "Employed": ["Yes", "Yes", "Yes", "No", "No"],
    "Existing Loan": ["No", "Yes", "No", "No", "Yes"]
})

# Display Customer Details

print("\nCustomer Details\n")
print(customers)

# Make Loan Decisions

customers["Decision"] = customers.apply(
    lambda row: loan_decision(
        row["Credit Score"],
        row["Income"],
        row["Employed"],
        row["Existing Loan"]
    ),
    axis=1
)

# Display Loan Decisions

print("\nLoan Decisions\n")
print(customers)
