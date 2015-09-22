__author__ = 'alessandrocucci'

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