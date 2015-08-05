"""Script per misurare o confrontare il tempo di esecuzione di una o piu' funzioni

Applicare il decoratore @timeit alla funzione di cui si vuole misurare il tempo di esecuzione,
poi chiamarla/e nel metodo main
"""
import time


def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print '%r (%r, %r) %2.6f sec' % \
              (method.__name__, args, kw, te-ts)
        return result

    return timed


@timeit
def prova1():
    a = [x for x in range(1000)]


@timeit
def prova2():
    a = [x for x in xrange(1000)]


def main():
    prova1()
    prova2()

if __name__ == '__main__':
    main()
