import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("spend_v_revenue.csv")


cols = df.columns
x_col = cols[1]
y_col = cols[2]

X = df[x_col].values
X = np.column_stack([np.ones(len(X)), X, X**2])

y = df[y_col]

vals = np.linalg.inv(X.T @ X) @ X.T @ y

x_curve = np.linspace(df[x_col].min(), df[x_col].max(), 100)

y_pred = vals[0] + vals[1] * x_curve + vals[2] * x_curve**2

print(
    f"curve eq: {y_col} = {vals[0]:.2f} + {vals[1]:.2f} * {x_col} + {vals[2]:.2f} * {x_col}^2"
)
print(f"mse = {np.mean((y - X @ vals)**2):.2f}")


plt.scatter(df[x_col], df[y_col])
plt.plot(x_curve, y_pred, color="red")
# labels and title
plt.xlabel(x_col)
plt.ylabel(y_col)

plt.title(f"{y_col} vs {x_col}")
# legend

plt.legend(["curve", "data"])

# show plot
plt.show()
