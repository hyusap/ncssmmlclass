import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


train = pd.read_csv("vehicles_training_data.csv")
test = pd.read_csv("vehicles_test_data.csv")


def predict_knn(X_train, y_train, x_test, k=3):
    distances = [np.sqrt(np.sum((x_test - x) ** 2)) for x in X_train]
    k_indices = np.argsort(distances)[:k]
    k_nearest_labels = [y_train[i] for i in k_indices]
    counts = {}
    for label in k_nearest_labels:
        if label in counts:
            counts[label] += 1
        else:
            counts[label] = 1
    return max(counts, key=counts.get)


X_train = train[["MaxSpeed", "FuelEfficiency"]].values
y_train = train["Category"].values


X_test = test[["MaxSpeed", "FuelEfficiency"]].values


X_train = (X_train - X_train.mean(axis=0)) / X_train.std(axis=0)
X_test = (X_test - X_test.mean(axis=0)) / X_test.std(axis=0)


predictions = [predict_knn(X_train, y_train, x, 5) for x in X_test]
print("predictions:", predictions)
test["Category"] = predictions
print("test:", test)


# plt.scatter(
#     train["MaxSpeed"], train["FuelEfficiency"], c=train["Category"], cmap="viridis"
# )
# plt.scatter(
#     test["MaxSpeed"],
#     test["FuelEfficiency"],
#     c=test["Category"],
#     marker="x",
#     s=100,
#     cmap="viridis",
# )


# looks odd if plotted unstandardized
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap="viridis")
plt.scatter(
    X_test[:, 0],
    X_test[:, 1],
    c=test["Category"],
    marker="x",
    s=100,
    cmap="viridis",
)


plt.xlabel("MaxSpeed")
plt.ylabel("FuelEfficiency")
plt.title("Vehicles")
plt.savefig("std.png")
plt.show()
