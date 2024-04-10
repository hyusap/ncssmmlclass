import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("train.csv")


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

misclassifications_by_k = []
accuracy_by_k = []


data_splits = np.array_split(data, folds)

for number_of_neighbors in knns:
    print(f"results for k={number_of_neighbors}")

    accuracys = []
    misclassifications = []

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
        X_train = train[["Test1", "Test2"]].values
        y_train = train["Pass"].values
        X_test = test[["Test1", "Test2"]].values
        predictions = [
            predict_knn(X_train, y_train, x, k=number_of_neighbors) for x in X_test
        ]
        test["Predicted"] = predictions
        for i in range(len(test)):
            confusion_matrix.loc[
                f"Actual {int(test.iloc[i]['Pass'])}",
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
        accuracys.append(accuracy)
        misclassifications.append(
            confusion_matrix.iloc[0, 1] + confusion_matrix.iloc[1, 0]
        )
    print(f"\tMean accuracy: {np.mean(accuracys)}")
    print(f"\tMean misclassifications: {np.mean(misclassifications)}")
    misclassifications_by_k.append(np.mean(misclassifications))
    accuracy_by_k.append(np.mean(accuracys))
    print()


plt.plot(knns, misclassifications_by_k)
plt.xlabel("k")
plt.ylabel("Misclassifications")
plt.title("Misclassifications by k")
plt.savefig("misclassifications_by_k.png")
plt.show()

plt.plot(knns, accuracy_by_k)
plt.xlabel("k")
plt.ylabel("Accuracy")
plt.title("Accuracy by k")
plt.savefig("accuracy_by_k.png")
plt.show()


# best value
best_k = knns[np.argmax(accuracy_by_k)]
print(f"Best k: {best_k}")


# run on test
test = pd.read_csv("test.csv")
X_train = data[["Test1", "Test2"]].values
y_train = data["Pass"].values
X_test = test[["Test1", "Test2"]].values
predictions = [predict_knn(X_train, y_train, x, k=best_k) for x in X_test]
test["Predicted"] = predictions

confusion_matrix = pd.DataFrame(
    {
        "Predicted 0": [0, 0],
        "Predicted 1": [0, 0],
    },
    index=["Actual 0", "Actual 1"],
)
for i in range(len(test)):
    confusion_matrix.loc[
        f"Actual {int(test.iloc[i]['Pass'])}",
        f"Predicted {int(test.iloc[i]['Predicted'])}",
    ] += 1
accuracy = (
    confusion_matrix.iloc[0, 0] + confusion_matrix.iloc[1, 1]
) / confusion_matrix.values.sum()
precision = confusion_matrix.iloc[1, 1] / confusion_matrix["Predicted 1"].sum()
recall = confusion_matrix.iloc[1, 1] / confusion_matrix.loc["Actual 1"].sum()
f1 = 2 * precision * recall / (precision + recall)
print(
    f"Test results: accuracy: {accuracy:.4f}, precision: {precision:.4f}, recall: {recall:.4f}, f1: {f1:.4f}"
)
print(confusion_matrix)

train_pass = data[data["Pass"] == 1]
train_fail = data[data["Pass"] == 0]

plt.scatter(
    train_pass["Test1"],
    train_pass["Test2"],
    color="green",
    label="Pass",
    alpha=0.5,
)
plt.scatter(
    train_fail["Test1"],
    train_fail["Test2"],
    color="red",
    label="Fail",
    alpha=0.5,
)

test_pass = test[test["Predicted"] == 1]
test_fail = test[test["Predicted"] == 0]

plt.scatter(
    test_pass["Test1"],
    test_pass["Test2"],
    color="green",
    label="Predicted Pass",
    marker="x",
)
plt.scatter(
    test_fail["Test1"],
    test_fail["Test2"],
    color="red",
    label="Predicted Fail",
    marker="x",
)

plt.legend()
plt.title("Test 1 vs Test 2")
plt.xlabel("Test 1")
plt.ylabel("Test 2")
plt.savefig("test_results.png")
plt.show()
