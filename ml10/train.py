from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import pandas as pd
from sklearn.model_selection import train_test_split
from pathlib import Path

# Load dataset from CSV file
df = pd.read_csv(Path(__file__).parent / "sample_dataset.csv")

X = df[["feature1", "feature2"]].values
y = df["target"].values
# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# Define the architecture of the neural network
model = Sequential(
    [
        Dense(
            4, activation="relu", input_shape=(2,)
        ),  # Hidden layer with 4 neurons and ReLU activation
        Dense(
            1, activation="sigmoid"
        ),  # Output layer with 1 neuron and sigmoid activation for binary classification
    ]
)
# Compile the model
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))
# Evaluate the model on test data
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Loss: {loss:.4f}")
print(f"Test Accuracy: {accuracy:.4f}")
# Assuming "model" is your trained neural network model
model.save(Path(__file__).parent / "model.h5")
