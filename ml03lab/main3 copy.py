import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Sleep Study Exam (1).csv")

X1 = df["study_hours"].values

X2 = df["sleep_hours"].values

X_des = np.column_stack((np.ones(len(X1)), X1, X1**2, X2, X2**2, X1 * X2))

Y = df["exam_scores"].values

coefficients = np.linalg.inv(X_des.T @ X_des) @ (X_des.T @ Y)

print(coefficients)
a = coefficients[0]
b = coefficients[1]
c = coefficients[2]
d = coefficients[3]
e = coefficients[4]
f = coefficients[5]
print(a, b, c, d, e, f)


mse = np.mean((Y - X_des @ coefficients) ** 2)
print(mse)
