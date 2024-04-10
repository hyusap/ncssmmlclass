import pandas as pd

mine = pd.read_csv("../p1/filtered.csv")
theirs = pd.read_csv("../p2/filtered.csv")


mine["NLTK"] = theirs["Subject"]
mine["Match"] = mine["Subject"] == mine["NLTK"]
print(mine)

mine.to_csv("comparison.csv", index=False)
