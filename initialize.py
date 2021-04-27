import numpy as np
from process import *

'''
prior var
alpha:
dirichlet distribution's hyperparameter to process the topic distribution theta
beta:
dirichlet distribution's hyperparameter to process the words distribution phi
iternum: max iter times
Z: save the topic
K: topic amount
N: docs amount
M: length of words
ndz: words amount in i th doc from topic z 
nzw: word w's amount from z th topic 
nz: words amount from z th topic
'''
alpha = 5
beta = 0.1
iternum = 500
Z = []
K = 3
N = len(docs)
M = len(word2id)
ndz = np.zeros([N, K]) + alpha
nzw = np.zeros([K, M]) + beta
nz = np.zeros([K]) + M * beta


def randominit():
    for d, doc in enumerate(docs):
        currentdoc = []
        for w in doc:

            '''
            calculate topic probability of word
            '''
            pz = np.divide(np.multiply(ndz[d, :], nzw[:, w]), nz)
            '''
            sampling from the topic distribution
            '''
            pz /= pz.sum()
            z = np.random.multinomial(1, pz).argmax()
            currentdoc.append(z)
            ndz[d, z] += 1
            nzw[z, w] += 1
            nz[z] += 1
        Z.append(currentdoc)
