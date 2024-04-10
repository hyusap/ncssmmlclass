import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

train["is_orange"] = train["Label"].astype(bool)


apples_train = train[train["is_orange"] == False]
oranges_train = train[train["is_orange"]]


def predict_knn(X_train, y_train, x_test, k=3):
    distances = [np.sqrt(np.sum((x_test - x) ** 2)) for x in X_train]
    k_indices = np.argsort(distances)[:k]
    k_nearest_labels = [y_train[i] for i in k_indices]
    return max(set(k_nearest_labels), key=k_nearest_labels.count)


apples_train = train[train["is_orange"] == False]
oranges_train = train[train["is_orange"]]

X_train = train[["Sweetness", "Crunchiness"]].values
y_train = train["is_orange"].values


X_test = test[["Sweetness", "Crunchiness"]].values

predictions = [predict_knn(X_train, y_train, x, k=3) for x in X_test]
test["is_orange"] = predictions

print(test)

apples_test = test[test["is_orange"] == False]
oranges_test = test[test["is_orange"]]


plt.scatter(apples_train["Sweetness"], apples_train["Crunchiness"], color="red")
plt.scatter(oranges_train["Sweetness"], oranges_train["Crunchiness"], color="orange")
plt.scatter(
    apples_test["Sweetness"], apples_test["Crunchiness"], color="red", marker="x", s=100
)
plt.scatter(
    oranges_test["Sweetness"],
    oranges_test["Crunchiness"],
    color="orange",
    marker="x",
    s=100,
)
plt.xlabel("Sweetness")
plt.ylabel("Crunchiness")
plt.title("Apples and Oranges")

plt.show()
