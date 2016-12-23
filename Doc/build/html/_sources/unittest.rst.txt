============
Unit Testing
============

Testare il codice è molto importante. Abituatevi a scrivere codice di test ogni volta che scrivete qualcosa di nuovo.
Spesso, scrivendo nuove funzionalità, siamo impegnati a pensare (come sviluppatori) troppo sull'algoritmo migliore
da utilizzare trascurando il punto di vista dell'utente.

I test sono anche il posto ideale per uno sviluppatore per imparare come funziona un software. Rappresentano l'insieme dei
casi d'uso principali per cui è stato scritto un determinato programma. Leggerli, quindi, ci aiuterà a capire
immediatamente come usare tale software, il che è molto più sbrigativo che cercare di analizzarne il codice.

Se dovrete scrivere software che verrà mantenuto da diverse persone, scrivete tanti test. Coloro che successivamente
prenderanno in consegna il vostro codice vi ringrazieranno.

Un pò di regole generali per scrivere test
==========================================
- Una testing unit dovrebbe focalizzarsi su una sola funzionalità e provare che sia corretta.
- ogni unit test deve essere completamente indipendente. Ognuno deve poter essere eseguito da solo,	indipendentemente dall'ordine in cui viene chiamato in una test suite.
- impegnati a scrivere test che vengono eseguiti rapidamente. Un test dovrebbe terminare l'esecuzione in pochi millisecondi.
- Studia e impara a scrivere ed eseguite test singoli. Quando sviluppi una nuova funzione per il tuo programma,	scrivi un test ed eseguilo spesso, dovrebbe venirti automatico dopo un pò.
- Sarebbe utile eseguire tutti i test prima di committare del codice in un repository condiviso.
- Se sei nel mezzo dello sviluppo di un codice, e devi fare una pausa, scrivi un test che si rompa sulla funzionalità che stavi per scrivere. Quando tornerai, saprai con certezza su cosa stavi lavorando.
- Scrivi nomi lunghi e descrittivi, nonchè estremamente dettagliati, per i metodi dei test.

Il modulo *unittest*
====================

In Python, il modulo *unittest* fa praticamente quello che JUnit fa per Java. Offre una classe base (TestCase) che ha
un insieme di metodi per verificare l'output di una chiamata a una funzione.
Attenzione, per far eseguire un test il nome del metodo deve iniziare per *test_* (es. test_faiqualcosacon).

Facciamo un esempio. Per creare un test che verifichi una funzione di somma tra due numeri scriveremo:
::

	import unittest

	def somma(x, y):
		return x + y

	class MyTest(unittest.TestCase):

		def test_somma_tra_due_interi(self):
			self.assertEqual(somma(3, 3), 6)

		def test_prova_una_condizione_vera(self):
			self.assertTrue('FOO'.isupper())

		def test_prova_una_condizione_falsa(self):
			self.assertFalse('foo'.isupper())

		def test_prova_eccezzione(self):
			with self.assertRaises(TypeError):
				somma(1, "ciao")

	if __name__ == '__main__':
			suite = unittest.TestLoader().loadTestsFromTestCase(MyTest)
			unittest.TextTestRunner(verbosity=2).run(suite)

il risultato sarà:
::
	test_prova_eccezzione (__main__.MyTest) ... ok
	test_prova_una_condizione_falsa (__main__.MyTest) ... ok
	test_prova_una_condizione_vera (__main__.MyTest) ... ok
	test_somma_tra_due_interi (__main__.MyTest) ... ok

	----------------------------------------------------------------------
	Ran 4 tests in 0.001s

	OK

Reference
=========

- I metodi di base che potranno servirci scrivendo test sono:

+--------------------------+--------------------------------+
|       Metodo             |            Controlla che...    |
+==========================+================================+
| assertEqual(a, b)        | a == b                         |
+--------------------------+--------------------------------+
| assertNotEqual(a, b)     | a != b                         |
+--------------------------+--------------------------------+
| assertTrue(x)            | bool(x) is True                |
+--------------------------+--------------------------------+
| assertFalse(x)           | bool(x) is False               |
+--------------------------+--------------------------------+
| assertIs(a, b)           | a is b                         |
+--------------------------+--------------------------------+
| assertIsNot(a, b)        | a is not b                     |
+--------------------------+--------------------------------+
| assertIsNone(x)          | x is None                      |
+--------------------------+--------------------------------+
| assertIsNotNone(x)       | x is not None                  |
+--------------------------+--------------------------------+
| assertIn(a, b)           | a in b                         |
+--------------------------+--------------------------------+
| assertNotIn(a, b)        | a not in b                     |
+--------------------------+--------------------------------+
| assertIsInstance(a, b)   | isinstance(a, b)               |
+--------------------------+--------------------------------+
| assertNotIsInstance(a, b)| not isinstance(a, b)           |
+--------------------------+--------------------------------+

- per le eccezioni utilizzeremo invece:

+-----------------------------------------+--------------------------------+
|       Metodo                            |            Controlla che...    |
+=========================================+================================+
| assertRaises(exc, fun, *args, **kwds)   | fun(*args, **kwds) sollevi exc |
+-----------------------------------------+--------------------------------+

- metodi per verificare cose più specifiche:

+-----------------------------------------+--------------------------------+
|       Metodo                            |            Controlla che...    |
+=========================================+================================+
| assertAlmostEqual(a, b)                 | round(a-b, 7) == 0             |
+-----------------------------------------+--------------------------------+
| assertNotAlmostEqual(a, b)              | round(a-b, 7) != 0             |
+-----------------------------------------+--------------------------------+
| assertGreater(a, b)                     | a > b                          |
+-----------------------------------------+--------------------------------+
| assertGreaterEqual(a, b)                | a >= b                         |
+-----------------------------------------+--------------------------------+
| assertLess(a, b)                        | a < b                          |
+-----------------------------------------+--------------------------------+
| assertLessEqual(a, b)                   | a <= b                         |
+-----------------------------------------+--------------------------------+
| assertDictContainsSubset(a, b)          | tutte le coppie chiave/valore  |
|                                         | di a esistano anche in b       |
+-----------------------------------------+--------------------------------+
| assertItemsEqual(a, b)                  | sorted(a) == sorted(b)         |
+-----------------------------------------+--------------------------------+
