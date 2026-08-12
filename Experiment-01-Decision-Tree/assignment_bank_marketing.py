# BANK MARKETING DATASET - DECISION TREE CLASSIFICATION
# Assignment: Compare Entropy and Gini Criteria

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer


# 1. Load Dataset

df = pd.read_csv("bank-full.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)


# 2. Separate Features and Target

# Target column is 'Target'

X = df.drop("Target", axis=1)
y = df["Target"]


# Convert target:
# yes = 1
# no = 0

y = y.map({"yes": 1, "no": 0})


# 3. Identify Numerical and Categorical Columns

categorical_columns = X.select_dtypes(
    include=["object"]
).columns

numerical_columns = X.select_dtypes(
    exclude=["object"]
).columns

print("\nCategorical Columns:")
print(list(categorical_columns))

print("\nNumerical Columns:")
print(list(numerical_columns))


# 4. One-Hot Encode Categorical Variables

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_columns
        )
    ],
    remainder="passthrough"
)

X_encoded = preprocessor.fit_transform(X)

feature_names = preprocessor.get_feature_names_out()

print("\nNumber of Features after Encoding:")
print(len(feature_names))


# 5. Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X_encoded,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Data:", X_train.shape)
print("Testing Data:", X_test.shape)


# 6. Decision Tree using Gini Criterion

gini_model = DecisionTreeClassifier(
    criterion="gini",
    random_state=42,
    max_depth=5
)

gini_model.fit(X_train, y_train)

gini_prediction = gini_model.predict(X_test)

gini_accuracy = accuracy_score(
    y_test,
    gini_prediction
)

print("\n====================================")
print("GINI DECISION TREE")
print("====================================")

print("Accuracy:", gini_accuracy)

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        gini_prediction
    )
)


# 7. Decision Tree using Entropy Criterion

entropy_model = DecisionTreeClassifier(
    criterion="entropy",
    random_state=42,
    max_depth=5
)

entropy_model.fit(X_train, y_train)

entropy_prediction = entropy_model.predict(X_test)

entropy_accuracy = accuracy_score(
    y_test,
    entropy_prediction
)

print("\n====================================")
print("ENTROPY DECISION TREE")
print("====================================")

print("Accuracy:", entropy_accuracy)

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        entropy_prediction
    )
)


# 8. Compare Gini and Entropy Accuracy

print("\n====================================")
print("ACCURACY COMPARISON")
print("====================================")

print(f"Gini Accuracy    : {gini_accuracy:.4f}")
print(f"Entropy Accuracy : {entropy_accuracy:.4f}")

if gini_accuracy > entropy_accuracy:
    print("Better Model: Gini")
elif entropy_accuracy > gini_accuracy:
    print("Better Model: Entropy")
else:
    print("Both models have the same accuracy.")


# 9. Visualize Gini Decision Tree

plt.figure(figsize=(25, 12))

plot_tree(
    gini_model,
    feature_names=feature_names,
    class_names=["No", "Yes"],
    filled=True,
    rounded=True,
    fontsize=8
)

plt.title("Decision Tree - Gini Criterion")
plt.show()


# 10. Visualize Entropy Decision Tree

plt.figure(figsize=(25, 12))

plot_tree(
    entropy_model,
    feature_names=feature_names,
    class_names=["No", "Yes"],
    filled=True,
    rounded=True,
    fontsize=8
)

plt.title("Decision Tree - Entropy Criterion")
plt.show()


# 11. Feature Importance - Gini

gini_importance = pd.DataFrame({
    "Feature": feature_names,
    "Importance": gini_model.feature_importances_
})

gini_importance = gini_importance.sort_values(
    by="Importance",
    ascending=False
)

print("\n====================================")
print("TOP IMPORTANT FEATURES - GINI")
print("====================================")

print(gini_importance.head(10))


# 12. Feature Importance - Entropy

entropy_importance = pd.DataFrame({
    "Feature": feature_names,
    "Importance": entropy_model.feature_importances_
})

entropy_importance = entropy_importance.sort_values(
    by="Importance",
    ascending=False
)

print("\n====================================")
print("TOP IMPORTANT FEATURES - ENTROPY")
print("====================================")

print(entropy_importance.head(10))


# 13. Plot Top 10 Important Features

top_features = gini_importance.head(10)

plt.figure(figsize=(10, 6))

plt.barh(
    top_features["Feature"][::-1],
    top_features["Importance"][::-1]
)

plt.xlabel("Feature Importance")
plt.ylabel("Features")
plt.title("Top 10 Important Features - Gini Decision Tree")

plt.tight_layout()
plt.show()