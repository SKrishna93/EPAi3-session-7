#%%
from functools import reduce

# Question 1 Checking doc string length

def func_docstring(fn: "function")->"length_of_docstring":
    '''
    This function takes another function as input and stores it as a func_name. length = 50 is stored as floating variable
    input: 
        'fn' - function
    output:
        True if the docstring length is greater than 50 else "No doc string present!"
    '''
    length = 50
    def length_of_docstring()->"Bool of docstring length > 50":
        '''
        This function takes the nonlocal variables length and func_name 
        '''
        nonlocal length
        nonlocal fn
        if fn.__doc__:
            return len(fn.__doc__) > length
        else:
            return "No doc string present!"
    return length_of_docstring

# Question 2 Fibonacci number

def fib_func() -> "next_fib_number":
    '''
    This function is an enclosing function for the next_fib_number function
    It returns the inner function next_fib_number after initializing the fib_seq list (floating var)
    '''
    fib_seq = [0, 1]
    def next_fib_number(num: int) -> "Next fibonacci number in the sequence":
        '''
        This function returns the next fibonacci number in the sequence
        This is the closure function with access to fib_seq var floating variable
        '''
        nonlocal fib_seq
        if isinstance(num,int):
            if num >= 0:
                if (num not in fib_seq):
                    while(not (fib_seq[-1] == num)):
                        fib_seq.append(fib_seq[-2] + fib_seq[-1])
                    fib_seq.append(fib_seq[-2] + fib_seq[-1])
                    return fib_seq[-1]
                else:
                    fib_seq.append(fib_seq[-2] + fib_seq[-1])
                    return fib_seq[fib_seq.index(num) + 1]
            else:
                raise TypeError("We are dealing with positive integers only")
        else:
            raise TypeError("Only integers are accepted")
    return next_fib_number

# Question 3 - Multiple Arithematic operations and counting with a common dictionary

count_dict = dict()
count_dict_add = dict()
count_dict_mul = dict()
count_dict_div = dict()

def counter_single_dict(fn: "funtion name",*args) -> "inner_single_dict":
    '''
    This function is an enclosing function which takes function name and returns the inner function.
    input:-
        fn - function name to be accessed, arithematic operation to be performed
    return:-
        inner_single_dict function object is returned
    '''
    count=0
    def inner_single_dict(*args)-> "func(args) call":
        '''
        This nested function is a closure function which increaments the count_dict by 1 for every call of the aruthematic fuintions
        input:-
            *args - tuple of positional arguments
        return:-
            func(args) - The function call to perform the arithematic operation
        '''
        nonlocal count
        nonlocal fn
        if args:
            count += 1
            count_dict[fn.__name__] = count
            return fn(args)
        else:
            raise ValueError("Arguments can't be empty")
    return inner_single_dict

def counter_multiple_dict(fn: "funtion name") -> "inner_multiple_dict":
    '''
    This function is an enclosing function which takes function name and returns the inner function.
    input:-
        fn - function name to be accessed, arithematic operation to be performed
    return:-
        inner_multiple_dict function object is returned
    '''
    count = 0
    def inner_multiple_dict(*args,**kwargs)-> "fn(args) call":
        '''
        This nested function is a closure function which increaments the dict_counter for the individual operation
        by 1 for every call of the aruthematic functions
        input:-
            *args - tuple of positional arguments
            **kwargs - gloabl dictionary variable to be updated with count
        return:-
            fn(args) - The function call to perform the arithematic operation
        '''
        nonlocal count
        if args:
            count += 1
            if kwargs:
                kwargs['dict_counter']['counter'] = count
                return fn(args)
            else:
                raise ValueError("Please pass the counter dictionary")
        else:
            raise ValueError("Arguments can't be empty")
    return inner_multiple_dict

def addition(*args)-> "Sum of all the elements of args":
    '''
    This function performs element wise addition of args
    input:-
        *args - positional arguments as a tuple
    output:-
        sum of the arguments passed
    '''
    for x in args[0]:
        if not (isinstance(x,int) or isinstance(x,float)):
            raise TypeError("Arithematic operations can be performed on integers or floats")
    return reduce(lambda x, y: x + y,args[0])
    
def multiplication(*args)-> "Element wise multiplication of all the arguments":
    '''
    This function performs element wise multiplication of args
    input:-
        *args - positional arguments as a tuple
    output:-
        poduct of the arguments passed
    '''
    for x in args[0]:
        if not (isinstance(x,int) or isinstance(x,float)):
            raise TypeError("Arithematic operations can be performed on integers or floats")
    if all(args[0]):
        return reduce(lambda x, y: x * y,args[0])
    else:
        return 0

def division(*args)-> "Element wise division of all the arguments":
    '''
    This function performs element wise division of args
    input:-
        *args - positional arguments as a tuple
    output:-
        division of the arguments passed
    '''
    for x in args[0]:
        if not (isinstance(x,int) or isinstance(x,float)):
            raise TypeError("Arithematic operations can be performed on integers or floats")
    if all(args[0]):
        return reduce(lambda x, y: x / y,args[0])
    else:
        return 0
#%%