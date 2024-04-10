import pickle
from pathlib import Path
import pandas as pd
import math


path = Path(__file__).parent

data = pickle.load(open((path / "data.pkl").resolve(), "rb"))
word_counts = data["word_counts"]
spam_count = data["spam_count"]
regular_count = data["regular_count"]
stop_words = data["stop_words"]

with open((path / "SpamTrain.txt").resolve()) as f:
    test_data = []
    for line in f:
        spam, subject = line.split(" ", 1)
        cleaned_subject = " ".join(
            [word for word in subject.split() if word not in stop_words]
        )
        test_data.append([int(spam), cleaned_subject])

print(test_data)

p_spam = spam_count / (spam_count + regular_count)
p_regular = regular_count / (spam_count + regular_count)
k = 1

tp = 0
tn = 0
fp = 0
fn = 0

for spam, subject in test_data:
    p_sl_spam = math.log(p_spam)
    p_sl_regular = math.log(p_regular)
    for word in subject.split():
        if word in word_counts:
            # Apply Laplace smoothing to individual word probabilities
            p_word_given_spam = (word_counts[word][0] + k) / (spam_count + 2 * k)
            p_word_given_regular = (word_counts[word][1] + k) / (regular_count + 2 * k)
        else:
            # If the word is not in the training set, use a default probability
            p_word_given_spam = k / (spam_count + 2 * k)
            p_word_given_regular = k / (regular_count + 2 * k)

        p_sl_spam += math.log(p_word_given_spam)
        p_sl_regular += math.log(p_word_given_regular)

    # Calculate the final probability
    p_spam_sl = math.exp(p_sl_spam) / (math.exp(p_sl_spam) + math.exp(p_sl_regular))
    print(subject, p_spam_sl)

    if p_spam_sl > 0.5:
        if spam:
            tp += 1
        else:
            fp += 1
    else:
        if spam:
            fn += 1
        else:
            tn += 1

print(tp, tn, fp, fn)
print("Accuracy:", (tp + tn) / (tp + tn + fp + fn))
print("Precision:", tp / (tp + fp))
print("Recall:", tp / (tp + fn))
print("F1 Score:", (2 * tp) / (2 * tp + fp + fn))
