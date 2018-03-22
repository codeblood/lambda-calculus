# natural numbers (Church encoding)
ZERO  = lambda f: lambda x: x
ONE   = lambda f: lambda x: f(x)
TWO   = lambda f: lambda x: f(f(x))
THREE = lambda f: lambda x: f(f(f(x)))
FOUR  = lambda f: lambda x: f(f(f(f(x))))
FIVE  = lambda f: lambda x: f(f(f(f(f(x)))))

# "isomorphism" with python (positive) int

# takes a natural number as defined above and converts it into a Python int
def lambda_to_int(l):
    return l(lambda x: x + 1)(0)

# takes a Python int and converts it into a natural number as defined above
def int_to_lambda(i):
    """ the condition below was added so that the following equations always hold:
        n == int_to_lambda(lambda_to_int(n)) where n is a natural number as above
        i == lambda_to_int(int_to_lambda(i)) where i is a Python int
    """
    if i < 0 or type(i) == float: raise Exception("undefined for negative integers and floating points")

    if i == 0: return ZERO
    else: return lambda f: lambda x: int_to_lambda(i - 1)(f)(f(x))

# takes a natural number and returns its successor
SUCC = lambda n: lambda f: lambda x: n(f)(f(x))

# takes a natural number and returns its predecessor and fixes "ZERO"
import common
PRED = lambda n: (lambda f: lambda x: n(common.COMPOSE(f))(common.FLIP(ZERO)(x))(common.ID))

# some testing cases for natural numbers

# Checks if the "isomorphism" consisting of the two functions above work on randomly generated numbers
def test_isomorphism():
    import random

    while True:
        n = random.randint(0,500)
        assert n == lambda_to_int(int_to_lambda(n))

        if n == 500:
            break

# Checks if the "SUCC" function corresponds to adding one to a random Python int
def test_successor():
    import random

    while True:
        n = random.randint(0,500)
        assert n + 1 == lambda_to_int(SUCC(int_to_lambda(n)))
        if n == 500:
            break

# Checks if the "PRED" function corresponds to subtracting one to a random Python int or fixes 0
def test_predecessor():
    import random

    while True:
        n = random.randint(0,500)
        if n == 0:
            assert n == lambda_to_int(ZERO)
        else:
            assert n - 1 == lambda_to_int(PRED(int_to_lambda(n)))
        if n == 500:
            break
