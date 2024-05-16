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

operations = ["-", "+"]
variables = [ "x", "y", "z"]
coefficients = [ str(x + 1) for x in range(25) ]
solutions = [ str(x + 1) for x in range(10) ]
bases = [ "e", "10", "2", "4", "7" ]
exponents = [ "2", "3", "4", "5", "6", "7" ]
fractions = [ "(1/2)", "(1/3)", "(1/4)", "(1/5)" ]

# FUNCTIONS

## 1: algebraic symbol randomization functions

def operation():
    ''' returns a random operation string from the choices "+" or "-".
    '''
    return random.choice(operations)


def coefficient():
    ''' returns a random numeric string between "1" and "25".
    '''
    return random.choice(coefficients)

def solution(): 
    ''' returns a random numeric string between "1" and "10"
    '''
    return random.choice(solutions)

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
    ''' returns the argument that is passed in. 
        if nothing is passed in, a random variable is returned.
    '''
    return variable() if var is None else var

def scalar_expression(var = None, function = identity):
    ''' returns a scalar expression: a * f(x)
    '''
    func = function(var)
    
    a = coefficient()

    return f"{a}*{func}"

def product_expression(var = None, function_1 = identity, function_2 = identity):
    ''' returns a product of two expressions
    '''
    
    func_1 = function_1(var)
    func_2 = function_2(var)

    return f"({func_1})*({func_2})"

def quotient_expression(var = None, function_1 = identity, function_2 = identity):
    ''' returns the quotient of two expressions
    '''

    func_1 = function_1(var)
    func_2 = function_2(var)

    return f"(({func_1})/({func_2}))"

def square_root_expression(var = None, function = identity):
    ''' returns a square root expression string
    '''

    func = function(var)

    return f"sqrt({func})"


def power_expression(var = None, function = identity):
    ''' returns an exponential expression string
    '''
    
    func = function(var)

    exp = exponent()

    return f"({func}^{exp})"


def log_expression(var = None, function = identity):
    ''' returns a log expression string
    '''

    func = function(var)
    
    b = base()
    
    return f"log_{b}({func})"

def linear_expression(var = None, function = identity):
    ''' returns a linear expression string, a * f(x) + b
    '''

    func = function(var)

    a = coefficient()
    b = coefficient()
    op = operation()

    return f"{a} * {func} {op} {b}"


def quadratic_expression(var = None, function = identity):
    ''' returns a quadratic expression string: a * f(x) ^ 2 + b * f(x) + c
    '''

    func = function(var)

    quad_term = f"{func}^2"
    linear_term = linear_expression(func)
    op = operation()

    return f"{quad_term} {op} {linear_term}"

## 3: algebraic equation function
   
def equation(expression = identity):
    ''' pass in an algebraic expression (function) and set it equal to a number!
    '''

    return expression() + " = " + solution()

# THE EXAM

if __name__ == "__main__":
    # The script entrypoint. This is where everything starts!

    print("THE FINAL EXAM \n\n")
    print("Part 1: Simplify the following expressions. \n \n")

    ## PART 1: SIMPLICATION
    q1 = product_expression(
        var = identity(), 
        function_1 = power_expression, 
        function_2 = power_expression
    )
    q2 = product_expression(
        var = identity(), 
        function_1 = lambda y: power_expression(y, function = scalar_expression), 
        function_2 = linear_expression
    )
    q3  = quotient_expression(
        var = identity(),
        function_1 = power_expression,
        function_2 = power_expression
    )
    q4 = power_expression(
        var = identity(),
        function = power_expression
    )
    
    print("\t 1. " + q1 + " \n")
    print("\t 2. " + q2 + " \n")
    print("\t 3. " + q3 + " \n")
    print("\t 4. " + q4 + " \n")

    print("\t TODO: do this part! \n \n") 
    
    print("Part 2: Solve the following equations using any method you choose. \n \n")

    ## PART 2: SOLUTION

    # NOTE: a function is being passed into a function here, i.e. f(g(x)) or *composition*.
    #       Notice the inner function isn't suffixed with "()", so it is not called.
    #       Instead, the "name" of the function is being passed into the "equation" function.
    q1 = equation(quadratic_expression)
    # NOTE: using an anoynmous "lambda function" to override default argument in the inner
    #       function. This is like a triple composition! f(g(h(x)))! Oh my!
    q2 = equation(lambda: square_root_expression(function = linear_expression))
    q3 = equation(lambda: log_expression(function = power_expression))
    q4 = equation(lambda: log_expression(function=quadratic_expression))

    print("\t 1. "  + q1 + "\n" )
    print("\t 2. " + q2 + "\n")
    print("\t 3. " + q3 + "\n")
    print("\t 4. " + q4 + "\n")

