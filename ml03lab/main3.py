import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sleepstudyexam.csv")


cols = df.columns
x_col = cols[0]
x_col2 = cols[1]
y_col = cols[2]

X1 = df[x_col].values
X2 = df[x_col2].values
X = np.column_stack([np.ones(len(X1)), X1, X1**2, X2, X2**2, X1 * X2])
print(X)
# print(X1)
# print(X2)

print()

y = df[y_col]

vals = np.linalg.inv(X.T @ X) @ (X.T @ y)
print(vals)

x_curve = np.linspace(df[x_col].min(), df[x_col].max(), 100)
x_curve2 = np.linspace(df[x_col2].min(), df[x_col2].max(), 100)

y_pred = (
    vals[0]
    + vals[1] * x_curve
    + vals[2] * x_curve**2
    + vals[3] * x_curve2
    + vals[4] * x_curve2**2
    + vals[5] * x_curve * x_curve2
)

print(
    f"curve eq: {y_col} = {vals[0]:.2f} + {vals[1]:.2f} * {x_col} + {vals[2]:.2f} * {x_col}^2 + {vals[3]:.2f} * {x_col2} + {vals[4]:.2f} * {x_col2}^2 + {vals[5]:.2f} * {x_col} * {x_col2}"
)
print(f"mse = {np.mean((y - X @ vals)**2):.2f}")


# plt.scatter(df[x_col], df[y_col])
# plt.plot(x_curve, y_pred, color="red")
# labels and title
# plt.xlabel(x_col)
# plt.ylabel(y_col)

# plt.title(f"{y_col} vs {x_col} and {x_col2}")
# # legend

# plt.legend(["curve", "data"])

# # show plot
# plt.show()
