# Session 7 Assignment of EPAi3.0

## Scopes and Closures

### Question - 1

### Objective: To write a closure that takes a function checks if the function passed has a docstring with more than 50 characters

* Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable

#### Closure to check the docstring length

* __func_docstring (fn)__ :
+ The method returns the clsoure function length_of_docstring.
+ The method takes 1 positional argument _'fn'_
+ fn: Function which needs to checked for docstring length
+ __Algorithm__: The function name is passed as argument, length = 50 is stored as a free variable accessible to the closure function 

* __length_of_docstring ()__ :
+ The method returns True if the function passed has docstring and longer than 50 characters else False
+ It is a closure function which utilizes the freevars length and function name to determine the length of docstring

### Question - 2

### Objective: To write a closure that gives you the next Fibonacci number

__fib_func ()__ :
+ The method is an enclosing function for next_fib_number which creates a freevar fib_seq
+ The function returns the inner function next_fib_number

__next_fib_number (num)__ :
+ This method takes an fibonacci number in the series and returns the next fibonacci number 
+ The method takes 1 positional argument *'num'*
+ num: A positive integer which is also a fibonacci number
+ __Algorithm__: num argument passed is checked for being a positive integer. If the same is present in the fib_seq, the next element is returned. If not, a loop is run to compute the sequence until num is the last element in the fib_seq and the next element is returned

### Question - 3

### Objective: To write a closure that counts how many times a function was called. Keep track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts

__counter_single_dict (fn, *args)__ :
+ This method is an enclosing function which takes the function name as an argument and returns the closure inner_single_dict function. It also initializes free variables count = 0 and fn
+ The method takes 1 positional argument *'fn'*
+ fn: Predefined functions addition, multiplication and division

__inner_single_dict (*args)__ :
+ The method processes args and calls the corresponding arithematic function fn(args). It also increaments the value of count by 1 and stores it in a global dictionary *count_dict*
+ The method takes 1 positional argument *'args'* which are passed on to the arithematic operation function
+ Returns the final add/mul/div of the list elements
+ __Algorithm__: Access the nonlocal variable count and increase it by 1 and store in a gobal dictionary. Call the addition/multiplication/division function based on the fn argument passed. Return the resultant of the operations call

__counter_multiple_dict (fn, *args, **kwargs)__ :
+ This method is an enclosing function which takes the function name as an argument and returns the closure inner_multiple_dict function. It also initializes free variables count = 0 and fn
+ The method takes 1 positional argument *'fn'* and takes any number of args and kwargs
+ fn: Predefined functions addition, multiplication and division

__inner_multiple_dict (*args, **kwargs)__ :
+ This method takes arguments for the operation function (addition, multiplication and division) and a keyword argument (global dictionary). Returns the operation function call along with the arguments
    + *args - numerical arguments for the arithematic operations functions
    + **kwargs - keyword argument for updating the count variable
+ Function is expected to take one of the global dictionaries count_dict_add, count_dict_mul or count_dict_div as a keyword argument and update the latest value of the variable count
+ __Algorithm__: Access the nonlocal variable count and increase it by 1 and store in a gobal dictionary passed as a keyword argument. Call the addition/multiplication/division function based on the fn argument passed. Return the resultant of the operations call

__addition (*args)__ :
+ The function takes the arguments passed and returns their sum
+ If the any of the values passed in args are not integer or float type, then a TypeError is raised

__multiplication (*args)__ :
+ The function takes the arguments passed and returns the product of the individual argument
+ If the any of the values passed in args are not integer or float type, then a TypeError is raised
+ If any of the arguments passed is zero, then 0 is returned

__division (*args)__ :
+ The function takes the arguments passed and returns the dividen of the arguments
+ If the any of the values passed in args are not integer or float type, then a TypeError is raised
+ If any of the arguments passed is zero, then 0 is returned. AS, division by zero would result in error