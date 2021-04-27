from process import *
from initialize import *
from gibbs_sampling import *
import numpy as np

'''
pre-process data
'''
docs, word2id, id2word = preprocessing("data.txt")
randominit()
run()

'''
output results
'''
topicwords = []
for z in range(0, K):
    ids = nzw[z, :].argsort()
    topicword = []
    for j in ids:
        topicword.insert(0, id2word[j])
    topicwords.append(topicword[0: min(10, len(topicword))])
for i in range(3):
    print("topic:",i,"    ",topicwords[i][:][:])
