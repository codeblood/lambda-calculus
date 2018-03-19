# Cesar Barata - github.com/codeblood

# identity function
ID    = lambda x: x

# boolean values

# by convention TRUE "chooses the leftmost" and FALSE "chooses the rightmost"
TRUE  = lambda x: lambda y: x
FALSE = lambda x: lambda y: y

AND   = lambda l: lambda r: l(r)(l)
OR    = lambda l: lambda r: l(l)(r)
NOT   = lambda b: lambda x: lambda y: b(y)(x)

# "isomorphism" with python bool

def lambda_to_boolean(l):
    return l(True)(False)

def boolean_to_lambda(b):
    if b: return TRUE
    else: return FALSE

# pretty printing

def boolean_to_str(b):
    return str(lambda_to_bool(b))

# natural numbers (Church encoding)
ZERO  = lambda f: lambda x: x
ONE   = lambda f: lambda x: f(x)
TWO   = lambda f: lambda x: f(f(x))
THREE = lambda f: lambda x: f(f(f(x)))
FOUR  = lambda f: lambda x: f(f(f(f(x))))
FIVE  = lambda f: lambda x: f(f(f(f(f(x)))))

# "isomorphism" with python (positive) int
def lambda_to_int(l):
    return l(lambda x: x + 1)(0)

def int_to_lambda(i):
    if i < 0 or type(i) == float: raise Exception("undefined for negative integers and floating points")

    if i == 0: return ZERO
    else: return lambda f: lambda x: int_to_lambda(i - 1)(f)(f(x))

# control structures

# if_then_else command
IF    = lambda cond: lambda true_case: lambda false_case: cond(true_case)(false_case)(ID)    # equivalent to IF = TRUE
OMEGA = lambda f: f(f)
WHILE = lambda cond: lambda body: OMEGA(lambda n: IF(cond)(body)(cond))


# testing

# some testing cases for booleans
def test_boolean():
    # testing AND
    (a,b) = (True, True)
    assert (a and b) == lambda_to_boolean(AND(boolean_to_lambda(a))(boolean_to_lambda(b)))
    (a,b) = (True, False)
    assert (a and b) == lambda_to_boolean(AND(boolean_to_lambda(a))(boolean_to_lambda(b)))
    (a,b) = (False, True)
    assert (a and b) == lambda_to_boolean(AND(boolean_to_lambda(a))(boolean_to_lambda(b)))
    (a,b) = (False, False)
    assert (a and b) == lambda_to_boolean(AND(boolean_to_lambda(a))(boolean_to_lambda(b)))

    # testing OR
    (a,b) = (True, True)
    assert (a or b) == lambda_to_boolean(OR(boolean_to_lambda(a))(boolean_to_lambda(b)))
    (a,b) = (True, False)
    assert (a or b) == lambda_to_boolean(OR(boolean_to_lambda(a))(boolean_to_lambda(b)))
    (a,b) = (False, True)
    assert (a or b) == lambda_to_boolean(OR(boolean_to_lambda(a))(boolean_to_lambda(b)))
    (a,b) = (False, False)
    assert (a or b) == lambda_to_boolean(OR(boolean_to_lambda(a))(boolean_to_lambda(b)))

    # testing NOT
    a = True
    assert (not a) == lambda_to_boolean(NOT(boolean_to_lambda(a)))
    a = False
    assert (not a) == lambda_to_boolean(NOT(boolean_to_lambda(a)))

# some testing cases for natural numbers
def test_natural():
    import random

    while True:
        n = random.randint(0,500)
        assert n == lambda_to_int(int_to_lambda(n))

        if n == 500:
            break



test_boolean()
test_natural()
