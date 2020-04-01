from gensim import models, corpora
from gensim.utils import simple_preprocess
from smart_open import smart_open
import os
import numpy as np

# Create the Dictionary and Corpus
mydict = corpora.Dictionary([simple_preprocess(line) for line in documents])
corpus = [mydict.doc2bow(simple_preprocess(line)) for line in documents]

# Show the Word Weights in Corpus
for doc in corpus:
    print([[mydict[id], freq] for id, freq in doc])

    # Create the TF-IDF model
    tfidf = models.TfidfModel(corpus, smartirs='ntc')

    # Show the TF-IDF weights
    for doc in tfidf[corpus]:
        print([[mydict[id], np.around(freq, decimals=2)] for id, freq in doc])
