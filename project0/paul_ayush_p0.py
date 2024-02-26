# Ayush Paul

import pandas as pd
import matplotlib.pyplot as plt


def main():
    input_file = input("Enter the name of the input file: ")
    df = pd.read_csv(input_file)

    print(df.head())
    headers = list(enumerate(df.columns))
    print(f"Choose two features to plot from the following list: {headers}")
    x = int(input("Enter the number of the feature to plot on the x-axis: "))
    y = int(input("Enter the number of the feature to plot on the y-axis: "))

    Setosa = df[df.species == "setosa"]
    Versicolor = df[df.species == "versicolor"]
    Virginica = df[df.species == "virginica"]

    plt.scatter(
        Setosa.iloc[:, x], Setosa.iloc[:, y], marker="v", c="red", label="Setosa"
    )

    plt.scatter(
        Versicolor.iloc[:, x],
        Versicolor.iloc[:, y],
        marker="x",
        c="green",
        label="Versicolor",
    )

    plt.scatter(Virginica.iloc[:, x], Virginica.iloc[:, y], c="blue", label="Virginica")

    plt.xlabel(df.columns[x])
    plt.ylabel(df.columns[y])
    plt.title(f"{df.columns[x]} vs {df.columns[y]}")
    plt.legend(loc="upper left")
    plt.plot()
    plt.show()


if __name__ == "__main__":
    repeat = True
    while repeat:
        main()
        repeat = input("Do you want to do another plot? (y/n): ").lower() == "y"
