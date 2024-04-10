import pandas as pd
from pathlib import Path


df = pd.read_csv((Path(__file__).parent / "../p1/filtered.csv").resolve())

print(df.head())

counts = {}
for index, row in df.iterrows():
    is_spam = row["Spam"] == 1
    print(row["Subject"], is_spam)
    for word in set([word.lower() for word in row["Subject"].split()]):
        if word in counts:
            counts[word][0 if is_spam else 1] += 1
        else:
            counts[word] = [1, 0] if is_spam else [0, 1]
print(counts)


spam_count = sum(df["Spam"] == 1)


df = pd.DataFrame.from_dict(counts, orient="index", columns=["Spam", "Not_Spam"])
df["Spam Percentage"] = (df["Spam"] + 1) / (spam_count + 2)
df["Not Spam Percentage"] = (df["Not_Spam"] + 1) / (spam_count + 2)
print(df)
