import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

mpl = 100
lr = 0.3
h = 20

n = lambda t: mpl / (1 + np.exp(-lr * (t - h)))

x = np.linspace(0, 50, 1000)
y = np.array([n(t) for t in x])
plt.plot(x, y)
plt.show()


print(f"{n(10)=}")
print(f"{n(20)=}")
print(f"{n(40)=}")
