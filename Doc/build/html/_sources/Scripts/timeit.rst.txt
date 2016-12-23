=================
Scripts/timeit.py
=================

Timeit è uno script che potrebbe tornarci utile quando vogliamo misurare il tempo di esecuzione di una o più funzioni.
Personalmente lo uso spesso per confrontare due o più metodi che restituiscono la stessa cosa per vedere quale è
il più performante.

NB Lo script, così com'è, è valido solo per **Python 2.7**, non sarà tuttavia impegnativo modificarlo per farlo girare
sulle vesioni successive.

Il codice consiste nel creare un decoratore che stampi il tempo di esecuzione della funzione decorata:
::
    def timeit(method):

        def timed(*args, **kw):
            ts = time.time()
            result = method(*args, **kw)
            te = time.time()

            print '%r (%r, %r) %2.6f sec' % \
                  (method.__name__, args, kw, te-ts)
            return result

        return timed

Molto semplice, in ts (time start) salviamo il tempo nell'istante prima di chiamare il metodo,
poi, una volta eseguito il metodo, salviamo in te (time end) il nuovo tempo. A questo punto stamperemo le informazioni
che ci servono, vale a dire:

* nome del metodo decorato
* argomenti passati
* keywords
* **tempo di esecuzione** (te-ti)

Per i giovani pythonisti
------------------------
Se non sapete cosa sono i decoratori, RTFM (Read the fucking manual). A parte gli scherzi, un decoratore è semplicemente
una funzione che prende come argomento un'altra funzione, in modo da poterne modificare il comportamento. Il decoratore,
una volta modificata la funzione passatagli, ritornerà quella funzione. Quindi attenzione, ripeto, normalmente
il return del decoratore ritornerà la funzione (non il risultato della funzione!).

Nel caso di timeit, il discorso è diverso. Il decoratore in realtà è un wrapper attorno alla funzione passatagli come
argomento. A result, infatti, stiamo assegnando il risultato della funzione method, questo per permetterci di
aggiungere codice in più a una funzione.
La domanda ora sarà, perchè ho fatto questo invece di aggiungere tre righe di codice nella funzione che voglio
misurare? Semplice, se voglio misurare il tempo di esecuzione di molte funzioni mi basterà applicare il decoratore invece
di riscrivere ogni volta il codice in più, come da esempio:
::
    @timeit
    def prova1():
        a = [x for x in range(1000)]


    @timeit
    def prova2():
        a = [x for x in xrange(1000)]

Il risultato sarà il seguente:
::
    $ python timeit.py
    'prova1' ((), {}) 0.000101 sec
    'prova2' ((), {}) 0.000051 sec