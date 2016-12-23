=====
PEP 8
=====
La community ci ha lasciato un documento che ogni programmatore Python dovrebbe conoscere a memoria: la PEP8.
Acronimo di Python Enhancement Proposal, la numero 8 si riferisce in particolare alla guida di stile nella scrittura
di codice Python. Un codice, una volta scritto, testato e rilasciato, verrà letto molte volte, e riscritto molte meno.
Quindi, rendere il codice più leggibile possibile deve diventare prioritario. Qui riassumeremo le regole principali
definite nella PEP8, se volete (dovete) conoscerle tutte, questo è il link al `documento originale`_.

.. _documento originale: https://www.python.org/dev/peps/pep-0008/

Indentazione
============

.. code-block:: python

    # Si
    foo = long_function_name(var_one, var_two,
                             var_three, var_four)


    # No
    def long_function_name(
        var_one, var_two, var_three,
        var_four):
        print(var_one)

    # Si
    my_dict = {
        'keyA': 'A',
        'B': 'C',
        'long_key_that_looks_odd': "Don't add extra spaces",
        'please_end_with': "a comma",
    }

    my_list = [
        1, 2, 3,
        4, 5, 6,
    ]

    result = some_function_that_takes_arguments(
        'a', 'b', 'c',
        'd', 'e', 'f',
    )

Il metodo preferito di spezzare linee troppo lunghe è usare le parentesi. Le espressioni troppo lunghe possono essere
racchiuse in parentesi. Andare a capo dopo l'operatore, non prima.

.. code-block:: python

    class Rectangle(Blob):

    def __init__(self, width, height,
                 color='black', emphasis=None, highlight=0):
        if (width == 0 and height == 0 and
            color == 'red' and emphasis == 'strong' or
            highlight > 100):
            raise ValueError("sorry, you lose")
        if width == 0 and height == 0 and (color == 'red' or
                                           emphasis is None):
            raise ValueError("I don't think so -- values are %s, %s" %
                             (width, height))
        Blob.__init__(self, width, height,
                      color, emphasis, highlight)

Imports
=======

* Sempre in cima al file
* raggruppati così (divisi con una riga vuota):
    * Standard lib
    * Librerie proprie e/o di terzi
    * Applicazione corrente
* NON USARE import-star (from module import *)
* salvo casi estremi non usare proprio il rename (import something as something_else)

.. code-block:: python

    # Yes:
    import os
    import sys
    from subprocess import Popen, PIPE

    # No:
    import sys, os
    from datetime import *
    from myclass import MyClass as myclass_myclass
    from foo.bar.yourclass import YourClass as Bar_YourClass


Whitespaces
===========

.. code-block:: python

    # Appena entro le parentesi:
    spam( ham[ 1 ], { eggs: 2 } ) # No
    spam(ham[1], {eggs: 2}) # Yes

    # Appena prima di virgole o due punti
    if x == 4 : print x , y # No
    if x == 4: print x, y # Yes

    # Appena prima delle parentesi nell'invocazione di una funzione:
    spam (1) # No
    spam(1) # Yes

    # Appena prima delle quadre (chiavi o indici)
    dict ['key'] = list [index] # No
    dict['key'] = list[index] # Yes

    # Spazi di troppo solo per allineare colonne
    # No:
    x         = 1
    y         = 2
    long_name = 3
    # Yes:
    x = 1
    y = 2
    long_name = 3

    # Spazi in meno solo per sottolineare la precedenza degli operatori:
    hypot2 = x*2 - 1 # No
    hypot2 = x * 2 - 1 # Yes

    # Niente spazi attorno ad "=" negli argomenti di una funzione:
    # No
    def complex(real, imag = 0.0):
        return magic(r = real, i = imag)
    # Yes
    def complex(real, imag=0.0):
        return magic(r=real, i=imag)


Operazioni per riga
===================

UNA (1)

.. code-block:: python

    # NO NO NO NO NO
    if foo == 'blah': do_blah_thing()
    x = 1; y = 2
    try: something()
    finally: cleanup()
    if foo == 'bar': one(); two(); three()

Commenti
========
Frasi di senso compiuto.

Meglio niente commenti che commenti sbagliati rispetto al codice.

Usare pochi commenti in linea (alla destra della operazione), distanziarli di almeno due spazi rispetto al codice.

Non descrivere cosa fa il codice, ma perché lo fa:

.. code-block:: python

    x = x + 1  # Aggiungo 1
    # Un commento cosi non aiuta. Meglio scrivere:
    x = x + 1  # Pixel di compensazione per il bordo

Naming Conventions
==================

.. code-block:: python

    # parole separate da underscore
    variabili_comuni = 42
    COSTANTI = 'bar'
    GLOBALI = 'foo'

    def mio_metodo(arg1, nome_lungo=None):
        pass

    # Camel Case solo per i nomi di classe
    class CamelCase(object):
        pass

    # In caso di sigle, tutte maiuscole:
    class HTMLView(object):
        pass

    # In caso di nomi che vanno in conflitto con nomi riservati per Python,
    # cercare di cambiare nome. In caso di assoluta necessita', usare un
    # trailing underscore:
    modulo.metodo('bagigio', class_="MiaClasse")

    # NO
    miaVariabile = 42
    MiaVariabile2 = 6
    def FunzioneMetodo():
        pass
    def Funzione_Metodo():
        pass

Altre Raccomandazioni
=====================

.. code-block:: python

    # test coi singleton: usare is
    if var is None:
        pass

    # Fare test lineari, preferire sempre il test "positivo"
    if not confirm(LABELS.CONFIRM_TO_NOT_CONTINUE) is not True:  # NO
        print "Eh..?"

    # Le sequenze vuote e i dizionari vuoti fanno false:
    for t in ('', [], (), {}):
        if t:
            raise Exception("Not possible!")
    # Inutile calcolarne la lunghezza:
    for t in ('', [], ()):
        if len(t):  # NO
            raise Exception("No use for checking len()")


    # Controllo di tipo:
    # NO:
    if type(smt) is type(1):
        pass
    # Yes:
    if isinstance(smt, int):
        pass


    # Eccezioni, try/except:
    # Definire sempre un errore che derivi da Exception oppure da una classe di errore
    # specifica del framework/progetto
    class MyError(ApplicationError):
        pass

    # Generalmente, limitare il codice dentro al blocco try al minimo necessario.
    try:
        do_something(float(n))  # NO: il try si deve riferire a do_something oppure a float
    except ValueError:
        # Restringere sempre il genere di eccezioni intercettate
        raise MyError(LABELS.ERROR)


    # Scorrendo una sequenza di sequenze, esplicitare cosa c'e' in ciascun elemento:
    for item in items:
        crea_ordine(item[0], item[1])  # NO: non so cosa item[0] e item[1] contengono.

    for modello, numero_capi in items:
        crea_ordine(modello, numero_capi)  # Yes
