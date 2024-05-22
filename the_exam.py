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
variables = [ "x", "y", "z", "✀", "✈", "🂡", "🀎", "Δ", "Ψ", "Ω", "β", "ω"]
coefficients = [ str(x) for x in range(1, 26) ]
solutions = [ str(x) for x in range(1, 11) ]
squares = [ str(i*i) for i in range(1, 11) ]
bases = [ "e", "10", "2", "4", "7" ]
exponents = [ "2", "3", "4", "5", "6", "7" ]
trigs = [ "sin", "cos", "tan" ]
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


def coefficient(limit = 25):
    ''' returns a random numeric string between "1" and "25".
    '''
    return random.choice([ str(x) for x in range(1, limit + 1) ])


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

def trig():
    ''' returns a random string from the choices: "sin", "tan", "cos"
    '''
    return random.choice(trigs)

def square():
    ''' returns a random square between 1^2 and 10^2
    '''
    return random.choice(squares)

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

def exp_expression(var =None, function = identity, b = None, parenthesis = False):
    ''' returns an exponential expression string
    '''
    
    func = function(var)

    b = base() if b is None else b

    res = f"{b}^{func}"

    if parenthesis: 
        return f"({res})"
    return res

def trig_expression(var = None, function = identity, ratio = None, parenthesis = False):
    ''' returns a trig expression string
    '''

    func = function(var)

    tr = trig() if ratio is None else ratio

    res = f"{tr}({func})"

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
        function, 
        lambda x: coefficient()
    )

    if parenthesis:
        return f"({res})"
    return res


def quadratic_expression(var = None, function = identity, parenthesis = False):
    ''' returns a quadratic expression string: a * f(x) ^ 2 + b * f(x) + c
    '''

    var = identity(var)

    res =  operation_expression(
        var,
        lambda x: power_expression(
            var = x, 
            function = function, 
            exp = 2
        ),
        lambda x: linear_expression(
            var = x, 
            function = lambda y: scalar_expression(
                y, 
                function = function
            )
        )
    )
    
    if parenthesis:
        return f"({res})"
    return res


## 3: algebraic equation function
   
def equation(expression = identity, solution = None, random_limit = 25):
    ''' pass in an algebraic expression (function) and set it equal to a number!
    '''
    
    if solution is None:
        return expression() + " = " + coefficient(random_limit)
    return expression() + " = " + solution
# THE EXAM

if __name__ == "__main__":
    # The script entrypoint. This is where everything starts!

    print("THE FINAL EXAM \n\n")
    
    ## PART 1: SIMPLICATION
    ### Question 1.1
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
    ### Question 1.2
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
    ### Question 1.3
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
    ### Question 1.4
    q4 = power_expression(
        var = identity(),
        function = lambda y: power_expression(
            y, 
            parenthesis = True
        )
    )
    ### Question 1.5
    q5 = operation_expression(
        var = identity(),
        function_1 = lambda y: linear_expression(
            y, 
            function = scalar_expression,
            parenthesis = True
        ),
        function_2 = lambda y: linear_expression(
            y, 
            function = scalar_expression,
            parenthesis = True
        ),
        op = "*"
    )
    ### Question 1.6
    q6 = operation_expression(
        var = identity(),
        function_1 = lambda y: linear_expression(
            y,
            parenthesis = True
        ),
        function_2 = lambda y: power_expression(
            y, 
            function = lambda x: linear_expression(
                x, 
                parenthesis = True
            ),
            exp = 2,
            parenthesis = True
        ),
        op = "*"
    )
    
    print("Part 1: Choose 3 of the 6 following problems to complete. Simplify each expression you choose using any method. \n \n")
    print("\t 1. " + q1 + "\n")
    print("\t 2. " + q2 + "\n")
    print("\t 3. " + q3 + "\n")
    print("\t 4. " + q4 + "\n")
    print("\t 5. " + q5 + "\n")
    print("\t 6. " + q6 + "\n")
    
    ## PART 2: GRAPHING
    ### Question 2.1
    q1 = equation(
        lambda: linear_expression(
            "x",
            function = lambda x: scalar_expression(
                x,
                a = coefficient(5)
            )
        ),
        "y"
    )
    ### Question 2.2
    q2 = equation(
        lambda: operation_expression(
            function_1 = lambda y: power_expression(
                "x",
                exp = 2
            ),
            function_2 = lambda y: power_expression(
                "y",
                exp = 2
            ),
            op = "+"
        ), 
        square()
    )
    ### Question 2.3
    q3 = equation(
        lambda: scalar_expression(
            "x",
            function = lambda y: power_expression(
                y, 
                function = lambda z: operation_expression(
                    z,
                    function_1 = identity,
                    function_2 = lambda p: coefficient(5),
                    op = "-",
                    parenthesis = True
                ),
                exp = 2
            ),
            a = coefficient(5)
        ),
        "y"
    )
    ### Question 2.4
    q4 = equation(
        lambda: operation_expression(
            function_1 = lambda y: power_expression(
                "x",
                function = lambda z: operation_expression(
                    z, 
                    function_1 = identity,
                    function_2 = lambda p: coefficient(10),
                    op = "/",
                    parenthesis = True
                ),
                exp = 2
            ),
            function_2 = lambda y: power_expression(
                "y",
                function = lambda z: operation_expression(
                    z, 
                    function_1 = identity,
                    function_2 = lambda p: coefficient(10),
                    op = "/",
                    parenthesis = True
                ),
                exp = 2
            ),
            op = "+"
        ),
        "1"
    )
    ### Question 2.5
    q5 = equation(
        lambda: exp_expression("x"),
        "y"
    )
    ### Question 2.6
    q6 = equation(
        lambda: 
            scalar_expression(
                function = lambda x: power_expression(
                    x,
                    function = lambda y: operation_expression(
                        y,
                        function_1 = identity,
                        function_2 = lambda z: coefficient(5),
                        parenthesis = True
                    ),
                    exp = 3
                ),
                a = coefficient(5)
            ),
        "y"
    )

    print("Part 2: Choose 3 of the following 6 problems to complete. Graph each function on the x-y plane as accurately as possible. \n \n")
    print("\t 1. " + q1 + "\n")
    print("\t 2. " + q2 + "\n")
    print("\t 3. " + q3 + "\n")
    print("\t 4. " + q4 + "\n")
    print("\t 5. " + q5 + "\n")
    print("\t 6. " + q6 + "\n")

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
    q6 = equation(
        lambda: trig_expression(
            function = lambda x: scalar_expression(
                x,
                a = coefficient(10)
            )
        ),
        str(round(random.random(), 2))
    )

    print("Part 3: Choose 3 of the 6 following problems to complete. Solve each equation you choose using any method. \n \n")
    print("\t 1. " + q1 + "\n" )
    print("\t 2. " + q2 + "\n")
    print("\t 3. " + q3 + "\n")
    print("\t 4. " + q4 + "\n")
    print("\t 5. " + q5 + "\n")
    print("\t 6. " + q6 + "\n") 


