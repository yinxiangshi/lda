# Quick start

This is a simple implementation of the LDA model, using gibbs sampling.

For an overview of LDA, visit :

[LDA]: https://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf

You can easily apply this model by change some parameters.

You can put your data set in the data.txt file in the home directory.

The number of iterations iternum is in the initialize.py file, you can change the iteration times by changing iternum.(default is 500)

```python
iternum = 500
```

You can change the number of the topics before training by changing the parameter K(also in the initialize.py) Default is 3.

```python
K = 3
```

After all parameters set down, run **lda.py**, the results will printed in console .

The structure of this implementation is:

| Filename          | Action                                                       |
| ----------------- | ------------------------------------------------------------ |
| initialize.py     | Initialization parameters and model                          |
| process.py        | Processing data set input                                    |
| gibbs_sampling.py | gibbs sampling and calculation of perplexity                 |
| data.txt          | Store the data set                                           |
| stopwords.dic     | Store the keywords of data set process                       |
| lda.py            | Main file of this model,Mainly used to call other functions and print results |

