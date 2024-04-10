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
    return max(counts, key=counts.get)


folds = 5
knns = [1, 3, 5, 7, 9]


data_splits = np.array_split(data, folds)

for number_of_neighbors in knns:
    print(f"results for k={number_of_neighbors}")
    for fold in range(folds):
        confusion_matrix = pd.DataFrame(
            {
                "Predicted 0": [0, 0],
                "Predicted 1": [0, 0],
            },
            index=["Actual 0", "Actual 1"],
        )
        train = pd.concat([data_splits[i] for i in range(folds) if i != fold])
        test = data_splits[fold]
        X_train = train[["Self_Indulgence", "Furriness"]].values
        y_train = train["Coyote"].values
        X_test = test[["Self_Indulgence", "Furriness"]].values
        predictions = [
            predict_knn(X_train, y_train, x, k=number_of_neighbors) for x in X_test
        ]
        test["Predicted"] = predictions
        for i in range(len(test)):
            confusion_matrix.loc[
                f"Actual {int(test.iloc[i]['Coyote'])}",
                f"Predicted {int(test.iloc[i]['Predicted'])}",
            ] += 1
        accuracy = (
            confusion_matrix.iloc[0, 0] + confusion_matrix.iloc[1, 1]
        ) / confusion_matrix.values.sum()
        precision = confusion_matrix.iloc[1, 1] / confusion_matrix["Predicted 1"].sum()
        recall = confusion_matrix.iloc[1, 1] / confusion_matrix.loc["Actual 1"].sum()
        f1 = 2 * precision * recall / (precision + recall)
        print(
            f"\tFold {fold}: accuracy: {accuracy:.4f}, precision: {precision:.4f}, recall: {recall:.4f}, f1: {f1:.4f}"
        )
