import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

df = pd.read_csv(Path(__file__).parent / "grad_desc_exam_scores.csv")

print(df.head())


def compute_loss(w0, w1, X, y):
    n = len(X)
    total_error = 0
    for i in range(n):
        y_hat = w0 + w1 * X[i]
        error = y[i] - y_hat
        total_error += error**2
    return total_error / (2 * n)


def gradient_descent(X, y, w0, w1, learning_rate, iterations):
    for i in range(iterations):
        error = compute_loss(w0, w1, X, y)
        n = len(X)
        for j in range(n):
            y_hat = w0 + w1 * X[j]
            error_grad = (y[j] - y_hat) / n
            w0 += learning_rate * error_grad
            w1 += learning_rate * error_grad * X[j]

    return w0, w1


w0 = 0
w1 = 0
learning_rate = 0.01
iterations = 10000

w0, w1 = gradient_descent(
    df["Hours Studied"], df["Exam Score"], w0, w1, learning_rate, iterations
)

plt.scatter(df["Hours Studied"], df["Exam Score"])
plt.plot(df["Hours Studied"], w0 + w1 * df["Hours Studied"])
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Gradient Descent")
plt.legend(["Data", "Fitted Line"])
plt.show()
