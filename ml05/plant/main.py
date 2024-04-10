import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")


def predict_knn(X_train, y_train, x_test, k=5):
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


# first two columns are features, last column is label
X_train = train[["Height", "LeafSize"]].values
y_train = train["Species"].values


X_test = test[["Height", "LeafSize"]].values


predictions = [predict_knn(X_train, y_train, x) for x in X_test]
print("predictions:", predictions)
test["Species"] = predictions
print("test:", test)


plt.scatter(train.iloc[:, 0], train.iloc[:, 1], c=train.iloc[:, -1], cmap="viridis")
plt.scatter(
    test.iloc[:, 0],
    test.iloc[:, 1],
    c=test.iloc[:, -1],
    marker="x",
    s=100,
    cmap="viridis",
)

# plt.scatter(
#     apples_test["Sweetness"], apples_test["Crunchiness"], color="red", marker="x", s=100
# )
# plt.scatter(
#     oranges_test["Sweetness"],
#     oranges_test["Crunchiness"],
#     color="orange",
#     marker="x",
#     s=100,
# )
plt.xlabel("Sweetness")
plt.ylabel("Crunchiness")
plt.title("Apples and Oranges")

plt.show()
