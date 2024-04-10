import pandas as pd

stop_words = []
with open("stop_words.txt") as f:
    for line in f:
        for word in line.strip().split():
            stop_words.append(word)
print(stop_words)


df = pd.read_csv("EmailSubjects.csv")
print(df)
df["Subject"] = df["Subject"].apply(
    lambda x: " ".join([word for word in x.split() if word not in stop_words])
)
print(df)

df.to_csv("filtered.csv", index=False)
