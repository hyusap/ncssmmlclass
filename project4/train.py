from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm


training_file = input("Enter the path to the training file: ") or "banknote_train.csv"
df = pd.read_csv(Path(__file__).parent / training_file)


theta = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
learning_rate = 0.001
iterations = 10000
X = df[["Variance", "Skewness", "Curtosis", "Entropy"]]
y = df["Genuine=1"]
m = len(y)


X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)
X.insert(0, "Intercept", 1.0)

print(X.head())


for i in tqdm(range(iterations)):
    gradient = (2 / m) * X.T.dot(X.dot(theta) - y)
    theta -= learning_rate * gradient.values


print(f"{theta=}")
with open(Path(__file__).parent / "weights.txt", "w") as f:
    for weight in theta:
        f.write(f"{weight}\n")
