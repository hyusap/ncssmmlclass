import pandas as pd
from pathlib import Path


df = pd.read_csv(Path(__file__).parent / "banknote_data.csv")

train_set = df.sample(frac=0.8, random_state=7)
test_set = df.drop(train_set.index)

train_set.to_csv(Path(__file__).parent / "banknote_train.csv", index=False)
test_set.to_csv(Path(__file__).parent / "banknote_test.csv", index=False)
