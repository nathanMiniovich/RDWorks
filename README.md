# RDWorks

Quick demo for RDWorks interview for consulting gig at Denso

### Environment Setup

This demo was built on Windows. In order to reproduce the environment used please install the latest version of Python for Windows (if you are running Windows 10+
I suggest you use WSL and your preferred package manager).


You will then need to install gensim for python since that is what we will be using for our word2vec implementation.
The gensim install for Windows is a bit tricky since it depends on SciPy, which requires a version of Numpy linked with the Intel Math Kernel Library (MKL) for optimal performance.
You can find prebuilt wheel files for numpy linked with MKL on both 32 and 64-bit Windows [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy).

After you have secured your numpy wheel file please perform the following pip installs:

```
pip install -U smart_open
pip install build/(32 or 64-bit wheel file).whl
pip install -U gensim
```

Aside from gensim (which should have implicitly installed scipy) we will also need sklearn and pandas, so please also run the following:

```
pip install -U sklearn
pip install -U pandas
```

Since we will be tokenizing Japanese text we will also need a Japanese text tokenizer. Japanese writing does not include spaces so writing one ourselves is quite a challenge.
This time around we will be leveraging MeCab to help us, you can download the unofficial 64-bit version of MeCab [here](https://github.com/ikegami-yukino/mecab/releases).
NOTE: The official version of MeCab only supports 32-bit

After you have installed MeCab please run the following installs:

```
pip install ipykernel
pip install mecab
```

We will be using a special colloquial japanese mecab dictionary from mecab-ipadic-neologd. Getting this for windows is a bit of a pain and requires a custom compilation so I will provide
my file in the repo once I have git-lfs up and running.
If you would like to compile your own you can find a guide [here](https://qiita.com/zincjp/items/c61c441426b9482b5a48) (text in Japanese).

### The Model

We will be using Japanese Wikipedia tokenized using mecab with a neologd dictionary as a source to train our Word2Vec model. To be more specific the source is
[https://dumps.wikimedia.org/jawiki/latest/jawiki-latest-pages-articles.xml.bz2](https://dumps.wikimedia.org/jawiki/latest/jawiki-latest-pages-articles.xml.bz2)

At the time of writing I do not recommend using wget.download() in python to retrieve this file as it is quite large and wget.download() cannot yet resume a download in the event of failure.
Either run wget on the commandline or use something else from urllib. 

I might add more detail about the scraping and tokenization process later, but for now I will just provide the model file. Feel free to spend a few hours figuring out how to recreate
them yourself ;)
NOTE: Only the main model file is small enough to be uploaded to github, will upload the others later using git-lfs. The other model files are also necessary to load the model.

You are now ready to run k_means_clustering.py!

### The Script

We will be performing k_means_clustering on the Word2Vec model in order to create clusters of related words. You can read more about it [here](https://en.wikipedia.org/wiki/K-means_clustering)

At the moment the script is fairly barebones and takes no arguments, you can just run it with:

```
python k_means_clustering.py
```

Clustering on the word vectors will take some time so just be patient and let it run. It should produce "jawiki_kmeans.csv" as output.
