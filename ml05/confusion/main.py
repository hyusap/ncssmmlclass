import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("data.csv")


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
    # check for tie and if so check next nearest neighbor
    if len(set(counts.values())) == 1:
        return predict_knn(X_train, y_train, x_test, k + 1)
    return max(counts, key=counts.get)


confusion_matrix = pd.DataFrame(
    {
        "Predicted 0": [0, 0],
        "Predicted 1": [0, 0],
    },
    index=["Actual 0", "Actual 1"],
)


for i in range(len(data)):
    # train = data.drop(i)
    train = data
    test = data.iloc[i]
    # print(f"train: {len(train)}, test: {len(test)}")

    X_train = train[["Feature1", "Feature2"]].values
    y_train = train["Label"].values
    X_test = test[["Feature2", "Feature2"]].values

    prediction = predict_knn(X_train, y_train, X_test, k=3)
    confusion_matrix.loc[
        f"Actual {int(test['Label'])}", f"Predicted {int(prediction)}"
    ] += 1


print(confusion_matrix)
accuracy = (
    confusion_matrix.iloc[0, 0] + confusion_matrix.iloc[1, 1]
) / confusion_matrix.values.sum()
precision = confusion_matrix.iloc[1, 1] / confusion_matrix["Predicted 1"].sum()
recall = confusion_matrix.iloc[1, 1] / confusion_matrix.loc["Actual 1"].sum()
f1 = 2 * precision * recall / (precision + recall)
print("accuracy:", accuracy)
print("precision:", precision)
print("recall:", recall)
print("f1:", f1)
