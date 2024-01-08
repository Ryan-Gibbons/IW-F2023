import csv
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

model = SentenceTransformer('bert-base-nli-mean-tokens')

# all using sentencetransformer
wordplay = []
wordplay_similarity = []
nonwordplay = []
nonwordplay_similarity = []

with open('../Data/separated_test/wordplay.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['source'].find("?") != -1: 
            wordplay.append((row['source'], row['target']))
        else:
            nonwordplay.append((row['source'], row['target']))

for pair in wordplay:
    embeddings = model.encode(pair)
    similarity = cosine_similarity([embeddings[0]], [embeddings[1]])
    wordplay_similarity.append(similarity[0][0])

for pair in nonwordplay:
    embeddings = model.encode(pair)
    similarity = cosine_similarity([embeddings[0]], [embeddings[1]])
    nonwordplay_similarity.append(similarity[0][0])

# desperately need to refactor
meaning = []
meaning_similarity = []
with open('../Data/separated_test/wordmeaning.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        meaning.append((row['source'], row['target']))

for pair in meaning:
    embeddings = model.encode(pair)
    similarity = cosine_similarity([embeddings[0]], [embeddings[1]])
    meaning_similarity.append(similarity[0][0])

print("***********************************")
print("PART I: SENTENCE SIMILARITY MEASURE")
print("***********************************")

print("================")
print("[?] MARKED WORDPLAY SIMILARITY")
print("================")
for entry in zip(wordplay, wordplay_similarity):
    print(entry)

print("================")
print("UNMARKED WORDPLAY SIMILARITY")
print("================")
for entry in zip(nonwordplay, nonwordplay_similarity):
    print(entry)

print("================")
print("NONWORDPLAY SIMILARITY STATISTICS")
print("================")
for entry in zip(meaning, meaning_similarity):
    print(entry)



print("================")
print("[?] MARKED WORDPLAY SIMILARITY STATISTICS")
print("================")

wordplay_summary = pd.Series(wordplay_similarity)
print(wordplay_summary.describe())

print("================")
print("UNMARKED WORDPLAY SIMILARITY STATISTICS")
print("================")

nonwordplay_summary = pd.Series(nonwordplay_similarity)
print(nonwordplay_summary.describe())


print("================")
print("MEANING SIMILARITY STATISTICS")
print("================")

meaning_summary = pd.Series(meaning_similarity)
print(meaning_summary.describe())


