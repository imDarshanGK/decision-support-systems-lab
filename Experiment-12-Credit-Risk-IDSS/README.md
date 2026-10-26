# Experiment 12 - Credit Risk Assessment Using IDSS

## Aim
To design and simulate an Intelligent Decision Support System using a Machine Learning classification model for credit-risk assessment.

## Problem Statement
Financial institutions need to assess the credit risk of loan applicants. This experiment uses historical customer information to predict risk categories and provide decision-support recommendations.

## Software Requirements
- Python 3.x
- pandas
- NumPy
- scikit-learn

## Dataset Description
The illustrative dataset contains 20 customer records with the following attributes:

- Age
- Income
- Credit Score
- Loan Amount
- Debt
- Previous Default
- Risk

The target variable classifies applicants into High, Medium, or Low credit risk.

## Algorithm
1. Create the illustrative credit-risk dataset.
2. Explore the dataset, data types, missing values, and statistical summary.
3. Encode categorical variables.
4. Select the input features and target variable.
5. Split the dataset into training and testing sets.
6. Train a Decision Tree Classifier.
7. Predict the risk categories of test records.
8. Evaluate the model using accuracy, confusion matrix, precision, recall, and F1-score.
9. Predict the credit risk of a new applicant.
10. Display the predicted risk category, class probabilities, and decision-support recommendation.

## Program File
- `credit_risk_idss.py` - Implements the credit-risk classification system.

## Result
The program executed successfully and achieved 100% accuracy on the four test records. For the example new applicant, the model predicted Medium credit risk and displayed a decision-support recommendation.

**Note:** The dataset is small and illustrative. The model is intended for academic demonstration and must not be used as a standalone real-world credit-risk decision system.

## Technologies Used
Python, pandas, NumPy, and scikit-learn.