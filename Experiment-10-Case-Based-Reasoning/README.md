# Experiment 10 - Case-Based Reasoning for Customer Support

## Aim
To develop a simple Case-Based Reasoning (CBR) system that retrieves similar historical customer complaints and recommends suitable solutions.

## Problem Statement
A customer support organization stores previously resolved complaints. The system compares a new complaint with historical cases and recommends a solution based on the most similar case.

## Software Requirements
- Python 3.x
- pandas
- NumPy
- scikit-learn

## Case Attributes
- Issue Type
- Product
- Priority
- Customer Type
- Solution

## Algorithm
1. Create a dataset containing historical customer-support cases.
2. Encode categorical attributes using LabelEncoder.
3. Define a new customer complaint.
4. Calculate Euclidean distances between the new complaint and historical cases.
5. Convert distances into similarity scores using `1 / (1 + distance)`.
6. Retrieve the most similar historical case.
7. Display the similarity score and recommended solution.
8. Demonstrate the CBR cycle: Retrieve, Reuse, Revise, and Retain.

## CBR Cycle
- **Retrieve:** Find similar historical cases.
- **Reuse:** Apply the solution from the retrieved case.
- **Revise:** Verify and modify the recommended solution if required.
- **Retain:** Store the resolved case for future recommendations.

## Program Files
- `case_based_reasoning.py` — Main experiment.
- `case_based_reasoning_assignment.py` — Assignment to retrieve the top three similar cases.

## Result
The Case-Based Reasoning system calculates similarity between customer complaints, retrieves relevant historical cases, and recommends solutions based on previous resolutions.

## Technologies Used
Python, pandas, NumPy, and scikit-learn.