import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

w = 0.5
b = 0
a = 0.1

df = pd.read_csv(Path(__file__).parent / "data.csv")

x = df["Feature"]
y = df["Label"]


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


iterations = 1000

for i in range(iterations):
    z = w * x + b
    pred = sigmoid(z)
    loss = -np.mean(y * np.log(pred) + (1 - y) * np.log(1 - pred))
    dw = np.mean((pred - y) * x)
    db = np.mean(pred - y)
    w -= a * dw
    b -= a * db
    print(f"{i=}, {loss=:.4f}, {dw=:.4f}, {db=:.4f}")


# Predict and plot results
z = w * x + b
predictions = sigmoid(z)

negatives = df[df["Label"] == 0]
positives = df[df["Label"] == 1]

plt.scatter(negatives["Feature"], negatives["Label"], c="red", label="Negative data")
plt.scatter(positives["Feature"], positives["Label"], c="green", label="Positive data")
plt.scatter(x, predictions, c="blue", label="Fitted line")
plt.xlabel("Feature")
plt.ylabel("Label")
plt.legend()
plt.show()


binary_predictions = (predictions > 0.5).astype(int)

TP = np.sum((y == 1) & (binary_predictions == 1))
TN = np.sum((y == 0) & (binary_predictions == 0))
FP = np.sum((y == 0) & (binary_predictions == 1))
FN = np.sum((y == 1) & (binary_predictions == 0))

conf_matrix = np.array([[TN, FP], [FN, TP]])

print("Confusion Matrix:")
print(conf_matrix)

print("Accuracy:", (TP + TN) / (TP + TN + FP + FN))
print("Precision:", TP / (TP + FP))
print("Recall:", TP / (TP + FN))
print("F1:", 2 * TP / (2 * TP + FP + FN))
