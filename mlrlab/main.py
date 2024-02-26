import numpy as np
import pandas as pd

df = pd.read_csv("data.csv")

cols = ["TV", "Radio", "Newspaper"]

X = df[cols].values
X = np.concatenate([np.ones((X.shape[0], 1)), X], axis=1)

print(X)


y = df["Sales"].values
vals = np.linalg.inv(X.T @ X) @ X.T @ y

# print mse
y_pred = X @ vals
mse = np.mean((df["Sales"].values - y_pred) ** 2)
print(f"mse = {mse:.2f}")


# print equation

print(
    f"Sales = {vals[0]:.2f} + {vals[1]:.2f} * TV + {vals[2]:.2f} * Radio + {vals[3]:.2f} * Newspaper"
)


"""
TV advertising is the most effective, followed by Radio and Newspaper, the mse of 3.35 is quite low, indicating a good fit. Overall, the model is a good fit for the data.
"""
