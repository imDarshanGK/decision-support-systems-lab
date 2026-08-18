# ============================================================
# Decision Support Systems Laboratory
# Experiment No. 4
#
# Model and Solve Problems Using Propositional Logic
# ============================================================

from sympy import symbols
from sympy.logic.boolalg import And, Or, Not, Implies
from sympy.logic import truth_table

# ------------------------------------------------------------
# Step 1: Define Propositions
# ------------------------------------------------------------

C, I, L, D, E = symbols('C I L D E')

# C = Good Credit Score
# I = Sufficient Income
# L = Existing Loan
# D = Loan Default
# E = Loan Eligibility

# ------------------------------------------------------------
# Step 2: Define Decision Rules
# ------------------------------------------------------------

rule1 = Implies(And(C, I), E)
rule2 = Implies(And(C, Not(L)), E)
rule3 = Implies(D, Not(E))

print("==============================================")
print("PROPOSITIONAL LOGIC RULES")
print("==============================================")

print("Rule 1:", rule1)
print("Rule 2:", rule2)
print("Rule 3:", rule3)

# ------------------------------------------------------------
# Step 3: Overall Decision Expression
# ------------------------------------------------------------

eligibility_rule = And(
    Or(
        And(C, I),
        And(C, Not(L))
    ),
    Not(D)
)

print("\n==============================================")
print("OVERALL ELIGIBILITY RULE")
print("==============================================")

print("E =", eligibility_rule)

# ------------------------------------------------------------
# Step 4: Customer Scenarios
# ------------------------------------------------------------

customers = [
    {
        "Customer": "C001",
        "Credit": True,
        "Income": True,
        "ExistingLoan": False,
        "Default": False
    },
    {
        "Customer": "C002",
        "Credit": True,
        "Income": False,
        "ExistingLoan": True,
        "Default": False
    },
    {
        "Customer": "C003",
        "Credit": True,
        "Income": True,
        "ExistingLoan": True,
        "Default": True
    },
    {
        "Customer": "C004",
        "Credit": False,
        "Income": True,
        "ExistingLoan": False,
        "Default": False
    },
    {
        "Customer": "C005",
        "Credit": True,
        "Income": False,
        "ExistingLoan": False,
        "Default": False
    }
]

# ------------------------------------------------------------
# Step 5: Evaluate Customer Scenarios
# ------------------------------------------------------------

print("\n==============================================")
print("CUSTOMER DECISION RESULTS")
print("==============================================")

for customer in customers:

    result = eligibility_rule.subs({
        C: customer["Credit"],
        I: customer["Income"],
        L: customer["ExistingLoan"],
        D: customer["Default"]
    })

    print(
        customer["Customer"],
        "->",
        "Eligible" if result else "Not Eligible"
    )

# ------------------------------------------------------------
# Step 6: Generate Truth Table
# ------------------------------------------------------------

print("\n==============================================")
print("TRUTH TABLE")
print("==============================================")

variables = [C, I, L, D]

table = truth_table(
    eligibility_rule,
    variables
)

for row, result in table:
    print(row, "=>", result)