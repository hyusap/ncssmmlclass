import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

p = 10000
a = 0.2
h = 6

n = lambda t: p / (1 + np.exp(-a * (t - h)))

x = np.linspace(0, 12, 1000)
y = np.array([n(t) for t in x])
plt.plot(x, y)
plt.show()


print(f"{n(3)=}")
print(f"{n(6)=}")
print(f"{n(12)=}")
