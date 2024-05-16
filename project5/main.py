import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
import random


def euclidean_distance(a, b):
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def find_closest_centroid(point, centroids):
    distances = [euclidean_distance(point, centroid) for centroid in centroids]
    return np.argmin(distances)


def recalculate_centroids(df, centroids):
    return [
        (
            np.mean(df[df["cluster"] == i]["x1"]),
            np.mean(df[df["cluster"] == i]["x2"]),
        )
        for i in range(len(centroids))
    ]


def sse(df, centroids):
    return np.sum(
        df.apply(
            lambda row: euclidean_distance(
                row[["x1", "x2"]].to_numpy(), centroids[int(row["cluster"])]
            ),
            axis=1,
        )
    )


results = pd.DataFrame(columns=["initial centroids", "final centroids", "j value"])

for i in range(5):

    df = pd.read_csv(Path(__file__).parent / "DataToCluster.csv")

    k = 2

    starting_centroid = df.sample(1)[["x1", "x2"]].to_numpy()[0]

    print(starting_centroid)

    centroids = [starting_centroid]

    while len(centroids) < k:
        distances = []
        for centroid in centroids:
            distances.append(
                df.apply(
                    lambda row: euclidean_distance(
                        row[["x1", "x2"]].to_numpy(), centroid
                    ),
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
        selected_point = df.loc[selected_index, ["x1", "x2"]].to_numpy()
        print("Selected point based on distribution:", selected_point)

        centroids.append(selected_point)

        print(df.head())

    kpp_results = centroids.copy()

    df["cluster"] = df.apply(
        lambda row: find_closest_centroid(row[["x1", "x2"]].to_numpy(), centroids),
        axis=1,
    )

    old_centroids = centroids
    has_converged = False

    while True:
        centroids = recalculate_centroids(df, old_centroids)

        print(f"old centroids: {old_centroids}")
        print(f"new centroids: {centroids}")

        # plt.scatter(df["x1"], df["x2"], c=df["cluster"])
        # for centroid in centroids:
        #     plt.plot(centroid[0], centroid[1], "ro")
        # plt.show()

        # check convergence
        if np.allclose(old_centroids, centroids, atol=1e-3):
            break

        old_centroids = centroids

    j_value = sse(df, centroids)

    plt.scatter(df["x1"], df["x2"], c=df["cluster"])
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.title(f"K++ Clustering")
    for centroid in centroids:
        plt.plot(centroid[0], centroid[1], "ro")
    plt.savefig(Path(__file__).parent / f"kpp_results_{i}.png")
    plt.show()

    results.loc[i] = [kpp_results, centroids, j_value]

print(results)
results.to_csv(Path(__file__).parent / "kpp_results.csv")
