import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
import random

df = pd.read_csv(Path(__file__).parent / "clustered_data.csv")

k = 3


starting_centroid = df.sample(1)[["x", "y"]].to_numpy()[0]

print(starting_centroid)


centroids = [starting_centroid]


def euclidean_distance(a, b):
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


while len(centroids) < k:
    distances = []
    for centroid in centroids:
        distances.append(
            df.apply(
                lambda row: euclidean_distance(row[["x", "y"]].to_numpy(), centroid),
                axis=1,
            )
        )

    df["distance"] = pd.DataFrame(distances).T.min(axis=1)

    # print("Minimum distance:", min_distance)

    distance_sum = df["distance"].sum()

    df["probability"] = df["distance"] / distance_sum
    df["distribution"] = df["probability"].cumsum()

    rand_val = random.random()

    selected_index = df[df["distribution"] >= rand_val].index[0]
    selected_point = df.loc[selected_index, ["x", "y"]].to_numpy()
    print("Selected point based on distribution:", selected_point)

    centroids.append(selected_point)

    print(df.head())

print(centroids)


plt.scatter(df["x"], df["y"], c="blue")
for centroid in centroids:
    plt.plot(centroid[0], centroid[1], "ro")
plt.show()
