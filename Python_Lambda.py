####################################################################
############################################################ Lambda
####################################################################

###################################################################
"""
1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
also create a lambda function that multiplies argument x with argument y and prints the result.
"""
from collections import namedtuple
lambda_func = lambda x,y:x+y
print(lambda_func(3,4))

###################################################################
"""
2. Write a Python program to create a function that takes one argument,
and that argument will be multiplied with an unknown given number.
"""
def func(n):
    return lambda x: n*x
result = func(2)
print("Double the number of 15 =", result(15))
result = func(3)
print("Triple the number of 15 =", result(15))
result = func(4)
print("Quadruple the number of 15 =", result(15))
result = func(5)
print("Quintuple the number 15 =", result(15))

###################################################################
"""
3. Write a Python program to sort a list of tuples using Lambda.
Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
"""
def sort_func(lst:list):
    lst.sort(key=lambda x:x[1])
    return lst
result = sort_func([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])
print(result)

###################################################################
"""
4. Write a Python program to sort a list of dictionaries using Lambda.
Original list of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'},
{'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
{'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'},
{'make': 'Samsung', 'model': 7, 'color': 'Blue'},
{'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
"""
def sort_func(lst):
    lst.sort(key=lambda x:x['color'])
    return lst
result = sort_func([{'make': 'Nokia', 'model': 216, 'color': 'Black'},
                    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
                    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}])
print(result)

###################################################################
"""
5. Write a Python program to filter a list of integers using Lambda.
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
"""
def filter_func(lst):
    even_lst = list(filter(lambda x: x % 2 == 0, lst))
    odd_lst = list(filter(lambda x: x % 2 != 0, lst))
    return "Even numbers from the said list:{}\nOdd numbers from the said list:{}".format(even_lst,odd_lst)
result = filter_func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(result)

###################################################################
"""
6. Write a Python program to square and cube every number in a given list
of integers using Lambda Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Square every number of the said list:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Cube every number of the said list:
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
"""
def exp_func(lst):
    square = list(map(lambda x: x**2, lst))
    cube = list(map(lambda x: x**3, lst))
    return "Square every number of the said list:{}\nCube every number of the said list:{}".format(square, cube)
result = exp_func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(result)

###################################################################
"""
7. Write a Python program to find if a given string starts with a given character using Lambda.
Sample Output:
True
False
"""
# 1st method
starts_with = lambda x: True if x.startswith('P') else False
print(starts_with('Python'))
print(starts_with('Java')) 


# 2nd method custom function
def check_str(my_string):
    result =  lambda x: True if x.startswith('a') else False
    return result(my_string)

print(check_str("ram"))  # Should print False
print(check_str("apple"))  # Should print True


###################################################################
"""
8. Write a Python program to extract year, month, date and time using Lambda.
Sample Output:
2020-01-15 09:03:32.744178
2020
1
15
09:03:32.744178
"""
# 1st.lambda function
import datetime
print(datetime.datetime.now())
func = lambda my_datetime: "{}\n{}\n{}\n{}".format(my_datetime.year, my_datetime.month, my_datetime.day, my_datetime.time())
print(func(datetime.datetime.now()))

# 2nd custom function
import datetime
def func(my_datetime):
    yr = my_datetime.year
    mnth = my_datetime.month
    dy = my_datetime.day
    tme = my_datetime.time()
    return "{}\n{}\n{}\n{}".format(yr, mnth, dy, tme)

# Test the function
print(func(datetime.datetime.now()))
print(func("ram", "a"))
print(func("apple", "a"))

###################################################################
"""
9. Write a Python program to check whether a given string is a number or not using Lambda.
"""
func = lambda strng: True if strng.isnumeric() else False
print(func("abhs"))


###################################################################
"""
10. Write a Python program to create Fibonacci series up to n using Lambda.
Fibonacci series upto 2:
[0, 1]
Fibonacci series upto 5:
[0, 1, 1, 2, 3]
"""
from functools import reduce
fib_func = fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])
print(fib_func(0))

###################################################################
"""
11. Write a Python program to find the intersection of two given arrays using Lambda.
Original arrays:
[1, 2, 3, 5, 7, 8, 9, 10]
[1, 2, 4, 8, 9]
Intersection of the said arrays: [1, 2, 8, 9]
"""
inter_sec = lambda arr1, arr2: [x for x in arr1 if x in arr2]
print(inter_sec([1, 2, 3, 5, 7, 8, 9, 10],
                [1, 2, 4, 8, 9]))

###################################################################
"""
12. Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
Original arrays:
[-1, 2, -3, 5, 7, 8, 9, -10]
Rearrange positive and negative numbers of the said array:
[2, 5, 7, 8, 9, -10, -3, -1]
"""
lambda_func = lambda lst : [x for x in lst if x > 0] + sorted([x for x in lst if x < 0], reverse = False)
print(lambda_func([-1, 2, -3, 5, 7, 8, 9, -10]))


###################################################################
"""
13. Write a Python program to count the even and odd numbers in a given array of integers using Lambda.
Original arrays:
[1, 2, 3, 5, 7, 8, 9, 10]
Number of even numbers in the above array: 3
Number of odd numbers in the above array: 5
"""
lambda_func = lambda lst : \
"Number of even numbers in the above array: {}\nNumber of odd numbers in the above array: {}"\
    .format(len([x for x in lst if x % 2 == 0]), len([x for x in lst if x%2 != 0]))
print(lambda_func([1, 2, 3, 5, 7, 8, 9, 10]))

###################################################################
"""
14. Write a Python program to filter a given list to determine if the 
values in the list have a length of 6 using Lambda.
Sample Output:
Monday Friday Sunday
"""
# Create a list 'weekdays' containing the names of the days of the week
weekdays = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']
days = filter(lambda day: True if len(day) == 6 else False, weekdays)
for d in days:
    print(d)

###################################################################
"""
15. Write a Python program to add two given lists using map and lambda.
Original list:
[1, 2, 3]
[4, 5, 6]
Result: after adding two list
[5, 7, 9]
"""
lst1, lst2 = [1, 2, 3], [4, 5, 6]
result = list(map(lambda x, y: x + y, lst1, lst2))
print(result)

###################################################################
"""
16. Write a Python program to find the second lowest total marks of any student(s)
from the given names and marks of each student using lists and lambda.
Input the number of students, the names and grades of each student.
Input number of students: 5
Name: S ROY Grade: 1
Name: B BOSE Grade: 3
Name: N KAR Grade: 2
Name: C DUTTA Grade: 1
Name: G GHOSH Grade: 1
Names and Grades of all students:
[['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]
Second lowest grade: 2.0
Names:
N KAR
"""
students = []  
sec_name = []  
second_low = 0  
n = int(input("Input number of students: "))
for _ in range(n):
    s_name = input("Name: ")
    score = float(input("Grade: "))
    students.append([s_name, score])
print("\nNames and Grades of all students:")
print(students)

order = sorted(students, key=lambda x: int(x[1]))
for i in range(n):
    if order[i][1] != order[0][1]:
        second_low = order[i][1]
        break
print("\nSecond lowest grade: ", second_low)

sec_student_name = [x[0] for x in order if x[1] == second_low]
sec_student_name.sort() 
print("\nNames:")
for s_name in sec_student_name:
    print(s_name)

###################################################################
"""
17. Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.
Orginal list:
[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
Numbers of the above list divisible by nineteen or thirteen:
[19, 65, 57, 39, 152, 190]
"""
lambda_func = lambda lst: [x for x in lst if x%19==0 or x%13==0]
print(lambda_func([19, 65, 57, 39, 152, 639, 121, 44, 90, 190]))

###################################################################
"""
18. Write a Python program to find palindromes in a given list of strings using Lambda.
Orginal list of strings:
['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
List of palindromes:
['php', 'aaa']
"""
lambda_func = lambda lst: [x for x in lst if (lambda x: x == x[::-1])(x)]
print(lambda_func(['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']))

lambda_func = lambda lst : list(filter(lambda x: x == x[::-1], lst))
print(lambda_func(['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']))

###################################################################
"""
19. Write a Python program to find all anagrams of a string in a given list of strings using Lambda.
Orginal list of strings:
['bcda', 'abce', 'cbda', 'cbea', 'adcb']
Anagrams of 'abcd' in the above string:
['bcda', 'cbda', 'adcb']
"""
lambda_func = lambda lst, ang: [x for x in lst if sorted(ang) == sorted(x)]
print(lambda_func(['bcda', 'abce', 'cbda', 'cbea', 'adcb'], 'abcd'))


###################################################################
"""
20. Write a Python program to find the numbers in a given string and store them in a list.
Afterward, display the numbers that are longer than the length of the list in sorted form.
Use the lambda function to solve the problem.
Original string: sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5
Numbers in sorted form:
20 23 56
"""
original_str = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"

lambda_fun = lambda strn: sorted([int(x) for x in strn.split() if x.isdigit() and int(x) > len([int(x) for x in strn.split() if x.isdigit()])])
result = lambda_fun(original_str)
print("Numbers in sorted form:")
print(result)

###################################################################
"""
21. Write a Python program that multiplies each number in a list with a given number
using lambda functions.
Print the results.
Original list: [2, 4, 6, 9, 11]
Given number: 2
Result:
4 8 12 18 22
"""
lambda_func = lambda lst, num:[x*num for x in lst]
print(lambda_func([2, 4, 6, 9, 11], 2))


###################################################################
"""
22. Write a Python program that sums the length of a list of names after removing
those that start with lowercase letters. Use the lambda function.
Result:
16
"""
sample_names = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']
sample_names = list(filter(lambda el: el[0].isupper() and el[1:].islower(), sample_names))
print("Result:")
print(len(''.join(sample_names)))

###################################################################
"""
23. Write a Python program to calculate the sum of the positive and negative numbers 
of a given list of numbers using the lambda function.
Original list: [2, 4, -6, -9, 11, -12, 14, -5, 17]
Sum of the positive numbers: -32
Sum of the negative numbers: 48
"""
lambda_func = lambda lst: "Sum of the positive numbers: {}\
                            \nSum of the negative numbers: {}".format(sum([x for x in lst if x <0]), sum([x for x in lst if x>0]))
print(lambda_func([2, 4, -6, -9, 11, -12, 14, -5, 17]))

###################################################################
"""
24. Write a Python program to find numbers within a given range where
every number is divisible by every digit it contains.
Sample Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
"""
def divisible_by_digits(start_num, end_num):
    return [n for n in range(start_num, end_num + 1) if not any(map(lambda x: int(x) == 0 or n % int(x) != 0, str(n)))]
print(divisible_by_digits(1, 22))

###################################################################
"""
25. Write a Python program to create the next bigger number by
rearranging the digits of a given number.
Original number: 12
Next bigger number: 21
Original number: 10
Next bigger number: False
Original number: 201
Next bigger number: 210
Original number: 102
Next bigger number: 120
Original number: 445
Next bigger number: 454
"""
from itertools import permutations
next_bigger_number = lambda n: min((int(''.join(p)) for p in permutations(str(n)) if int(''.join(p)) > n), default=False)
# Test cases
numbers = [12, 10, 201, 102, 445]
results = {number: next_bigger_number(number) for number in numbers}
for original, next_bigger in results.items():
    print(f"Original number: {original}")
    print(f"Next bigger number: {next_bigger}")

###################################################################
"""
26. Write a Python program to find a list with maximum and minimum length using lambda.
Original list:
[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
List with maximum length of lists:
(3, [13, 15, 17])
List with minimum length of lists:
(1, [0])
"""
# 1st method
def max_func(lst):
    max_lst =  max(lst, key=lambda x: len(x))
    return (len(max_lst), max_lst)
def min_func(lst):
    min_lst =  min(lst, key = lambda x:len(x))
    return (len(min_lst), min_lst)

print(max_func([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]))
print(min_func([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]))

# 2nd method
def max_func(lst):
    max_len = max(len(x) for x in lst)
    max_lst = [k for k in lst if len(k) == max_len]
    return (max_len, *max_lst)

def min_func(lst):
    min_len = min(len(x) for x in lst)
    min_lst = [k for k in lst if len(k) == min_len]
    return (min_len, *min_lst)

print(max_func([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]))
print(min_func([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]))

# Read
def custom_sort(data, key_func):
    return sorted(data, key=key_func)
# Example usage
data = ['apple', 'banana', 'cherry', 'date']
sorted_data = custom_sort(data, key_func=len)
print(sorted_data)  # Output: ['apple', 'date', 'banana', 'cherry']


###################################################################
"""
27. Write a Python program to sort each sublist of strings in a given list of lists using lambda.
Original list:
[['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
After sorting each sublist of the said list of lists:
[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
"""
# Lambda function to sort each sublist
lambda_func = lambda lst: list(map(lambda x:sorted(x), lst))
print(lambda_func([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]))


###################################################################
"""
28. Write a Python program to sort a given list of lists by length and value using lambda.
Original list:
[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
Sort the list of lists by length and value:
[[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]
"""
lambda_func = lambda big_list: sorted(big_list, key = lambda x: (len(x), x))
# Sorting the original list
sorted_list = lambda_func([[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]])

print("Original list:")
print("Sort the list of lists by length and value:")
print(sorted_list)

###################################################################
"""
29. Write a Python program to find the maximum value in a given heterogeneous list using lambda.
Original list:
['Python', 3, 2, 4, 5, 'version']
Maximum values in the said list using lambda:
5
"""
lambda_func = lambda big_list: max([k for k in big_list if type(k) != str])
print("Maximum values in the said list using lambda:")
print(lambda_func(['Python', 3, 2, 4, 5, 'version']))

# Define a function 'max_val' that takes a list 'list_val' as input
def max_val(list_val):
    max_val = max(list_val, key=lambda i: (isinstance(i, int), i))
    return max_val
list_val = ['Python', 3, 2, 4, 5, 'version']

print("Original list:")
print(list_val)
print("\nMaximum values in the said list using lambda:")
print(max_val(list_val)) 


###################################################################
"""
30. Write a Python program to sort a given matrix in ascending order according
to the sum of its rows using lambda.
Original Matrix:
[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
Sort the said matrix in ascending order according to the sum of its rows
[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
Original Matrix:
[[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
Sort the said matrix in ascending order according to the sum of its rows
[[-2, 4, -5], [1, -1, 1], [1, 2, 3]]
"""
lambda_func = lambda matrix: sorted(matrix, key = lambda x: sum(x))
print(lambda_func([[1, 2, 3], [2, 4, 5], [1, 1, 1]]))
print(lambda_func([[1, 2, 3], [-2, 4, -5], [1, -1, 1]]))

###################################################################
"""
31. Write a Python program to extract a specified size of strings from a given
list of string values using lambda.
Original list:
['Python', 'list', 'exercises', 'practice', 'solution']
length of the string to extract:
8
After extracting strings of specified length from the said list:
['practice', 'solution']
"""
lambda_func = lambda lst: list(filter(lambda x:len(x)==8, lst))
print(lambda_func(['Python', 'list', 'exercises', 'practice', 'solution']))

###################################################################
"""
32. Write a Python program to count float values in a mixed list using lambda.
Original list:
[1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
Number of floats in the said mixed list:
3
"""
lambda_func = lambda lst: list(filter(lambda i: isinstance(i, float), lst))
print(lambda_func([1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]))

###################################################################
"""
33. Write a Python program to check whether a given string contains a capital letter,
a lower case letter, a number and a minimum length using lambda.
Input the string: W3resource
['Valid string.']
"""
import re
lambda_func = lambda s: (len(s) >= 8 and
                        any(c.islower() for c in s) and
                        any(c.isupper() for c in s) and
                        any(c.isdigit() for c in s))
input_string = "W3resource"
result = ["Valid string."] if lambda_func(input_string) else ["Invalid string."]
print("Input the string:", input_string)
print(result)

###################################################################
"""
34. Write a Python program to filter the height and width of students,
which are stored in a dictionary using lambda.
Original Dictionary:
{'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}

Height> 6ft and Weight> 70kg:

{'Cierra Vega': (6.2, 70)}
"""
def filter_data(students):
    result = dict(filter(lambda x: (x[1][0], x[1][1]) > (6.0, 70), students.items()))    
    return result  

students = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}

print("Original Dictionary:")
print(students)

print("\nHeight > 6ft and Weight > 70kg:")
print(filter_data(students)) 

###################################################################
"""
35. Write a Python program to check whether a specified list is sorted or not using lambda.
Original list:
[1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
Is the said list is sorted!
True
Original list:
[1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
Is the said list is sorted!
False
"""
lambda_func = lambda lst: sorted(lst) == lst
print(lambda_func([1, 2, 4, 20, 8, 10, 12, 14, 16, 17]))


###################################################################
"""
36. Write a Python program to extract the nth element from a given list of tuples using lambda.
Original list:
[('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
Extract nth element ( n = 0 ) from the said list of tuples:
['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
"""
lambda_func = lambda lst,n : [x[n] for x in lst]
result = lambda_func([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96),
            ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)], 0)
print(result)

# 2nd way
lambda_func = lambda lst,n : list(map(lambda x:x[n], lst))
result = lambda_func([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96),
                    ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)], 2)
print(result)

###################################################################
"""
37. Write a Python program to sort a list of lists by a given index of the inner list using lambda.
Original list:
[('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
Sort the said list of lists by a given index ( Index = 0 ) of the inner list
[('Beau Turnbull', 94, 98), ('Brady Kent', 97, 96), ('Greyson Fulton', 98, 99), ('Wyatt Knott', 91, 94)]
"""
lambda_func = lambda lst,i: list(sorted(lst, key = lambda x:x[i]))
result = lambda_func([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)],0)
print(result)


###################################################################
"""
38. Write a Python program to remove all elements from a given list present in another list using lambda.
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]
Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
"""
lambda_func = lambda lst1, lst2: list(set(lst1)-set(lst2))
result = lambda_func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8])
print(result)

# or
lambda_func = lambda lst1, lst2: [x for x in lst1 if x not in lst2]
result = lambda_func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8])
print(result)

# OR
lambda_func = lambda lst1, lst2: list(filter(lambda x: x not in lst2, lst1))
result = lambda_func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8])
print(result)

###################################################################
"""
39. Write a Python program to find the elements of a given list of strings
that contain a specific substring using lambda.
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search: ack
"""
lambda_func = lambda lst, mystr: list(filter(lambda k: mystr in k, lst))
print(lambda_func(['red', 'black', 'white', 'green', 'orange'], "ack"))

###################################################################
"""
40. Write a Python program to find the nested list elements, which are present in another list using lambda.
"""
# Original lists
main_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
nested_lists = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
lambda_func = lambda lst, main_lst: [list(filter(lambda x: x in main_lst, sublist)) for sublist in lst]
result = lambda_func(nested_lists, main_list)

###################################################################
"""
41. Write a Python program to reverse strings in a given list of string values using lambda.
Original lists:
['Red', 'Green', 'Blue', 'White', 'Black']
Reverse strings of the said given list:
['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
"""
lambda_func = lambda lst: list(map(lambda x:x[::-1], lst))
result = lambda_func(['Red', 'Green', 'Blue', 'White', 'Black'])
print(result)

###################################################################
"""
42. Write a Python program to calculate the product of a given list of numbers using lambda.
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Product of the said list numbers:
3628800
list2: [2.2, 4.12, 6.6, 8.1, 8.3]
Product of the said list numbers:
4021.8599520000007
"""
from functools import reduce
from operator import mul
lambda_func = lambda lst: reduce(mul, lst)
print(lambda_func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# 2nd method
import math
def calculate_product_2(lst): return math.prod(lst)

###################################################################
"""
43. Write a Python program to multiply all the numbers in a given list using lambda 
"""
import math
lambda_func = lambda lst: math.prod(lst)

###################################################################
"""
44. Write a Python program to calculate the average value of the numbers in a given
tuple of tuples using lambda.
Original Tuple:
((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
Average value of the numbers of the said tuple of tuples:
(30.5, 34.25, 27.0)
"""
lambda_func = lambda tpl: ((sum(k)/len(k)) for k in tpl)
print(*lambda_func(((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))))

###################################################################
"""
45. Write a Python program to convert string elements to integers inside a given tuple using lambda.
Original tuple values:
(('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))
New tuple values:
((233, 33), (1416, 55), (2345, 34))
"""
# Original tuple
original_tuple = (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))

# Correct lambda function to convert string elements to integers
lambda_func = lambda tpl: tuple(tuple(int(elem) for elem in sub_tup if elem.isdigit()) for sub_tup in tpl)
result = lambda_func(original_tuple)
print("Original tuple values:", original_tuple)
print("New tuple values:", result)

# 2nd method
original_tuple = (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))
convert_to_int = lambda x: int(x) if x.isdigit() else None
process_tuple = lambda t: tuple(filter(None, map(convert_to_int, t)))
lambda_func = lambda tpl: tuple(map(process_tuple, tpl))
result = lambda_func(original_tuple)
print("Original tuple values:", original_tuple)
print("New tuple values:", result)

###################################################################
"""
46. Write a Python program to find the index position and value of the maximum and
minimum values in a given list of numbers using lambda.
Original list: [12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]

Index position and value of the maximum value of the said list: (5, 89)
Index position and value of the minimum value of the said list: (3, 10.11)
"""
# 1st method
lambda_func = lambda lst: (lst.index((max([k for k in lst]))), max([k for k in lst]))
print(lambda_func([12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]))

# 2nd method
print("Index position and value of the maximum value of the said list:")
lambda_func = lambda lst: max(enumerate(lst), key=lambda x: x[1])
print(lambda_func([12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]))
print("Index position and value of the minimum value of the said list:")
lambda_func = lambda lst: max(enumerate(lst), key=lambda x: x[1])
print(lambda_func([12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]))

###################################################################
"""
47. Write a Python program to sort a given mixed list of integers and strings using lambda.
Numbers must be sorted before strings.
Original list:
[19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
Sort the said mixed list of integers and strings:
[1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']
"""
lambda_func = lambda lst: sorted(lst, key=lambda x: (isinstance(x, str), x if isinstance(x, str) else float(x)))
print(lambda_func([19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]))


###################################################################
"""
48. Write a Python program to sort a given list of strings (numbers) numerically using lambda.
Original list: ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
Sort the said list of strings(numbers) numerically:
['-500', '-12', '0', '4', '7', '12', '45', '100', '200']
"""
lambda_func = lambda lst: sorted(lst, key=lambda x: float(x))
print(lambda_func(['4', '12', '45', '7', '0', '100', '200', '-12', '-500']))

###################################################################
"""
49. Write a Python program to count the occurrences of items in a given list using lambda .
Original list:
[3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
Count the occurrences of the items in the said list:
{3: 4, 4: 2, 5: 3, 8: 2, 0: 2, 1: 1, 2: 2}
"""
from collections import Counter
lambda_func = lambda lst: Counter(lst)
print(lambda_func(*[3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]))

###################################################################
"""
50. Write a Python program to remove specific words from a given list using lambda .
Original list: ['orange', 'red', 'green', 'blue', 'white', 'black']
Remove words: ['orange', 'black']
After removing the specified words from the said list: ['red', 'green', 'blue', 'white']
"""
lambda_func = lambda lst1, lst2 : [k for k in lst1 if k not in lst2]
print(lambda_func(['orange', 'red', 'green', 'blue', 'white', 'black'], ['orange', 'black']))

###################################################################
"""
51. Write a Python program to find the maximum and minimum values in a given list of tuples using the lambda function.
Original list with tuples: [('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
Maximum and minimum values of the said list of tuples: (74, 62)
"""
lambda_func = lambda lst: max(lst, key=lambda x:x[1])[1]
lambda_func = lambda lst: min(lst, key=lambda x:x[1])[1]
print(lambda_func([('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]))

###################################################################
"""
52. Write a Python program to remove None values from a given list using the lambda function.
Original list:
[12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
Remove None value from the said list:
[12, 0, 23, -55, 234, 89, 0, 6, -12]
"""
lambda_func = lambda lst: list(filter(None, lst))
print(lambda_func([12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]))