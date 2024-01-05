from sklearn.metrics.pairwise import cosine_similarity
import pandas
from sentence_transformers import SentenceTransformer


def similarity(pair, model):
    embeddings = model.encode(pair)
    sim = cosine_similarity([embeddings[0]], [embeddings[1]])
    return sim[0][0]

def get_similarity_list(pairs, model):
    ret = []
    for pair in pairs:
        ret.append(similarity(pair, model))
    return ret

def append_model_statistic_to_dfs(model, colname):
    for y in range(1993, 2025):
        df = pandas.read_pickle(f'{y}.pkl')
        pairs = zip(df.Clue, df.Answer)
        sims = get_similarity_list(pairs, model)
        df.insert(len(df.axes[1]), colname, sims)
        df.to_pickle(f'{y}.pkl')
        
bertmodel = SentenceTransformer('all-MiniLM-L12-v2')

append_model_statistic_to_dfs(bertmodel, 'Sentence Similarity')