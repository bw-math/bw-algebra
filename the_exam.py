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

def linear_expression(var = None, function = None):
    ''' returns a linear expression string
    '''

    # generate random variable if nothing is passed
    var = variable() if var is None else var
    # apply function to variable if one is passed in
    func = var if function is None else function(var)

    a = coefficient()
    b = coefficient()
    op = sign()

    return f"{a} * {func} {op} {b}"

        
def quadratic_expression(var = None, function = None):
    ''' returns a quadratic expression string: a * x ^ 2 + b * x + c
    '''

    # generate random variable if nothing is passed
    var = variable() if var is None else var
    # apply function to variable if one is passed in
    func = var if function is None else function(var)

    quad_term = f"{func}^2"
    linear_term = linear_expression(func)
    op = sign()

    return f"{quad_term} {op} {linear_term}"


def square_root_expression(var = None, function = None):
    ''' returns a square root expression string
    '''
    
    # generate random variable if nothing is passed
    var = variable() if var is None else var
    # apply function to variable if one is passed in
    func = var if function is None else function(var)

    return f"sqrt({func})"


def power_expression(var = None, function = None):
    ''' returns an exponential expression string
    '''
    
    # generate random variable if nothing is passed
    var = variable() if var is None else var
    # apply function to variable if one is passed in
    func = var if function is None else function(var)

    exp = exponent()

    return f"{func}^{exp}"


def log_expression(var = None, function = None):
    ''' returns a log expression string
    '''

    # generate random variable if nothing is passed
    var = variable() if var is None else var
    # apply function to variable if one is passed in
    func = var if function is None else function(var)
    
    b = base()
    
    return f"log_{b}({func})"
     

## 3: algebraic equation function
   
def equals(expression):
    ''' pass in an algebraic expression (function) and set it equal to a number!
    '''

    return expression() + " = " + coefficient()

# THE EXAM

if __name__ == "__main__":

    print("THE FINAL EXAM \n\n")

    print("Part 1: Simplify the following expressions. \n \n")

    print("\t TODO: do this part! \n \n") 

    print("Part 2: Solve the following equations using any method you choose. \n \n")

    print("\t 1. "  + equals(quadratic_expression) + "\n" )

    print("\t 2. " + equals(lambda: square_root_expression(function = linear_expression)) + "\n")

    print("\t 3. " + equals(lambda: log_expression(function = power_expression))+ "\n")


