from initialize import *
import time


def gibbssampling():
    for d, doc in enumerate(docs):
        for i, w in enumerate(doc):
            z = Z[d][i]  # load the i th word's topic in d th doc

            '''
            related statistic counts minus 1
            '''
            ndz[d, z] -= 1
            nzw[z, w] -= 1
            nz[z] -= 1

            '''
            re-calculate topic probability of current word
            '''
            pz = np.divide(np.multiply(ndz[d, :], nzw[:, w]), nz)

            '''
            sampling from the calculated distribution
            '''
            pz /= pz.sum()
            z = np.random.multinomial(1, pz).argmax()
            Z[d][i] = z

            '''
            related statistic counts plus 1
            '''
            ndz[d, z] += 1
            nzw[z, w] += 1
            nz[z] += 1


def perplexity():
    nd = np.sum(ndz, 1)
    n = 0
    ll = 0.0
    for d, doc in enumerate(docs):
        for w in doc:
            ll += np.log(((nzw[:, w] / nz) * (ndz[d, :] / nd[d])).sum())
            n = n + 1
    return np.exp(ll / (-n))


def run():
    for i in range(iternum):
        gibbssampling()
        print(time.strftime('%X'), "Iteration: ", i, " Completed", " Perplexity: ", perplexity())
