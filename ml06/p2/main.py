import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd

nltk.download("punkt")
nltk.download("stopwords")

stop_words = set(stopwords.words("english"))
print(stop_words)


def remove_stop_words(sentence):
    return " ".join(
        [word for word in word_tokenize(sentence) if word.lower() not in stop_words]
    )


df = pd.read_csv("EmailSubjects.csv")
print(df)
filtered = df["Subject"].apply(remove_stop_words)
print(filtered)
filtered.to_csv("filtered.csv", index=False)
