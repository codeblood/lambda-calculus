# identity function
ID = lambda x: x

# function composition
COMPOSE = lambda x: lambda f: lambda g: g(f(x))

# flips a binary function's parameters
FLIP = lambda f: lambda x: lambda y: f(y)(x)
