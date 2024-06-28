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
8. Write a Python program to extract year, month, date and time using Lambda.
Sample Output:
2020-01-15 09:03:32.744178
2020
1
15
09:03:32.744178
"""
