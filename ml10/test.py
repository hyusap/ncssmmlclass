import pandas as pd
from pathlib import Path
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model(Path(__file__).parent / "model.h5")

# Load the sample data to predict
df_new = pd.read_csv(Path(__file__).parent / "sample_data_to_predict.csv")
X_new = df_new.values

# Make predictions
predictions = model.predict(X_new)

# Threshold predictions for binary classification
binary_predictions = (predictions > 0.5).astype(int)

# Print the predictions
print("Predictions:")
print(binary_predictions)
