import pandas as pd

df = pd.read_csv("OriginalWordSimilarityDataset/score_noun.csv")
feature_selection = ['word1', 'word2', 'mean']

dataset = df[feature_selection]

# word1, word2の文字数が同じ行を削除
word1Length = dataset['word1'].str.len()
word2Length = dataset['word2'].str.len()
dataset = dataset[word1Length != word2Length]

# 1列目が文字数の小さい方、2列目が文字数の大きい方にする
smallWord1LengthData = dataset[word1Length < word2Length]
bigWord1LengthData = dataset[word1Length > word2Length]
bigWord1LengthData = bigWord1LengthData[['word2', 'word1', 'mean']]
bigWord1LengthData = pd.DataFrame(data=bigWord1LengthData.values, columns=feature_selection)
dataset = pd.concat([smallWord1LengthData, bigWord1LengthData], axis=0)