"""Script per confrontare due dizionari
"""

__author__ = 'alessandrocucci'

a = {
   'x' : 1,
   'y' : 2,
   'z' : 3
}

b = {
   'w' : 10,
   'x' : 11,
   'y' : 2
}

try:
	print('Common keys:', a.keys() & b.keys())
	print('Keys in a not in b:', a.keys() - b.keys())
	print('(key,value) pairs in common:', a.items() & b.items())
except TypeError:
	raise TypeError("Funziona solo con Python 3")


