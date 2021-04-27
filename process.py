import re
import jieba
import codecs


def preprocessing():
    # load stopword
    file = codecs.open('stopwords.dic', 'r', 'utf-8')
    stopwords = [line.strip() for line in file]
    file.close()

    # load dataset
    file = codecs.open('data.txt', 'r', 'utf-8')
    documents = [document.strip() for document in file]
    file.close()

    word2id = {}
    id2word = {}
    docs = []
    currentdocument = []
    currentwordid = 0

    for document in documents:
        seglist = jieba.cut(document)
        for word in seglist:
            word = word.lower().strip()
            if len(word) > 1 and not re.search('[0-9]', word) and word not in stopwords:
                if word in word2id:
                    currentdocument.append(word2id[word])
                else:
                    currentdocument.append(currentwordid)
                    word2id[word] = currentwordid
                    id2word[currentwordid] = word
                    currentwordid += 1
        docs.append(currentdocument)
        currentdocument = []
    return docs, word2id, id2word


docs, word2id, id2word = preprocessing()
