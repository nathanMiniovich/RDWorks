from gensim.models import Word2Vec
from sklearn.cluster import KMeans;
from sklearn.neighbors import KDTree;

import pandas as pd
import numpy as np

def get_top_words(index2word, k, centers, wordvecs):
    tree = KDTree(wordvecs)

    #Closest points for each Cluster center is used to query the closest 20 points to it.
    closest_points = [tree.query(np.reshape(x, (1, -1)), k=k) for x in centers]
    closest_words_idxs = [x[1] for x in closest_points]

    #Word Index is queried for each position in the above array, and added to a Dictionary.
    closest_words = {}
    for i in range(0, len(closest_words_idxs)):
        closest_words['Cluster #' + str(i)] = [index2word[j] for j in closest_words_idxs[i][0]]

    #A DataFrame is generated from the dictionary.
    df = pd.DataFrame(closest_words)
    df.index = df.index+1

    return df

def clustering_on_wordvecs(word_vectors, num_clusters):
    # Initalize a k-means object and use it to extract centroids
    kmeans_clustering = KMeans(n_clusters = num_clusters, init='k-means++')
    idx = kmeans_clustering.fit_predict(word_vectors)

    return kmeans_clustering.cluster_centers_, idx

def main():
    print("Loading model...")

    model = Word2Vec.load("model\ja-gensim.50d.data.model")
    vectors = model.wv.vectors

    print("Model loaded.")

    print("Clustering on wordvecs...")
    centers, clusters = clustering_on_wordvecs(vectors, 50);

    print("Getting top words in each cluster...")
    top_words = get_top_words(model.wv.index2word, 5000, centers, vectors)

    top_words.to_csv("jawiki_kmeans.csv", encoding="utf-8")

    return

if __name__ == "__main__":
    main()
