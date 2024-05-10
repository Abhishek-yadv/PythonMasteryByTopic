####################################################################
############################################# (Exception Handling)
####################################################################

######################################################################
""" 
*Question 1:
1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero. 
"""
from numpy import apply_along_axis


def Handler(x,y):
    try:
        result = x/y
        print("result: {result}")
    except ZeroDivisionError:
        print("Can not be divided by zero")
Handler(100, 0)


# 2nd method
def Handle():
    try:
        1/0
    except Exception as e:
        print("An error occurred:", type(e).__name__, ":", str(e))
Handle()

######################################################################
""" 
*Question 2:
2. Write a Python program that prompts the user to input an integer and
raises a ValueError exception if the input is not a valid integer. 
"""
def valid_int():
    try:
        my_input = int(input("Enter the input: "))
        return my_input
    except ValueError:
        print('Not a valid integer')
valid_int()

######################################################################
""" 
*Question 3:
3. Write a Python program that opens a file and handles a FileNotFoundError exception 
if the file does not exist. Click me to see the sample solution
"""
def invalid_file():
    try:
        with open("abc.txt", 'r') as file_handle:
            contents = file_handle.read()
            return contents
    except FileNotFoundError:
        print("File not found yarr")

invalid_file()

######################################################################
""" 
*Question 5:
5. Write a Python program that opens a file and handles a 
PermissionError exception if there is a permission issue.
"""
def open_file(filename):
    try:
        with open(filename, 'w') as file:
            contents = file.read()
            print("File contents:")
            print(contents)
    except PermissionError:
        print("Error: Permission denied to open the file.")

file_name = input("Input a file name: ")
open_file(file_name)

######################################################################
""" 
*Question 6:
6. Write a Python program that executes an operation on a list and 
handles an IndexError exception if the index is out of range.
"""
def index_list(my_list, my_index):
    try:
        result = my_list[my_index]
        return result
    except IndexError:
        print("Index Error: The given index value does not exists in the given list")
my_list = [10, 12, 13]
my_index = 23
index_list(my_list, my_index)

######################################################################
""" 
*Question 7:
7. Write a Python program that prompts the user to input a number and handles
a KeyboardInterrupt exception if the user cancels the input.
"""
try:
    n = int(input("Input a number: "))
    print("You entered:", n)
except KeyboardInterrupt:
    print("Input canceled by the user.")

######################################################################
""" 
*Question 8:
8. Write a Python program that executes division and handles an ArithmeticError
exception if there is an arithmetic error.
"""
try:
    n = int(input("Input a number: "))
    d = int(input("Input divisor: "))
    result = n / d
except ValueError:
    print("Invalid Input! Please enter an integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ArithmeticError:
    print("Arithmetic Error! Cannot perform this operation")
else:
    print("Result:", result)

######################################################################
""" 
*Question 9:
# 9. Write a Python program that opens a file and handles a UnicodeDecodeError
# exception if there is an encoding issue.
"""
def open_file(filename):
    encoding = input(
        "Input the encoding (ASCII, UTF-16, UTF-8) for the file: ")
    try:
        with open(filename, 'r', encoding=encoding) as file:
            contents = file.read()
            print("File contents:")
            print(contents)
    except UnicodeDecodeError:
        print("Error: Encoding issue occurred while reading the file.")

file_name = input("Input the file name: ")
open_file(file_name)

######################################################################
""" 
*Question 10:
# 10. Write a Python program that executes a list operation and handles
# an AttributeError exception if the attribute does not exist.
"""
def list_attr(my_list, method: str, *args):
    try:
        getattr(my_list, method)(*args)
    except AttributeError:
        print("This attribute does not exist.")
my_list = [1, 2, 3, 4]
method = 'append'
list_attr(my_list, method, 5) 
print(my_list)  # Output: [1, 2, 3, 4, 5]
