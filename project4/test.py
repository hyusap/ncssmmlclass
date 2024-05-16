import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

weight_path = input("Enter the path to the weights file: ") or "weights.txt"
with open(Path(__file__).parent / weight_path) as f:
    theta = np.array([float(line) for line in f])
    print(theta)

test_path = input("Enter the path to the test file: ") or "banknote_test.csv"
df = pd.read_csv(Path(__file__).parent / test_path)
X = df[["Variance", "Skewness", "Curtosis", "Entropy"]]
y = df["Genuine=1"]

# Standardize the features
X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)
X.insert(0, "Intercept", 1.0)

# Predict the output
predictions = X.dot(theta)
predictions = (predictions >= 0.5).astype(int)

# Metrics
TP = np.sum((y == 1) & (predictions == 1))
TN = np.sum((y == 0) & (predictions == 0))
FP = np.sum((y == 0) & (predictions == 1))
FN = np.sum((y == 1) & (predictions == 0))

conf_matrix = pd.DataFrame(
    [[TP, FP], [FN, TN]],
    index=["Actual Positive", "Actual Negative"],
    columns=["Predicted Positive", "Predicted Negative"],
)

print("Confusion Matrix:")
print(conf_matrix)

print("Accuracy:", (TP + TN) / (TP + TN + FP + FN))
print("Precision:", TP / (TP + FP))
print("Recall:", TP / (TP + FN))
print("F1:", 2 * TP / (2 * TP + FP + FN))
