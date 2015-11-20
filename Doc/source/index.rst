.. Energee3 Python Tools documentation master file, created by
   Alessandro Cucci on Wed Aug  5 13:05:07 2015.

Energee3 Python Tools
=====================
.. image:: /img/cropped-header21.png
    :align: center

*Energee3 Python Tools* è un repository git creato per avere un insieme di strumenti (script, esempi e documentazione)
di codice Python che possano tornarci utili nello sviluppo di codice in sede e/o presso clienti.

Abbiamo voluto questo strumento in seguito a delle review di codice che doveva sottostare a rigorosi criteri di
performance e stile, e lo scopo è fornire una piattaforma di consulting per tutti i colleghi Energee che si trovano
(o si troveranno in futuro) a scrivere programmi in linguaggio Python.

Indice della Documentazione
---------------------------
vai all':doc:`contents`

.. toctree::
   :maxdepth: 2

   about
   todo
   copyright


   Scripts/index
   CodeStyle/index
   Strutture/index
   unittest

Struttura del repository
------------------------
Energy3 Python Tools è composto da due macro sezioni:

* **Scripts:**
    collezione di script python che possono essere usati in contemporanea allo sviluppo di software presso
    i clienti. Esempio: Timeit.py, il primo script che abbiamo creato, confronta il tempo di esecuzione di due funzioni
    che ritornano la stessa cosa con metodi diversi. Lo scopo era quello di scegliere un costrutto o un algoritmo piuttosto
    che un altro per fornire al cliente il codice più performante possibile.

* **Doc:**
    è la parte più corposa, contiene tutorial, esempi, guide per scrivere codice leggibile, checklist da usare
    prima di dare codice in pasto alle review, trucchetti imparati sul campo e molto altro. Tutta la documentazione, inclusa
    questa pagina, è scritta in codice rst, un linguaggio utilizzato dai Core Developers di Python per generare facilmente
    della documentazione a partire dal codice.

Versione
--------
0.0.7

Licenza
-------
Copyright (c) 2015 Energee3 srl

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.


What's New in 0.0.7
-------------------

+--------------------------+---------------------------------------------------------------+
|        File              |                       Descrizione                             |
+==========================+===============================================================+
| GoogleDriveApi           | Script per leggere un file csv da Google Drive e              |
|                          | parsarne il contenuto                                         |
+--------------------------+---------------------------------------------------------------+
| scriptbaruffa.py         | Script per generare un file html contenente un libro di       |
|                          | flylib.                                                       |
+--------------------------+---------------------------------------------------------------+
| line_count.py            | Script per contare numero di file e numero di righe di codice |
|                          | in un progetto.                                               |
+--------------------------+---------------------------------------------------------------+
| read_replace.py          | Script per printare, copiare o sostituire file a chunks       |
+--------------------------+---------------------------------------------------------------+
| :doc:`unittest`          | Esempio di utilizzo di unittest                               |
+--------------------------+---------------------------------------------------------------+