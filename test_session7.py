import pytest
import random
import string
import session7
import os
import inspect
import re
import math
import time
from functools import reduce
from session7 import func_docstring
from session7 import fib_func
from session7 import counter_single_dict
from session7 import counter_multiple_dict
from session7 import count_dict, count_dict_add, count_dict_mul, count_dict_div
from session7 import addition, multiplication, division

README_CONTENT_CHECK_FOR = [
    'func_docstring',
    'fib_func',
    'counter_single_dict',
    'counter_multiple_dict',
    'count_dict',
    'count_dict_add',
    'count_dict_mul',
    'count_dict_div',
    'length_of_docstring',
    'next_fib_number',
    'inner_single_dict',
    'inner_multiple_dict',
    'addition',
    'multiplication',
    'division'
]

def test_session7_readme_exists():
    """
    Method checks if there is a README.md file. 
    failure_message: "README.md file missing!"  
    """
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_session7_readme_500_words():
    """
    Method checks if there are atleast 500 words in the README.md file
    failures_message: Make your README.md file interesting! Add atleast 500 words
    """
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_session7_readme_proper_description():
    """
    Method checks if all the functions are described in the README.md file
    failures_message: You have not described all the functions/classes well in your README.md file
    """
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_session7_readme_file_for_more_than_10_hashes():
    """
    Method checks if README.md file has atleast 10 '#' (indentations)
    failures_message: You have not described all the functions/classes well in your README.md file 
    """
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_session7_indentations():
    """
    Method checks for proper indentations \
    Returns pass if used four spaces for each level of syntactically significant indenting.
    failures_message_1: Your script contains misplaced indentations
    failures_message_2: Your code indentation does not follow PEP8 guidelines
    """
    lines = inspect.getsource(session7)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_session7_function_name_had_cap_letter():
    """
    Method checks for any Upper case in the function names in session7.py
    failures_message: You have used Capital letter(s) in your function names
    """
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def function_without_docstring():
    return "This function has no docstring"

def function_with_less_docstring():
    '''
    Introverted docstring
    '''
    return "A very short docstring"

############################## Assignment Validations ###########################

# Docstring problem

def test_session7_func_docstring(): # True test case scenario
    """
    This method checks the length of the docstring of the function passed has <50 characters
    failures_message: Docstring is defined for the function and <50 characters
    """
    len_of_docstring = func_docstring(test_session7_indentations)
    assert len_of_docstring() == True, "Docstring is defined for the function and <50 characters"

def test_session7_func_docstring_nodocstring(): # No docstring test case
    """
    This method checks the function with no docstring passed
    failures_message: Docstring is not defined defined for the function
    """
    len_of_docstring = func_docstring(function_without_docstring)
    assert len_of_docstring() == "No doc string present!", "Docstring is not defined defined for the function"

def test_session7_func_docstring_sparsedocstring(): # Docstring with less than 50 char
    """
    This method checks the function with >50 character docstring
    failures_message: This docstring is very sparse
    """
    len_of_docstring = func_docstring(function_with_less_docstring)
    assert len_of_docstring() == False, "This docstring is very sparse"

def test_session7_length_of_docstring_closure(): # Inner function is closure
    """
    This method checks if the docstring function is a closure
    failures_message: len_of_docstring is a closure function
    failures_message: func_docstring is not a closure function
    """
    len_of_docstring = func_docstring(function_with_less_docstring)
    assert len_of_docstring.__closure__ != None, "len_of_docstring is a closure function"
    assert func_docstring.__closure__ == None, "func_docstring is not a closure function"

def test_session7_length_freevars(): # Length variable is free variable
    """
    This method checks the length variable is a freevar in the closure function
    failures_message: Length variable should be a free variable
    """
    len_of_docstring = func_docstring(function_with_less_docstring)
    assert len_of_docstring.__code__.co_freevars == ('fn','length'), "Length variable should be a free variable"

# Fibonacci Sequence

def test_session7_fibonacci_seq(): # Check the Fibonacci number generated
    """
    This method checks the next fibonacci number returned in the sequence
    failures_message: That is not the next Fibonacci number in the series
    """
    fib_number = fib_func()
    assert fib_number(21) == 34, "That is not the next Fibonacci number in the series"
    assert fib_number(233) == 377, "That is not the next Fibonacci number in the series"
    assert fib_number(3) == 5, "That is not the next Fibonacci number in the series"

def test_session7_fibonacci_negative(): # Check the negative integer
    """
    This method checks the function with negative integers
    failures_message: That is not the next Fibonacci number in the series
    """
    fib_number = fib_func()
    with pytest.raises(TypeError, match=r".*We are dealing with positive integers only*"):
        fib_number(-21)
    with pytest.raises(TypeError, match=r".*Only integers are accepted*"):
        fib_number('233')
    with pytest.raises(TypeError, match=r".*Only integers are accepted*"):
        fib_number(3+7j)

def test_session7_next_fib_number_closure(): # Inner function is closure
    """
    This method checks if the fib_number is a closure
    failures_message: len_of_docstring is a closure function
    failures_message: func_docstring is not a closure function
    """
    fib_numb = fib_func()
    assert fib_numb.__closure__ != None, "fib_numb is a closure function"
    assert fib_func.__closure__ == None, "fib_func is not a closure function"

def test_session7_fib_seq_freevars(): # Length variable is free variable
    """
    This method checks the fib_seq variable is a freevar in the closure function
    failures_message: Length variable should be a free variable
    """
    fib_numb = fib_func()
    assert fib_numb.__code__.co_freevars == ('fib_seq',), "Length variable should be a free variable"

# Arithematic operations using closure

def test_session7_counter_single_dict():
    """
    This method checks if the counter_single_dict function is working as expected
    failure_message1: Check your addition program
    failure_message2: Check your multiplication program
    failure_message3: Check your division program
    failure_message4: Check you dictionary and counter program
    """
    add = counter_single_dict(addition)
    mul = counter_single_dict(multiplication)
    div = counter_single_dict(division)
    input_list = [random.randint(-100,100) for x in range(5)]
    #global count_dict={}
    assert add(*input_list) == sum(input_list), "Check your addition program"
    assert mul(*input_list) == reduce(lambda x, y: x * y, input_list), "Check your multiplication program"
    assert div(*input_list) == reduce(lambda x, y: x / y, input_list), "Check your division program"
    assert count_dict == {'addition': 1, 'multiplication':1, 'division': 1}, "Check you dictionary and counter program"

def test_session7_counter_single_dict_count_dict():
    """
    This method checks if the count_dict counts the operations properly
    failure_message: Inconsistency in the dictionary counter
    """
    add = counter_single_dict(addition)
    mul = counter_single_dict(multiplication)
    div = counter_single_dict(division)
    for x in range(3):
        input_list = [random.randint(-100,100) for x in range(3)]
        _ = add(*input_list)
    for x in range(5):
        input_list = [random.randint(-100,100) for x in range(3)]
        _ = mul(*input_list)
    for x in range(2):
        input_list = [random.randint(-100,100) for x in range(3)]
        _ = div(*input_list)
    assert count_dict == {'addition': 3, 'multiplication':5, 'division': 2}, "Inconsistency in the dictionary counter"

def test_session7_counter_single_dict_count_zero(): #pass zero in args
    """
    This method checks the addition, multiplication and division functions for edge cases
    failure_message1: Check your addition program
    failure_message2: Check your multiplication program
    failure_message3: Check your division program
    failure_message4: Check you dictionary and counter program
    """
    add = counter_single_dict(addition)
    mul = counter_single_dict(multiplication)
    div = counter_single_dict(division)
    assert add(10, 0, 5, 3, 2) == sum([10, 0, 5, 3, 2]), "Check your addition program"
    assert mul(10, 0, 5, 3, 2) == 0, "Check your multiplication program"
    assert div(10, 0, 5, 3, 2) == 0, "Check your division program"
    assert count_dict == {'addition': 1, 'multiplication':1, 'division': 1}, "Check you dictionary and counter program"

def test_session7_counter_single_dict_noargs(): #pass no args
    """
    This method checks the addition, multiplication and division functions for edge cases
    failure_message1: Check your addition program
    failure_message2: Check your multiplication program
    failure_message3: Check your division program
    failure_message4: Check you dictionary and counter program
    """
    add = counter_single_dict(addition)
    mul = counter_single_dict(multiplication)
    div = counter_single_dict(division)
    with pytest.raises(ValueError, match=r".*Arguments can't be empty*"):
        add()
    with pytest.raises(ValueError, match=r".*Arguments can't be empty*"):
        mul()
    with pytest.raises(ValueError, match=r".*Arguments can't be empty*"):
        div()

def test_session7_counter_single_dict_nonintargs(): #pass non integer/float args
    """
    This method checks the addition, multiplication and division functions for edge cases
    failure_message1: Check your addition program
    failure_message2: Check your multiplication program
    failure_message3: Check your division program
    failure_message4: Check you dictionary and counter program
    """
    add = counter_single_dict(addition)
    mul = counter_single_dict(multiplication)
    div = counter_single_dict(division)
    with pytest.raises(TypeError, match=r".*Arithematic operations can be performed on integers or floats*"):
        add(2, 10, '5')
    with pytest.raises(TypeError, match=r".*Arithematic operations can be performed on integers or floats*"):
        add(1, 2, 3, 10+5j, 5)
    with pytest.raises(TypeError, match=r".*Arithematic operations can be performed on integers or floats*"):
        mul(100, '7', 8)
    with pytest.raises(TypeError, match=r".*Arithematic operations can be performed on integers or floats*"):
        mul(9, 8, 5+10j)
    with pytest.raises(TypeError, match=r".*Arithematic operations can be performed on integers or floats*"):
        div('0', 16, 2)
    with pytest.raises(TypeError, match=r".*Arithematic operations can be performed on integers or floats*"):
        div(23, 55, 5+10j)

def test_session7_counter_multiple_dict_count_dict():
    """
    This method checks if the count_dict_add, count_dict_mul and count_dict_div counts the operations properly
    failure_message: Inconsistency in the dictionary counter
    """
    add = counter_multiple_dict(addition)
    mul = counter_multiple_dict(multiplication)
    div = counter_multiple_dict(division)
    for x in range(5):
        input_list = [random.randint(-100,100) for x in range(3)]
        _ = add(*input_list, dict_counter = count_dict_add)
    for x in range(2):
        input_list = [random.randint(-100,100) for x in range(3)]
        _ = mul(*input_list, dict_counter = count_dict_mul)
    for x in range(4):
        input_list = [random.randint(-100,100) for x in range(3)]
        _ = div(*input_list, dict_counter = count_dict_div)
    assert count_dict_add == {'counter': 5}, "Inconsistency in the dictionary counter"
    assert count_dict_mul == {'counter': 2}, "Inconsistency in the dictionary counter"
    assert count_dict_div == {'counter': 4}, "Inconsistency in the dictionary counter"

def test_session7_counter_multiple_dict_noargs(): # Check when no args
    """
    This method checks if the closure handles no arguments
    failure_message: Arguments can't be empty
    """
    add = counter_multiple_dict(addition)
    mul = counter_multiple_dict(multiplication)
    div = counter_multiple_dict(division)
    with pytest.raises(ValueError, match=r".*Arguments can't be empty*"):
        add(dict_counter = count_dict_add)
    with pytest.raises(ValueError, match=r".*Arguments can't be empty*"):
        mul(dict_counter = count_dict_mul)
    with pytest.raises(ValueError, match=r".*Arguments can't be empty*"):
        div(dict_counter = count_dict_div)

def test_session7_counter_multiple_dict_nokwargs(): #Check no kwargs
    """
    This method checks if the individual count_dict is not passed as kwargs
    failure_message: Please pass the counter dictionary
    """
    add = counter_multiple_dict(addition)
    mul = counter_multiple_dict(multiplication)
    div = counter_multiple_dict(division)
    with pytest.raises(ValueError, match=r".*Please pass the counter dictionary*"):
        add(10, 5, 3, 2)
    with pytest.raises(ValueError, match=r".*Please pass the counter dictionary*"):
        mul(10, 5, 3, 2)
    with pytest.raises(ValueError, match=r".*Please pass the counter dictionary*"):
        div(10, 5, 3, 2)

def test_session7_counter_multiple_dict_closure(): #Check closure
    """
    This method checks if counter_multiple_dict is a closure and the freevars accessible
    failure_message: counter_multiple_dict is not a closure
    """
    add = counter_multiple_dict(addition)
    mul = counter_multiple_dict(multiplication)
    div = counter_multiple_dict(division)
    assert counter_multiple_dict.__closure__ == None, "counter_multiple_dict is not a closure"
    assert add.__closure__ != None, "add is a closure function"
    assert mul.__closure__ != None, "add is a closure function"
    assert div.__closure__ != None, "add is a closure function"
    assert add.__code__.co_freevars == ('count', 'fn'), "Closure should have two free vars"
    assert mul.__code__.co_freevars == ('count', 'fn'), "Closure should have two free vars"
    assert div.__code__.co_freevars == ('count', 'fn'), "Closure should have two free vars"

def test_session7_counter_single_dict_closure(): #Check closure
    """
    This method checks if the counter_multiple_dict is a closure and the freevars accessible
    failure_message: counter_multiple_dict is not a closure
    """
    add = counter_single_dict(addition)
    mul = counter_single_dict(multiplication)
    div = counter_single_dict(division)
    assert counter_single_dict.__closure__ == None, "counter_multiple_dict is not a closure"
    assert add.__closure__ != None, "add is a closure function"
    assert mul.__closure__ != None, "add is a closure function"
    assert div.__closure__ != None, "add is a closure function"
    assert add.__code__.co_freevars == ('count', 'fn'), "Closure should have two free vars"
    assert mul.__code__.co_freevars == ('count', 'fn'), "Closure should have two free vars"
    assert div.__code__.co_freevars == ('count', 'fn'), "Closure should have two free vars"