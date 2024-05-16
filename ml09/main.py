import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

df = pd.read_csv(Path(__file__).parent / "clustered_data.csv")


centroids = [(2.7, 3.36), (2.42, 2.53), (2.64, 10.15)]

# plt.scatter(df["x"], df["y"])
# for centroid in centroids:
#     plt.plot(centroid[0], centroid[1], "ro")
# plt.show()


def euclidean_distance(a, b):
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def find_closest_centroid(point, centroids):
    distances = [euclidean_distance(point, centroid) for centroid in centroids]
    return np.argmin(distances)


df["cluster"] = df.apply(
    lambda row: find_closest_centroid(row[["x", "y"]].to_numpy(), centroids), axis=1
)


def recalculate_centroids(df, centroids):
    return [
        (np.mean(df[df["cluster"] == i]["x"]), np.mean(df[df["cluster"] == i]["y"]))
        for i in range(len(centroids))
    ]


old_centroids = centroids
has_converged = False

while True:
    centroids = recalculate_centroids(df, old_centroids)

    print(f"old centroids: {old_centroids}")
    print(f"new centroids: {centroids}")

    plt.scatter(df["x"], df["y"], c=df["cluster"])
    for centroid in centroids:
        plt.plot(centroid[0], centroid[1], "ro")
    plt.show()

    # check convergence
    if np.allclose(old_centroids, centroids, atol=1e-3):
        break

    old_centroids = centroids
