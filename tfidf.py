from collections import defaultdict
import math

def compute_tf(doc_tokens):
    tf = defaultdict(int)
    for token in doc_tokens:
        tf[token] += 1
    return tf

def compute_idf(index, total_docs):
    idf = {}
    for term, doc_ids in index.items():
        idf[term] = math.log(total_docs / len(doc_ids))
    return idf

def compute_tfidf(doc_tokens, index, total_docs):
    tf = compute_tf(doc_tokens)
    idf = compute_idf(index, total_docs)
    tfidf = {}
    for term in doc_tokens:
        tfidf[term] = tf[term] * idf.get(term, 0)
    return tfidf
