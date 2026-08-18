# ============================================================
# Decision Support Systems Laboratory
# Experiment No. 4 - Assignment
#
# Modify Loan Eligibility System Using Propositional Logic
# ============================================================

from sympy import symbols
from sympy.logic.boolalg import And, Or, Not, Implies
from sympy.logic import truth_table

# ------------------------------------------------------------
# Define Propositions
# ------------------------------------------------------------

C, I, L, D, A, S, E = symbols('C I L D A S E')

# C = Good Credit Score
# I = Sufficient Income
# L = Existing Loan
# D = Loan Default
# A = Acceptable Age
# S = Stable Employment
# E = Loan Eligibility

# ------------------------------------------------------------
# Original Decision Rules
# ------------------------------------------------------------

rule1 = Implies(And(C, I), E)
rule2 = Implies(And(C, Not(L)), E)
rule3 = Implies(D, Not(E))

# ------------------------------------------------------------
# New Decision Rule
# ------------------------------------------------------------

rule4 = Implies(
    And(C, I, A, S),
    E
)

print("==============================================")
print("PROPOSITIONAL LOGIC RULES")
print("==============================================")

print("Rule 1:", rule1)
print("Rule 2:", rule2)
print("Rule 3:", rule3)
print("Rule 4:", rule4)

# ------------------------------------------------------------
# Modified Eligibility Rule
# ------------------------------------------------------------

eligibility_rule = And(
    Or(
        And(C, I),
        And(C, Not(L)),
        And(C, I, A, S)
    ),
    Not(D)
)

print("\n==============================================")
print("MODIFIED ELIGIBILITY RULE")
print("==============================================")

print("E =", eligibility_rule)

# ------------------------------------------------------------
# Customer Scenarios
# ------------------------------------------------------------

customers = [
    {
        "Customer": "C001",
        "Credit": True,
        "Income": True,
        "ExistingLoan": False,
        "Default": False,
        "Age": True,
        "StableEmployment": True
    },
    {
        "Customer": "C002",
        "Credit": True,
        "Income": False,
        "ExistingLoan": False,
        "Default": False,
        "Age": True,
        "StableEmployment": True
    },
    {
        "Customer": "C003",
        "Credit": True,
        "Income": True,
        "ExistingLoan": True,
        "Default": False,
        "Age": True,
        "StableEmployment": True
    },
    {
        "Customer": "C004",
        "Credit": False,
        "Income": True,
        "ExistingLoan": False,
        "Default": False,
        "Age": True,
        "StableEmployment": True
    },
    {
        "Customer": "C005",
        "Credit": True,
        "Income": True,
        "ExistingLoan": True,
        "Default": True,
        "Age": True,
        "StableEmployment": True
    },
    {
        "Customer": "C006",
        "Credit": False,
        "Income": True,
        "ExistingLoan": False,
        "Default": False,
        "Age": False,
        "StableEmployment": True
    },
    {
        "Customer": "C007",
        "Credit": True,
        "Income": False,
        "ExistingLoan": True,
        "Default": False,
        "Age": True,
        "StableEmployment": False
    },
    {
        "Customer": "C008",
        "Credit": True,
        "Income": True,
        "ExistingLoan": False,
        "Default": False,
        "Age": False,
        "StableEmployment": False
    },
    {
        "Customer": "C009",
        "Credit": True,
        "Income": False,
        "ExistingLoan": False,
        "Default": False,
        "Age": False,
        "StableEmployment": True
    },
    {
        "Customer": "C010",
        "Credit": True,
        "Income": True,
        "ExistingLoan": True,
        "Default": False,
        "Age": False,
        "StableEmployment": False
    }
]

# ------------------------------------------------------------
# Evaluate Customer Scenarios
# ------------------------------------------------------------

print("\n==============================================")
print("CUSTOMER DECISION RESULTS")
print("==============================================")

for customer in customers:

    result = eligibility_rule.subs({
        C: customer["Credit"],
        I: customer["Income"],
        L: customer["ExistingLoan"],
        D: customer["Default"],
        A: customer["Age"],
        S: customer["StableEmployment"]
    })

    print(
        customer["Customer"],
        "->",
        "Eligible" if result else "Not Eligible"
    )

# ------------------------------------------------------------
# Generate Truth Table
# ------------------------------------------------------------

print("\n==============================================")
print("NEW TRUTH TABLE")
print("==============================================")

variables = [C, I, L, D, A, S]

table = truth_table(
    eligibility_rule,
    variables
)

for row, result in table:
    print(row, "=>", result)