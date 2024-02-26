import numpy as np
import pandas as pd

df = pd.read_csv("salary_data.csv")

# Engine Size,Weight,Horsepower
cols = df.columns
x_cols = cols[:-1]
y_col = cols[-1]

X = df[x_cols].values
X = np.concatenate([np.ones((X.shape[0], 1)), X], axis=1)


y = df[y_col]
vals = np.linalg.inv(X.T @ X) @ X.T @ y

# print mse
y_pred = X @ vals
mse = np.mean((df[y_col].values - y_pred) ** 2)
print(f"mse = {mse:.2f}")


# print equation

print(
    f"{y_col} = {vals[0]:.2f} + {vals[1]:.2f} * {x_cols[0]} + {vals[2]:.2f} * {x_cols[1]} + {vals[3]:.2f} * {x_cols[2]}"
)
