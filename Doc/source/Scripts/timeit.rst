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
Se non sapete cosa sono i decoratori, RTFM (Read the fucking manual)