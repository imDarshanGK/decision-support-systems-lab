# Experiment 11 - Intelligent DSS Using Machine Learning

## Aim
To implement a basic Intelligent Decision Support System using Machine Learning to predict loan decisions and provide decision-support recommendations.

## Problem Statement
Develop an ML-based system that analyzes customer information and predicts whether a loan application is likely to be approved or rejected.

## Software Requirements
- Python 3.x
- pandas
- NumPy
- scikit-learn

## Dataset Description
The dataset contains 15 customer records with the following attributes:

- Age
- Income
- Credit Score
- Loan Amount
- Debt
- Employment
- Loan Decision

## Algorithm
1. Create the historical customer dataset.
2. Check missing values and data types.
3. Encode employment status and loan decisions.
4. Separate input features and target variable.
5. Split the dataset into training and testing sets.
6. Train a Decision Tree Classifier.
7. Predict test outcomes.
8. Evaluate the model using accuracy, confusion matrix, and classification report.
9. Predict the decision for a new customer.
10. Display the predicted decision, class probabilities, and recommendation.

## Assignment
The assignment compares two Machine Learning classifiers:

- Decision Tree Classifier
- Random Forest Classifier

Both models are evaluated using the same training and testing split. The assignment selects a model based on test accuracy and predicts the decision for a new customer.

## Program Files
- `intelligent_dss.py` - Main experiment using a Decision Tree Classifier.
- `intelligent_dss_assignment.py` - Assignment comparing Decision Tree and Random Forest classifiers.

## Result
Both programs executed successfully. The Decision Tree and Random Forest models achieved 100% accuracy on the five test records. The system predicted the new customer's loan decision and displayed a decision-support recommendation.

**Note:** The dataset is very small and illustrative. The results are for academic demonstration only and should not be used to make real loan approval decisions.

## Technologies Used
Python, pandas, NumPy, and scikit-learn.