from dict import *
import logging

'''
this file is a basic set of docs group
'''


class CorpuSet(object):
    def __init__(self):
        '''
        initialization
        parameters about words
        local_bidict: a dict of id(key) & words(value)
        words_count: number of words(before remove duplicates)
        V: number of words(after remove duplicates)
        '''
        self.local_bidict = Bidict()
        self.words_count = 0
        self.V = 0

        '''
        parameters about docs
        docids_list: a list of docs'id
        docs_word_id: all id about words in docs(docs_count * doc.length())
        M: number of docs
        '''
        self.docids_list = []
        self.docs_words_id = []
        self.M = 0

        '''
        var for inference
        global_bidict: global dict of id(key)&words(value)
        local_2_global: a dict to save connection of local dict to global dict
        '''
        self.global_bidict = None
        self.local_2_global = {}

        return

    def init_corpus_with_file(self, file_name):
        '''
        initial corpus data. form:id[tab]word1 word2...etc
        '''
        with open(file_name, "r", encoding="utf-8") as file_iter:
            self.init_corpus_with_docs(file_iter)
        return

    def init_corpus_with_docs(self, docs_list):
        '''
        initial corpus by docs list. form:id[tab]doc1 doc2...etc
        '''
        # clear words data
        self.local_bidict.clear()
        self.words_count = 0
        self.V = 0

        # clear docs data
        self.docs_words_id.clear()
        self.docids_list.clear()
        self.M = 0

        self.local_2_global.clear()

        # load do data
        for line in docs_list:
            frags = line.strip().split()
            if len(frags) < 2:
                continue

            # get id of docs
            doc_id = frags[0].strip()

            # get id of word
            doc_wordid_list = []
            for word in [w.strip() for w in frags[1:] if w.strip()]:
                local_id = self.local_bidict.get_key(word) if self.local_bidict.contins_value(word) else len(self.local_bidict)

                if self.global_bidict is None:
                    # updata id info
                    self.local_bidict.add_key_value(local_id, word)
                    doc_wordid_list.append(local_id)
                else:
                    if self.global_bidict.continues_value(word):
                        self.local_bidict.add_key_value(local_id, word)
                        doc_wordid_list.append(local_id)
                        self.local_2_global[local_id] = self.global_bidict.get_key(word)

            if len(doc_wordid_list) > 0:
                self.words_count += len(doc_wordid_list)
                self.docids_list.append(doc_id)
                self.docs_words_id.append(doc_wordid_list)
        self.V = len(self.local_bidict)
        logging.debug("words number:" + str(self.V) + ",", str(self.words_count))
        self.docs_count = len(self.docids_list)
        logging.debug("docs number:" + str(self.docs_count))

        return

    def save_wordmap(self, file_name):
        '''
        save word dict from self.local_bidict
        '''
        with open(file_name, "w", encoding="utf-8") as f_save:
            f_save.write(str(self.local_bidict))
        return

    def load_wordmap(self, file_name):
        self.local_bidict.clear()
        with open(file_name, "r", encoding="utf-8") as f_load:
            for _id, _word in [line.strip().split() for line in f_load if line.strip()]:
                self.local_bidict.add_key_value(int(_id), _word.strip())
        self.V = len(self.local_bidict)
        return

