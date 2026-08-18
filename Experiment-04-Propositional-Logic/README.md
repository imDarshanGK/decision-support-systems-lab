# Experiment 04 - Propositional Logic

## Decision Support Systems Lab

### Experiment Title

Model and Solve Problems Using Propositional Logic

### Aim

To model and solve a real-world decision-making problem using Propositional Logic and Python, and to determine the appropriate decision based on logical rules.

### Main Experiment

A bank loan eligibility system is developed using propositional logic.

The propositions used are:

- C = Good Credit Score
- I = Sufficient Income
- L = Existing Loan
- D = Loan Default
- E = Loan Eligibility

The decision rules are:

1. Good credit score AND sufficient income → Eligible.
2. Good credit score AND no existing loan → Eligible.
3. Loan default → Not Eligible.

### Algorithm

1. Define the propositions using Boolean variables.
2. Define the logical operators and decision rules.
3. Construct the overall propositional expression.
4. Create different customer scenarios.
5. Substitute the truth values into the logical expression.
6. Evaluate the expression.
7. Display the loan eligibility decision.
8. Generate a truth table.

### Assignment

The loan eligibility system is modified by introducing two additional conditions:

- A = Acceptable Age
- S = Stable Employment

The additional rule is:

(C AND I AND A AND S) → E

The modified system is tested with 10 customer scenarios and a new truth table is generated.

### Files

- `propositional_logic.py` - Main Experiment 4 program.
- `loan_eligibility_propositional_logic.py` - Assignment implementation.

### Technologies Used

- Python
- SymPy

### Result

The loan eligibility problem was successfully modeled and solved using Propositional Logic in Python. The system evaluates customer scenarios using logical rules and generates a truth table for the decision.