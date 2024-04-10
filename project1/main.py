import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


SHOULD_GRAPH = False

df = pd.read_csv("data.csv")
print(df.head())


x_col = df.columns[0]
y_col = df.columns[1]
x = df[x_col].values
y = df[y_col].values
# split into folds
k = 5
x_folds = np.array_split(x, k)
y_folds = np.array_split(y, k)

df_of_train_mses = pd.DataFrame(columns=["linear", "quadratic", "sqrt"])
df_of_test_mses = pd.DataFrame(columns=["linear", "quadratic", "sqrt"])

for fold in range(k):
    x_train = np.concatenate([x_folds[i] for i in range(k) if i != fold])
    y_train = np.concatenate([y_folds[i] for i in range(k) if i != fold])
    train_label = "".join([f"{i+1}" for i in range(k) if i != fold])
    test_label = f"{fold+1}"
    print(train_label)
    print(test_label)
    x_test = x_folds[fold]
    y_test = y_folds[fold]

    linear_X_train = np.column_stack([np.ones(len(x_train)), x_train])
    linear_X_test = np.column_stack([np.ones(len(x_test)), x_test])
    linear_y_pred = (
        np.linalg.inv(linear_X_train.T @ linear_X_train) @ linear_X_train.T @ y_train
    )

    train_mse = np.mean((y_train - linear_X_train @ linear_y_pred) ** 2)
    test_mse = np.mean((y_test - linear_X_test @ linear_y_pred) ** 2)
    df_of_train_mses.loc[train_label, "linear"] = train_mse
    df_of_test_mses.loc[test_label, "linear"] = test_mse

    quadratic_X_train = np.column_stack([linear_X_train, x_train**2])
    quadratic_X_test = np.column_stack([linear_X_test, x_test**2])
    quadratic_y_pred = (
        np.linalg.inv(quadratic_X_train.T @ quadratic_X_train)
        @ quadratic_X_train.T
        @ y_train
    )

    train_mse = np.mean((y_train - quadratic_X_train @ quadratic_y_pred) ** 2)
    test_mse = np.mean((y_test - quadratic_X_test @ quadratic_y_pred) ** 2)
    df_of_train_mses.loc[train_label, "quadratic"] = train_mse
    df_of_test_mses.loc[test_label, "quadratic"] = test_mse

    sqrt_X_train = np.column_stack([linear_X_train, np.sqrt(x_train)])
    sqrt_X_test = np.column_stack([linear_X_test, np.sqrt(x_test)])
    sqrt_y_pred = (
        np.linalg.inv(sqrt_X_train.T @ sqrt_X_train) @ sqrt_X_train.T @ y_train
    )

    train_mse = np.mean((y_train - sqrt_X_train @ sqrt_y_pred) ** 2)
    test_mse = np.mean((y_test - sqrt_X_test @ sqrt_y_pred) ** 2)
    df_of_train_mses.loc[train_label, "sqrt"] = train_mse
    df_of_test_mses.loc[test_label, "sqrt"] = test_mse


df_of_train_mses.loc["average"] = df_of_train_mses.mean()
df_of_test_mses.loc["average"] = df_of_test_mses.mean()

df_of_mses = pd.concat([df_of_train_mses, df_of_test_mses], keys=["train", "test"])

print(df_of_mses)
df_of_mses.to_clipboard(excel=True)


train_avg_mses = df_of_train_mses.loc["average"]
test_avg_mses = df_of_test_mses.loc["average"]

plt.plot(train_avg_mses, label="train")
plt.plot(test_avg_mses, label="test")
plt.legend()
# save plot
plt.savefig("train_test_mse.png")
plt.show()


sqrt_X_train = np.column_stack([np.ones(len(x)), x, np.sqrt(x)])
sqrt_y_pred = np.linalg.inv(sqrt_X_train.T @ sqrt_X_train) @ sqrt_X_train.T @ y
mse = np.mean((y - sqrt_X_train @ sqrt_y_pred) ** 2)
print(f"mse: {mse}")
y_intercept = sqrt_y_pred[0]
x_coefficient = sqrt_y_pred[1]
sqrt_x_coefficient = sqrt_y_pred[2]

print(y_intercept, x_coefficient, sqrt_x_coefficient)


# for degree in range(1, 5):
#     x_col = df.columns[0]
#     y_col = df.columns[1]
#     x = df[x_col].values
#     y = df[y_col].values
#     # split into folds
#     k = 5
#     x_folds = np.array_split(x, k)
#     print(x_folds)
#     y_folds = np.array_split(y, k)
#     mse_table_of_folds = []
#     print(f"degree {degree}")

#     mse_sum = 0

#     for fold in range(k):
#         x_train = np.concatenate([x_folds[i] for i in range(k) if i != fold])
#         y_train = np.concatenate([y_folds[i] for i in range(k) if i != fold])
#         x_test = x_folds[fold]
#         y_test = y_folds[fold]

#         degrees = [x_train**i for i in range(degree + 1)]
#         X = np.column_stack(degrees)
#         degrees_test = [x_test**i for i in range(degree + 1)]
#         X_test = np.column_stack(degrees_test)

#         y_pred = np.linalg.inv(X.T @ X) @ X.T @ y_train

#         graph_x = np.linspace(x.min(), x.max(), 100)
#         graph_X = np.column_stack([graph_x**i for i in range(degree + 1)])
#         graph_y = graph_X @ y_pred

#         train_mse = np.mean((y_train - X @ y_pred) ** 2)
#         test_mse = np.mean((y_test - X_test @ y_pred) ** 2)
#         coefficients = ", ".join([f"{y_pred[i]:.2f}x^{i}" for i in range(len(y_pred))])
#         mse_sum += test_mse + train_mse

#         print(
#             f"\tfold {fold + 1}\n\t\ttest mse: {test_mse:.2f}\n\t\ttrain mse: {train_mse:.2f}\n\t\tcoefficients: {coefficients}"
#         )

#         # predict the next few values

#         next_x = np.array([x.max() + i for i in range(4, 13, 4)])
#         next_degrees = [next_x**i for i in range(degree + 1)]
#         next_X = np.column_stack(next_degrees)
#         next_y = next_X @ y_pred
#         print(f"\t\tnext values: {next_y}")

#         # graph
#         if SHOULD_GRAPH:
#             plt.scatter(x_train, y_train)
#             plt.scatter(x_folds[fold], y_folds[fold], color="red")
#             plt.plot(graph_x, graph_y, color="purple")
#             plt.show()

#         # store mse
#         mse_table_of_folds.append(test_mse)

#     print(f"\taverage mse: {mse_sum / (k*2)}")

#     mse_table_of_degrees_and_folds.append(mse_table_of_folds)

# print mse table as df with labels
