import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import seaborn as sns

w = np.array([0.5, 0.5])
b = 0
a = 0.01

df = pd.read_csv(Path(__file__).parent / "email_data.csv")

x1 = df["Keyword Frequency"]
x2 = df["Email Length"]

x1 = (x1 - np.mean(x1)) / np.std(x1)
x2 = (x2 - np.mean(x2)) / np.std(x2)

# df["Keyword Frequency"] = x1
# df["Email Length"] = x2

y = df["Is Spam"]
X = np.column_stack((x1, x2))
losses = []


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def logistic_loss(z, y):
    return -np.mean(y * np.log(sigmoid(z)) + (1 - y) * np.log(1 - sigmoid(z)))


iterations = 1000

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

negatives = df[df["Is Spam"] == 0]
positives = df[df["Is Spam"] == 1]

plt.scatter(
    negatives["Keyword Frequency"],
    negatives["Email Length"],
    c="red",
    label="Negative",
)
plt.scatter(
    positives["Keyword Frequency"],
    positives["Email Length"],
    c="green",
    label="Positive",
)

original_x1 = df["Keyword Frequency"]
hypothesis_values = hypothesis(x1, w, b)
original_y_values = hypothesis_values * np.std(df["Email Length"]) + np.mean(
    df["Email Length"]
)
plt.plot(
    original_x1, original_y_values, c="blue", label="Fitted line", linestyle="dotted"
)

plt.xlabel("Keyword Frequency")
plt.ylabel("Email Length")
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

conf_matrix = pd.DataFrame(
    [[TN, FP], [FN, TP]],
    index=["Actual Not Spam", "Actual Spam"],
    columns=["Predicted Not Spam", "Predicted Spam"],
)

sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues")
plt.xlabel("Predicted Labels")
plt.ylabel("True Labels")
plt.title("Confusion Matrix")
plt.show()

print("Accuracy:", (TP + TN) / (TP + TN + FP + FN))
print("Precision:", TP / (TP + FP))
print("Recall:", TP / (TP + FN))
print("F1:", 2 * TP / (2 * TP + FP + FN))
