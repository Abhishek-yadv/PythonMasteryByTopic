####################################################################
############################################### (Python Resursion||)
####################################################################
""" 1. Write a Python program to calculate the sum of a list of numbers using recursion."""
def sum_list(lst):
    """Calculate the sum of a list of numbers using recursion."""
    if not lst:  # Base case: if the list is empty
        return 0
    else:
        return lst[0] + sum_list(lst[1:])
print("Sum of list:", sum_list([1, 2, 3, 4, 5]))
""" 2. Write a Python program to convert an integer to a string in any base using recursion ."""
def int_to_str(n, base):
    """Convert an integer to a string in any base using recursion."""
    digits = "0123456789ABCDEF"
    if n < base:
        return digits[n]
    else:
        return int_to_str(n // base, base) + digits[n % base]
    
print("Integer to string in base 2:", int_to_str(255, 2))  # Binary representation
print("Integer to string in base 2:", int_to_str(255, 8))  # Octal representation
print("Integer to string in base 16:", int_to_str(255, 16))  # Hexadecimal representation
# write a python program to convert an string to integer from any base using recursion.
def str_to_int(s, base):
    """Convert a string to an integer in any base using recursion."""
    digits = "0123456789ABCDEF"
    if len(s) == 0:
        return 0
    else:
        return str_to_int(s[:-1], base) * base + digits.index(s[-1])
    
print("String to integer in base 2:", str_to_int("11111111", 2))  # Binary representation
print("String to integer in base 8:", str_to_int("377", 8))  # Octal representation
print("String to integer in base 16:", str_to_int("FF", 16))  # Hexadecimal representation

""" 3. Write a Python program to sum recursion lists using recursion."""
def sum_recursion(lst):
    """Sum recursion lists using recursion."""
    if not lst:  # Base case: if the list is empty
        return 0
    elif isinstance(lst[0], list):  # If the first element is a list, recurse into it
        return sum_recursion(lst[0]) + sum_recursion(lst[1:])
    else:
        return lst[0] + sum_recursion(lst[1:])

""" 4. Write a Python program to get the factorial of a non-negative integer using recursion."""
def factorial(n):
    """Calculate the factorial of a non-negative integer using recursion."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0 or n == 1:  # Base case: factorial of 0 or 1 is 1
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial of 5:", factorial(5))  # Output: 120
print("Factorial of 0:", factorial(0))  # Output: 1
print("Factorial of 1:", factorial(1))  # Output: 1

""" 5. Write a Python program to solve the Fibonacci sequence using recursion."""
def fibonacci(n):
    """Calculate the nth Fibonacci number using recursion."""
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    elif n == 0:  # Base case: Fibonacci(0) = 0
        return 0
    elif n == 1:  # Base case: Fibonacci(1) = 1
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print("Fibonacci of 5:", fibonacci(5))  # Output: 5

""" 6. Write a Python program to get the sum of a non-negative integer using recursion."""
def sum_of_digits(n):
    """Calculate the sum of digits of a non-negative integer using recursion."""
    if n < 0:
        raise ValueError("Sum of digits is not defined for negative numbers")
    elif n == 0:  # Base case: sum of digits of 0 is 0
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)  # Add last digit and recurse on the rest
    
""" 7. Write a Python program to calculate the sum of the positive integers of
n+(n-2)+(n-4)... (until n-x =< 0) using recursion ."""
def sum_positive_integers(n):
    """Calculate the sum of positive integers n + (n-2) + (n-4) ... using recursion."""
    if n <= 0:  # Base case: if n is less than or equal to 0, return 0
        return 0
    else:
        return n + sum_positive_integers(n - 2)  # Add n and recurse with n-2
print("Sum of positive integers:", sum_positive_integers(10))  # Output: 30 (10 + 8 + 6 + 4 + 2)

""" 8. Write a Python program to calculate the sum of harmonic series upto n terms."""
def harmonic_sum(n):
    """Calculate the sum of the harmonic series up to n terms using recursion."""
    if n <= 0:  # Base case: if n is less than or equal to 0, return 0
        return 0
    else:
        return 1 / n + harmonic_sum(n - 1)  # Add 1/n and recurse with n-1
print("Harmonic sum of 5 terms:", harmonic_sum(5))  # Output: 2.283333333333333

""" 9. Write a Python program to calculate the geometric sum up to 'n' terms."""
def geometric_sum(n):
    """Calculate the geometric sum up to n terms using recursion."""
    if n <= 0:  # Base case: if n is less than or equal to 0, return 0
        return 0
    else:
        return 1 / (2 ** n) + geometric_sum(n - 1)  # Add 1/(2^n) and recurse with n-1
print("Geometric sum of 5 terms:", geometric_sum(5))  # Output: 2.283333333333333

""" 10. Write a Python program to calculate the value of 'a' to the power of 'b' using recursion."""
def power(a, b):
    """Calculate a to the power of b using recursion."""
    if b < 0:
        raise ValueError("Power is not defined for negative exponents")
    elif b == 0:  # Base case: a^0 = 1
        return 1
    else:
        return a * power(a, b - 1)  # Multiply a by the result of a^(b-1)
print("5 raised to the power of 3:", power(5, 3))  # Output: 125

""" 11. Write a Python program to find the greatest common divisor (GCD) of two integers using recursion."""
def gcd(a, b):
    """Calculate the GCD of two integers using recursion."""
    if b == 0:  # Base case: GCD(a, 0) = a
        return a
    else:
        return gcd(b, a % b)  # Recurse with b and the remainder of a divided by b
print("GCD of 48 and 18:", gcd(48, 18))  # Output: 6