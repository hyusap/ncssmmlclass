from pathlib import Path
import pickle


path = Path(__file__).parent
stop_words = []
with open((path / "StopWords.txt").resolve()) as f:
    for line in f:
        for word in line.strip().split():
            stop_words.append(word)
print(stop_words)


# df = pd.read_csv((path / "SpamTrain.txt").resolve(), sep=" ")
# print(df)
# df["Subject"] = df["Subject"].apply(
#     lambda x: " ".join([word for word in x.split() if word not in stop_words])
# )
# print(df)

# df.to_csv("filtered.csv", index=False)
with open((path / "SpamTrain.txt").resolve()) as f:
    data = []
    for line in f:
        spam, subject = line.split(" ", 1)
        cleaned_subject = " ".join(
            [word for word in subject.split() if word not in stop_words]
        )
        data.append([int(spam), cleaned_subject])

word_counts = {}

for spam, subject in data:
    for word in set([word.lower() for word in subject.split()]):
        if word in word_counts:
            word_counts[word][0 if spam else 1] += 1
        else:
            word_counts[word] = [1, 0] if spam else [0, 1]

spam_count = sum([spam for spam, _ in data])
regular_count = len(data) - spam_count

for word, counts in word_counts.items():
    counts[0] /= spam_count
    counts[1] /= regular_count

print(word_counts)

pickle.dump(
    {
        "word_counts": word_counts,
        "spam_count": spam_count,
        "regular_count": regular_count,
        "stop_words": stop_words,
    },
    open((path / "data.pkl").resolve(), "wb"),
)
