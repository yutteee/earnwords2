import pandas as pd

df = pd.read_csv("OriginalWordSimilarityDataset/score_noun.csv")
feature_selection = ['word1', 'word2', 'mean']

dataset = df[feature_selection]
print(dataset)