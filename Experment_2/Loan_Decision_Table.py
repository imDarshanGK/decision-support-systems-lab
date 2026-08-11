import pandas as pd

# 1. ORIGINAL LOAN DECISION FUNCTION

def original_loan_decision(credit_score, income, employed, existing_loan):

    if (credit_score >= 750 and
        income >= 50000 and
        employed == "Yes" and
        existing_loan == "No"):

        return "Approve Loan"

    elif credit_score >= 750 and employed == "Yes":
        return "Manual Review"

    elif income >= 50000 and employed == "Yes":
        return "Manual Review"

    elif credit_score >= 750 and income >= 50000:
        return "Manual Review"

    else:
        return "Reject Loan"


# 2. ENHANCED LOAN DECISION FUNCTION
#    New Conditions:
#    - Customer Age
#    - Debt-to-Income Ratio (DTI)

def enhanced_loan_decision(
    credit_score,
    income,
    employed,
    existing_loan,
    age,
    dti
):

    # Rule 1: All conditions satisfied
    if (credit_score >= 750 and
        income >= 50000 and
        employed == "Yes" and
        existing_loan == "No" and
        21 <= age <= 60 and
        dti <= 40):

        return "Approve Loan"

    # Rule 2: Good credit and employment,
    # but age or DTI requires review
    elif (credit_score >= 750 and
          employed == "Yes" and
          21 <= age <= 60 and
          dti <= 50):

        return "Manual Review"

    # Rule 3: Good income and employment,
    # but DTI/age requires review
    elif (income >= 50000 and
          employed == "Yes" and
          21 <= age <= 60 and
          dti <= 50):

        return "Manual Review"

    # Rule 4: Good credit and income,
    # but other conditions require review
    elif (credit_score >= 750 and
          income >= 50000 and
          21 <= age <= 60):

        return "Manual Review"

    # Rule 5: Otherwise reject
    else:
        return "Reject Loan"

# 3. CUSTOMER RECORDS

customers = pd.DataFrame({

    "Customer": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],

    "Credit Score":
        [780, 760, 690, 720, 810, 800, 740, 770, 680, 790],

    "Income":
        [65000, 45000, 70000, 30000, 90000,
         60000, 55000, 80000, 75000, 40000],

    "Employed":
        ["Yes", "Yes", "Yes", "No", "No",
         "Yes", "Yes", "Yes", "Yes", "Yes"],

    "Existing Loan":
        ["No", "Yes", "No", "No", "Yes",
         "No", "No", "No", "Yes", "No"],

    "Age":
        [30, 35, 45, 25, 65,
         40, 22, 55, 70, 19],

    "DTI":
        [25, 35, 30, 45, 20,
         55, 45, 38, 60, 25]
})

# 4. APPLY ORIGINAL DECISION

customers["Original Decision"] = customers.apply(
    lambda row: original_loan_decision(
        row["Credit Score"],
        row["Income"],
        row["Employed"],
        row["Existing Loan"]
    ),
    axis=1
)

# 5. APPLY ENHANCED DECISION

customers["Enhanced Decision"] = customers.apply(
    lambda row: enhanced_loan_decision(
        row["Credit Score"],
        row["Income"],
        row["Employed"],
        row["Existing Loan"],
        row["Age"],
        row["DTI"]
    ),
    axis=1
)

# 6. CHECK WHETHER DECISION CHANGED

customers["Decision Changed"] = (
    customers["Original Decision"] !=
    customers["Enhanced Decision"]
)

# 7. DISPLAY RESULTS

print("\n================ CUSTOMER RECORDS ================\n")

print(customers)


print("\n================ DECISION COMPARISON ================\n")

print(
    customers[
        [
            "Customer",
            "Original Decision",
            "Enhanced Decision",
            "Decision Changed"
        ]
    ]
)

# 8. DISPLAY ONLY CHANGED DECISIONS

print("\n================ CHANGED DECISIONS ================\n")

changed = customers[
    customers["Decision Changed"] == True
]

print(changed[
    [
        "Customer",
        "Age",
        "DTI",
        "Original Decision",
        "Enhanced Decision"
    ]
])

# 9. SUMMARY

print("\n================ SUMMARY ================\n")

print(
    "Original Approvals:",
    (customers["Original Decision"] == "Approve Loan").sum()
)

print(
    "Enhanced Approvals:",
    (customers["Enhanced Decision"] == "Approve Loan").sum()
)

print(
    "Original Manual Reviews:",
    (customers["Original Decision"] == "Manual Review").sum()
)

print(
    "Enhanced Manual Reviews:",
    (customers["Enhanced Decision"] == "Manual Review").sum()
)

print(
    "Original Rejections:",
    (customers["Original Decision"] == "Reject Loan").sum()
)

print(
    "Enhanced Rejections:",
    (customers["Enhanced Decision"] == "Reject Loan").sum()
)

print(
    "Number of Changed Decisions:",
    customers["Decision Changed"].sum()
)