from corpuset import CorpuSet
import numpy
from collections import defaultdict


class LdaBase(CorpuSet):
    '''
    base of lda
    docs ~ [0,self.M] m
    wrods ~ [0,self.V] w
    topic ~ [0,self.k] k/topic
    words in docs ~ [0, docs.size()) n
    '''

    def __init__(self):
        CorpuSet.__init__(self)
        '''
        dir_path: file path, save data 
        model_name: model name , read train results
        current_iter: iter times
        iters_num: overall times of gibbs iter
        topic_num: number of topic(self.K)
        K: number of topic
        twords_num: number of words related to topic after training or interence
        '''
        self.dir_path = ""
        self.model_name = ""
        self.current_iter = 0
        self.iters_num = 0
        self.topic_num = 0
        self.K = 0
        self.twords_num = 0

        '''
        hyperparameter
      '''
        self.alpha = numpy.zeros(self.K)
        self.beta = numpy.zeros(self.V)

        '''
        all the topic info of word  M*docs.size()
        '''
        self.Z = []

        '''
        statistic count
        nd:save kth topic in mth docs creates words, M*K
        ndsum:save overall words of mth docs M*1
        nw:save wth words number of kth topic K*V
        nwsum:save overall words from kth topic K*1
        '''
        self.nd = numpy.zeros((self.M, self.K))
        self.ndsum = numpy.zeros((self.M, 1))
        self.nw = numpy.zeros((self.K, self.V))
        self.nwsum = numpy.zeros((self.K, 1))

        '''
        distribution var
        theta: doc-topic M*K
        phi: topic-word K*V
        '''
        self.theta = numpy.zeros((self.M, self.K))
        self.phi = numpy.zeros((self.K, self.V))

        self.sum_alpha = 0.0
        self.sum_beta = 0.0

        self.prior_word = defaultdict(list)
        self.train_model = None

        return

    '''
    some functions
    '''

    def init_statistics_document(self):
        assert self.M > 0 and self.K > 0 and self.Z

        self.nd=numpy.zeros((self.M,self.M), dtype=numpy.int)
        self.ndsum=numpy.zeros((self.M,1),dtype=numpy.int)

        
