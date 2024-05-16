import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

df = pd.read_csv(Path(__file__).parent / "elbow.csv")

k_min = 1
k_max = 10


def euclidean_distance(a, b):
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def find_closest_centroid(point, centroids):
    distances = [euclidean_distance(point, centroid) for centroid in centroids]
    return np.argmin(distances)


def recalculate_centroids(df, centroids):
    return [
        (np.mean(df[df["cluster"] == i]["x"]), np.mean(df[df["cluster"] == i]["y"]))
        for i in range(len(centroids))
    ]


def sse(df, centroids):
    return np.sum(
        df.apply(
            lambda row: euclidean_distance(
                row[["x", "y"]].to_numpy(), centroids[int(row["cluster"])]
            ),
            axis=1,
        )
    )


sses = []

for k in range(k_min, k_max + 1):

    centroids = df[["x", "y"]].sample(k)
    print(f"k = {k}")
    print(f"centroids: {centroids}")

    df["cluster"] = df.apply(
        lambda row: int(
            find_closest_centroid(
                row[["x", "y"]].to_numpy(), centroids[["x", "y"]].to_numpy()
            )
        ),
        axis=1,
    )

    print(df.head())

    old_centroids = centroids
    has_converged = False

    while True:
        centroids = recalculate_centroids(df, old_centroids)

        print(f"old centroids: {old_centroids}")
        print(f"new centroids: {centroids}")

        # plt.scatter(df["x"], df["y"], c=df["cluster"])
        # for centroid in centroids:
        #     plt.plot(centroid[0], centroid[1], "ro")
        # plt.show()

        # check convergence
        if np.allclose(old_centroids, centroids, atol=1e-3):
            sses.append(sse(df, centroids))
            break

        old_centroids = centroids

plt.plot(range(k_min, k_max + 1), sses)
plt.scatter(range(k_min, k_max + 1), sses)
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Sum of Squared Errors (SSE)")
plt.title("Elbow Method")
plt.show()
