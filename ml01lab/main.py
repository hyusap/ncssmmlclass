import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
x = df.Height
y = df.Shoe_Size

x_bar = np.mean(x)
y_bar = np.mean(y)

x_diff = x - x_bar
y_diff = y - y_bar

m = np.sum(x_diff * y_diff) / np.sum(x_diff**2)
b = y_bar - m * x_bar

y_pred = m * x + b
mse = np.mean((y - y_pred) ** 2)

print(f"y = {m:.2f}x + {b:.2f}")
print(f"mse = {mse:.2f}")


plt.xlabel("Height")
plt.ylabel("Shoe Size")
plt.title(f"Height vs Shoe Size (m={m:.2f}, b={b:.2f}, mse={mse:.2f})")

plt.scatter(x, y)
plt.plot(x, m * x + b, color="red")
plt.show()
