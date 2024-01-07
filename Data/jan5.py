from sklearn.metrics.pairwise import cosine_similarity
import pandas
# from sentence_transformers import SentenceTransformer
# import gensim.downloader as api
# import string

# used three similarity measures
# 1. sentence similarity
# 2. mean word similarity
# 3. max individual word similarity

def similarity(pair, model):
    # stripped into individual words, removing punctuation
    p0 = pair[0].lower().translate(str.maketrans('', '', string.punctuation))
    p1 = pair[1].lower()
    # embeddings = model.similarity(pair[0], pair[1])
    # sim = cosine_similarity([embeddings[0]], [embeddings[1]])
    ret0 = 0
    ret1 = 0
    try: 
        ret0 = model.n_similarity(p0.split(), p1)
    except:
        pass
    try: 
        ret1 = max([model.similarity(x, p1) for x in p0.split()])
    except:
        pass
    return (ret0, ret1)

def get_similarity_list(pairs, model):
    sets = []
    maxwords = []
    for pair in pairs:
        res = similarity(pair, model)
        sets.append(res[0])
        maxwords.append(res[1])
    return (sets, maxwords)

def append_model_statistic_to_dfs(model, colname):
    for y in range(1993, 2025):
        df = pandas.read_pickle(f'{y}.pkl')
        df.drop("Mean Word Similarity", axis=1, inplace=True)
        df.drop("Max Ind. Word Similarity", axis=1, inplace=True)
        pairs = zip(df.Clue, df.Answer)
        sims = get_similarity_list(pairs, model)
        df.insert(len(df.axes[1]), "Mean Word Similarity", sims[0])
        df.insert(len(df.axes[1]), "Max Ind. Word Similarity", sims[1])
        print(y)
        print(df)
        df.to_pickle(f'{y}.pkl')
        
        
# bertmodel = SentenceTransformer('all-MiniLM-L12-v2')

# info = api.info()
# model = api.load("glove-wiki-gigaword-100")

# append_model_statistic_to_dfs(model, 'Average Word Similarity')
        

# COMPILED DATA FROM YEARS INTO WEEKDAYS 
        

# dfs = [pandas.DataFrame(columns=['Clue','Answer','Sentence Similarity', 'Mean Word Similarity', 'Max Ind. Word Similarity']) for _ in range(7)] 
# data = [[] for _ in range(7)]

# for y in range(1993, 2025):
#     df = pandas.read_pickle(f'{y}.pkl')
#     for index, row in df.iterrows():
#         day = row["Weekday"]
#         data[day].append([row['Clue'], row["Answer"], row["Sentence Similarity"], row['Mean Word Similarity'], row['Max Ind. Word Similarity']])


# for i in range(len(data)):
#     df = pandas.DataFrame(data[i], columns=['Clue', "Answer", "Sentence Similarity", "Mean Word Similarity", "Max Ind. Word Similarity"])
#     print(df)
#     df.to_pickle(f'weekday{i}.pkl')
        

# STRIPPED DATA TO THOSE WITH LEGIBLE WORD EMBEDDINGS
# for i in range(7):
#     df = pandas.read_pickle(f'weekday{i}.pkl')
#     df = df.drop(df[df['Max Ind. Word Similarity'] == 0.0].index)
#     print(df.describe())
#     df.to_pickle(f'weekday{i}stripped.pkl')
    

# STRIPPED DATA TO THOSE WITH QUESTION MARKS
# for i in range(7):
#     df = pandas.read_pickle(f'weekday{i}stripped.pkl')
#     df = df[df['Answer'].str.contains("?")]
#     print(df.describe())
#     df.to_pickle(f'weekday{i}question.pkl')
    

# COMPILED DATA ACROSS WEEKDAYS TO COMPARE 
weekdays = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 
            4: "Friday", 5: "Saturday", 6: "Sunday"}

data = []

for i in range(7):
    df = pandas.read_pickle(f'weekday{i}stripped.pkl')
    data.append([weekdays[i], df["Sentence Similarity"].mean(), df["Sentence Similarity"].std(),
                 df["Mean Word Similarity"].mean(), df["Mean Word Similarity"].std(),
                 df["Max Ind. Word Similarity"].mean(), df["Max Ind. Word Similarity"].std()])
    
summary = pandas.DataFrame(data, columns=['Weekday', 'Sentence Similarity', 'ssstd', 'Mean Word Similarity', 
                                    'mwsstd', 'Max Ind. Word Similarity', 'miwsstd'])
print(summary)
summary.to_pickle('summarydata.pkl')