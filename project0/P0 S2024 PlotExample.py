"""
Reading in and manipulating the Iris Data Set using Pandas Library functions and 
matplotlib.pyplot to plot Sepal Length vs Petal Length
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# What is in this file?
data = pd.read_csv("Data/iris_data.csv")
print("Number of records is: ", len(data.index))  # How many rows of data
print(" ")
print(data.head())
print(" ")
# How many species do we have?
print(data.pivot_table(index="species", aggfunc="count"))


# Create a table of each type of Iris flowr
Setosa = data[data.species == "setosa"]
Versicolor = data[data.species == "versicolor"]
Virginica = data[data.species == "virginica"]

# Create scatter plots of sepal length vs petal length
plt.scatter(
    Setosa["sepal_length"], Setosa["petal_length"], marker="v", c="red", label="Setosa"
)
plt.scatter(
    Versicolor["sepal_length"],
    Versicolor["petal_length"],
    marker="x",
    c="green",
    label="Versicolor",
)
plt.scatter(
    Virginica["sepal_length"], Virginica["petal_length"], c="blue", label="Virginica"
)

# Add plot lables
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.title("Sepal vs Petal Length")
plt.legend(loc="upper left")
plt.plot()
plt.show()
# Save the plot
# plt.savefig("P0.png")
