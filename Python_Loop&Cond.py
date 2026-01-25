################################################################
############################# (Conditional Statements and loops)
################################################################
"""1. Write a Python program to find those numbers which are divisible by 7 and multiples of 5,
between 1500 and 2700 (both included)."""
def divisible():
    for i in range(1500,2701):
        if i%7==0 and i%5==0:
            print(i)
divisible()

"""2. Write a Python program to convert temperatures to and from Celsius and Fahrenheit."""
def convert_temperature():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius.")
convert_temperature()

"""3. Write a Python program to guess a number between 1 and 9."""
import random
def guess_number():
    numner = random.randint(1, 9)
    guess = int(input("Guess a number between 1 and 9: "))
    if guess == numner:
        print("You guessed right!")
    else:
        print(f"Sorry, the correct number was {numner}.")
guess_number()

"""4. Write a Python program to construct the following pattern, using a nested for loop."""
def pattern():
    n = 5
    for i in range(n):
        for j in range(i+1):
            print("*", end=" ")
        print()
pattern()

"""5. Write a Python program that accepts a word from the user and reverses it."""
def reverse_word():
    word = input("Enter a word: ")
    reversed_word = word[::-1]
    print(f"Reversed word: {reversed_word}")
reverse_word()

"""6. Write a Python program to count the number of even and odd numbers in a series of numbers"""
def count_even_odd():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print(f"Number of even numbers: {even_count}")
    print(f"Number of odd numbers: {odd_count}")
count_even_odd()

"""7. Write a Python program that prints each item and its corresponding type from the following list."""
def print_items_and_types():
    items = [1, 2.5, "Hello", True, None]
    for item in items:
        print(f"Item: {item}, Type: {type(item)}")
print_items_and_types()

"""8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6."""
def print_numbers():
    for i in range(6):
        if i == 3 or i == 6:
            continue
        print(i)
print_numbers()

"""9. Write a Python program to get the Fibonacci series between 0 and 50."""
def fibonacci_series():
    a,b = 0,1
    while a < 50:
        print(a, end=" ")
        a,b = b,a+b
fibonacci_series()

# OR
fib = lambda x: x if x < 2 else fib(x - 1) + fib(x - 2) # fib = lambda x: x if x < 2 else fib(x - 1) + fib(x - 2)
for i in range(10):
    print(fib(i), end=" ")
print()

# OR
def fibonacci_series_recursive(n):
    if n < 2:
        return n
    else:
        return fibonacci_series_recursive(n-1) + fibonacci_series_recursive(n-2)
for i in range(10):
    print(fibonacci_series_recursive(i), end=" ")
print()
    
"""10. Write a Python program that iterates the integers from 1 to 50.
For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz".
For numbers that are multiples of three and five, print "FizzBuzz"."""
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

"""11. Write a Python program that takes two digits m (row) and n (column) as input and generates
a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j."""
def generate_2d_array(m, n):
    array = [[i * j for j in range(n)] for i in range(m)]
    for row in array:
        print(row)
generate_2d_array(4, 4)  # Example: 3 rows and 4 columns

print(f"Top-level __name__: {__name__}")

"""12. Write a Python program that accepts a sequence of lines (blank line to terminate) as input
and prints the lines as output (all characters in lower case)."""
def func():
    lines = []
    while True:
        line = input("Enter a line (blank line to terminate): ")
        if not line:
            break
        lines.append(line.lower())
    print("\n".join(lines))
func()

"""13. Write a Python program that accepts a sequence of comma separated 4 digit binary
numbers as its input. The program will print the numbers that are divisible by 5
in a comma separated sequence."""
def func():
    numbers = input("Enter comma separated 4 digit binary numbers: ").split(",")
    divisible_by_5 = [num for num in numbers if int(num, 2) % 5 == 0]
    print(",".join(divisible_by_5))
func()

num = input("Enter a number: ").split(",")
for k in num:
    print(int(k, 1))
    print(int(k, 2))
    print(int(k, 3))
    print(int(k, 4))
    print(int(k, 6))
    print(int(k, 8))
print()

"""14. Write a Python program that accepts a string and calculates the number of digits and letters."""
def func():
    string = input("Enter a string: ")
    digits = 0
    letters = 0
    for char in string:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            letters += 1
    print(f"Number of digits: {digits}")
    print(f"Number of letters: {letters}")
func()

# OR
lambda_func = lambda string: (len([char for char in string if char.isdigit()]), len([char for char in string if char.isalpha()]))
print(lambda_func("hello123"))

"""15. Write a Python program to check the validity of passwords input by users.
Validation rules:
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.
"""
import re
pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,16}$')
def check_password():
    password = input("Enter a password: ")
    if pattern.match(password):
        print("Valid password.")
    else:
        print("Invalid password.")
check_password()

# OR
def check_password():
    password = input("Enter a password: ")
    if len(password) < 6 or len(password) > 12:
        print("Invalid password length.")
        return
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one digit.")
        return
    if not any(char.isalpha() for char in password):
        print("Password must contain at least one letter.")
        return
    if not any(char in "!@#$%^&*()" for char in password):
        print("Password must contain at least one special character.")
        return
    print("Valid password.")
check_password()

"""16. Write a Python program to find numbers between 100 and 400 (both included)
where each digit of a number is an even number. The numbers obtained should be printed
in a comma-separated sequence."""
def func():
    even_numbers = []
    for num in range(100, 401):
        if all(int(digit) % 2 == 0 for digit in str(num)):
            even_numbers.append(str(num))
    print(",".join(even_numbers))
func()

"""17. Write a Python program to print the alphabet pattern 'A'."""
def print_alphabet_A():
    n = 5
    for i in range(n):
        for j in range(n):
            if (i == 0 and j > 0 and j < n - 1) or (i == n // 2) or (j == 0 and i > 0) or (j == n - 1 and i > 0):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
print_alphabet_A()

"""18. Write a Python program to print the alphabet pattern 'D'."""
def print_alphabet_D():
    n = 5
    for i in range(n):
        for j in range(n):
            if (j == 0) or (i == 0 and j < n - 1) or (i == n - 1 and j < n - 1) or (j == n - 1 and i != 0 and i != n - 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
print_alphabet_D()

"""19. Write a Python program to print the alphabet pattern 'E'."""
def print_alphabet_E():
    n = 5
    for i in range(n):
        for j in range(n):
            if (i == 0) or (i == n - 1) or (j == 0) or (i == n // 2 and j < n - 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
print_alphabet_E()

"""20. Write a Python program to print the alphabet pattern 'G'."""
def print_alphabet_G():
    n = 5
    for i in range(n):
        for j in range(n):
            if (i == 0 and j > 0) or (i == n - 1 and j < n - 1) or (j == 0 and i != 0 and i != n - 1) or (j == n - 1 and i > n // 2) or (i == n // 2 and j > n // 2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
print_alphabet_G()

"""21. Write a Python program to print the alphabet pattern 'L'."""
def print_alphabet_L():
    n = 5
    for i in range(n):
        for j in range(n):
            if (j == 0) or (i == n - 1 and j < n - 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
print_alphabet_L()

"""22. Write a Python program to print the alphabet pattern 'M'."""
def print_alphabet_M():
    n = 5
    for i in range(n):
        for j in range(n):
            if (j == 0) or (j == n - 1) or (i == j and i <= n // 2) or (i + j == n - 1 and i <= n // 2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
print_alphabet_M()

"""23. Write a Python program to print the alphabet pattern 'O'."""
def print_alphabet_O():
    n = 5
    for i in range(n):
        for j in range(n):
            if (i == 0 and j > 0 and j < n - 1) or (i == n - 1 and j > 0 and j < n - 1) or (j == 0 and i != 0 and i != n - 1) or (j == n - 1 and i != 0 and i != n - 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
print_alphabet_O()

"""24. Write a Python program to print the alphabet pattern 'P'."""
def print_alphabet_P():
    n = 5
    for i in range(n):
        for j in range(n):
            if (j == 0) or (i == 0 and j < n - 1) or (i == n // 2 and j < n - 1) or (j == n - 1 and i != 0 and i != n // 2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
print_alphabet_P()

"""25. Write a Python program to print the alphabet pattern 'R'."""
def print_alphabet_R():
    n = 5
    for i in range(n):
        for j in range(n):
            if (j == 0) or (i == 0 and j < n - 1) or (i == n // 2 and j < n - 1) or (j == n - 1 and i != 0 and i != n // 2) or (i + j == n - 1 and i > n // 2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
print_alphabet_R()

"""26. Write a Python program to print the following patterns.'S'"""
def print_alphabet_S():
    n = 5
    for i in range(n):
        for j in range(n):
            if (i == 0 and j > 0) or (i == n - 1 and j < n - 1) or (j == 0 and i != 0 and i != n - 1) or (j == n - 1 and i > n // 2) or (i == n // 2 and j > n // 2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
print_alphabet_S()

"""27. Write a Python program to print the alphabet pattern 'T'."""
def print_alphabet_T():
    n = 5
    for i in range(n):
        for j in range(n):
            if (i == 0) or (j == n // 2 and i != 0):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
print_alphabet_T()

"""28. Write a Python program to print the alphabet pattern 'U'."""
def print_alphabet_U():
    n = 5
    for i in range(n):
        for j in range(n):
            if (j == 0 and i != n - 1) or (j == n - 1 and i != n - 1) or (i == n - 1 and j > 0 and j < n - 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
print_alphabet_U()

"""29. Write a Python program to print the alphabet pattern 'X'."""
def print_alphabet_X():
    n = 5  # Size of the grid
    for i in range(n):
        for j in range(n):
            if j == i or j == n - i - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
print_alphabet_X()

"""30. Write a Python program to print the alphabet pattern 'Z'."""
def print_alphabet_Z():
    n = 5  # Size of the grid
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
print_alphabet_Z()

"""31. Write a Python program to calculate a dog's age in dog years.

Note: For the first two years, a dog year is equal to 10.5 human years.
After that, each dog year equals 4 human years
"""
def dog_stuff():
    age = int(input("Enter your dog's age in human years: "))
    print(f"Your dog's age in dog years is {age * 7}")
dog_stuff()

"""32. Write a Python program to check whether an alphabet is a vowel or consonant."""
def vowel_or_consonant():
    letter = input("Enter a letter: ")
    if letter in "aeiouAEIOU":
        print(f"{letter} is a vowel.")
    else:
        print(f"{letter} is a consonant.")
vowel_or_consonant()

"""33. Write a Python program to convert a month name to a number of days."""
import calendar
def month_to_days():
    month = input("Enter a month: ")
    days = calendar.monthrange(2023, month)[1]
    print(f"{month} has {days} days.")
month_to_days()

def month_to_days():
    month = input("Enter a month: ")
    days = {
        "January": 31,
        "February": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }
    print(f"{month} has {days[month]} days.")
month_to_days()

"""34. Write a Python program to sum two integers. However, if the sum is between 15
and 20 it will return 20."""
def program():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    sum = num1 + num2
    if sum >= 15 and sum <= 20:
        print("The sum is between 15 and 20.")
    else:
        print("The sum is not between 15 and 20.")
program()

"""35. Write a Python program that checks whether a string represents an integer or not."""
def function():
    string = input("Enter a string: ")
    try:
        int(string)
        print("The string represents an integer.")
    except ValueError:
        print("The string does not represent an integer.")
        
"""36. Write a Python program to check if a triangle is equilateral, isosceles or scalene."""
def equilateral_isosceles_scalene():
    side1 = int(input("Enter the length of side 1: "))
    side2 = int(input("Enter the length of side 2: "))
    side3 = int(input("Enter the length of side 3: "))
    if side1 == side2 == side3:
        print("The triangle is equilateral.")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")
equilateral_isosceles_scalene()

"""37. Write a Python program that reads two integers representing a month and day
and prints the season for that month and day."""
def season():
    month = int(input("Enter the month: "))
    day = int(input("Enter the day: "))
    if month == 3 and day >= 21 or month == 4 and day <= 19:
        print("Spring")
    elif month == 6 and day >= 21 or month == 7 and day <= 22:
        print("Summer")
    elif month == 9 and day >= 23 or month == 10 and day <= 22:
        print("Autumn")
    else:
        print("Winter")
season()

"""38. Write a Python program to display the astrological sign for a given date of birth."""
def astrological_sign():
    month = int(input("Enter the month: "))
    day = int(input("Enter the day: "))
    if month == 3 and day >= 21 or month == 4 and day <= 19:
        print("Aries")
    elif month == 4 and day >= 20 or month == 5 and day <= 20:
        print("Taurus")
    elif month == 5 and day >= 21 or month == 6 and day <= 20:
        print("Gemini")
    elif month == 6 and day >= 21 or month == 7 and day <= 22:
        print("Cancer")
astrological_sign()
        
"""39. Write a Python program to display the sign of the Chinese Zodiac for 
the given year in which you were born."""
def zodiac_sign():
    year = int(input("Enter the year: "))
    if year % 12 == 0:
        print("Rat")
    elif year % 12 == 1:
        print("Ox")
"""40. Write a Python program to find the median of three values."""
def median(a,b,c):
    return sorted([a,b,c])[1]
lambda_func = lambda a,b,c: sorted([a,b,c])[1]

"""41. Write a Python program to get the next day of a given date."""
import datetime
def next_day():
    date = input("Enter the date (YYYY-MM-DD): ")
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    next_date = date + datetime.timedelta(days=1)
    print("The next day is:", next_date.strftime("%Y-%m-%d"))   
next_day()
"""42. Write a Python program to calculate the sum and average of n integer
numbers (input from the user). Input 0 to finish."""
def func():
    sum = 0
    count = 0
    while True:
        num = int(input("Enter a number: "))
        if num == 0:
            break
        sum += num
        count += 1
    print("The sum is:", sum)
    print("The average is:", sum / count)
func()

"""43. Write a Python program to create the multiplication table (from 1 to 10) of a number."""
def func():
    num = int(input("Enter a number: "))
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)
func()

"""44. Write a Python program to construct the following pattern, using a nested loop number."""
def func():
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
func()

"""45. Write a Python program to construct the following pattern, using a nested loop number."""