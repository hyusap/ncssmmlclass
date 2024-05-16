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
            np.mean(df[df["cluster"] == i]["sepal_length"]),
            np.mean(df[df["cluster"] == i]["sepal_width"]),
        )
        for i in range(len(centroids))
    ]


for should_standardize in [True, False]:

    df = pd.read_csv(Path(__file__).parent / "iris_data_two_features.csv")

    if should_standardize:
        df["sepal_length"] = (
            df["sepal_length"] - np.mean(df["sepal_length"])
        ) / np.std(df["sepal_length"])
        df["sepal_width"] = (df["sepal_width"] - np.mean(df["sepal_width"])) / np.std(
            df["sepal_width"]
        )

    k = 3

    starting_centroid = df.sample(1)[["sepal_length", "sepal_width"]].to_numpy()[0]

    print(starting_centroid)

    centroids = [starting_centroid]

    while len(centroids) < k:
        distances = []
        for centroid in centroids:
            distances.append(
                df.apply(
                    lambda row: euclidean_distance(
                        row[["sepal_length", "sepal_width"]].to_numpy(), centroid
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
        selected_point = df.loc[
            selected_index, ["sepal_length", "sepal_width"]
        ].to_numpy()
        print("Selected point based on distribution:", selected_point)

        centroids.append(selected_point)

        print(df.head())

    print(centroids)

    df["cluster"] = df.apply(
        lambda row: find_closest_centroid(
            row[["sepal_length", "sepal_width"]].to_numpy(), centroids
        ),
        axis=1,
    )

    old_centroids = centroids
    has_converged = False

    while True:
        centroids = recalculate_centroids(df, old_centroids)

        print(f"old centroids: {old_centroids}")
        print(f"new centroids: {centroids}")

        # plt.scatter(df["sepal_length"], df["sepal_width"], c=df["cluster"])
        # for centroid in centroids:
        #     plt.plot(centroid[0], centroid[1], "ro")
        # plt.show()

        # check convergence
        if np.allclose(old_centroids, centroids, atol=1e-3):
            break

        old_centroids = centroids

    plt.scatter(df["sepal_length"], df["sepal_width"], c=df["cluster"])
    plt.xlabel("Sepal Length")
    plt.ylabel("Sepal Width")
    plt.title(f"K++ Clustering {"with" if should_standardize else "without"} Standardization")
    for centroid in centroids:
        plt.plot(centroid[0], centroid[1], "ro")
    plt.show()
