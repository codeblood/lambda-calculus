from common import ID

# control structures

# if_then_else command
# This definition of the "IF" command is equivalent to setting "IF = boolean.TRUE"
IF    = lambda cond: lambda true_case: lambda false_case: cond(true_case)(false_case)(ID)

# omega combinator (infinite loop)
OMEGA = lambda f: f(f)
