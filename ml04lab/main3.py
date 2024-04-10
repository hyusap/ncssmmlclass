import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


SHOULD_GRAPH = False

df = pd.read_csv("Salary data.csv")
print(df.head())


mse_table_of_degrees_and_folds = []


for degree in range(1, 4):
    x_col = df.columns[0]
    y_col = df.columns[1]
    x = df[x_col].values
    y = df[y_col].values
    # split into folds
    k = 5
    x_folds = np.array_split(x, k)
    y_folds = np.array_split(y, k)
    mse_table_of_folds = []
    print(f"degree {degree}")

    mse_sum = 0

    for fold in range(k):
        x_train = np.concatenate([x_folds[i] for i in range(k) if i != fold])
        y_train = np.concatenate([y_folds[i] for i in range(k) if i != fold])
        x_test = x_folds[fold]
        y_test = y_folds[fold]

        degrees = [x_train**i for i in range(degree + 1)]
        X = np.column_stack(degrees)
        degrees_test = [x_test**i for i in range(degree + 1)]
        X_test = np.column_stack(degrees_test)

        y_pred = np.linalg.inv(X.T @ X) @ X.T @ y_train

        graph_x = np.linspace(x.min(), x.max(), 100)
        graph_X = np.column_stack([graph_x**i for i in range(degree + 1)])
        graph_y = graph_X @ y_pred

        train_mse = np.mean((y_train - X @ y_pred) ** 2)
        test_mse = np.mean((y_test - X_test @ y_pred) ** 2)
        coefficients = ", ".join([f"{y_pred[i]:.2f}x^{i}" for i in range(len(y_pred))])
        mse_sum += test_mse + train_mse

        print(
            f"\tfold {fold + 1}\n\t\ttest mse: {test_mse:.2f}\n\t\ttrain mse: {train_mse:.2f}\n\t\tcoefficients: {coefficients}"
        )

        # predict the next few values

        next_x = np.array([x.max() + i for i in range(4, 13, 4)])
        next_degrees = [next_x**i for i in range(degree + 1)]
        next_X = np.column_stack(next_degrees)
        next_y = next_X @ y_pred
        print(f"\t\tnext values: {next_y}")

        # graph
        if SHOULD_GRAPH:
            plt.scatter(x_train, y_train)
            plt.scatter(x_folds[fold], y_folds[fold], color="red")
            plt.plot(graph_x, graph_y, color="purple")
            plt.show()

        # store mse
        mse_table_of_folds.append(test_mse)

    print(f"\taverage mse: {mse_sum / (k*2)}")

    mse_table_of_degrees_and_folds.append(mse_table_of_folds)

# print mse table as df with labels
mse_df = pd.DataFrame(mse_table_of_degrees_and_folds)
mse_df.columns = [f"fold {i}" for i in range(1, k + 1)]
mse_df.index = [f"degree {i}" for i in range(1, 4)]
print(mse_df.T)
