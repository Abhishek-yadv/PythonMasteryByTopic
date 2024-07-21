####################################################################
########################################################## Lambda
####################################################################

###################################################################
"""
1. Write a Python program to triple all numbers in a given list of integers. Use Python map.
"""
import itertools
my_list = [1, 2, 3, 4, 5]
lambda_func = list(map(lambda x: 3*x, my_list))
print(lambda_func)

###################################################################
"""
2. Write a Python program to add three given lists using Python map and lambda.
"""
list1 = [1,2,3,4]
list2 = [4,5,6,7]
list3 = [9,7,2,3]
lambda_func = list(map(lambda x,y,z : x+y+z, list1,list2, list3))
print(lambda_func)

###################################################################
"""
3. Write a Python program to listify the list of given strings individually using Python map.
"""
color = ['Red', 'Blue', 'Black', 'White', 'Pink']
print("Original list:")
print(color)
print("\nAfter listify the list of strings are:")
result = list(map(list, color))
print(result)

###################################################################
"""
4. Write a Python program to create a list containing the power of said number in bases raised to
the corresponding number in the index using Python map.
"""
base = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
my_index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lambda_func = list(map(lambda x,y:x**y, base, my_index))
print(lambda_func)

###################################################################
"""
5. Write a Python program to square the elements of a list using the map() function.
"""
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
def square(x): return x**2
map_func = list(map(square, my_list))
print(map_func)

###################################################################
"""
6. Write a Python program to convert all the characters into uppercase and lowercase and eliminate
duplicate letters from a given sequence. Use the map() function.
"""
# Define a function named change_cases that converts a character to its upper and lower cases
def change_cases(s):
    return str(s).upper(), str(s).lower()
chrars = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}
print("Original Characters:\n", chrars)
result = map(change_cases, chrars)
print("\nAfter converting above characters in upper and lower cases\nand eliminating duplicate letters:")
print(set(result))

###################################################################
"""
7. Write a Python program to add two given lists and find
the difference between them. Use the map() function.
"""
def addition_subtrction(x, y):
    return x + y, x - y
nums1 = [6, 5, 3, 9]
nums2 = [0, 1, 7, 7]
print("Original lists:")
print(nums1)
print(nums2)
result = map(addition_subtrction, nums1, nums2)
print("\nResult:")
print(list(result))

###################################################################
"""
8. Write a Python program to convert a given list of integers and a tuple of integers in a list of strings.
"""
nums_list = [1, 2, 3, 4]
nums_tuple = (0, 1, 2, 3)
result_list = list(map(str, nums_list))
result_tuple = tuple(map(str, nums_tuple))
print(result_list)
print(result_tuple)


###################################################################
"""
9. Write a Python program to create a new list taking specific elements from a tuple
and convert a string value to an integer.
"""
student_data = [('Alberto Franco', '15/05/2002', '35kg'), ('Gino Mcneill', '17/05/2002','37kg'),
                ('Ryan Parkes', '16/02/1999', '39kg'), ('Eesha Hinton', '25/09/1998', '35kg')]

print("Original data:")
print(student_data)
students_data_name = list(map(lambda x: x[0], student_data))
students_data_dob = list(map(lambda x: x[1], student_data))
students_data_weight = list(map(lambda x: int(x[2][:-2]), student_data))
print(students_data_name)
print(students_data_dob)
print(students_data_weight)

###################################################################
"""
10. Write a Python program to compute the square of the first N Fibonacci numbers,
using the map function and generate a list of the numbers.
"""
import itertools
n = 10
def fibonacci_nums(x=0, y=1):
    yield x
    while True:
        yield y
        x, y = y, x + y
print("First 10 Fibonacci numbers:")
result = list(itertools.islice(fibonacci_nums(), n))
print(result)
def square(x): return x * x
print("\nAfter squaring said numbers of the list:")
print(list(map(square, result)))

###################################################################
"""
11. Write a Python program to compute the sum of elements of an array of integers.
Use the map() function. 
"""
from functools import reduce
lst = [3,6,7,9]
map_func = (map(reduce(lst)))
print(map_func)

###################################################################
"""
12. Write a Python program to compute the sum of elements of an array of integers.
Use the map() function. 
"""
from array import array
def array_sum(nums_arr):
    sum_n=0
    for n in nums_arr:
        sum_n += n
    return sum_n

nums=array('i', [1, 2, 3, 4, 5, -15])
nums_arr=list(map(int, nums))
result=array_sum(nums_arr)
print(result)

###################################################################
"""
13. Write a Python program to count the same pair in two given lists. 
use map() function.
"""
from operator import eq
def count_same_pair(nums1, nums2):
    result = sum(map(eq, nums1, nums2))
    return result
nums1 = [1, 2, 3, 4, 5, 6, 7, 8]
nums2 = [2, 2, 3, 1, 2, 6, 7, 9]
print(count_same_pair(nums1, nums2))


###################################################################
"""
14. Write a Python program to interleave two lists into another list randomly.
Use the map() function.
"""
import random
def randomly_interleave(nums1, nums2):
    iterators = [iter(nums1)] * len(nums1) + [iter(nums2)] * len(nums2)
    result = list(map(next, random.sample(iterators, len(nums1) + len(nums2))))
    return result

nums1 = [1, 2, 7, 8, 3, 7]
nums2 = [4, 3, 8, 9, 4, 3, 8, 9]
print(nums1)
print(nums2)
print(randomly_interleave(nums1, nums2))


###################################################################
"""
15. Write a Python program to split a given dictionary of lists into list
of dictionaries using the map function.
"""
def list_of_dicts(marks):
    result = map(dict, zip(*[[(key, val) for val in value] for key, value in marks.items()]))
    return list(result)

marks = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}

print(marks)
print("\n")
print(list_of_dicts(marks))

###################################################################L
"""
16. Write a Python program to convert a given list of strings into a list of
lists using the map function.

Original list of strings:
['Red', 'Green', 'Black', 'Orange']

Convert the said list of strings into list of lists:
[['R', 'e', 'd'], ['G', 'r', 'e', 'e', 'n'], ['B', 'l', 'a', 'c', 'k'], ['O', 'r', 'a', 'n', 'g', 'e']]
"""
def func(lst):
    return list(map(list, lst))
print(func(['Red', 'Green', 'Black', 'Orange']))

###################################################################L
"""
17. Write a Python program to convert a given list of tuples to a list of strings using the map function.
"""
func = lambda lst: list(map(" ".join, lst))
print(func([('red', 'pink'), ('white', 'black'), ('orange', 'green')]))


