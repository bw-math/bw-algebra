# this is a line comment! it doesn't affect the code! 
# it just helps the reader understand what's going on!
# line comments are typically reserved for quick explanations!
''' this is a block comment! it doesn't affect the code! 
take note! i don't have to prefix every line with the triple comma!
a block comment exists until you close the triple comma!
block comments are typically reserved for function headings and 
module descriptions! they are meant to be higher level and occupy
more space!
'''

import random 

# CONSTANTS

signs = ["-", "+"]
variables = [ "x", "y", "z"]
coefficients = [ str(x + 1) for x in range(25) ]
bases = [ "e", "10", "2", "4", "7" ]
exponents = [ "2", "3", "4", "5", "6", "7" ]
fractions = [ "1/2", "1/3", "1/4", "1/5" ]

# FUNCTIONS

## 1: algebraic symbol randomization functions

def sign():
    ''' returns a random sign string from the choices "+" or "-".
    '''
    return random.choice(signs)


def coefficient():
    ''' returns a random numeric string between "1" and "25".
    '''
    return random.choice(coefficients)


def variable():
    ''' returns a random variable string from the choices "x", "y", "z".
    '''
    return random.choice(variables)


def base():
    ''' returns a random base string from the choices "e", "10", "2", "4" and "7".
    ''' 
    return random.choice(bases)


def exponent():
    ''' return a random exponent string from the choices "2", "3", "4", "5"
    '''
    return random.choice(exponents)


def fraction():
    ''' return a random fraction string from the choices "1/2", "1/3", "1/4", "1/5"
    '''
    return random.choice(fractions)


## 2: algebraic expression functions

def identity(var = None):
    return variable() if var is None else var

def linear_expression(var = None, function = identity):
    ''' returns a linear expression string, a * f(x) + b
    '''

    # apply function to variable
    func = function(var)

    a = coefficient()
    b = coefficient()
    op = sign()

    return f"{a} * {func} {op} {b}"


def square_root_expression(var = None, function = identity):
    ''' returns a square root expression string
    '''

    # apply function to variable
    func = function(var)

    return f"sqrt({func})"


def power_expression(var = None, function = identity):
    ''' returns an exponential expression string
    '''
    
    # apply function to variable
    func = function(var)

    exp = exponent()

    return f"{func}^{exp}"


def log_expression(var = None, function = identity):
    ''' returns a log expression string
    '''

    func = function(var)
    
    b = base()
    
    return f"log_{b}({func})"
     
def quadratic_expression(var = None, function = identity):
    ''' returns a quadratic expression string: a * f(x) ^ 2 + b * f(x) + c
    '''

    # apply function to variable
    func = function(var)

    # generate quadratic in func
    quad_term = f"{func}^2"
    linear_term = linear_expression(func)
    op = sign()

    return f"{quad_term} {op} {linear_term}"

## 3: algebraic equation function
   
def equation(expression = identity):
    ''' pass in an algebraic expression (function) and set it equal to a number!
    '''

    return expression() + " = " + coefficient()

# THE EXAM

if __name__ == "__main__":
    # The script entrypoint. This is where everything starts!

    # Create the questions
    # NOTE: a function is being passed into a function here, i.e. f(g(x)) or *composition*.
    #       Notice the inner function isn't suffixed with "()", so it is not called.
    #       Instead, the "name" of the function is being passed into the "equation" function.
    q1 = equation(quadratic_expression)
    # NOTE: using an anoynmous "lambda function" to override default argument in the inner
    #       function. This is like a triple composition! f(g(h(x)))! Oh my!
    q2 = equation(lambda: square_root_expression(function = linear_expression))
    q3 = equation(lambda: log_expression(function = power_expression))
    q4 = equation(lambda: log_expression(function=quadratic_expression))

    print("THE FINAL EXAM \n\n")

    print("Part 1: Simplify the following expressions. \n \n")

    print("\t TODO: do this part! \n \n") 

    print("Part 2: Solve the following equations using any method you choose. \n \n")

    print("\t 1. "  + q1 + "\n" )

    print("\t 2. " + q2 + "\n")

    print("\t 3. " + q3 + "\n")

    print("\t 4. " + q4 + "\n")

