===================
Python Antipatterns
===================

Prima di mandare del codice in review, controllate sempre questa pagina, contiene una lista dei più comuni Python
antipatterns, con consigli su come evitarli.

Leggibilità
===========
Usare enumerate nei loops
-------------------------
Questo esempio che segue fa semplicemente schifo:
::
    l = [1,2,3]

    for indice in xrange(0,len(l)):
        elemento = l[indice]
        print indice, elemento

se abbiamo bisogno dell'indice, usiamo enumerate:
::
    for indice, elemento in enumerate(l):
        print indice, elemento


Chiedere il permesso prima di fare qualcosa
-------------------------------------------
Mai chiedere il permesso prima di fare qualcosa, roba tipo questa va evitata:
::
    if qualcosa:
        fai_qualcosa_con(qualcosa)


Molto meglio fare così:
::
    try:
        fai_qualcosa_con(qualcosa)
    except NameError:
        raise NameError("qualcosa non esiste")


Questo approccio è conosciuto nella comunità Python come EAFP coding style (easier to ask for forgiveness than permission).
Nel primo caso, se "qualcosa" non esiste, il programma continuerà normalmente, probabilmente rompendosi più avanti;
nel secondo caso, invece, capiremo meglio perchè il programma si è bloccato.


Formattare stringhe a partire da un dizionario
----------------------------------------------
Una volta capito questo Antipattern, sarà molto più semplice scrivere codice che potremmo estendere in futuro.
Prendiamo ad esempio un dizionario fatto così:
::
    persona = {
        'nome': 'Alessandro',
        'cognome': 'Cucci',
        'email': 'alessandro.cucci@energee3.com'
    }

se io volessi, a partire da questo dizionario, formattare una stringa del tipo

"Ciao, mi chiamo x e la mia email è z"

potrei sicuramente fare una cosa del tipo:
::
    print "Ciao, mi chiamo {0} e la mia mail è {1}".format(
                                                    persona['nome'],
                                                    persona['email'])

Mettiamo caso che fra un mese volessi modificare la stringa in modo che stampi:

"Ciao, mi chiamo x y e la mia mail è z"

Dovrei modificare la print di prima con
::
    print "Ciao, mi chiamo {0} {1} e la mia mail è {2}".format(
                                                    persona['nome'],
                                                    persona['cognome'],
                                                    persona['email'])

Qual'è il problema di questo approccio? Abbiamo dovuto cambiare i campi nella stringa, e aggiungere un valore a format.
Sarebbe stato molto meglio fin da principio formattare la stringa come segue:
::
    print "Ciao, mi chiamo {nome} {cognome} e la mia mail è {email}".format(**persona)

questo approccio ha numerosi vantaggi, non dobbiamo sbatterci a cercare a cosa corrispondono i numeri (è più leggibile),
e se dovremmo in futuro aggiungere valori, basterà semplicemente aggiungere la chiave del dizionario tra graffe.


For su un dizionario
--------------------
Prendiamo un dizionario di esempio:
::
    diz = {'uno': 1, 'due': 2, 'tre': 3}

per iterare su di esso mai fare così:
::
    for chiave in diz:
        print "{}: {}".format(chiave, diz[chiave])

è molto più leggibile (nonchè performante) scrivere invece:
::
    for chiave, valore in diz.iteritems():
        print "{}: {}".format(chiave, valore)


Usare le named tuples quando una funzione restituisce più di un valore
----------------------------------------------------------------------
Quando abbiamo una funzione che restituisce più di un valore, dovrebbe subito illuminarsi una lampadina che dice "Usa le
named tuples!!!". Ecco cosa succede altrimenti:
::
    def get_name():
        return "Alessandro", "Cucci", "Developer"

    name = get_name()

    print name[0], name[1], name[2]

se get_name si trovasse in un file diverso dal print, leggendo il codice diremmo "0, 1 e 2 cosa sono??"
Proviamo invece a usare un metodo diverso:
::
    from collections import namedtuple

    def get_name():
        name = namedtuple("name", ["first", "last", "role"])
        return name("Alessandro", "Cucci", "Developer")

    name = get_name()

    print name.first, name.last, name.role

Molto, molto meglio!