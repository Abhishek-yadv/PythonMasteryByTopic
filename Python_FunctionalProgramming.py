####################################################################
########################################## (Functional Programming)
####################################################################

###################################################################
# 1.* Write a Python function to find the maximum of three numbers
import sys
import textwrap
import math
def max_num(list):
    max = None
    for k in list:
        if k>None:
            max = k
        else:
            max
    return max
print(max([1,5,2]))

# OR
def max_two(a,b):
    if a>b:
        return a
    else:
        return b
def max_three(i,j,k):
    return max_two(i, max_two(j,k))
result = max_three(2,3,6)
print(result)

###################################################################
# 2.*  Write a Python function to sum all the numbers in a list.
def sum_func(*args):
    my_sum = 0
    for k in args:
        my_sum += k
    return my_sum
print(sum_func(1,2,3,4,5))

#OR
def sum_func(*args):
    return sum(args)
print(sum_func(1, 2, 3, 4, 5))

#######################################################################
# 3.*  Write a Python function to multiply all the numbers in a list.
def sum_func(*args):
    my_sum = 1
    for k in args:
        my_sum *= k
    return my_sum
print(sum_func(1, 2,3,4,5))

#OR
from operator import mul
from functools import reduce
def product_func(*args):
    return reduce(mul, args)
    # return reduce(lambda x,y:x*y, args)
print(product_func(1, 2, 3, 4, 5))

#Or
def product_func(*args):
    result =  sum((k*1) for k in args)
    return result
print(product_func(1, 2, 3, 4, 5))

#######################################################################
# 4.*  Write a Python program to reverse a string.
def func(string):
    new_string = ""
    for k in range(len(string)-1, -1, -1):
        new_string = new_string+string[k]
    return new_string
print(func("abhishek"))

# Or
def func(string):
    new_string = "".join(string[k] for k in range(len(string)-1, -1, -1))
    return new_string
print(func("abhishek"))

#Or
def func(string):
    my_string = ""
    my_index = len(string)-1
    while my_index>=0:
        my_string = my_string + string[my_index]
        my_index = my_index - 1
    return my_string
print(func("1234abcd"))
        
#######################################################################
# 5. Write a Python function to calculate the factorial of a number(a non-negative integer).
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)  
print(factorial(4))

#######################################################################
# 6. Write a Python function to check whether a number falls within a given range..
def cumulative_sum(lst: list) -> list:
    if not lst:
        return []
    elif isinstance(lst[0], str):
        return ["".join(lst[:i+1]) for i in range(len(lst))]
    else:
        return [sum(lst[:i+1]) for i in range(len(lst))]
print(cumulative_sum([1, 2, 3, 4]))
print(cumulative_sum([4, 3, 2, 1]))
print(cumulative_sum(['a', 'b', 'c', 'd']))  # Output: ['a', 'ab', 'abc', 'abcd']

#######################################################################
# 7. Write a Python function that accepts a string and counts the number of upper & lower case letters.
def func_count(arg):
    upper = 0
    lower = 0
    for x in arg:
        if x.isupper():
            upper = upper + 1
        elif x.islower():
            lower = lower + 1
    result = [upper, lower]
    return result
print(func_count('The quick Brow Fox'))
            
#######################################################################
# 8. Write a Python function that takes a list and returns a new list with distinct elements from the first list.
def unique_list(num_list):
    my_list = []
    for k in num_list:
        if k not in my_list:
            my_list.append(k)
    return my_list
print(unique_list([1, 2, 3, 3, 3, 3, 4, 5]))

#######################################################################
"""
9. Write a Python function that takes a number as a parameter and checks whether
the number is prime or not.
Note : A prime number is a natural number greater than 1 and that has no positive divisors other than 1 * itself.
"""
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True
print(is_prime(1))  # False
print(is_prime(2))  # True
print(is_prime(3))  # True
print(is_prime(4))  # False
print(is_prime(29))  # True
print(is_prime(30))  # False

#######################################################################
# 10. Write a Python program to print the even numbers from a given list.
def print_even(lst):
    even_list = [k for k in lst if k%2==0]
    return even_list

# Or
def print_even(lst:list)->list:return [k for k in lst if k % 2 == 0]

#######################################################################
"""
11. Write a Python function to check whether a number is "Perfect" or not.
According to Wikipedia : In number theory, a perfect number is a positive integer
that is equal to the sum of its proper positive divisors, that is,
the sum of its positive divisors excluding the number itself (also known as its aliquot sum).
Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself).

Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors,
and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum of all its positive divisors:
( 1 + 2 + 3 + 6 ) / 2 = 6. The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by 
the perfect numbers 496 and 8128.
"""
def my_function(num):
    my_list = []
    for k in range(1, num):
        if num%k==0:
            my_list.append(k)
    print(my_list)
    return True if ((sum(my_list) == num) and (sum(my_list) + num)/2 == num) else False
print(my_function(8128))

#######################################################################
"""
12. Write a Python function that checks whether a passed string is a palindrome or not .
Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
"""
def palindrome(strarg):
    # normalized_strarg = ''.join(strarg.split()).lower()
    cleaned_strarg = ''.join(char.lower() for char in strarg if char.isalnum())
    return cleaned_strarg == cleaned_strarg[::-1]

# Test the function with some examples
print(palindrome("madam"))           # True
print(palindrome("nurses run"))      # True
print(palindrome("hello"))           # False
print(palindrome("A man a plan a canal Panama")) # True


#######################################################################
""" 13. Write a Python function that prints out the first n rows of Pascal's triangle.
Note: Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal."""
[1]                                                                                                           
[1, 1]                                                                                                        
[1, 2, 1]                                                                                                     
[1, 3, 3, 1]                                                                                                  
[1, 4, 6, 4, 1]                                                                                               
[1, 5, 10, 10, 5, 1] 


#######################################################################
""" 14. Write a Python function to check whether a string is a pangram or not.
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog."""
# 1st method
import string
def pangram(s: str) -> bool:
    alphabet = string.ascii_lowercase
    return all(letter in s.lower() for letter in alphabet)

# Testing the function
print(pangram("The quick brown fox jumps over the lazy dog"))  # Should return True
print(pangram("Hello World"))  # Should return False


# 2nd method
import string
def pangram(s: str) -> list:
    my_list = []
    alphabet = string.ascii_lowercase
    for k in alphabet:
        if k in set(s):
            my_list.append(k)
    return my_list == list(alphabet)
print(pangram("The quick brown fox jumps over the lazy dog"))  # Should return True
print(pangram("Hello World"))  # Should return False

# 3rd method
import string
def pangram(s: str) -> bool:
    alphabet = string.ascii_lowercase
    s = s.lower()  # Convert the input string to lowercase
    for letter in alphabet:
        if letter not in s:
            return False
    return True
# Testing the function
print(pangram("The quick brown fox jumps over the lazy dog"))  # Should return True
print(pangram("Hello World"))  # Should return False


#######################################################################
""" 15. Write a Python program that accepts a hyphen-separated sequence of words
as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
Sample Items : green-red-yellow-black-white Expected Result : black-green-red-white-yellow."""
def sort_func(s:str):
    words = s.split('-')
    words.sort()
    return "-".join(words)
print(sort_func("green-red-yellow-black-white"))

#######################################################################
""" 16. Write a Python function to create and print a list where the values are the squares
of numbers between 1 and 30 (both included).."""
import time
start = time.time()
def square_func():
    return [i**2 for i in range(1,31)]
print(square_func())
print(start - time.time())

import time
start = time.time()
def square_func():
    return (i**2 for i in range(1,31))
print(list(square_func()))
print(start - time.time())

#######################################################################
# 17. Write a Python program to create a chain of function decorators (bold, italic, underline etc.)...
def bold(func):
    def wrapper():
        return "<b>" + func() + "<b>"
    return wrapper

def italic(func):
    def wrapper():
        return "<i>" + func() + "<i>"
    return wrapper

def underline(func):
    def wrapper():
        return "<u>" + func() + "<u>"
    return wrapper

@bold
@italic
@underline
def func():
    return "hello world"
print(func())


#######################################################################
# 18. Write a Python program to execute a string containing Python code.
def exe_func(code):
    return exec(code)
mycode = 'print("hello world")'
exe_func(mycode)

code = """
def mutiply(x,y):
    return x*y

print('Multiply of 2 and 3 is:',mutiply(2,3))
"""
exe_func(code)

#######################################################################
# 19. Write a Python program to access a function inside a function..
def ins_func(a):
    def inner_func(b):
        nonlocal a
        a = a+1
        return a+b
    return inner_func

func = ins_func(4)
print(func(7))

#######################################################################
# 20. Write a Python program to detect the number of local variables declared in a function.
def dec(func):
    def wrapper():
        result = func()
        return "result: {} And total number of local variable in function is:{}".format(result, len(locals()))
    return wrapper

@dec
def test():
    a = 10
    b = 10
    return a+b
print(test())

#######################################################################
# 21. Write a Python program to detect the number of local variables declared in a function.
from time import sleep
import math

def delay(fn, ms, *args):
    sleep(ms / 1000)    
    return fn(*args)

print("Square root after specific milliseconds:") 
print(delay(lambda x: math.sqrt(x), 100, 16))
print(delay(lambda x: math.sqrt(x), 1000, 100))
print(delay(lambda x: math.sqrt(x), 2000, 25100))

import math
print((lambda x: math.sqrt(x))(25100))


#######################################################################
# 22. Provide an implementation for zip function using list comprehensions
import faker
m = faker.Faker()
content = """
I'm sure that the shells are s
eashore shells.
So if she sells seashells on t
he seashore,
The shells that she sells are
seashells I'm sure.
"""
with open("sample.txt", 'w') as file_object:
    file_object.write(content)

import textwrap
def wrap(filename, width):
    with open(filename, 'r') as file_object:
        lines = file_object.readlines()
    wrapped_lines = []
    for line in lines:
        wrapped_lines.extend(textwrap.wrap(line, width))
    for line in wrapped_lines:
        print(line)
wrap("sample.txt", 30)

import textwrap
def word_wrap(filename, width):
    with open(filename, 'r') as file_object:
        content = file_object.read()
    wrapped_text = textwrap.fill(content, width)
    print(wrapped_text)
word_wrap("sample.txt", 30)

#######################################################################
# 23. Provide an implementation for zip function using list comprehensions
def zip(x, y):
    return [(x[i], y[i]) for i in range(min(len(x), len(y)))]
print(zip([1, 2, 3], ["a", "b", "c"]))

#######################################################################
""" 24. Python provides a built-in function map that applies a function to each element of a list.
# Provide an implementation for map using list comprehensions """
def square(x): return x * x
def map(func, lst):
    return [square(x) for x in lst]
print(map(square, range(5)))

#######################################################################
""" 
25.Python provides a built-in function filter(f, a) that returns items of the list a for which
f(item) returns true. Provide an implementation for filter using list comprehensions."""
def even(x): return x %2 == 0
def filter(func, iter):
    return [x for x in range(10) if even(x)]
print(filter(even, range(10)))

#######################################################################
"""
26. Write a function enumerate that takes a list and returns a list of tuples containing
(index,item) for each item in the list.
"""
def enumerate(iter):
    return [(i, iter[i]) for i in range(len(iter))]
print(enumerate(["a", "b", "c"]))

#######################################################################
"""
27: Write a function array to create an 2-dimensional array. The function should take both dimensions
as arguments. Value of each element can be initialized to None:.
"""
def create_2d_array(rows, cols):
    return [[None for _ in range(cols)] for _ in range(rows)]

# Example usage
array = create_2d_array(2, 3)
for row in array:
    print(row)

#######################################################################
"""
28: Write a function triplets that takes a number n as argument and returns a list of triplets such
that sum of first two elements of the triplet equals the third element using numbers below n. Please note that (a,
b, c) and (b, a, c) represent same triplet. """
def triplets(n):
    result = []
    for a in range(1, n):
        for b in range(a, n):
            c = a + b
            if c < n:
                result.append((a, b, c))
    return result
print(triplets(5))

#######################################################################
# 29 Write a python function parse_csv to parse csv (comma separated values) files.
def parse_csv(filename):
    with open(filename, 'r') as file:
        content = file.read()

    lines = content.splitlines()
    return [line.split(',') for line in lines]
# Example usage
print(parse_csv('a.csv'))


#######################################################################
# 30. Generalize the above implementation of csv parser to support any delimiter and comments.
def parse(filename, delimiter=',', comment_char='#'):
    with open(filename, 'r') as file:
        lines = file.readlines()
    result = []
    for line in lines:
        # Skip lines starting with comment_char
        if line.startswith(comment_char):
            continue
        # Split the line by the delimiter and strip whitespace
        fields = [field.strip() for field in line.strip().split(delimiter)]
        result.append(fields)
    return result
# Example usage
print(parse('a.txt', '!', '#'))

#######################################################################
"""
31. Write a function mutate to compute all words generated by a single mutation on a given word. A
mutation is defined as inserting a character, deleting a character, replacing a character, or swapping 2 consecutive
characters in a string. For simplicity consider only letters from a to z
"""
def mutate(word):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    mutations = set()
    
    # Insertion
    for i in range(len(word) + 1):
        for char in alphabet:
            mutated_word = word[:i] + char + word[i:]
            mutations.add(mutated_word)
    
    # Deletion
    for i in range(len(word)):
        mutated_word = word[:i] + word[i+1:]
        mutations.add(mutated_word)
    
    # Replacement
    for i in range(len(word)):
        for char in alphabet:
            mutated_word = word[:i] + char + word[i+1:]
            mutations.add(mutated_word)
    
    # Swapping consecutive characters
    for i in range(len(word) - 1):
        mutated_word = word[:i] + word[i+1] + word[i] + word[i+2:]
        mutations.add(mutated_word)
    return mutations

# Test the function
words = mutate('hello')
print('helo' in words)   # True
print('cello' in words)  # True
print('helol' in words)  # True

#######################################################################
"""
32. Write a function nearly_equal to test whether two strings are nearly equal. Two strings a and
b are nearly equal when a can be generated by a single mutation on b.
"""
def mutate(word):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    mutations = set()

    for i in range(len(word) + 1):
        for char in alphabet:
            mutated_word = word[:i] + char + word[i:]
            mutations.add(mutated_word)

    for i in range(len(word)):
        mutated_word = word[:i] + word[i+1:]
        mutations.add(mutated_word)

    for i in range(len(word)):
        for char in alphabet:
            mutated_word = word[:i] + char + word[i+1:]
            mutations.add(mutated_word)

    for i in range(len(word) - 1):
        mutated_word = word[:i] + word[i+1] + word[i] + word[i+2:]
        mutations.add(mutated_word)
    return mutations

def nearly_equal(a, b):
    return a in mutate(b)

# Test cases
print(nearly_equal('python', 'perl'))   # False
print(nearly_equal('perl', 'pearl'))    # True
print(nearly_equal('python', 'jython'))  # True
print(nearly_equal('man', 'woman'))     # False

