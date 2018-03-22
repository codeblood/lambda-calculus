#boolean values

# by convention TRUE "chooses the leftmost" and FALSE "chooses the rightmost"
TRUE  = lambda x: lambda y: x
FALSE = lambda x: lambda y: y


# "AND" logical operator takes two booleans "l" and "r". If "l" is "FALSE" then it chooses itself, otherwise it chooses "r"
AND   = lambda l: lambda r: l(r)(l)

# "OR" logical operator takes two booleans "l" and "r". If "l" is "TRUE" then it chooses itself, otherwise it chooses "r"
OR    = lambda l: lambda r: l(l)(r)

# "NOT" logical operator takes a boolean and reverses the "choosing" relation
# The parenthesis were added to make it explicit that "NOT" takes a boolean and returns another boolean (the one inside the parenthesis)
NOT   = lambda b: (lambda x: lambda y: b(y)(x))

# "isomorphism" with python bool

# Takes a boolean as defined above and converts it into a Python bool
def lambda_to_boolean(l):
    return l(True)(False)

# Takes a Python bool and converts it into a boolean as defined above
def boolean_to_lambda(b):
    if b: return TRUE
    else: return FALSE

# pretty printing
def boolean_to_str(b):
    return str(lambda_to_bool(b))

# some testing cases for booleans

def test_AND_truth_table():
    # testing AND
    (a,b) = (True, True)
    assert (a and b) == lambda_to_boolean(AND(boolean_to_lambda(a))(boolean_to_lambda(b)))
    (a,b) = (True, False)
    assert (a and b) == lambda_to_boolean(AND(boolean_to_lambda(a))(boolean_to_lambda(b)))
    (a,b) = (False, True)
    assert (a and b) == lambda_to_boolean(AND(boolean_to_lambda(a))(boolean_to_lambda(b)))
    (a,b) = (False, False)
    assert (a and b) == lambda_to_boolean(AND(boolean_to_lambda(a))(boolean_to_lambda(b)))

def test_OR_truth_table():
    # testing OR
    (a,b) = (True, True)
    assert (a or b) == lambda_to_boolean(OR(boolean_to_lambda(a))(boolean_to_lambda(b)))
    (a,b) = (True, False)
    assert (a or b) == lambda_to_boolean(OR(boolean_to_lambda(a))(boolean_to_lambda(b)))
    (a,b) = (False, True)
    assert (a or b) == lambda_to_boolean(OR(boolean_to_lambda(a))(boolean_to_lambda(b)))
    (a,b) = (False, False)
    assert (a or b) == lambda_to_boolean(OR(boolean_to_lambda(a))(boolean_to_lambda(b)))

def test_NOT_truth_table()
    # testing NOT
    a = True
    assert (not a) == lambda_to_boolean(NOT(boolean_to_lambda(a)))
    a = False
    assert (not a) == lambda_to_boolean(NOT(boolean_to_lambda(a)))
