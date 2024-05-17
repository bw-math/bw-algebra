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

##############################################
# CONSTANTS
##############################################

operations = ["-", "+"]
variables = [ "x", "y", "z"]
coefficients = [ str(x + 1) for x in range(25) ]
solutions = [ str(x + 1) for x in range(10) ]
bases = [ "e", "10", "2", "4", "7" ]
exponents = [ "2", "3", "4", "5", "6", "7" ]
fractions = [ "(1/2)", "(1/3)", "(1/4)", "(1/5)" ]


##############################################
# FUNCTIONS
##############################################
## 1: symbol randomization functions
##############################################

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
    ''' return a random exponent string from the choices "2", "3", "4", "5", "6", "7"
    '''
    return random.choice(exponents)


def fraction():
    ''' return a random fraction string from the choices "1/2", "1/3", "1/4", "1/5"
    '''
    return random.choice(fractions)

##############################################
## 2: algebraic expression functions
##############################################

def identity(var = None):
    ''' returns the argument that is passed in. 
        if nothing is passed in, a random variable is returned.
    '''
    return variable() if var is None else var

##############################################
### a: one-place expressions
##############################################

def scalar_expression(var = None, function = identity, a = None):
    ''' returns a scalar expression: a * f(x)
    '''
    func = function(var)
    
    a = coefficient() if a is None else a

    return f"{a}*{func}"

def root_expression(var = None, function = identity, n = None, parenthesis = False):
    ''' returns a square root expression string
    '''

    func = function(var)

    n = exponent() if n is None else n

    res = f"{n}root({func})"

    if parenthesis:
        return f"({res})"
    return res


def power_expression(var = None, function = identity, exp = None, parenthesis = False):
    ''' returns an exponential expression string
    '''
    
    func = function(var)

    exp = exponent() if exp is None else exp

    res = f"{func}^{exp}"

    if parenthesis:
        return f"({res})"
    return res


def log_expression(var = None, function = identity, b = None, parenthesis = False):
    ''' returns a log expression string
    '''

    func = function(var)
    
    b = base() if b is None else b
    
    res = f"log_{b}({func})"

    if parenthesis:
        return f"({res})"
    return res

##############################################
### b: two place expressions
##############################################

def operation_expression(var = None, function_1 = identity, function_2 = identity, op = None, parenthesis = False):
    ''' returns a sum or difference of two expressions
    ''' 

    func_1 = function_1(var)
    func_2 = function_2(var)

    op = operation() if op is None else op

    res = f"{func_1} {op} {func_2}"

    if parenthesis:
        return f"({res})"
    return res

##############################################
### c: composite expressions
##############################################

def linear_expression(var = None, function = identity, parenthesis = False):
    ''' returns a linear expression string, a * f(x) + b
    '''

    res = operation_expression(
        var, 
        lambda x: scalar_expression(
            var = x,
            function = function
        ), 
        lambda x: coefficient()
    )

    if parenthesis:
        return f"({res})"
    return res


def quadratic_expression(var = None, function = identity, parenthesis = False):
    ''' returns a quadratic expression string: a * f(x) ^ 2 + b * f(x) + c
    '''

    res =  operation_expression(
        var,
        lambda x: power_expression(
            var = x, 
            exp = 2
        ),
        linear_expression
    )
    
    if parenthesis:
        return f"({res})"
    return res


## 3: algebraic equation function
   
def equation(expression = identity, sol = None):
    ''' pass in an algebraic expression (function) and set it equal to a number!
    '''

    if sol is None:
        return expression() + " = " + solution()
    return expression() + " = " + sol
    
# THE EXAM

if __name__ == "__main__":
    # The script entrypoint. This is where everything starts!

    print("THE FINAL EXAM \n\n")
    
    ## PART 1: SIMPLICATION
    ### Question 1
    q1 = operation_expression(
        var = identity(), 
        op = "*",
        function_1 = lambda x: power_expression(
            x, 
            parenthesis = True
        ), 
        function_2 = lambda x: power_expression(
            x, 
            parenthesis = True
        ),
    )
    ### Question 2
    q2 = operation_expression(
        var = identity(), 
        op = "*",
        function_1 = lambda y: power_expression(
            y, 
            function = scalar_expression,
            parenthesis = True
        ), 
        function_2 = lambda y: linear_expression(
            y,
            parenthesis = True
        )
    )
    ### Question 3
    q3  = operation_expression(
        var = identity(),
        op = "/",
        function_1 = lambda y: power_expression(
            y,
            parenthesis = True
        ),
        function_2 = lambda y: power_expression(
            y, 
            parenthesis = True
        )
    )
    ### Question 4
    q4 = power_expression(
        var = identity(),
        function = lambda y: power_expression(
            y, 
            parenthesis = True
        )
    )
    
    print("Part 1: Choose 3 of the 6 following problems to complete. Simplify each expression you choose using any method. \n \n")
    print("\t 1. " + q1 + "\n")
    print("\t 2. " + q2 + "\n")
    print("\t 3. " + q3 + "\n")
    print("\t 4. " + q4 + "\n")
    print("\t TODO: two more! \n\n") 
    
    print("Part 2: Choose 3 of the following 6 problems to complete. Graph each function on the x-y plane as accurately as possible. \n \n")
    print("\t TODO \n \n")

    ## PART 3: SOLUTION
    q1 = equation(quadratic_expression)
    q2 = equation(
        lambda: root_expression(
            function = linear_expression, 
            n = "2"
        )
    )
    q3 = equation(
        lambda: log_expression(
            function = power_expression
        )
    )
    q4 = equation(
        lambda: log_expression(
            function = quadratic_expression
        )
    )
    q5 = equation(
        lambda: linear_expression(
            function = power_expression
        ),
        coefficient()
    )

    print("Part 3: Choose 3 of the 6 following problems to complete. Solve each equation you choose using any method. \n \n")
    print("\t 1. " + q1 + "\n" )
    print("\t 2. " + q2 + "\n")
    print("\t 3. " + q3 + "\n")
    print("\t 4. " + q4 + "\n")
    print("\t 5. " + q5 + "\n")
    print("\t TODO: one more! \n\n") 


