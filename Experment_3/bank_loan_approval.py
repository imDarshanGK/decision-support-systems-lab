# Decision Support Systems Laboratory
# Experiment
#
# Bank Loan Approval System using Decision Tables

import pandas as pd

# ORIGINAL DECISION TABLE

original_table = pd.DataFrame({
    "Credit Score": [
        "Good",
        "Good",
        "Good",
        "Good",
        "Poor",
        "Poor",
        "Poor",
        "Poor"
    ],

    "Income": [
        "High",
        "High",
        "Low",
        "Low",
        "High",
        "High",
        "Low",
        "Low"
    ],

    "Employment": [
        "Yes",
        "No",
        "Yes",
        "No",
        "Yes",
        "No",
        "Yes",
        "No"
    ],

    "Existing Loan": [
        "No",
        "No",
        "No",
        "Yes",
        "No",
        "Yes",
        "Yes",
        "Yes"
    ],

    "Age": [
        "21-60",
        "21-60",
        "21-60",
        "21-60",
        "21-60",
        "21-60",
        "Below/Above",
        "Below/Above"
    ],

    "Decision": [
        "Approve Loan",
        "Manual Review",
        "Approve Loan",
        "Manual Review",
        "Manual Review",
        "Reject Loan",
        "Reject Loan",
        "Reject Loan"
    ]
})


print("\n==============================================")
print("ORIGINAL DECISION TABLE")
print("==============================================")

print(original_table.to_string(index=False))


# ORIGINAL DECISION FUNCTION

def original_loan_decision(
    credit_score,
    income,
    employment,
    existing_loan,
    age
):

    # Rule 1
    if (credit_score == "Good" and
        income == "High" and
        employment == "Yes" and
        existing_loan == "No" and
        age == "21-60"):

        return "Approve Loan"

    # Rule 2
    elif (credit_score == "Good" and
          income == "High" and
          employment == "No"):

        return "Manual Review"

    # Rule 3
    elif (credit_score == "Good" and
          income == "Low" and
          employment == "Yes" and
          existing_loan == "No"):

        return "Approve Loan"

    # Rule 4
    elif (credit_score == "Good" and
          income == "Low" and
          employment == "No"):

        return "Manual Review"

    # Rule 5
    elif (credit_score == "Poor" and
          income == "High" and
          employment == "Yes" and
          existing_loan == "No"):

        return "Manual Review"

    # Rule 6
    elif (credit_score == "Poor" and
          existing_loan == "Yes"):

        return "Reject Loan"

    # Rule 7
    elif (credit_score == "Poor" and
          income == "Low" and
          employment == "Yes"):

        return "Reject Loan"

    # Rule 8
    else:

        return "Reject Loan"

# IDENTIFYING REDUNDANT CONDITIONS

print("\n==============================================")
print("REDUNDANT / LESS IMPORTANT CONDITIONS")
print("==============================================")

print("Age is not required in most original rules.")
print("Existing Loan is not required for every decision.")
print("Income is not required when credit score is Poor.")
print("These conditions can be represented using Don't-Care (-).")

# MODIFIED DECISION TABLE
# Using Don't-Care (-) conditions

modified_table = pd.DataFrame({
    "Credit Score": [
        "Good",
        "Good",
        "Poor",
        "Poor",
        "Poor"
    ],

    "Income": [
        "High",
        "Low",
        "High",
        "-",
        "-"
    ],

    "Employment": [
        "Yes",
        "Yes",
        "Yes",
        "-",
        "-"
    ],

    "Existing Loan": [
        "No",
        "No",
        "No",
        "Yes",
        "-"
    ],

    "Age": [
        "21-60",
        "21-60",
        "-",
        "-",
        "Below/Above"
    ],

    "Decision": [
        "Approve Loan",
        "Approve Loan",
        "Manual Review",
        "Reject Loan",
        "Reject Loan"
    ]
})


print("\n==============================================")
print("MODIFIED DECISION TABLE")
print("==============================================")

print(modified_table.to_string(index=False))

# MODIFIED DECISION FUNCTION

def modified_loan_decision(
    credit_score,
    income,
    employment,
    existing_loan,
    age
):

    # Rule 1
    if (credit_score == "Good" and
        income == "High" and
        employment == "Yes" and
        existing_loan == "No" and
        age == "21-60"):

        return "Approve Loan"

    # Rule 2
    elif (credit_score == "Good" and
          income == "Low" and
          employment == "Yes" and
          existing_loan == "No" and
          age == "21-60"):

        return "Approve Loan"

    # Rule 3
    elif (credit_score == "Poor" and
          income == "High" and
          employment == "Yes" and
          existing_loan == "No"):

        return "Manual Review"

    # Rule 4
    elif (credit_score == "Poor" and
          existing_loan == "Yes"):

        return "Reject Loan"

    # Rule 5
    elif (credit_score == "Poor" and
          age == "Below/Above"):

        return "Reject Loan"

    # Other cases
    else:

        return "Manual Review"

# TEST CUSTOMER RECORDS

customers = pd.DataFrame({

    "Customer_ID": [
        "C001",
        "C002",
        "C003",
        "C004",
        "C005",
        "C006",
        "C007",
        "C008",
        "C009",
        "C010"
    ],

    "Credit Score": [
        "Good",
        "Good",
        "Good",
        "Good",
        "Poor",
        "Poor",
        "Poor",
        "Poor",
        "Good",
        "Poor"
    ],

    "Income": [
        "High",
        "Low",
        "High",
        "Low",
        "High",
        "High",
        "Low",
        "Low",
        "High",
        "Low"
    ],

    "Employment": [
        "Yes",
        "Yes",
        "No",
        "No",
        "Yes",
        "No",
        "Yes",
        "No",
        "Yes",
        "Yes"
    ],

    "Existing Loan": [
        "No",
        "No",
        "No",
        "Yes",
        "No",
        "Yes",
        "Yes",
        "Yes",
        "No",
        "No"
    ],

    "Age": [
        "21-60",
        "21-60",
        "21-60",
        "21-60",
        "21-60",
        "21-60",
        "Below/Above",
        "Below/Above",
        "Below/Above",
        "Below/Above"
    ]
})

# APPLY ORIGINAL DECISION

customers["Original Decision"] = customers.apply(
    lambda row: original_loan_decision(
        row["Credit Score"],
        row["Income"],
        row["Employment"],
        row["Existing Loan"],
        row["Age"]
    ),
    axis=1
)

# APPLY MODIFIED DECISION

customers["Modified Decision"] = customers.apply(
    lambda row: modified_loan_decision(
        row["Credit Score"],
        row["Income"],
        row["Employment"],
        row["Existing Loan"],
        row["Age"]
    ),
    axis=1
)

# CHECK WHETHER DECISION CHANGED

customers["Decision Changed"] = (
    customers["Original Decision"] !=
    customers["Modified Decision"]
)

# DISPLAY TEST RESULTS

print("\n==============================================")
print("CUSTOMER TEST RESULTS")
print("==============================================")

print(customers.to_string(index=False))


# DECISION SUMMARY - ORIGINAL

print("\n==============================================")
print("ORIGINAL DECISION SUMMARY")
print("==============================================")

original_summary = customers["Original Decision"].value_counts()

print(original_summary)

# DECISION SUMMARY - MODIFIED

print("\n==============================================")
print("MODIFIED DECISION SUMMARY")
print("==============================================")

modified_summary = customers["Modified Decision"].value_counts()

print(modified_summary)

# COMPARISON

print("\n==============================================")
print("RULE AND OUTCOME COMPARISON")
print("==============================================")

print(
    "Number of Original Rules:",
    len(original_table)
)

print(
    "Number of Modified Rules:",
    len(modified_table)
)

print(
    "Number of Customers Tested:",
    len(customers)
)

print(
    "Number of Changed Decisions:",
    customers["Decision Changed"].sum()
)

# DISPLAY CHANGED DECISIONS

print("\n==============================================")
print("CHANGED DECISIONS")
print("==============================================")

changed = customers[
    customers["Decision Changed"] == True
]

if len(changed) == 0:

    print("No decisions changed.")

else:

    print(
        changed[
            [
                "Customer_ID",
                "Original Decision",
                "Modified Decision"
            ]
        ].to_string(index=False)
    )

# FINAL COMPARISON TABLE

comparison = pd.DataFrame({
    "Version": [
        "Original Decision Table",
        "Modified Decision Table"
    ],

    "Number of Rules": [
        len(original_table),
        len(modified_table)
    ],

    "Approve Loan": [
        (customers["Original Decision"] == "Approve Loan").sum(),
        (customers["Modified Decision"] == "Approve Loan").sum()
    ],

    "Manual Review": [
        (customers["Original Decision"] == "Manual Review").sum(),
        (customers["Modified Decision"] == "Manual Review").sum()
    ],

    "Reject Loan": [
        (customers["Original Decision"] == "Reject Loan").sum(),
        (customers["Modified Decision"] == "Reject Loan").sum()
    ]
})


print("\n==============================================")
print("FINAL COMPARISON")
print("==============================================")

print(comparison.to_string(index=False))