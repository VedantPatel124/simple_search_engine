from flask import Flask, request, render_template
import os
from indexing import build_index, load_index, tokenize
from tfidf import compute_tfidf
from collections import defaultdict

app = Flask(__name__)
doc_dir = 'documents'
total_docs = len(os.listdir(doc_dir))
index, doc_lengths = build_index(doc_dir)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    query_tokens = tokenize(query)
    query_tfidf = compute_tfidf(query_tokens, index, total_docs)

    scores = defaultdict(float)
    for term, weight in query_tfidf.items():
        for doc_id in index.get(term, []):
            scores[doc_id] += weight

    ranked_docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return render_template('results.html', query=query, results=ranked_docs)

if __name__ == '__main__':
    app.run(debug=True)
