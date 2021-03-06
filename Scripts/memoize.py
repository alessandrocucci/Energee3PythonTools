def memoize(f):
    """ Memoization decorator for functions taking one or more arguments. """
    class memodict(dict):
        def __init__(self, f):
            self.f = f
        def __call__(self, *args):
            return self[args]
        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)

@memoize
def foo(a, b):
    return a * b

print foo(4, 2)  # 8
print foo  # {(4, 2): 8}
print foo('xo', 3)  # xoxoxo
print foo  # {(4, 2): 8, ('xo', 3): 'xoxoxo'}
