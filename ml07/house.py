from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv(Path(__file__).parent / "generated_house_prices.csv")


theta = np.array([0.0, 0.0, 0.0])
learning_rate = 0.01
iterations = [50, 100, 500, 1000, 2000]
X = df[["House Size (sq ft)", "Bedrooms"]]
y = df["Price (thousand $)"]
m = len(y)


# Standardize the data
X_standardized = (X - np.mean(X, axis=0)) / np.std(X, axis=0)
X = X_standardized
X.insert(0, "Intercept", 1.0)


print(X.head())

for iteration in iterations:
    for i in range(iteration):
        gradient = (2 / m) * X.T.dot(X.dot(theta) - y)
        theta -= learning_rate * gradient.values

    plt.scatter(X["House Size (sq ft)"], y, color="red", label="Actual Prices")
    plt.scatter(
        X["House Size (sq ft)"], X @ theta, color="blue", label="Predicted Prices"
    )
    plt.xlabel("House Size (sq ft)")
    plt.ylabel("Price (thousand $)")
    plt.title("Gradient Descent")
    plt.legend()

    plt.show()

    print(f"{theta=}")
