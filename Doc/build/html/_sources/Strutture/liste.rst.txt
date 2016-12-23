=====
Liste
=====

Nested List Comprehension
=========================
Partiamo subito da esempi. Abbiamo due liste fatte così:
::
	lista1 = [x for x in xrange(10)]
	lista2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

Mettiamo il caso che vorremmo una lista di tuple fatta in questo modo

[(0, 'a'), (0, 'b'), ..., (1, 'a'), (1, 'b'), ... , (9, j)]

per ottenerla scriveremo semplicemente:
::
	[(x,y) for x in list1 for y in list2]

What the f**?
In pratica stiamo facendo questo:

* Creiamo una lista, i cui elementi saranno tuple di due valori (x, y)
* Cicliamo lista1
* per ogni valore che troviamo in lista1 (x) cicliamo tutti gli elementi di lista2
* ogni volta che troviamo un nuovo valore in lista2 (y) creiamo una tupla con i valori (x, y)
* aggiungiamo alla lista finale questa tupla appena costruita


