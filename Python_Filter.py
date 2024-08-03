####################################################################
######################################################## (Filter)
####################################################################
"""
1. Write a Python function that filters out even numbers from a list
of integers using the filter function.
"""
from datetime import datetime
def func(lst):
    return list(filter(lambda x: x%2==0, lst))
num = [2,3,5,56,76,34,33,11]
print(func(num))

lambda_func = lambda lst: list(filter(lambda x: x%2==0, lst))
num = [2, 3, 5, 56, 76, 34, 33, 11]
print(lambda_func(num))


"""
2. Write a Python program that uses the filter function to extract all uppercase
letters from a list of mixed-case strings.
"""
def func(lst):
    return list(filter(lambda char: char.isupper(), ''.join(lst)))

# 
mixed_case_strings = ["Hello", "w3resource", "Python", "Filter", "Learning"]
uppercase_letters = list(filter(lambda char: char.isupper(), ''.join(mixed_case_strings)))
print(uppercase_letters)

"""
3. Write a Python function that filters out all elements less than or equal
than a specified value from a list of numbers using the filter function.
"""
def filter_greater_than(lst, n):
    return list(filter(lambda x: x > n, lst))

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_greater_than(lst, 2))

"""
4. Write a Python program that creates a list of names and uses the filter function
to extract names that start with a vowel (A, E, I, O, U).
"""
import re
def filter_consonant_start(lst):
    return list(filter(lambda x: re.match(r'^[AEIOUaeiou]', x), lst))
lst = ["apple", "banana", "orange", "grape", "kiwi"]
print(filter_consonant_start(lst))


def starts_with_vowel(name):
    return name[0].lower() in ['a', 'e', 'i', 'o', 'u']

lst = ["apple", "banana", "orange", "grape", "kiwi"]
vowel_names = list(filter(starts_with_vowel, lst))
print("\nExtract names starting with a vowel:")
print(vowel_names)

"""
5. Write a Python function that filters out all empty strings
from a list of strings using the filter function.
"""
# Define a list of names
# 1st method
def empty(lst):
    return list(filter(lambda x:len(x)!=0, lst))

strings = ["", "w3resource", "Filter", "", "Python", ""]
print(empty(strings))

# 2nd method
def filter_non_empty(lst):
    return list(filter(bool, lst))

strings = ["", "w3resource", "Filter", "", "Python", ""]
print(filter_non_empty(strings))  # Output: ['w3resource', 'Filter', 'Python']

# 3rd method
def filter_non_empty(lst):
    return list(filter(lambda x: x.strip(), lst))
strings = ["", "w3resource", "Filter", " ", "Python", ""]
print(filter_non_empty(strings))  # Output: ['w3resource', 'Filter', 'Python']

"""
6. Write a Python program that creates a list of dictionaries containing 
student information (name, age, grade) and uses the filter function
to extract students with a grade greater than or equal to 95.
"""
# Define a list of dictionaries containing student information
students = [
    {"name": "Denis Helio", "age": 17, "grade": 97},
    {"name": "Hania Mehtap", "age": 16, "grade": 92},
    {"name": "Kelan Stasys", "age": 17, "grade": 90},
    {"name": "Velvet Mirko", "age": 16, "grade": 94},
    {"name": "Delores Aeneas", "age": 17, "grade": 100},]

def func(dct):
    return list(filter(lambda dct: dct["grade"] >= 95, dct))
print(func(students))

# Or
lambda_func = lambda dct: list(filter(lambda dct: dct["grade"] >= 95, dct))
print(lambda_func(students))

"""
7. Write a Python program that filters out prime numbers from
a list of integers using the filter function.
"""
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_primes(lst):
    return list(filter(is_prime, lst))
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime_numbers = filter_primes(numbers)
print(prime_numbers)  # Output: [2, 3, 5, 7, 11, 13]

"""
8. Write a Python program that creates a list of words and use the filter
function to extract words that contain more than five letters.
"""
def func(lst):
    return list(filter(lambda x:len(x) > 5, lst))
print(func(["Red", "Green", "Orange","White", "Black", "Pink", "Yellow"]))

# OR
lambda_func = lambda lst : list(filter(lambda x:len(x) > 5, lst))
print(lambda_func(["Red", "Green", "Orange","White", "Black", "Pink", "Yellow"]))

"""
9. Write a Python function that filters out elements from a list of strings
containing a specific substring using the filter function.
"""
def func(strings, substring):
    def contains_substring(string):
        return substring in string

    # Use the filter function to filter out strings with the substring
    filtered_strings = list(filter(contains_substring, strings))
    return filtered_strings

# Example usage:
strings = ["Red", "Green", "Orange", "White", "Black", "Pink", "Yellow"]
substring = "l"
print(func(strings, substring))

"""
10. Write a Python program that implements a Python program that filters out dates
(in the format "YYYY-MM-DD") that are in the future using the filter function..
"""
from datetime import datetime
date_strings = ["2023-07-11", "2022-02-22",
            "2024-05-11", "2025-12-31", "2021-01-01"]
print(date_strings)
dates = [datetime.strptime(date, "%Y-%m-%d") for date in date_strings]
current_date = datetime.now()
print("Current date:", current_date)
def is_date_in_future(date):
    return date > current_date
dates_in_past = list(filter(is_date_in_future, dates))

filtered_date_strings = [date.strftime("%Y-%m-%d") for date in dates_in_past]
print(filtered_date_strings)


"""
11. Write a Python program that creates a list of tuples, each containing
a city name and its population. Use the filter function to extract
cities with a population greater than 2 million.
"""
cities = [
    ("New York", 8500000),
    ("Los Angeles", 4000000),
    ("Chicago", 2700000),
    ("Houston", 2300000),
    ("Phoenix", 1600000),
    ("Philadelphia", 1500000),
    ("San Antonio", 1500000),]

def func(lst):
    return list(filter(lambda x: x[1] > 2000000, lst))
print(func(cities))