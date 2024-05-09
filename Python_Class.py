########################################################
################################################# Class
#########################################################

##########################################################
""" 
*Question 1:
Write a Python program to import a built-in array
module & display the namespace of the said module. 
"""

import array
for name in array.__dict__:
    print(name)
# >>> __name__
# >>> __doc__
# >>> __package__
# >>> __loader__
# >>> __spec__
# >>> _array_reconstructor
# >>> ArrayType
# >>> array
# >>> typecodes

import builtins
for k in builtins.__dict__:
    print(k)
    
# Note: This function
class Cal(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    # Methods
    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

print("\n")
cal = Cal(5, 3)
print("Addition : ", cal.add())
print("Subtraction : ", cal.subtract())

# Print class namespace and scope
print("Class Namespace and Scope:")
for k, v in Cal.__dict__.items():
    print(f"{k}: {v}")
    print()

"""
Output:Addition :  8
Subtraction :  2
Class Namespace and Scope:
__module__: __main__

__init__: <function Cal.__init__ at 0x000001EA6BAF9120>
add: <function Cal.add at 0x000001EA6BAF9440>
subtract: <function Cal.subtract at 0x000001EA6BAFA340>
__dict__: <attribute '__dict__' of 'Cal' objects>      
__weakref__: <attribute '__weakref__' of 'Cal' objects>
__doc__: None
"""

###########################################################
""" 
# *Questions 2:
Write a Python program to create a class and display the namespace of that class.
"""  
class py_solution:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))    
    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]
for name in py_solution.__dict__:
    print(name)
    

###############################################################
"""
*Question 3:
Write a Python program to create an instance of a specified class &
display the namespace of the said instance."""
class Student: 
    def __init__(self, student_id, student_name, class_name):
        self.student_id = student_id
        self.student_name = student_name
        self.class_name = class_name 
student = Student('V12', 'Frank Gibson', 'V')
print(student.__dict__)
# Output ={'student_id': 'V12', 'student_name': 'Frank Gibson', 'class_name': 'V'}

# Things to be noted
class Namespace_display():
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        
    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y
    
my_var = Namespace_display(9,4,3) # Creating an object of the class
print("Namespace & scope of my_var Class: ")  
print()
print("Namescape      Scope")
for name, value in Namespace_display.__dict__.items():  # Using vars() function to get all attributes of the class
    print(f"{name:15}:{value}")
    
print("\nInstance variable name and values:")
for k in my_var.__dict__:
    value = getattr(my_var, k)
    print(f"{k:15} {value}")
    
"""
Output:
Namespace & scope of my_var Class: 

Namescape      Scope
__module__     :__main__
__init__       :<function Namespace_display.__init__ at 0x00000224388C9120>
add            :<function Namespace_display.add at 0x00000224388C9440>     
sub            :<function Namespace_display.sub at 0x00000224388CA340>     
__dict__       :<attribute '__dict__' of 'Namespace_display' objects>      
__weakref__    :<attribute '__weakref__' of 'Namespace_display' objects>   
__doc__        :None

Instance variable values:
x               9
y               4
"""

# 2nd thing note
class Namespace_display():
    # Define class methods
    pass

my_var = Namespace_display(9, 4, 3)
print("Instance variable values:")
for k, v in my_var.__dict__.items():
    print(f"{k}: {v}")

############################################
################ 3rd thing to note
class Car:
    # Class attributes
    brand = "Toyota"
    model = "Camry"
    year = 2022
    color = "Silver"

# Creating an instance of the Car class
my_car = Car()

print("Namescape      Scope")
# Using vars() function to get all attributes of the class
for name, value in Car.__dict__.items():
    print(f"{name:15}:{value}")

print("\nInstance variable name values:")
for k in Car.__dict__:
    value = getattr(my_car, k)
    print(f"{k:15} {value}")

"""
Output:
Namescape      Scope
__module__     :__main__
brand          :Toyota
model          :Camry
year           :2022
color          :Silver
__dict__       :<attribute '__dict__' of 'Car' objects>
__weakref__    :<attribute '__weakref__' of 'Car' objects>
__doc__        :None


Instance variable name and values:
__module__      __main__
brand           Toyota
model           Camry
year            2022
color           Silver
__dict__        {}
__weakref__     None
__doc__         None
"""

###############################################################
"""
* Question 4:
'builtins' module provides direct access to all 'built-in' identifiers of Python.
Write a Python program that imports the abs() function using the builtins module,
displays the documentation of the abs() function and finds the absolute value of - 155.
"""

from builtins import abs
class Display_doc():
    def __init__(self,n):
        self.n = n

    def dis(self):
        return "{}\n{}".format(abs.__doc__, abs(self.n))
        
display = Display_doc(-155)
print(display.dis())

# 2nd method
import builtins 
help(builtins.abs)
print(builtins.abs(-155))

##########################################################
"""
*Questions 5:
Define a Python function student().
Using function attributes display the names of all arguments.
""" 
def student(student_id, student_name, student_class):
    return f'Student ID: {student_id}\nStudent Name: {student_name}\nClass: {student_class}'
print(student('S122', 'Wilson Medina', 'VI'))

#############################################################
"""
* Question 6:
Write a Python function student_data() that will print the ID of a student(student_id).
the user passes an argument student_name or student_class the function will print the student name and class .
"""

def student_data(student_id, **kwargs):
    print("Student_Id is {}".format(student_id))
    if not student_id:
        raise ValueError("Please provide a valid student id.")
    else:
        for k, v in student_id.items():
            print(k, v)
student_data(student)

##########################################################
"""
*Question 7:
Write a simple Python class named Student and display its type.
Also, display the __dict__ attribute keys and the value of the __module__ attribute of the Student class.
"""

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(type(Student))
        print(Student.__dict__.keys())
        print(Student.__module__)

s = Student(name = "John",  age = 30)
s.show()

##########################################################
"""
*Question 8:
8. Write a Python program to create two empty classes, Student and Marks.
Now create some instances and check whether they are instances of the said classes or not.
Also, check whether the said classes are subclasses of the built-in object class or not.
"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_student(self):
        print(f"Student name is {self.name} and Age is {self.age}")

class Marks(Student):
    def __init__(self, student, grade, marks):
        super().__init__(student.name, student.age)  # Call the __init__ method of the parent class with name and age from the Student instance
        self.grade = grade
        self.marks = marks

    def show_grade(self):
        print(f"{self.name} has grade {self.grade} with total marks {self.marks}")

student_one = Student('rohan', 35)
student_one.show_student()

student_marks = Marks(student_one, 'A', 80)
student_marks.show_grade()

print("Student marks is instance of the Student? {}".format(isinstance(student_marks, Student))) #True
print("Student is subclass of the object class? {}".format(issubclass(Marks, object))) #True

# 2nd example
class Student:
    pass 
class Marks:
    pass 
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student)) # True
print(isinstance(marks1, Student))   # False
print(isinstance(marks1, Marks))     # True
print(isinstance(student1, Marks))   # False
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object)) #True
print(issubclass(Marks, object)) #True

##################################################################################
"""
*Question 9:
Write a Python class named Student with two attributes student_name, marks.
Modify the attribute values of the said class and print the original and modified values of the said attributes.
"""
class Student:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks
    
my_instance = Student('Abhishek', 34)

# Originsl class
print(my_instance.student_name) # Output: Abhishek
print(my_instance.marks) # Output: 34
# Modify class
my_instance.student_name = 'Pappu'
my_instance.marks = 50
print(my_instance.student_name)  # Output: Pappu
print(my_instance.marks)  # Output: 50


##################################################################################
"""
*Question 10:
Write a Python class named Student with two attributes student_id, student_name.
Add a new attribute student_class and display the entire attribute and the values of the class.
Now remove the student_name attribute and display the entire attribute with values.
"""
class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
    
my_instance = Student('4', "Abhishek")
for k,v in my_instance.__dict__.items():
    if not k.startswith('_'):
        print(k)
# create new atributes a student_class
my_instance.student_class = 'HighSchool'
# print all attributes
for k,v in my_instance.__dict__.items():
    if not k.startswith('_'):
        print(k)
# delete all attributes
del my_instance.student_name
for k,v in my_instance.__dict__.items():
    if not k.startswith('_'):
        print(f"{k} -> {v}")

# >>> ('student_id', '4')
# >>> ('student_name', 'Abhishek')
# >>> ('student_id', '4')
# >>> ('student_name', 'Abhishek')
# >>> ('student_class', 'HighSchool')
# >>> ('student_id', '4')
# >>> ('student_class', 'HighSchool')


##################################################################################
"""
*Question 11:
Write a Python class named Student with two attributes: student_id, student_name.
Add a new attribute: student_class. Create a function to display all attributes
and their values in the Student class.
"""

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
    
    def show(self):
        return (f"Attribute name: {self.student_name}\nAttribute value: {self.student_id}")

s = Student("2", "John")
print(s.show())
# >>> Attribute name: John
# >>> Attribute value: 2


##################################################################################
"""
*Question 12:
Write a Python class named Student with two instances student1, student2 and assign values to the instances' attributes.
Print all the attributes of the student1, student2 instances with their values in the given format.
"""
class Student:
    school = 'TVS'
    Adress = "90fit"
student1 = Student()
student2 = Student()
student1.student_id =  1
student1.student_name = "Abhishek"
student2 = Student()
student2.student_id =  2
student2.student_name = "Vivek"
for k in [student1, student2]:
    for k, v in k.__dict__.items():
        print(k,v)

#########################################################################
# 13. Write a Python class to convert an integer to a Roman numeral.
class Roman:
    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,1]
        
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV","I"]
        
        roman_numeral = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_numeral = roman_numeral +  syb[i]
                num = num - val[i]
            i = i + 1
        return roman_numeral

R = Roman()
print(R.int_to_Roman(20))  # Output: XX


#########################################################################
## 14. Write a Python class to convert a Roman numeral to an integer.
class py_solution:
    def roman_to_int(self, s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val

print(py_solution().roman_to_int('MMMCMLXXXVI'))
print(py_solution().roman_to_int('MMMM'))
print(py_solution().roman_to_int('C'))

#########################################################################
"""
*Question 12:
Write a Python class to check the validity of a string of parentheses, '(', ')', '{', '}', '[' and '].
These brackets must be closed in the correct order,
for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid..
"""
class py_solution:
    def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

print(py_solution().is_valid_parenthese("(){}[]"))
print(py_solution().is_valid_parenthese("()[{)}"))
print(py_solution().is_valid_parenthese("()"))

#########################################################################
"""
*Question 13:
Write a Python class to find a pair of elements (indices of the two numbers) from a given array 
whose sum equals a specific target number.

Note: There will be one solution for each input and do not use the same element twice.

Input: numbers= [10,20,10,40,50,60,70], target=50
Output: 2, 3
"""
# 1st method
class Solution:
    def find_indices(self, numbers, target):
        seen = {}
        for i in range(len(numbers)):
            num = numbers[i]
            complement = target - num
            if complement in seen:
                return seen[complement], i
            seen[num] = i

numbers = [10, 20, 10, 40, 50, 60, 70]
target = 50
print(Solution().find_indices(numbers, target))


# 2nd method
class py_solution:
    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i)
            lookup[num] = i
print(py_solution().twoSum((10, 20, 10, 40,50,60,70),50))


#########################################################################
""" 
14. Write a Python class to find the three elements that sum to zero from a set of n real numbers.
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]
"""
class SumZero:
    def three_sum_zero(self, nums):
        nums.sort()
        result = []
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, n-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result

# Test the function
s = SumZero()
print(s.three_sum_zero([-25, -10, -7, -3, 2, 4, 8, 10]))

#########################################################################
""" 
14. Write a Python class to find the three elements that sum to zero from a set of n real numbers.
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]
"""
# 1st method
from itertools import permutations
class Sum_Zero:
    def solution(self, arr):
        result = []
        seen = set()  # To keep track of unique combinations
        for combo in permutations(arr, 3):
            if sum(combo) == 0 and tuple(sorted(combo)) not in seen:
                result.append(sorted(combo))
                seen.add(tuple(sorted(combo)))  # Add the sorted tuple to the set
        return result

arr = [-25, -10, -7, -3, 2, 4, 8, 10]
my_instance = Sum_Zero()
print(my_instance.solution(arr))

# 2nd method


#########################################################################
""" 
15. Write a Python class to implement pow(x, n).
"""
class py_solution:
    def pow(self, num, power):
        if num == 0 or num == 1 or power == 1:
            return num

        if num == -1:
            if power % 2 == 0:
                return 1
            else:
                return -1
        # Handling power parameter scenirio
        if power == 0:
            return 1
        if power < 0:
            return 1/self.pow(num, -power)
        val = self.pow(num, power//2)
        if power % 2 == 0:
            return val*val
        return val*val*num

print(py_solution().pow(2, -3))
print(py_solution().pow(3, 5))
print(py_solution().pow(100, 0))

#########################################################################
""" 
16. Write a Python class to reverse a string word by word.
Input string : 'hello .py'
Expected Output : '.py hello'
"""
class Reverse_class:
    def Reverse(slef,my_string):
        my_list = []
        count = 1
        my_str = my_string.split()
        len_index = len(my_str)
        for k in range(len_index):
            my_list.append(my_str[len_index-count])
            count = count + 1
        return " ".join(my_list)
my_intance = Reverse_class()
print(my_intance.Reverse('hello .py'))

####################################################################
""" 
17. Write a Python class that has two methods:
get_String & print_String, get_String accept a string from the user &
print_String prints the string in upper case.
"""
class My_string:
    def __init__(self):
        self.user_string = input("Enter a String : ")
        
    def get_String(self):
        return self.user_string
    
    def print_String(self):
        print(self.user_string.upper())

obj = My_string()
obj.get_String()
obj.print_String()

##################################################################
############################################################
""" 
18. Write a Python class named Rectangle constructed from length
and width and a method that will compute the area of a rectangle.
"""
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
rec = Rectangle(5,4)
print("Area of Rectangle is", rec.area())
# >>> Area of Rectangle is 20


##################################################################
############################################################
""" 
19. Write a Python class named Circle constructed from a radius and
two methods that will compute the area and the perimeter of a circle.
"""
class Circle:
    def __inti__(self,a,b):
        self.a = a
        self.b = b
    
    def area(self):
        r=math.sqrt((self.a-self.b)**2 + (self.a+self.b)**2/4)
        pi = math.pi
        return pi*r**2

    def perimiter(self):
        r=(abs(self.a-self.b)/2)
        return 2*math.pi*r**2

import math
c = Circle(3, 6)
print("Area of Circle is ", c.area())
print("Perimiter of Circle is ", c.perimiter())   

#####################################################################
# 20. Write a Python program get class name of an instance in Python.
class Get_intances:
    pass

my_instances = Get_intances()
print(type(my_instances).__name__)
# Output : Get_intances

# 2nd example
my_list = [1,2,3,4,5]
print(type(my_list).__name__)
# Output : list

##################################################################
"""
21. Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department
and methods like calculate_emp_salary, emp_assign_department, and print_employee_details.
Sample Employee Data:
"ADAMS", "E7876", 50000, "ACCOUNTING"
"JONES", "E7499", 45000, "RESEARCH"
"MARTIN", "E7900", 50000, "SALES"
"SMITH", "E7698", 55000, "OPERATIONS"
Use 'assign_department' method to change the department of an employee.
Use 'print_employee_details' method to print the details of an employee.
Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked, which is the number of hours
worked by the employee. If the number of hours worked is more than 50,
the method computes overtime and adds it to the salary. Overtime is calculated as following formula:

overtime = hours_worked - 50
Overtime amount = (overtime * (salary / 50))
"""

class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department
        
    # calculate_emp_salary, emp_assign_department, and print_employee_details.
    def calculate_salary(self, salary, hours):
        if hours > 50:
            overtime = hours - 50
            ot_amount = overtime * (salary/50)
            return salary + ot_amount
        else:
            return salary* hours
    
    def assign_department(self, new_dep):
        self.emp_department = new_dep
        
    def print_employee_details(self):
        print("Employee ID: ", self.emp_id)


employee1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
employee2 = Employee("JONES", "E7499", 45000, "RESEARCH")
employee3 = Employee("MARTIN", "E7900", 50000, "SALES")
employee4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")

print("Original Employee Details:")
employee1.print_employee_details()
employee2.print_employee_details()
employee3.print_employee_details()
employee4.print_employee_details()
# Change the departments of employee1 and employee4
employee1.assign_department("OPERATIONS")
employee4.assign_department("SALES")

# Now calculate the overtime of the employees who are eligible:
employee2.calculate_salary(45000, 52)
employee4.calculate_salary(45000, 60)
print()
print("Updated Employee Details:")
employee1.print_employee_details()
employee2.print_employee_details()
employee3.print_employee_details()
employee4.print_employee_details()

##################################################################
"""
22. Write a Python class Restaurant with attributes like menu_items, book_table, and customer_orders,
and methods like add_item_to_menu, book_tables, and customer_order.
Perform the following tasks now:
Now add items to the menu.
Make table reservations.
Take customer orders.
Print the menu.
Print table reservations.
Print customer orders.
Note: Use dictionaries and lists to store the data.
"""
class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.book_table = []
        self.customer_orders = []

    def add_item_to_menu(self, item, price):
        self.menu_items[item] = price

    def book_tables(self, table_number):
        self.book_table.append(table_number)

    def customer_order(self, table_number, order):
        order_details = {'table_number': table_number, 'order': order}
        self.customer_orders.append(order_details)

    def print_menu_items(self):
        for item, price in self.menu_items.items():
            print("{}: {}".format(item, price))

    def print_table_reservations(self):
        for table in self.book_table:
            print("Table {}".format(table))

    def print_customer_orders(self):
        for order in self.customer_orders:
            print("Table {}: {}".format(order['table_number'], order['order']))

restaurant = Restaurant()
# Add items
restaurant.add_item_to_menu("Cheeseburger", 9.99)
restaurant.add_item_to_menu("Caesar Salad", 8)
restaurant.add_item_to_menu("Grilled Salmon", 19.99)
restaurant.add_item_to_menu("French Fries", 3.99)
restaurant.add_item_to_menu("Fish & Chips:", 15)
# Book table
restaurant.book_tables(1)
restaurant.book_tables(2)
restaurant.book_tables(3)
# Order items
restaurant.customer_order(1, "Cheeseburger")
restaurant.customer_order(1, "Grilled Salmon")
restaurant.customer_order(2, "Fish & Chips")
restaurant.customer_order(2, "Grilled Salmon")

print("\nPopular dishes in the restaurant along with their prices:")
restaurant.print_menu_items()
print("\nTable reserved in the Restaurant:")
restaurant.print_table_reservations()
print("\nPrint customer orders:")
restaurant.print_customer_orders()

##################################################################
"""
23. Write a Python class BankAccount with attributes like account_number, balance,
date_of_opening and customer_name, and methods like deposit, withdraw, and check_balance.
"""
class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
        
    def deposit(self):
        amount = float(input("Enter the amount to be deposited: "))
        if amount < 0:
            print("Please enter correct amount: ")
        else:
            self.balance = self.balance + amount
            
    def withdraw(self):
        amount = float(input("Enter the amount you want to withdraw: "))
        if amount > self.balance:
            print("Insufficient funds! Please enter correct amount.")
        elif amount < 0:
            print("Invalid transaction. Please enter positive amount.")
            
        else:
            self.balance = self.balance - amount
            
    def check_balance(self):
        print(f"Your current balance is:{self.balance}")
            
    def print_customer_details(self):
        return f"\nCustomer Name: {self.customer_name}\nAccount Number: {self.account_number}\nDate of Opening: {self.date_of_opening}"

# Input customer details
ac_no_1 = BankAccount(2345, 1000, "01-01-2011", "Toninho Takeo")
ac_no_2 = BankAccount(1234, 2000, "11-03-2011", "Astrid Rugile")
ac_no_3 = BankAccount(2312, 3000, "12-01-2009", "Orli Kerenza")
ac_no_4 = BankAccount(1395, 3000, "01-01-2011", "Luciana Chika")
ac_no_5 = BankAccount(6345, 4000, "01-05-2011", "Toninho Takeo")

print("Customer Details:")
ac_no_1.print_customer_details()
ac_no_2.print_customer_details()
ac_no_3.print_customer_details()
ac_no_4.print_customer_details()
ac_no_5.print_customer_details()

print("=============================")
ac_no_4.print_customer_details()
ac_no_4.deposit()
ac_no_4.check_balance()
ac_no_4.withdraw()
ac_no_4.withdraw()
ac_no_4.check_balance()



class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
        
    # Method to make deposit
    @staticmethod
    def deposit(acc, amount):
        if amount <= 0:
            print("Please enter a positive number.")
        else:
            acc.balance += acc.balance + amount
            return True
            
    # Method to make withdrawal
    @staticmethod
    def withdraw(acc, amount):
        if amount > acc.balance or amount <= 0:
            print("Invalid transaction!")
            return False
        else:
            acc.balance -= amount
            return True
            
    # Method to check current balance
    @staticmethod
    def check_balance(acc):
        return f"The current balance is: ${round(acc.balance, 2)}."

# Test the BankAccount class
if __name__ == "__main__":
    # Create an instance of the BankAccount class
    my_bank_account = BankAccount('123456789', 500.00, '2001-01-15', 'John Doe')
    
    # Call the methods using the dot notation (my_bank_account.methods())
    print(BankAccount.deposit(my_bank_account, 100))   # Should display True
    print(BankAccount.check_balance(my_bank_account))     # Should display "The current balance is: $600.00."</s

##################################################################
"""
24. Write a Python class Inventory with attributes like item_id, item_name, stock_count, and price,
and methods like add_item, update_item, and check_item_details.
Use a dictionary to store the item details, where the key is the item_id 
and the value is a dictionary containing the item_name, stock_count, and price.
"""
class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_id, item_name, stock_count, price):
        self.inventory[item_id] = {
            "item_name": item_name, "stock_count": stock_count, "price": price}

    def update_item(self, item_id, stock_count, price):
        if item_id in self.inventory:
            self.inventory[item_id]["stock_count"] = stock_count
            self.inventory[item_id]["price"] = price
        else:
            print("Item not found in inventory.")

    def check_item_details(self, item_id):
        if item_id in self.inventory:
            item = self.inventory[item_id]
            return f"Product Name: {item['item_name']}, Stock Count: {item['stock_count']}, Price: {item['price']}"
        else:
            return "Item not found in inventory."

inventory = Inventory()
inventory.add_item("I001", "Laptop", 100, 500.00)
inventory.add_item("I002", "Mobile", 110, 450.00)
inventory.add_item("I003", "Desktop", 120, 500.00)
inventory.add_item("I004", "Tablet", 90, 550.00)
print("Item Details:")
print(inventory.check_item_details("I001"))
print(inventory.check_item_details("I002"))
print(inventory.check_item_details("I003"))
print(inventory.check_item_details("I004"))
print("\nUpdate the price of item code - 'I001':")
inventory.update_item("I001", 100, 505.00)
print(inventory.check_item_details("I001"))
print("\nUpdate the stock of item code - 'I003':")
inventory.update_item("I003", 115, 500.00)
print(inventory.check_item_details("I003"))


##################################################################################
############# #* Questions Create a class inheritance class using super methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number
    def show_info(self):
        super().show_info()
        print(f"Role: Student, Roll Number: {self.roll_number}")
    def study(self):
        print(f"{self.name} is studying.")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    def show_info(self):
        super().show_info()
        print(f"Role: Teacher, Subject: {self.subject}")
    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

class Admin(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department
    def show_info(self):
        super().show_info()
        print(f"Role: Admin, Department: {self.department}")
    def manage(self):
        print(f"{self.name} is managing {self.department}.")

student = Student("Alice", 15, "S001")
student.show_info()
student.study()

teacher = Teacher("Mr. Smith", 35, "Mathematics")
teacher.show_info()
teacher.teach()

admin = Admin("Ms. Johnson", 40, "Administration")
admin.show_info()
admin.manage()


