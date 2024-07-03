####################################################################
############################################################ Lambda
####################################################################

###################################################################
"""
1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
also create a lambda function that multiplies argument x with argument y and prints the result.
"""
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

