import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

w = np.array([0.5, 0.5])
b = 0
a = 0.01

df = pd.read_csv(Path(__file__).parent / "logistic_regression_data_standard.csv")

x1 = df["X1"]
x2 = df["X2"]
y = df["Y"]
X = np.column_stack((x1, x2))
losses = []


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def logistic_loss(z, y):
    return -np.mean(y * np.log(sigmoid(z)) + (1 - y) * np.log(1 - sigmoid(z)))


iterations = 10000

for i in range(iterations):
    z = X @ w + b
    pred = sigmoid(z)
    loss = -np.mean(y * np.log(pred) + (1 - y) * np.log(1 - pred))
    losses.append(loss)
    dw = (pred - y) @ X / len(y)
    db = np.mean(pred - y)
    w -= a * dw
    b -= a * db
    print(f"{i=}, {loss=:.4f}, {dw=}, {db=:.4f}")


def hypothesis(x, w, b):
    return (-w[1] / w[0]) * x + (b / w[0])


# Predict and plot results
z = X @ w + b
predictions = sigmoid(z)

negatives = df[df["Y"] == 0]
positives = df[df["Y"] == 1]

plt.scatter(df[df["Y"] == 0]["X1"], df[df["Y"] == 0]["X2"], c="red", label="Negative")
plt.scatter(df[df["Y"] == 1]["X1"], df[df["Y"] == 1]["X2"], c="green", label="Positive")
plt.plot(x1, hypothesis(x1, w, b), c="blue", label="Fitted line")
plt.xlabel("X1")
plt.ylabel("X2")
plt.legend()
plt.show()

plt.plot(losses)
plt.xlabel("Iteration")
plt.ylabel("Loss")
plt.title("Logistic Regression Loss")
plt.show()

print(f"b={b}, w1={w[1]}, w2={w[0]}")


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
