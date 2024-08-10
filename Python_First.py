####################################################################
######################################################## (Basic)
####################################################################
"""
1. Write a Python program to print the following string in a specific format (see the output).
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
Output :

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
"""
import sys  # Import the sys module to use sys.getsizeof()
import time
import os.path
print("""
print("Twinkle, twinkle, little star,
\n\tHow I wonder what you are! \n\t\t
Up above the world so high,
\n\t\tLike a diamond in the sky.
\nTwinkle, twinkle, little star,
\n\tHow I wonder what you are!")
""")

"""
1. Write a Python program to print the following string in a specific format (see the output).
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
Output :

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
"""

"""
2. Write a Python program to find out what version of Python you are using.
"""
import sys
print(sys.version)
print()
print("Python Version")
print(sys.version_info)

""" 
3. Write a Python program to display the current date and time.
"""
import datetime
print("Current date and time: ")
print(datetime.datetime.now())

""" 
4. Write a Python program that calculates the area of a circle
based on the radius entered by the user.
"""
import math
radius = int(input())
area = math.pi * radius * radius

""" 
5. Write a Python program that accepts the user's first and last name
and prints them in reverse order with a space between them.
"""
first_name = input("Enter Your First Name: ")
last_name = input("Enter Your last Name: ")
print(f"{last_name} {first_name}")
print("Hello  " + last_name +" " + first_name)

""" 
6. Write a Python program that accepts a sequence of comma-separated numbers
from the user and generates a list and a tuple of those numbers.
"""
# Prompt the user to input a sequence of comma-separated numbers and store it in the 'values' variable
values = input("Input some comma-separated numbers: ")
list = values.split(",")
tuple = tuple(list)
print('List : ', list)
print('Tuple : ', tuple)

""" 
7. Write a Python program that accepts a filename from the user and 
prints the extension of the file.
Sample filename : abc.java
Output : java
"""
file_ex = input("Enter ile extentions: ")
ext = file_ex.split(sep=".")
print(ext[1])

""" 
8. Write a Python program to display the first and last colors from the following list.
"""
color_list = ["Red", "Green", "White", "Black"]
print(color_list[0], color_list[-1])

""" 
9. Write a Python program to display the examination schedule.
(extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
"""
exam_st_date = (11, 12, 2014)
print(f"The examination will start from: {exam_st_date[0]} / {exam_st_date[1]} / {exam_st_date[2]}")

""" 
10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
"""
my_input = int(input("Enter your number: "))
result = my_input + my_input*my_input + my_input*my_input*my_input
print(result)

""" 
11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.
"""
samp_func = abs
print(samp_func.__doc__)
print("Help")
print(help(samp_func))

""" 
12. Write a Python program that prints the calendar for a given month and year.
Note : Use 'calendar' module.
"""
import calendar
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))
print(calendar.month(yy, mm))

""" 
13. Write a Python program to print the following 'here document'.
Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example.
"""
# Use triple double-quotes to create a multi-line string
print(""" a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example """)

""" 
14. Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days.
"""
import datetime
date1 = datetime.date(2014, 7, 2)
date2 = datetime.date(2014, 7, 11)
date_diff = date2 - date1
print(date_diff)

""" 
15. Write a Python program to get the volume of a sphere with radius six.
"""
import math
def get_volume(radius):
    return (4/3) * math.pi * radius**3
radius = 6
volume = get_volume(radius)
print(f"The volume of the sphere with radius {radius} is {volume}")

""" 
16. Write a Python program to calculate the difference between a given number and 17.
If the number is greater than 17, return twice the absolute difference.
"""
def func():
    num = int(input("Enter your number: "))
    if num > 17:
        return (num - 17) * 2
    else:
        return 17 - num
print(func())

""" 
17. Write a Python program to test whether a number is within 100 of 1000 or 2000.
"""
def near_thousand(n):
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
print(near_thousand(1000))
print(near_thousand(900))

""" 
18. Write a Python program to calculate the sum of three given numbers. 
If the values are equal, return three times their sum..
"""
def sum_thrice(x, y, z):
    sum = x + y + z
    if x == y == z:
        sum = sum * 3
    return sum
print(sum_thrice(1, 2, 3))
print(sum_thrice(3, 3, 3))

""" 
19. Write a Python program to get a newly-generated string from a given string where
"Is" has been added to the front. Return the string unchanged
if the given string already begins with "Is".
"""
def new_string(text):
    if len(text) >= 2 and text[:2] == "Is":
        return text
    else:
        return "Is" + text
print(new_string("Array"))
print(new_string("IsEmpty"))

""" 
20. Write a Python program that returns a string that is n (non-negative integer) copies of a given string.
"""
def copy(strng, n):
    return strng * n
print(copy("abc", 3))

""" 
21. Write a Python program that determines whether a given number (accepted from the user)
is even or odd, and prints an appropriate message to the user."""
def copy(num):
    return "Even" if num % 2 == 0 else "Odd"
print(copy(5))

""" 
22. Write a Python program to count the number 4 in a given list.
"""
lambda_func = lambda lst: lst.count(4)
my_list = [1,2,4,2,4,6,4,3]
print(lambda_func(my_list))

def func(lst):
    count = 0
    for k in lst:
        if k == 4:
            count+=1
    return count

""" 
23. Write a Python program to get n (non-negative integer) copies of the first 2 characters 
of a given string. Return n copies of the whole string if the length is less than 2..
"""
def func(strn, n):
    if len(strn) < 2:
        return strn * n
    else:
        return strn[:2]*2

print(func("ab", 5))
print(func("abcd", 5))

# 2nd method
def func(strn, n):
    return strn * n if len(strn) < 2 else strn[:2]*2
print(func("a", 5))
print(func("abcd", 5))

""" 
24. Write a Python program to test whether a passed letter is a vowel or not.
"""
vowels = 'aeiou'
def func(strn):
    return strn in vowels
print(func('a'))

""" 
25. Write a Python program that checks whether a specified value is contained
within a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False.
"""
def is_group_member(group_data, n):
    for value in group_data:
        if n == value:
            return True  
    return False  
print(is_group_member([1, 5, 8, 3], 3))  
print(is_group_member([5, 8, 3], -1))    

"""
26. Write a Python program to create a histogram from a given list of integers.
"""
def hist(lst):
    for k in lst:
        print("*" * k)
# Example usage
hist([2, 5, 3, 8])

"""
27. Write a Python program that concatenates all elements in a list into a string and returns it.    
"""
lambda_func = lambda lst: "".join(str(k) for k in lst)
print(lambda_func([11, 23, 54, 76]))

""" 
28. Write a Python program to print all even numbers from a given list of numbers
in the same order and stop printing any after 237 in the sequence. """
# Sample numbers list :
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527]
def func(lst):
    for k in lst:
        if k != 237 and k%2==0:
            print(k)
print(func(numbers))

""" 
29. Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.
Test Data :
"""
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
diff = color_list_1.difference(color_list_2)
print(diff)

# OR
my_set = set()
for k in color_list_1:
    if k not in color_list_2:
        my_set.add(k)
print(my_set)

""" 
30. Write a Python program that will accept the base and height of a triangle and compute its area.
"""
def area(base, height):
    return 1/2* base * height
print(area(9,7))

""" 
31. Write a Python program that computes the greatest common divisor (GCD) of two positive integers.
"""
def gcd(x, y):
    gcd = 1
    if x % y == 0:
        return y
    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break
        return gcd
print("GCD of 12 & 17 =", gcd(12, 17))
print("GCD of 4 & 6 =", gcd(4, 6))

# OR
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print("GCD of 12 & 17 =", gcd(12, 17))
print("GCD of 4 & 6 =", gcd(4, 6))


""" 
32. Write a Python program to find the least common multiple (LCM) of two positive integers.
"""
def lcm(a, b):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    return abs(a * b) // gcd(a, b)

print("GCD of 12 & 17 =", lcm(12, 17))
print("GCD of 4 & 6 =", lcm(4, 6))


""" 
33. Write a Python program to sum three given integers. However,
if two values are equal, the sum will be zero.
"""
def func(x,y,z):
    if x == y or y == z or x == z:
        sum = 0
    else:
        sum = x + y + z
    return sum
print(func(2,3,4))

""" 
34. Write a Python program to sum two given integers. However,
if the sum is between 15 and 20 it will return 20..
"""
def func(a, b):
    sum = a + b
    return 20 if 15 < sum < 20 else sum
print(func(12, 3))

""" 
35. Write a Python program that returns true if the two given integer values
are equal or their sum or difference is 5.
"""
def func(a,b):
    if a == b or abs(a-b) == 5 or (a+b) == 5:
        return True
    else:
        return False
print(func(3,3))

""" 
36. Write a Python program to add two objects if both objects are integers.
"""
def func(q,p):
    if type(q) == int and type(q) == int:
        return q + p
    else:
        print("numbers are not integers")
        
def func(q, p):
    return q + p if type(q) == int and type(q) == int else print("numbers are not integers")

""" 
37. Write a Python program that displays your name, age, and address on three different lines.
"""
def personal_details():
    name, age = "Simon", 19
    address = "Bangalore, Karnataka, India"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))
personal_details()

""" 
38. Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49
"""
def func(x,y):
    return (x+y) ** 2
func = lambda x,y: (x+y)**2
print(func(4,3))

""" 
39. Write a Python program to compute the future value of a specified principal amount,
rate of interest, and number of years.
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79
"""
def interest():
    amt = int(input("Enter your amount: "))
    integer = int(input("Enter Your integer: "))
    years = int(input("Enter Years: "))
    return amt * ((1 + (0.01 * integer)) ** years)
print(interest())

""" 
40. Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).
"""
def distance(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**1/5
print(distance(2,5,7,2))

""" 
41. Write a Python program to check whether a file exists.
"""
import os.path
print(os.path.isfile('main.txt'))
print(os.path.isfile('main.py'))

""" 
42. Write a Python program to determine if a Python shell is
executing in 32bit or 64bit mode on OS.
"""
import struct
print(struct.calcsize("P") * 8)

""" 
43. Write a Python program to get OS name, platform and release information.
"""
# Import the 'platform' and 'os' modules.
import platform
import os
print("Name of the operating system:", os.name)
print("\nName of the OS system:", platform.system())
print("\nVersion of the operating system:", platform.release())

""" 
44. Write a Python program to locate Python site packages.
"""
import site
print(site.getsitepackages())

""" 
45. Write a Python program that calls an external command.
"""
from subprocess import call
result = call(["ls", "-l"])
print(f"Command exited with status code: {result}")

""" 
46. Write a Python program to retrieve the path and name of the file currently being executed.
"""
import os
print(os.getcwd())

# Import the 'os' module to work with the operating system.
import os
print("Current File Name: ", os.path.realpath(__file__))

""" 
47. Write a Python program to find out the number of CPUs used.
"""
import multiprocessing
cpu_count = multiprocessing.cpu_count()
print(cpu_count)

""" 
48. Write a Python program to parse a string to float or integer.
"""
n = "246.2458"
print(float(n))
print(int(float(n)))

""" 
49. Write a Python program to list all files in a directory.
"""
import os
print(os.listdir())

""" 
50. Write a Python program to print without a newline or space.
"""
for i in range(0, 10):
    print('*', end="")
print("\n")

"""  
51. Write a Python program to determine the profiling of Python programs.
Note: A profile is a set of statistics that describes how often and
    for how long various parts of the program executed. 
These statistics can be formatted into reports via the pstats module.
"""
import time
def dec(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()  # Start the timer
        print("*******************")
        result = func(*args, **kwargs)  # Call the decorated function
        print("*******************")
        end = time.perf_counter()  # End the timer
        elapsed_time = end - start
        print(f"Elapsed time: {elapsed_time:.8f} seconds")
        return result
    return wrapper

@dec
def func(a, b):
    return a + b

result = func(4, 6)
print(f"Result: {result}")

"""  
52. Write a Python program to print to STDERR.
"""
from __future__ import print_function
import sys
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
eprint("abc", "efg", "xyz", sep="--")

"""  
53. Write a Python program to access environment variables.
"""
import os
print('*----------------------------------*')
print(os.environ)
print('*----------------------------------*')
print(os.environ.get('HOME', 'HOME not found'))
print('*----------------------------------*')
print(os.environ.get('PATH', 'PATH not found'))
print('*----------------------------------*')

# 2nd ways
import os
for data in os.environ:
    print(data)
    print('-' * 15)
    print(os.environ[data])
    print('=' * 30)

# 3rd ways
import os
for item, value in os.environ.items():
    print('{}: {}'.format(item, value))

# 4th ways
import os
for item in os.environ:
    print('{}: {}'.format(item, os.environ[item]))

"""  
54. Write a Python program to get the current username.
"""
import getpass
print(getpass.getuser())

""" 
55. Write a Python program to find local IP addresses using Python's stdlib.
"""
import socket
# The following code retrieves the local IP address of the current machine:
# 1. Use 'socket.gethostname()' to get the local hostname.
# 2. Use 'socket.gethostbyname_ex()' to get a list of IP addresses associated with the hostname.
# 3. Filter the list to exclude any IP addresses starting with "127." (loopback addresses).
# 4. Extract the first IP address (if available) from the filtered list.
# 5. Print the obtained IP address to the console.

local_hostname = socket.gethostname()
ip_addresses = socket.gethostbyname_ex(local_hostname)[2]
filtered_ips = [ip for ip in ip_addresses if not ip.startswith("127.")]
first_ip = filtered_ips[:1]
print(first_ip[0])

""" 
56. Write a Python program to get the height and width of the console window.
"""
import shutil
def terminal_size():
    size = shutil.get_terminal_size()
    return size.columns, size.lines
print('Number of columns and rows: ', terminal_size())

""" 
57. Write a Python program to get the execution time of a Python method.
"""
import time
def sum_of_n_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1, n + 1):
        s = s + i
    end_time = time.time()
    return s, end_time - start_time
n = 5
print("\nTime to sum of 1 to", n, "and required time to calculate is:", sum_of_n_numbers(n))

""" 
58. Write a Python program to sum the first n positive integers.
"""
lambda_func = lambda x: sum(list(range(1, x+1)))
print(lambda_func(4))

""" 
59. Write a Python program to convert height (in feet and inches) to centimeters.
"""
print("Input your height: ")
h_ft = int(input("Feet: "))
h_inch = int(input("Inches: "))
h_inch += h_ft * 12
h_cm = round(h_inch * 2.54, 1)
print("Your height is : %d cm." % h_cm)

""" 
60. Write a Python program to calculate the hypotenuse of a right angled triangle.
"""
from math import sqrt
def hyp():
    a = int(input("Enter your input: "))
    b = int(input("Enter your input: "))
    c = sqrt(a**2 + b**2)
    print(c)
    return c
hyp()

""" 
61. Write a Python program to convert the distance (in feet) to inches, yards, and miles.
"""
def dis():
    a = int(input("Enter your input: "))
    print(a*12, "inches")
    print(a/3, "yards")
    print(a/5280, "miles")
    return
dis()

""" 
62. Write a Python program to convert all units of time into seconds.
"""
def tm():
    a = int(input("Enter your input: "))
    print(a*60, "seconds")
    print(a*3600, "seconds")
    print(a*86400, "seconds")
    return
tm()

""" 
63. Write a Python program to get an absolute file path.
"""
import os
def get_absolute_path(file_name):
    return os.path.abspath(file_name)
# Replace 'example.txt' with the name of the file you want to get the absolute path for
file_name = 'Python_Class.py'
print(f'Absolute path of {file_name}: {get_absolute_path(file_name)}')

""" 
64. Write a Python program that retrieves the date and time of file creation and modification.
"""
import os.path
import time
file_path = r'C:\VsCode\Python_Class.py'
modification_time = time.ctime(os.path.getmtime(file_path))
print("Last modified: %s" % modification_time)
creation_time = time.ctime(os.path.getctime(file_path))
print("Created: %s" % creation_time)


""" 
65. Write a Python program that converts seconds into days, hours, minutes, and seconds.
"""
time_in_seconds = float(input("Input time in seconds: "))
day = time_in_seconds // (24 * 3600)
time_in_seconds %= (24 * 3600)
hour = time_in_seconds // 3600
time_in_seconds %= 3600
minutes = time_in_seconds // 60
time_in_seconds %= 60
seconds = time_in_seconds
print(f"d:h:m:s -> {int(day)}:{int(hour)}:{int(minutes)}:{int(seconds)}")

""" 
66. Write a Python program to calculate the body mass index.
"""
weight = int(input("Enter your weight in KG: "))
height = int(input("Enter your height in Feet: "))
bmi = weight / (height * height)
rounded_bmi = round(bmi, 2)
print("Your body mass index is: ", rounded_bmi)

""" 
67. Write a Python program to convert pressure in kilopascals to pounds per square inch,
a millimeter of mercury (mmHg) and atmosphere pressure..
"""
kpa = float(input("Input the pressure in kilopascals > "))
pressure_in_psi = round(kpa * 0.145038, 3)
pressure_in_mmHg = round(kpa * 7.50062, 3)
pressure_in_atmp = round(kpa * 0.0098692382432766, 3)
print(f"Pressure = {pressure_in_psi} psi \nor {pressure_in_mmHg} mmHg \nor {pressure_in_atmp} atmp")

""" 
68. Write a Python program to calculate sum of digits of a number..
"""
num = int(input("Input a four-digit number: "))
lambda_func = lambda num: sum(list(map(int, (str(num)))))
print(lambda_func(num))

# OR
num = int(input("Input a four-digit number: "))
lambda_func  = lambda num: sum(int(x) for x in str(num))
print(lambda_func(num))

""" 
69. Write a Python program to sort three integers without using conditional
statements and loops.
"""
func = lambda x,y,z: sorted([x,y,z])
print(func(*[5,2,8]))


""" 
70. Write a Python program to sort files by date.
"""
# Import the necessary libraries to work with file operations and globbing.
import glob
import os
files = glob.glob("*.txt")
files.sort(key=os.path.getmtime)
print("\n".join(files))

# 2nd
import os
# Change the current working directory to 'D:'.
os.chdir('D:')
file_list = filter(os.path.isfile, os.listdir('.'))
sorted_files = sorted(file_list, key=os.path.getmtime)
print('\n'.join(map(str, sorted_files)))

""" 
71. Write a Python program to get a directory listing,
sorted by creation date.
"""
from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time
dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'
data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
data = ((os.stat(path), path) for path in data)
data = ((stat[ST_CTIME], path) for stat, path in data if S_ISREG(stat[ST_MODE]))
# Sort the files based on their creation times and then print the sorted list, including the creation time and the file name.
for cdate, path in sorted(data):
    print(time.ctime(cdate), os.path.basename(path)) 

""" 
72. Write a Python program to get the details of the math module.
"""
import math            
math_ls = dir(math)
print(math_ls)

""" 
73. Write a Python program to calculate the midpoints of a line.
"""
def midpoint():
    x1 = int(input("Enput the number: "))
    y1 = int(input("Enput the number: "))
    x2 = int(input("Enput the number: "))
    y2 = int(input("Enput the number: "))
    p1 = (x1 + x2)/2
    p2 = (y1 + y2)/2
    return p1,p2
print(midpoint())

""" 
74. Write a Python program to hash a word.
"""
soundex = [0, 1, 2, 3, 0, 1, 2, 0, 0, 2, 2, 4,
        5, 5, 0, 1, 2, 6, 2, 3, 0, 1, 0, 2, 0, 2]
word = input("Input the word to be hashed: ")
word = word.upper()
coded = word[0]

# Iterate over the remaining characters in the word to calculate the Soundex code.
for a in word[1:len(word)]:
    i = 65 - ord(a)
    coded = coded + str(soundex[i])
print()
print("The coded word is: " + coded)
print()

""" 
75. Write a Python program to get the copyright information
and write Copyright information in Python code.
"""
import sys
print("\nPython Copyright Information")
print(sys.copyright)
print()

""" 
76. Write a Python program to get the command-line arguments (name of the script, 
the number of arguments, arguments) passed to a script..
"""
import sys
print("This is the name/path of the script:"), sys.argv[0]
print("Number of arguments:", len(sys.argv))
print("Argument List:", str(sys.argv))

""" 
77. Write a Python program to test whether the system
is a big-endian platform or a little-endian platform..
"""
import sys
print()
if sys.byteorder == "little":
    print("Little-endian platform.")
else:
    print("Big-endian platform.")
print()

""" 
78. Write a Python program to find the available built-in modules..
"""
import builtins
print(dir(builtins))

"""
79. Write a Python program to get the size of an object in bytes.
"""
import sys
def dec(func):
    def wrapper(*args, **kwargs):
        print("This is size of arguments: ")
        print(sys.getsizeof(func(*args, **kwargs)))
    return wrapper

@dec
def fun(a, b, c):
    return a + b + c
print(fun(1, 2, 3))

"""
79. Write a Python program to get the size of an object in bytes.
"""
# Define three strings and assign values to them
import sys
str1 = "one"
str2 = "four"
str3 = "three"
x = 0
y = 112
z = 122.56

# Print the size in bytes of each variable
print("Size of ", str1, "=", str(sys.getsizeof(str1)) + " bytes")
print("Size of ", str2, "=", str(sys.getsizeof(str2)) + " bytes")
print("Size of ", str3, "=", str(sys.getsizeof(str3)) + " bytes")
print("Size of", x, "=", str(sys.getsizeof(x)) + " bytes")
print("Size of", y, "=", str(sys.getsizeof(y)) + " bytes")

L = [1, 2, 3, 'Red', 'Black']
print("Size of", L, "=", sys.getsizeof(L), " bytes")
T = ("Red", [8, 4, 6], (1, 2, 3))
print("Size of", T, "=", sys.getsizeof(T), " bytes")
S = {'apple', 'orange', 'apple', 'pear'}
print("Size of", S, "=", sys.getsizeof(S), " bytes")
D = {'Name': 'David', 'Age': 6, 'Class': 'First'}
print("Size of", D, "=", sys.getsizeof(S), " bytes")

"""
80. Write a Python program to get the current value of the recursion limit.
"""
import sys
print()
print("Current value of the recursion limit:")
print(sys.getrecursionlimit())
print()

"""
81. Write a Python program to concatenate N strings.
"""
def func():
    str1 = "Hello, "
    str2 = "World"
    print(str1 + str2)
func()

"""
82. Write a Python program to calculate the sum of all items
of a container (tuple, list, set, dictionary).
"""
s = sum([10, 20, 30])
print("\nSum of the container: ", s)
print()

"""
83. Write a Python program to test whether all numbers in a
list are greater than a certain number..
"""
# Create a list 'num' containing integer values.
num = [2, 3, 4, 5]
print()
print(all(x > 1 for x in num))
print(all(x > 4 for x in num))
print()

"""
84. Write a Python program to count the number of occurrences
of a specific character in a string...
"""
def func(strn, n):
    count = 0
    for x in strn:
        if x == n:
            count += 1
    return count
# OR
s = "The quick brown fox jumps over the lazy dog."
print("Original string:")
print(s)
print("Number of occurrences of 'o' in the said string:")
print(s.count("o"))

"""
85. Write a Python program to check whether a file
path is a file or a directory....
"""
import os
path = "abc.txt"
if os.path.isdir(path):
    print("\nIt is a directory")
elif os.path.isfile(path):
    print("\nIt is a normal file")
else:
    print("It is a special file (socket, FIFO, device file)")
print()

"""
86. Write a Python program to get the
ASCII value of a character.
"""
print("ASCII value of 'a' is:", ord('a'))

""" 
87. Write a Python program to get the size of a file
"""
import sys
with open(r"PythonFile\PythonByTopics\Python_Basic.py", "r") as file_handle:
    print(sys.getsizeof(file_handle))
    print()
    
""" 
88. Given variables x=30 and y=20, write a Python program to print "30+20=50".
"""
lambda_func = lambda x,y: x+y
print(lambda_func(3,4))

""" 
89. Write a Python program to perform an action if a condition is true.
Given a variable name, if the value is 1, display the string "First day of a Month!"
and do nothing if the value is not equal.
"""
# Assign the value 1 to the variable n.
n = 1
if n == 1:
    print("\nFirst day of a Month!")
print()

""" 
90. Write a Python program to create a copy of its own source code.
"""
def file_copy(src, dest):
    with open(src, 'r') as f, open(dest, 'w') as d:
        for line in f:
            d.write(line)

# Copy content from 'untitled0.py' to 'z.py'
file_copy("untitled0.py", "z.py")

# Use the 'with' statement to open the 'z.py' file for reading ('r').
with open('z.py', 'r') as filehandle:
    for line in filehandle:
        print(line, end='')

""" 
91. Write a Python program to swap two variables.
"""
lambda_func = lambda a,b: (b,a)
print(lambda_func(4,5))

""" 
92. Write a Python program to define a string containing
special characters in various forms.
"""
print()
print("\#{'}${\"}@/")
print("\#{'}${\"}@/")
print(r"""\#{'}${"}@/""")
print('\#{\'}${"}@/')
print('\#{'"'"'}${"}@/')
print(r'''\#{'}${"}@/''')
print()

""" 
93. Write a Python program to get the Identity, Type,
and Value of an object..
"""
def func():
    x = 5
    print(x, type(x), id(x))
func()

""" 
94. Write a Python program to convert the bytes in a given
string to a list of integers..
"""
x = b'Abc'
print()
print("Convert bytes of the said string to a list of integers:")
print(list(x))
print()

""" 
95. Write a Python program to check whether a string is numeric.
"""
str = 'a123'
try:
    i = float(str)
except (ValueError, TypeError):
    print('\nNot numeric')
print()

""" 
96. Write a Python program to print the current call stack.
"""
# Import the 'traceback' module.
import traceback
def f1():
    return abc()
def abc():
    traceback.print_stack()
f1()
print()
print()

""" 
97. Write a Python program to list the special variables used in the language.
"""
s_var_names = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('_ names i'.split()))
print()
print( '\n'.join(' '.join(s_var_names[i:i+8]) for i in range(0, len(s_var_names), 8)) )
print()

# OR
global_variable_names = set(globals().keys())
builtin_variable_names = set(dir(__builtins__))
combined_variable_names = global_variable_names | builtin_variable_names
sorted_variable_names = sorted(combined_variable_names)
excluded_names = {'_', 'names', 'i'}
filtered_variable_names = [
    name for name in sorted_variable_names if name not in excluded_names]
for index in range(0, len(filtered_variable_names), 8):
    print(' '.join(filtered_variable_names[index:index + 8]))

""" 
98. Write a Python program to get system time.
Note : The system time is important for debugging, network information,
random number seeds, or something as simple as program performance.
"""
import time
print()
print(time.ctime())
print()

""" 
99. Write a Python program to clear the screen or terminal.
"""
import os
import time
os.system("ls")  # Use "dir" for Windows
time.sleep(2)
if os.name == 'posix':
    os.system('clear')
elif os.name == 'nt':
    os.system('cls')

""" 
100. Write a Python program to get the name of the host on which the routine is running.
"""
# Import the 'socket' module to work with networking functionalities.
import socket
# Use 'socket.gethostname()' to retrieve the name of the current host or machine.
host_name = socket.gethostname()
# Print the host name to the console.
print("Host name:", host_name)

""" 
101. Write a Python program to access and print a URL's content to the console.
"""
# Import the HTTPConnection class from the http.client module.
from http.client import HTTPConnection
conn = HTTPConnection("example.com")
conn.request("GET", "/")
result = conn.getresponse()
contents = result.read()
print(contents)

"""
102. Write a Python program to get system command output.
"""
# Import the subprocess module to run shell commands.
import subprocess
# Use the 'subprocess.check_output' function to execute the 'dir' command in the shell.
# 'universal_newlines=True' ensures text mode for cross-platform compatibility.
returned_text = subprocess.check_output("dir", shell=True, universal_newlines=True)
# Print a message indicating the purpose of running the 'dir' command.
print("dir command to list files and directories")
# Print the output (list of files and directories) returned by the 'dir' command.
print(returned_text)

""" 
103. Write a Python program to extract the filename from a given path.
"""
import os
print()
print(os.path.basename('/users/system1/student1/homework-1.py'))
print()

""" 
104.Write a Python program to get the effective group id, effective user id,
real group id, and a list of supplemental group ids associated with the current process.
Note: Availability: Unix..
"""
import os
print()
print("Effective group id: ", os.getegid())
print("Effective user id: ", os.geteuid())
print("Real group id: ", os.getgid())
print("List of supplemental group ids: ", os.getgroups())
print()

""" 
105. Write a Python program to get the users environment..
Note: Availability: Unix..
"""
import os
print()
print(os.environ)
print()

""" 
106. Write a Python program to divide a path by the extension separator.
"""
import os.path
for path in ['test.txt', 'filename', '/user/system/test.txt', '/', '']:
    print('"%s" :' % path, os.path.splitext(path))

import os.path
for path in ['test.txt', 'filename', '/user/system/test.txt', '/', '']:
    print('"', path, '" :', os.path.splitext(path))


""" 
107. Write a Python program to retrieve file properties.
"""
# Import the 'os.path' and 'time' modules for working with file paths and time-related functions.
import os.path
import time
print('File         :', __file__)
# Print the access time of the current file using 'os.path.getatime()' and 'time.ctime()'.
print('Access time  :', time.ctime(os.path.getatime(__file__)))
# Print the modified time of the current file using 'os.path.getmtime()' and 'time.ctime()'.
print('Modified time:', time.ctime(os.path.getmtime(__file__)))
# Print the change time of the current file using 'os.path.getctime()' and 'time.ctime()'.
print('Change time  :', time.ctime(os.path.getctime(__file__)))
# Print the size of the current file using 'os.path.getsize()'.
print('Size         :', os.path.getsize(__file__))


""" 
108. Write a Python program to find the path to a file or directory when you encounter a path name.
"""
# Import the 'os.path' module for working with file paths.
import os.path
# Iterate through a list of file paths, including '__file__', the directory of '__file__', '/', and a broken link.
for file in [__file__, os.path.dirname(__file__), '/', './broken_link']:
    print('File        :', file)
    print('Absolute    :', os.path.isabs(file))
    print('Is File?    :', os.path.isfile(file))
    print('Is Dir?     :', os.path.isdir(file))
    print('Is Link?    :', os.path.islink(file))
    print('Exists?     :', os.path.exists(file))
    print('Link Exists?:', os.path.lexists(file))

""" 
109. Write a Python program to find the path to a file or directory when you encounter a path name.
"""
import os.path
for file in [__file__, os.path.dirname(__file__), '/', './broken_link']:
    print('File        :', file)
    print('Absolute    :', os.path.isabs(file))
    print('Is File?    :', os.path.isfile(file))
    print('Is Dir?     :', os.path.isdir(file))
    print('Is Link?    :', os.path.islink(file))
    print('Exists?     :', os.path.exists(file))
    print('Link Exists?:', os.path.lexists(file))

import os
script_dir = os.path.dirname(__file__)  # Get the directory of the script
data_file_path = os.path.join(script_dir, 'data.txt')  # Construct a full path to 'data.txt'

""" 
110. Write a Python program to get numbers divisible by 
fifteen from a list using an anonymous function..
"""
lambda_func = lambda lst: list(filter(lambda x: x%15==0,lst))
print(lambda_func([12,34,654,23,30,15,45,34,565,34]))

""" 
111. Write a Python program to make file lists from the current directory using a wildcard...
"""
import os
print(os.listdir(os.getcwd()))

""" 
112. Write a Python program to remove the first item from a specified list.
"""
lambda_func = lambda lst: lst[1:]

""" 
113. Write a Python program that inputs a number and generates an error message if it is not a number.
"""
# Create an infinite loop using "while True."
while True:
    try:
        a = int(input("Input a number: "))
        break
    except ValueError:
        print("\nThis is not a number. Try again...")
        print()

""" 
114. Write a Python program to filter positive numbers from a list.
"""
lambda_func = lambda lst: list(filter(lambda x:x>0, lst))

""" 
115. Write a Python program to compute the product of a list of integers (without using a for loop).
"""
# 1st method
import math
lambda_func = lambda lst: sum(lst)
print(lambda_func([2,3,4,5,9]))

# 2nd method
from functools import reduce
import operator
lambda_func = lambda lst: reduce(operator.add, lst)
print(lambda_func([2,3,4,5,9]))

# 3rd method
def func(lst): return sum(lst)
print(func([2,3,4,5,9]))

""" 
116. Write a Python program to print Unicode characters.
"""
str = u'\u0050\u0079\u0074\u0068\u006f\u006e \u0045\u0078\u0065\u0072\u0063\u0069\u0073\
    u0065\u0073 \u002d \u0077\u0033\u0072\u0065\u0073\u006f\u0075\u0072\u0063\u0065'
print()
print(str)
print()

""" 
117. Write a Python program to prove that two string variables 
of the same value point to the same memory location.
"""
x = 'abhishek'
y = 'vivek'
lambda_func = lambda x,y: id(x)== id(y)
print(lambda_func(x,y))

""" 
118. Write a Python program to create a bytearray from a list.
"""
bytearray_func = lambda lst: bytearray(lst)
print(bytearray_func([23,45,65]))

""" 
119. Write a Python program to round a floating-point number 
to a specified number of decimal places.
"""
lambda_func = lambda x,n: round(x,n)
print(lambda_func(4.343,2))

""" 
120. Write a Python program to format a specified string 
and limit the length of a string.
"""
def format_and_limit_string(input_string, max_length):
    if len(input_string) > max_length:
        formatted_string = input_string[:max_length] + '...'
    else:
        formatted_string = input_string
    return formatted_string
input_str = "This is a sample string that needs to be formatted and possibly shortened."
max_len = 30
result = format_and_limit_string(input_str, max_len)
print(result)

""" 
121. Write a Python program to determine if a variable is defined or not..
"""
try:
    x = 1
except NameError:
    print("Variable is not defined....!")
else:
    print("Variable is defined.")

try:
    y
except NameError:
    print("Variable is not defined....!")
else:
    print("Variable is defined.")

""" 
122. Write a Python program to empty a variable without destroying it.
Sample data: n=20
d = {"x":200}
Expected Output : 0
{}
"""
n = 20
d = {"x": 200}
l = [1, 3, 5]
t = (5, 7, 8)
print(type(n)())
print(type(d)())
print(type(l)())
print(type(t)())

""" 
123. Write a Python program to determine the largest and smallest integers, longs, and floats.
"""
# Import the sys module to access system-related information.
import sys
print("Float value information: ", sys.float_info)
print("\nInteger value information: ", sys.int_info)
print("\nMaximum size of an integer: ", sys.maxsize)

"""
124. Write a Python program to check whether multiple variables have the same value.
"""
x = 20
y = 20
z = 20
if x == y == z == 20:
    print("All variables have the same value!")

"""
125. Write a Python program to sum all counts in a collection.
"""
import collections
num = [2, 2, 4, 6, 6, 8, 6, 10, 4]
result = sum(collections.Counter(num).values())
print(result)

"""
126. Write a Python program to get the actual module object for a given object.
"""
from inspect import getmodule
from math import sqrt
print(getmodule(sqrt))

""" 
127. Write a Python program to check whether an integer fits in 64 bits.
"""
# Assign the integer value 30 to the variable 'int_val'.
int_val = 30
if int_val.bit_length() <= 63:
    print((-2 ** 63).bit_length())
    print((2 ** 63).bit_length())

""" 
128. Write a Python program to check whether lowercase letters exist in a string.
"""
lambda_func = lambda strn: strn.islower()
print(lambda_func("abhishek"))

"""  
129. Write a Python program to add leading zeroes to a string.
"""
str1 = '122.22'
print("Original String: ", str1)
print("\nAdded trailing zeros:")
str1 = str1.ljust(8, '0')
print(str1)
str1 = str1.ljust(10, '0')
print(str1)
print("\nAdded leading zeros:")
str1 = '122.22'
str1 = str1.rjust(8, '0')
print(str1)
str1 = str1.rjust(10, '0')
print(str1)

""" 
130. Write a Python program that uses double quotes to display strings.
"""
import json
data = {'Alex': 1, 'Suresh': 2, 'Agnessa': 3}
json_string = json.dumps(data)
print(json_string)

"""  
131. Write a Python program to split a variable length string into variables.
"""
var_list = ['a', 'b', 'c']
x, y, z = (var_list + [None] * 3)[:3]
print(x, y, z)
var_list = [100, 20.25]
x, y = (var_list + [None] * 2)[:2]
print(x, y)

"""
132. Write a Python program to list the home directory without an absolute path. 
"""
import os.path
print(os.path.expanduser(""))

""" 
133. Write a Python program to calculate the time runs
(difference between start and current time) of a program.
"""
import time
def dec(func):
    def wrapper(*arg, **kwargs):
        start = time.time()
        func(*arg, **kwargs)
        end = time.time()
        result = end - start
        print(result)
    return wrapper
@dec
def func(a,b):
    return a**b
print(func(4,23289985))

""" 
133. Write a Python program to calculate the time runs 
(difference between start and current time) of a program.
"""
from timeit import default_timer
def timer(n):
    start = default_timer()
    for row in range(0, n):
        print(row)
    print(default_timer() - start)
timer(5)
timer(15)

"""
134. Write a Python program to input two integers on a single line.
"""
print("Input the values of x & y (separated by a space):")
x, y = map(int, input().split())
print("The values of x & y are:", x, y)

"""
135. Write a Python program to print a variable without spaces between values.
Sample value : x =30
Expected output : Value of x is "30"
"""
x = 30
formatted_string = 'Value of x is "{}"'.format(x)
print(formatted_string)

""" 
136. Write a Python program to find files and skip directories in a given directory.
"""
# Import the 'os' module to work with the operating system.
import os
print([f for f in os.listdir('C:\VsCode') if os.path.isfile(os.path.join('C:\VsCode', f))])

""" 
137. Write a Python program to extract a single key-value pair from a dictionary into variables.
"""
my_dict = {"ram":10, "laxman":20}
(c1, c2) = my_dict.items()
print(c1)
print(c2)

""" 
138. Write a Python program to convert true to 1 and false to 0.
"""
x = 'true'
x = int(x == 'true')
print(x)
x = 'abcd'
x = int(x == 'true')
print(x)

""" 
139. Write a Python program to validate an IP address
"""
import socket
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(f"Laptop's IP address: {ip_address}")

import socket
addr = '192.168.3.221'
try:
    socket.inet_aton(addr)
    print("Valid IP")
except socket.error:
    print("Invalid IP")

""" 
140. Write a Python program to convert an integer to binary that keeps leading zeros.
Sample data : x=12
Expected output : 00001100
0000001100
"""
x = 12
print(format(x, '08b'))
print(format(x, '010b'))

""" 
141. Write a python program to convert decimal to hexadecimal.
Sample decimal number: 30, 4
Expected output: 1e, 04
"""
x = 30
print(format(x, '02x'))
x = 4
print(format(x, '02x'))

""" 
142. Write a Python program to check if every consecutive sequence of zeroes is followed by
a consecutive sequence of ones of same length in a given string. Return True/False.
Original sequence: 01010101
Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
True
"""
def test(str1):
    while '01' in str1:
        str1 = str1.replace('01', '')
    return len(str1) == 0

# Define the input string 'str1'.
str1 = "01010101"
print("Original sequence:", str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))
str1 = "00"
print("\nOriginal sequence:", str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))

""" 
143. Write a Python program to determine if the Python shell is executing
in 32-bit or 64-bit mode on the operating system.
"""
import struct
print(struct.calcsize("P") * 8)

""" 
144. Write a Python program to check whether a variable is an integer or string.
"""
print(isinstance(25, int) or isinstance(25, str))
print(isinstance([25], int) or isinstance([25], str))
print(isinstance("25", int) or isinstance("25", str))

""" 
145. Write a Python program to test if a variable is a list, tuple, or set
"""
my_list = [2,3,4,5]
my_tuple = (2,3,4,5)
my_set = {2,3,4,5}
print(isinstance(my_list, list) or isinstance(my_list, list))
print(isinstance(my_tuple, tuple) or isinstance(my_tuple, tuple))
print(isinstance(my_set, set) or isinstance(my_set, set))

""" 
146. Write a Python program to find the location of Python module sources.
"""
import importlib.util
def find_module_location(module_name):
    try:
        spec = importlib.util.find_spec(module_name)
        if spec and spec.origin:
            return spec.origin
        else:
            return f"Module '{module_name}' not found."
    except ImportError as e:
        return str(e)
# Example usage
module_name = "os"
location = find_module_location(module_name)
print(f"The location of the '{module_name}' module is: {location}")

""" 
147. Write a Python function to check whether a number is divisible by another number.
Accept two integer values from the user.
"""
def multiple(m, n):
    return True if m % n == 0 else False
print(multiple(20, 5))  # Check if 20 is a multiple of 5 and print the result.
print(multiple(7, 2))   # Check if 7 is a multiple of 2 and print the result.

""" 
148. Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
"""
def max_min(data):
    l = data[0]  # 'l' is used to keep track of the maximum value.
    s = data[0]  # 's' is used to keep track of the minimum value.
    for num in data:
        if num > l:
            l = num  # If 'num' is greater, update 'l' with 'num'.
        elif num < s:
            s = num  # If 'num' is smaller, update 's' with 'num'.
    return l, s
print(max_min([0, 10, 15, 40, -5, 42, 17, 28, 75]))

""" 
149. Write a Python function that takes a positive integer and returns the sum of the
cube of all positive integers smaller than the specified number.
"""
def sum_of_cubes(n):
    sum = 0
    for k in range(n):
        sum = sum + k*k*k
    return sum
print("Sum of cubes smaller than the specified number: ", sum_of_cubes(3))

""" 
150. Write a Python function to check whether a distinct pair of numbers whose product is odd
is present in a sequence of integer values.
"""
def odd_product(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                product = nums[i] * nums[j]
                if product & 1:
                    return True
    return False

# Define three lists of integers.
dt1 = [2, 4, 6, 8]
dt2 = [1, 6, 4, 7, 8]
dt3 = [1, 3, 5, 7, 9]

# Call the 'odd_product' function for each list and print the result.
print(dt1, odd_product(dt1))
print(dt2, odd_product(dt2))
print(dt3, odd_product(dt3))
