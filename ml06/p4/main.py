import pandas as pd

df = pd.read_csv("../p1/filtered.csv")
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
