import os
import math
from collections import defaultdict

def tokenize(text):
    return text.lower().split()

def build_index(doc_dir):
    index = defaultdict(list)
    doc_lengths = {}
    for filename in os.listdir(doc_dir):
        with open(os.path.join(doc_dir, filename), 'r') as file:
            text = file.read()
            tokens = tokenize(text)
            doc_id = filename
            doc_lengths[doc_id] = len(tokens)
            for token in set(tokens):
                index[token].append(doc_id)
    return index, doc_lengths

def save_index(index, filename='index.txt'):
    with open(filename, 'w') as f:
        for term, doc_ids in index.items():
            f.write(f'{term}: {" ".join(doc_ids)}\n')

def load_index(filename='index.txt'):
    index = defaultdict(list)
    with open(filename, 'r') as f:
        for line in f:
            term, doc_ids = line.strip().split(': ')
            index[term] = doc_ids.split()
    return index
