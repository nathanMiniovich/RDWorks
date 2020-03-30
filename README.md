# RDWorks

Quick demo for RDWorks interview for consulting gig at Denso

### Environment Setup

This demo was built on Windows. In order to reproduce the environment used please install the latest version of Python and perform the following commands (if you are running Windows 10+
I suggest you use WSL and your preferred package manager):


You will then need to install gensim for python since that is what we will be using for our word2vec implementation.
The gensim install for Windows is a bit tricky since it depends on SciPy, which requires a version of Numpy linked with the Intel Math Kernel Library (MKL) for optimal performance.
I have provided prebuilt wheels for numpy on both 32 and 64-bit Windows linked with MKL [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy).

After you have secured your numpy wheel file please perform the following pip installs:

```
pip install -U smart_open
pip install build/(32 or 64-bit wheel file).whl
pip install -U gensim
```

You are now ready to run word2vec.py!
