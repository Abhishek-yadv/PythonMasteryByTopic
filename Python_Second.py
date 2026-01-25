####################################################################
################################################ (Python Basics||)
####################################################################
"""1.Write a Python function that takes a sequence of numbers and determines
whether all the numbers are different from each other.. """
from functools import partial
from importlib.metadata import distributions
import pkgutil
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from bs4 import BeautifulSoup
import requests
from faker import Faker
from collections import Counter
from itertools import combinations
import itertools
import platform as pl
lst = [1, 2, 3, 4, 5, 4, 3, 2, 1]

def function(lst):
    if len(lst) == len(set(lst)):
        return True
    else:
        return False

print(function(lst))
# OR

def function(lst):
    return True if len(lst) == len(set(lst)) else False

print(function(lst))

"""
2.Write a Python program that creates all possible strings using the letters 'a',
'e', 'i', 'o', and 'I'. Ensure that each character is used only once.
"""
lst = ['a', 'e', 'i', 'o', 'I']
result = list(itertools.permutations(lst))
for i in result:
    print(''.join(i))

# OR
vowels = ['a', 'e', 'i', 'o', 'I']
result = []
for i in range(len(vowels)):
    for j in range(len(vowels)):
        if i != j:
            for k in range(len(vowels)):
                if i != k and j != k:
                    for l in range(len(vowels)):
                        if i != l and j != l and k != l:
                            for m in range(len(vowels)):
                                if i != m and j != m and k != m and l != m:
                                    result.append(
                                        vowels[i] + vowels[j] + vowels[k] + vowels[l] + vowels[m])
print(result)

# OR
# Using a generator to produce permutations lazily

def generate_permutations(letters, current=""):
    if len(current) == len(letters):  # Base case: when the length matches the original list
        yield current
    else:
        for letter in letters:
            if letter not in current:  # Avoid duplicate positions
                yield from generate_permutations(letters, current + letter)

# Input list
vowels = ['a', 'e', 'i', 'o', 'I']
# Using generator to produce permutations lazily
permutations = list(generate_permutations(vowels))
# Print results
print(permutations)

"""
3.Write a Python program that removes and prints every third number
from a list of numbers until the list is empty.
"""

def remove_third(lst):
    idx = 2  # Start from the third element (0-based index)
    while lst:
        idx = (idx % len(lst))  # Ensure circular behavior
        yield lst.pop(idx)  # Remove and yield the third element
        idx += 2  # Move to the next third element

lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]
result = list(remove_third(lst))
print(result)

"""
4.Write a Python program to identify unique triplets whose
three elements sum to zero from an array of n integers
"""
lst = [-25, -10, -7, -3, 2, 4, 8, 10]
result = list(itertools.combinations(lst, 3))
for i in result:
    if sum(i) == 0:
        print(i)
# OR
lst = [-25, -10, -7, -3, 2, 4, 8, 10]
result = []
for i in range(len(lst)):
    for j in range(len(lst)):
        for k in range(len(lst)):
            if i != j and i != k and j != k:
                if lst[i] + lst[j] + lst[k] == 0:
                    result.append((lst[i], lst[j], lst[k]))
                    print(result)
# OR

def find_unique_triplets(lst):
    seen = set()  # To store unique triplets and avoid duplicates
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):  # Avoid duplicate pairs by starting from `i+1`
            for k in range(j + 1, n):  # Ensure unique indices
                if lst[i] + lst[j] + lst[k] == 0:
                    triplet = tuple(sorted([lst[i], lst[j], lst[k]]))
                    if triplet not in seen:
                        seen.add(triplet)
                        yield triplet  # Yield instead of storing in list

lst = [-25, -10, -7, -3, 2, 4, 8, 10]
result = list(find_unique_triplets(lst))
print(result)

"""
5.Write a Python program to make combinations of 3 digits.
"""
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = list(combinations(lst, 3))
print(result)

# OR
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = []
for i in range(len(lst)):
    for j in range(len(lst)):
        for k in range(len(lst)):
            if i != j and i != k and j != k:
                result.append((lst[i], lst[j], lst[k]))
print(result)

"""6.Write a Python program that prints long text, converts it to a list,
and prints all the words and the frequency of each word."""
long_text = """
Python is an interpreted high-level general-purpose programming language.
Python's design philosophy emphasizes code readability with its notable
use of significant indentation. Its language constructs and object-oriented
approach aim to help programmers write clear, logical code for small and large-scale projects."""
words = long_text.split()
word_freq = [k + ": " + str(words.count(k)) for k in set(words)]
print("\n".join(word_freq))

# OR
words = long_text.split()
word_freq = Counter(words)
print(word_freq)

"""7.Character Frequency in File
Write a Python program to count the number of each character in a text file."""
text_file = Faker()
fake = text_file.text(300)
with open("text.txt", "w") as file_handler:
    file_handler.write(fake)
with open("text.txt", "r") as file_handler:
    text = file_handler.read()
print(text)
# Count character frequency
char_freq = Counter(text)
print(char_freq)

""" 
8.Write a Python program that retrieves the top stories from Google News.
"""
url = "https://news.google.com/news/rss"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
articles = soup.find_all('article')
for article in articles:
    print(article.text)

# OR
with urlopen("https://news.google.com/news/rss") as client:
    xml_page = client.read()
news_list = soup(xml_page, "xml").findAll("item")
for news in news_list:
    print(f"{news.title.text}\n{news.link.text}\n{news.pubDate.text}\n" + "-" * 60)

"""9.Write a Python program to get a list of locally installed Python modules."""

for importer, modname, ispkg in pkgutil.iter_modules():
    print(modname)

# OR
# Import the 'pkg_resources' module for working with Python packages.
for dist in distributions():
    print(dist.metadata["Name"], dist.version)

"""10.Write a Python program to display some information about the OS where the script is running."""
# List of attributes to retrieve from the 'platform' module.
import platform as pl
os_profile = [
    'architecture',
    'linux_distribution',
    'mac_ver',
    'machine',
    'node',
    'platform',
    'processor',
    'python_build',
    'python_compiler',
    'python_version',
    'release',
    'system',
    'uname',
    'version',
]
for key in os_profile:
    if hasattr(pl, key):
        print(key + ": " + str(getattr(pl, key)()))

"""
11.Write a Python program to check the sum of three elements (each from an array) from three arrays
is equal to a target value. Print all those three-element combinations.
Sample data:
/*
X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]
target = 70
*/
"""
# Import the 'itertools' module for advanced iteration tools and 'partial' from 'functools'.
X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]
T = 70

def check_sum_array(N, *nums):
    if sum(x for x in nums) == N:
        return (True, nums)
    else:
        return (False, nums)

pro = itertools.product(X, Y, Z)
func = partial(check_sum_array, T)
sums = list(itertools.starmap(func, pro))
result = set()
for s in sums:
    if s[0] == True and s[1] not in result:
        result.add(s[1])
        print(result)

"""12.Write a Python program that generates a list of
all possible permutations from a given collection of distinct numbers. """
dist_lst = [1, 2, 3]
# Generate all permutations of the list
permutations = list(itertools.permutations(dist_lst))
print(permutations)

"""13.
Write a Python program to get all possible two-digit letter combinations from a 1-9 digit string.
"""
def letter_combinations(digits):
    if not digits:
        return []
    string_maps = {
        "1": "abc", "2": "def", "3": "ghi", "4": "jkl",
        "5": "mno", "6": "pqrs", "7": "tuv", "8": "wxy", "9": "z"}
    result = [""]
    for num in digits:
        result = [prev + char for prev in result for char in string_maps[num]]
    return result

print(letter_combinations("47"))
print(letter_combinations("29"))

"""14.
Write a Python program to add two positive integers without using the '+' operator.
Note: Use bit wise operations to add two numbers.
"""

def add(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

print(add(10, 20))

"""15."
Write a Python program to check the priority of the four operators (+, -, *, /)."
"""

def priority(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or '/':
        return 2
    else:
        return 0
print(priority('+'))

"""16.Write a Python program to get the third side of a right-angled triangle from two given sides."""
import math
def right_triangle(a, b):
    return math.sqrt(a**2 + b**2)
print(right_triangle(3, 4))

"""17.Write a Python program to get all strobogrammatic numbers that are of length n."""
def strobogrammatic(n):
    if n == 0:
        return ['']
    if n == 1:
        return ['0', '1', '8']
    result = []
    for num in strobogrammatic(n - 2):
        result.append('0' + num + '0')
        result.append('1' + num + '1')
        result.append('6' + num + '9')
        result.append('8' + num + '8')
        result.append('9' + num + '6')
    return result
print(strobogrammatic(3))

"""18.Write a Python program to find the median among three given numbers."""
def median(a,b,c):
    return sorted([a,b,c])[1]
print(median(1,2,3))

"""19.Write a Python program that finds the value of n when n degrees of number 2 
are written sequentially on a line without spaces between them."""
def zero_num(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * zero_num(n-1)
    return n
n = 100
result = zero_num(n)
def count_zero(result):
    count = 0
    while result % 10 == 0:
        count += 1
        result //= 10
    return count
print(count_zero(result))  # Output: 1

# 2nd method
from functools import reduce
fact = lambda n: reduce(lambda x, y: x * y, range(1, n+1), 1)
zeros = lambda n: len(str(fact(n))) - len(str(fact(n)).rstrip('0'))
print(zeros(10))  # 24

"""
21.Write a Python program to find the number of notes (Samples of notes: 10, 20, 50, 100, 200, 500)
against an amount.Range - Number of notes(n) n (1 <= n <= 1000000).
"""
def find_notes(amount):
    notes = [500, 200, 100, 50, 20, 10]  # Start from the largest note
    note_count = []
    for note in notes:
        count = amount // note
        if count:
            note_count.append((note, count))
            amount %= note
    return note_count

result = find_notes(880)
print("Note breakdown:")
for note, count in result:
    print(f"{note} x {count}")

"""
22.
Write a Python program to create a sequence where the first four members of the
sequence are equal to one. Each successive term of the sequence is equal
to the sum of the four previous ones. Find the Nth member of the sequence.
"""
def find_nth_term(n):
    seq = [1, 1, 1, 1]
    for i in range(4, n):
        seq.append(sum(seq[-4:]))
    return seq[n - 1]
print(find_nth_term(6))

# OR
from functools import reduce
find_nth = lambda n: reduce(lambda seq, _: seq + [sum(seq[-4:])], range(n - 4), [1, 1, 1, 1])[n - 1]
print(find_nth(10))  # Output: 94

# OR
from functools import lru_cache
@lru_cache(maxsize=None)
def find_nth_recursive(n):
    if n <= 4:
        return 1
    return sum(find_nth_recursive(i) for i in range(n - 4, n))
print(find_nth_recursive(10))  # Output: 94

# OR
def new_seq(n):
    if n ==1 or n == 2 or n == 3 or n == 4:
        return 1
    return new_seq(n - 1) + new_seq(n - 2) + new_seq(n - 3) + new_seq(n - 4)
print(new_seq(5))

"""
23.
Write a Python program that accepts a positive number and subtracts from 
it the sum of its digits,and so on. Continue this operation until the number is positive.
"""
def subtract_sum(n):
    while n > 0:
        digit_sum = sum(int(digit) for digit in str(n))
        # digit_sum = sum(map(int, str(n)))  # Alternative using map
        n -= digit_sum
    return n
print(subtract_sum(100))  # Output: 0

"""
24.
Write a Python program to find the total number of even or odd divisors of a given integer.
"""
def count_div(n):
    even_count = 0
    odd_count = 0
    for i in range(1, n+1):
        if n%i == 0:
            if i%2==0:
                even_count +=1
            else:
                odd_count +=1
    return even_count, odd_count
print(count_div(4))  # Output: (4, 3) - 4 even divisors and 3 odd divisors
# OR
def count_div(n):
    even_count = len([i for i in range(1, n+1) if n % i == 0 and i % 2 == 0])
    odd_count = len([i for i in range(1, n+1) if n % i == 0 and i % 2 != 0])
    return even_count, odd_count
print(count_div(4))

# OR
count_div = lambda n: (len([i for i in range(1, n+1) if n % i == 0 and i % 2 == 0]), len([i for i in range(1, n+1) if n % i == 0 and i % 2 != 0]))
print(count_div(4))

"""
25.Write a Python program to find the digits that are missing from a given mobile number.
"""
def missing_digits(mobile_number):
    all_digits = set('0123456789')
    mobile_digits = set(str(mobile_number))
    miss_digits = all_digits - mobile_digits
    return sorted(miss_digits)
dig = missing_digits(1234567890)  # Output: [] (no missing digits)
print(dig)

"""
26.
Write a Python program to compute the summation of the absolute difference
of all distinct pairs in a given array (non-decreasing order).
Sample array: [1, 2, 3]
Then all the distinct pairs will be:
1 2
1 3
2 3
"""
import itertools
def sum_abs_diff(arr):
    total = 0
    for pair in itertools.combinations(arr, 2):
        total += abs(pair[0] - pair[1])
    return total    
print(sum_abs_diff([1, 2, 3]))  # Output: 4

"""
27.Write a Python program to find the type of the progression (arithmetic progression / geometric progression)
and the next successive member of the three successive members of a sequence.
"""
def find_progression_type(a, b, c):
    if b - a == c - b:
        return "Arithmetic Progression", c + (b - a)
    elif b / a == c / b:
        return "Geometric Progression", c * (b / a)
    else:
        return "Not a progression", None
print(find_progression_type(2, 4, 6))  # Output: ('Arithmetic Progression', 8)
print(find_progression_type(2, 4, 8))  # Output: ('Geometric Progression', 16)

"""
28.
Write a Python program to print the length of the series and the series from
the given 3rd term, 3rd last term and the sum of a series.
Sample Data:
Input third term of the series: 3
Input 3rd last term: 3
Input Sum of the series: 15
Length of the series: 5
Series:
1 2 3 4 5
"""
def print_series():
    # Take user input
    third_term = int(input("Input third term of the series: "))
    third_last_term = int(input("Input 3rd last term: "))
    total_sum = int(input("Sum of the series: "))

    # Calculate the number of terms using the formula: n = 2S / (a + l)
    n = int(2 * total_sum / (third_term + third_last_term))
    print("Length of the series:", n)

    # Handle the edge case when n == 5 to avoid division by zero
    if n - 5 == 0:
        d = (total_sum - 3 * third_term) // 6
    else:
        d = (third_last_term - third_term) / (n - 5)

    # Calculate the first term
    a = third_term - 2 * d

    # Generate the series
    print("Series:")
    for i in range(n):
        print(int(a + i * d), end=" ")
print_series()

"""
29.Write a Python program to find common divisors between two numbers in a given pair.
"""
def common_divisors(a, b):
    divisors_a = [i for i in range(1, a + 1) if a % i == 0]
    divisors_b = [i for i in range(1, b + 1) if b % i == 0]
    return list(set(divisors_a) & set(divisors_b))
print(common_divisors(12, 15))

"""
30.Write a Python program to reverse the digits of a given number and add them to the original.
Repeat this procedure if the sum is not a palindrome.
"""
def reverse_and_add(n):
    if str(n) == str(n)[::-1]:
        return n
    else:
        reversed_n = int(str(n)[::-1])
        return reverse_and_add(n + reversed_n)
    print(reverse_and_add(1234))  # Output: 6666 (palindrome)
# OR    
def reverse_and_add(n):
    while str(n) != str(n)[::-1]:
        reversed_n = int(str(n)[::-1])
        n += reversed_n
    return n
print(reverse_and_add(1234))  # Output: 6666 (palindrome)

"""
31.Write a Python program to count the number of carry operations for each addition problem.
"""
def count_carry_operations(a, b):
    carry = 0
    count = 0
    while a > 0 or b > 0:
        digit_a = a % 10
        digit_b = b % 10
        if digit_a + digit_b + carry >= 10:
            count += 1
            carry = 1
        else:
            carry = 0
        a //= 10
        b //= 10
    return count
print(count_carry_operations(123, 456))  # Output: 0 (no carry operations)

"""
32.Write a Python program to find the heights of the top three
buildings in descending order from eight given buildings.
"""
def top_three_buildings(buildings):
    return sorted(buildings, reverse=True)[:3]
print(top_three_buildings([1, 2, 3, 4, 5, 6, 7, 8]))# Output: [8, 7, 6]
"""
['os.path', 'os.path.dirname()', 'os.path.basename()',
'os.path.splitext()', 'os.path.join()', 'os.path.isabs()',
'os.path.relpath()', 'os.path.expanduser()', 'os.path.realpath()',
'os.path.abspath()', 'os.path.exists()', 'os.path.isfile()', 'os.path.isdir()',
'os.path.islink()', 'os.path.isjunction()', 'os.path.ismount()',
'os.path.samefile()', 'os.getcwd()', 'os.stat()', 'os.lstat()',
'os.listdir()', 'os.walk()', 'os.mkdir(), os.makedirs()', 'os.link()',
'os.symlink()', 'os.readlink()', 'os.rename()', 'os.replace()', 'os.remove(),
os.unlink()', 'os.rmdir()', 'os.chmod()', 'os.lchmod()']
"""

"""
33.Write a Python program to compute the digit number of the sum of two given integers.
"""
a = input("Enter first number: ")
b = input("Enter second number: ")
def digit_sum(a, b):
    return len(str(int(a) + int(b)))

print("Input two integers(a b): ")
a, b = map(int, input().split(" "))
print("Number of digits of a and b:")
print(len(str(a + b)))

""" 34.Write a Python program to check whether three given lengths (integers) of three
sides form a right triangle.Print "Yes" if the given sides form a right triangle otherwise print "No".
"""
def is_right_triangle(a, b, c):
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2

def right_triangle(a,b,c):
    return "Yes" if (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == b**2 + a**2) else "No"
print(right_triangle(3,4,5))
print("Yes" if (lambda s: s[2]**2 == s[0]**2 + s[1]**2)(sorted([3, 4, 5])) else "No")

def right_triangle(a, b, c):
    return "Yes" if any(x**2 == y**2 + z**2 for x, y, z in [(a, b, c), (b, a, c), (c, a, b)]) else "No"
print(right_triangle(3, 4, 5))

"""
35.Write a Python program which solve the equation:
ax+by=c
dx+ey=f
Print the values of x, y where a, b, c, d, e and f are given.
"""
import numpy as np
a, b, c = 2, 3, 8
d, e, f = 1, 2, 5
A = np.array([[a, b], [d, e]])
B = np.array([c, f])
X = np.linalg.solve(A, B)
print(X[0])
print(X[1])

def solve_equation(a, b, c, d, e, f):
    x = (c * e - b * f) / (a * e - b * d)
    y = (c - a * x) / b
    return x, y
a, b, c, d, e, f = map(int, input("Enter a, b and c: ").split())

"""
36.Write a Python program to compute the amount of debt in n months.
Each month, the loan adds 5% interest to the $100,000 debt and rounds to the nearest 1,000 above.
"""
def debt(n):
    amount = 100000
    for i in range(n):
        amount = amount * 0.05 + amount
        amount = round(amount, -3)
    return amount
print(debt(7))  # Output: 105000.0

"""
37.Write a Python program that reads an integer n and finds the number of combinations of 
a,b,c and d (0 = a,b,c,d = 9) where (a + b + c + d) will be equal to n
"""
import itertools
print("Input the number(n):")
n = int(input())
result = 0
for (i, j, k) in itertools.product(range(10), range(10), range(10)):
    result += (0 <= n - (i + j + k) <= 9)
print("Number of combinations:", result)

import sys
print(sys.builtin_module_names)

"""
38.Write a Python program to print the number of prime numbers that
are less than or equal to a given number.
"""
def prime(n):
    count = 0
    for i in range(2, n + 1):
        if is_prime(i):
            count += 1
    return count
def is_prime(n):    
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n % 2 == 0:
        return 0
    for i in range(3, n, 2):
        if n % i == 0:
            return 0
    return 1
print(prime(10))  # Output: 4 (2, 3, 5, 7)
# OR
print(sum(all(i % d for d in range(2, int(i**0.5)+1)) and i != 1 for i in range(2, 11)))
prime_num = lambda n: len([i for i in range(2, n + 1) if all(i % d for d in range(2, int(i**0.5)+1)) and i != 1])
print(prime_num(10))  # Output: 4 (2, 3, 5, 7)

"""
39.Write a program to compute the radius and the central coordinate (x, y) of a circle
which is constructed from three given points on the plane surface.
"""
def get_circle_data(x1, y1, x2, y2, x3, y3):
    a = (x2 - x3)**2 + (y2 - y3)**2
    b = (x3 - x1)**2 + (y3 - y1)**2
    c = (x1 - x2)**2 + (y1 - y2)**2
    s = 2 * (a*b + b*c + c*a) - (a**2 + b**2 + c**2)
    px = (a*(b+c-a)*x1 + b*(c+a-b)*x2 + c*(a+b-c)*x3) / s
    py = (a*(b+c-a)*y1 + b*(c+a-b)*y2 + c*(a+b-c)*y3) / s
    ar, br, cr = a**0.5, b**0.5, c**0.5
    r = ar * br * cr / ((ar + br + cr) * (-ar + br + cr) * (ar - br + cr) * (ar + br - cr))**0.5
    return round(r, 3), round(px, 3), round(py, 3)

coords = list(map(float, input("Enter three coordinates (x1 y1 x2 y2 x3 y3): ").split()))
r, cx, cy = get_circle_data(*coords)
print(f"Radius: {r}")
print(f"Center: ({cx}, {cy})")


"""
40.Write a Python program to check if a point (x,y) is in a triangle or not.
A triangle is formed by three points.
"""
# Prompt user to input coordinates of the triangle vertices (x1, y1), (x2, y2), (x3, y3),
# and the point (xp, yp) to check if it lies inside the triangle
print("Input x1, y1, x2, y2, x3, y3, xp, yp:")
x1, y1, x2, y2, x3, y3, xp, yp = map(float, input().split())

# Calculate the cross products (c1, c2, c3) for the point relative to each edge of the triangle
c1 = (x2 - x1) * (yp - y1) - (y2 - y1) * (xp - x1)
c2 = (x3 - x2) * (yp - y2) - (y3 - y2) * (xp - x2)
c3 = (x1 - x3) * (yp - y3) - (y1 - y3) * (xp - x3)

# Check if all cross products have the same sign (inside the triangle) or different signs (outside the triangle)
if (c1 < 0 and c2 < 0 and c3 < 0) or (c1 > 0 and c2 > 0 and c3 > 0):
    print("The point is in the triangle.")
else:
    print("The point is outside the triangle.")


"""
41.Write a Python program to compute and print the sum of two given integers (greater or equal to zero).
In the event that the given integers or the sum exceed 80 digits, print "overflow".
"""
def sum_of_two(num1, num2):
    if num1 < 0 or num2 < 0:
        return "Invalid input. Both numbers must be non-negative."
    return "overflow" if len(str(num1 + num2)) > 80 else num1 + num2

"""
42.Write a Python program that accepts six numbers as input and sorts them in descending order.
"""
def sort_numbers(numbers):
    return sorted(numbers, reverse=True)
num = input("Enter six numbers separated by spaces: ").split()
numbers = list(map(int, num))
sorted_numbers = sort_numbers(numbers)
print("Sorted numbers in descending order:", sorted_numbers)

"""
43.Write a Python program to test whether two lines PQ and RS are parallel.
The four points are P(x1, y1), Q(x2, y2), R(x3, y3), S(x4, y4).
"""
print("Input x1, y1, x2, y2, x3, y3, x4, y4:")
x1, y1, x2, y2, x3, y3, x4, y4 = map(float, input().split())
print('PQ and RS are parallel.' if abs((x2 - x1)*(y4 - y3) - (x4 - x3)*(y2 - y1)) < 1e-10 else 'PQ and RS are not parallel')


"""
44. Write a Python program to find the maximum sum of a contiguous subsequence from a given sequence
of numbers a1,a2, a3, ... an.A subsequence of one element is also a continuous subsequence.
"""
def max_subsequence_sum(sequence):
    max_sum = current_sum = sequence[0]
    for num in sequence[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
sequence = list(map(int, input("Enter a sequence of numbers separated by spaces: ").split()))
print("Maximum subsequence sum:", max_subsequence_sum(sequence))


# Infinite loop to continuously receive input until the user enters 0
while True:
    print("Input number of sequence of numbers you want to input (0 to exit):")
    n = int(input())
    if n == 0:
        break
    else:
        A = []
        Sum = []
        print("Input numbers:")
        for i in range(n):
            A.append(int(input()))        
        Wa = 0
        for i in range(0, n):
            Wa += A[i]
            Sum.append(Wa)
        
        # Generate all possible contiguous subsequences and add them to the Sum list
        for i in range(0, n):
            for j in range(0, i):
                Num = Sum[i] - Sum[j]
                Sum.append(Num)
        
        # Print the maximum sum of the contiguous subsequence
        print("Maximum sum of the said contiguous subsequence:")
        print(max(Sum))

"""
45.There are two circles C1 with radius r1, central coordinate (x1, y1)
and C2 with radius r2 and central coordinate (x2, y2).

Write a Python program to test the followings -
"C2 is in C1" if C2 is in C1
"C1 is in C2" if C1 is in C2
"Circumference of C1 and C2 intersect" if circumference of C1 and C2 intersect
"C1 and C2 do not overlap" if C1 and C2 do not overlap and
"Circumference of C1 and C2 will touch" if C1 and C2 touch
"""
# Import the math module
import math
print("Input x1, y1, r1, x2, y2, r2:")
x1, y1, r1, x2, y2, r2 = [float(i) for i in input().split()]
d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
if d <= r1 - r2:
    print("C2 is in C1")
elif d <= r2 - r1:
    print("C1 is in C2")
elif d < r1 + r2:
    print("Circumference of C1 and C2 intersect")
elif d == r1 + r2:
    print("Circumference of C1 and C2 will touch")
else:
    print("C1 and C2 do not overlap")

"""
46. Write a Python program that reads a date (from 2016/1/1 to 2016/12/31) and
prints the day of the date.Jan. 1, 2016, is Friday. Note that 2016 is a leap year.
"""
import datetime
print("Input date (YYYY/MM/DD):")
date = input()
date = datetime.datetime.strptime(date, "%Y/%m/%d")
print("Day of the date:", date.strftime("%A"))

"""
47.Write a Python program that reads text (only alphabetical characters and spaces) and
prints two words. The first word is the one that appears most often in the text. The second 
one is the word with the most letters.
"""
from collections import Counter
words = input("Enter text: ").split()
word_count = Counter(words)
most_common_word = word_count.most_common(1)[0][0]
longest_word = max(words, key=len)
print("Most frequent word:", most_common_word)
print("Longest word:", longest_word)

"""
48.Write a Python program that reads n digits (given) chosen from 0 to 9 and prints the number
of combinations where the sum of the digits equals another given number (s).
Do not use the same digits in a combination.
"""
import itertools
print("Input n and s:")
n, s = map(int, input().split())
result = 0
for combination in itertools.combinations(range(10), n):
    if sum(combination) == s:
        result += 1
print("Number of combinations:", result)

"""
49.Write a Python program that reads the two adjoining sides and the diagonal of a parallelogram
and checks whether the parallelogram is a rectangle or a rhombus.
"""
import math
a, b, d = map(float, input("Input two adjoined sides and the diagonal of a parallelogram (comma separated): ").split(','))
if a + b <= d:
    print("Invalid parallelogram: the diagonal is too long.")
else:
    is_rectangle = math.isclose(d**2, a**2 + b**2, rel_tol=1e-9)
    is_rhombus = math.isclose(a, b, rel_tol=1e-9)
    if is_rectangle and is_rhombus:
        print("This is a square.")
    elif is_rectangle:
        print("This is a rectangle.")
    elif is_rhombus:
        print("This is a rhombus.")
    else:
        print("This is just a parallelogram.")

"""
50.Write a Python program to replace a string "Python" with
"Java" and "Java" with "Python" in a given string.
"""
text = input("Enter a sentence with 'Python' and 'Java': ")
text = text.replace("Python", "__TEMP__")
text = text.replace("Java", "Python")
text = text.replace("__TEMP__", "Java")
print("Modified text:")
print(text)

import sys
text = sys.stdin.read()  # Reads until EOF (Ctrl+D or Ctrl+Z+Enter)
text = text.replace("Python", "__TEMP__").replace("Java", "Python").replace("__TEMP__", "Java")
print(text)


print("Input a text with two words 'Python' and 'Java'")
text = input().split()
for i in range(len(text)):
    # Check if 'Python' is present in the current word
    if "Python" in text[i]:
        # Find the index of 'Python' in the current word
        n = text[i].index("Python")
        # Replace 'Python' with 'Java' in the current word
        text[i] = text[i][:n] + "Java" + text[i][n + 6:]
    # Check if 'Java' is present in the current word
    elif "Java" in text[i]:
        # Find the index of 'Java' in the current word
        n = text[i].index("Java")
        # Replace 'Java' with 'Python' in the current word
        text[i] = text[i][:n] + "Python" + text[i][n + 4:]
print(*text)

"""
51.Write a Python program that determines the difference between the largest and smallest integers
created by 8 numbers from 0 to 9.The number that can be rearranged shall start with 0 as in 00135668.
"""
def diff(m):
    # Ensure input is a string to preserve leading zeros
    m = str(m).zfill(8)  # Pads with zeros if length < 8
    m_big = int("".join(sorted(m, reverse=True)))
    m_small = int("".join(sorted(m)))
    return m_big - m_small
print(diff("668"))
# OR
def diff(m):
    m = str(m).zfill(8)
    m_big = "".join(sorted(m, reverse=True))  # Sorted digits in descending order
    m_small = "".join(sorted(m))              # Sorted digits in ascending order
    return int(m_big) - int(m_small)
print(diff("668"))

"""
52.Write a Python program to compute the sum of the first n prime numbers.
"""
def sum_primes(n):
    prime_num = lambda n:True if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)) else False
    primes = [i for i in range(2, n) if prime_num(i)]  # Generate first n prime numbers
    return sum(primes)
print(sum_primes(10))  # Output: 17 (2 + 3 + 5 + 7)

# OR
def sum_primes(n):
    return sum(i for i in range(2, n) if all(i % j for j in range(2, int(i**0.5) + 1)))
print(sum_primes(10))

"""
53.Write a Python program which accepts an even number (>=4, Goldbach number) from the user and creates
combinations which express the given number as a sum of two prime numbers. Print the number of combinations.
"""
from itertools import combinations
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def goldbach(n):
    primes = [i for i in range(2, n) if is_prime(i)]
    print("Primes:", primes)
    combinations_count = 0
    for i in combinations(primes, 2):
        if sum(i) == n:
            combinations_count += 1
    return combinations_count
print("Input an even number (>=4):")
n = int(input())
print("Number of combinations:", goldbach(n))

"""
54. Write a Python program to create the maximum number of regions obtained by drawing n given straight lines.
"""
def max_regions(n):
    return (n * (n + 1)) // 2 + 1
print("Input number of lines:")
n = int(input())
print("Maximum number of regions:", max_regions(n)) 

"""
55. Orthogonal Line Checker
There are four different points on a plane, P(xp,yp), Q(xq, yq), R(xr, yr) and S(xs, ys).
Write a Python program to determine whether AB and CD are orthogonal.
"""
print("Input x1, y1, x2, y2, x3, y3, x4, y4:")
x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
if (x2 - x1) * (x4 - x3) + (y2 - y1) * (y4 - y3) == 0:
    print("AB and CD are orthogonal.")
else:
    print("AB and CD are not orthogonal.")

"""
56.Write a Python program to sum all numerical values (positive integers) embedded in a sentence.
"""
import re
def sum_numbers_in_text(text):
    return sum(map(int, re.findall(r'\d+', text)))
# Example usage
sentence = "Walked 4 kilometers, burned 250 calories, and drank 2 liters."
print(sum_numbers_in_text(sentence))  # Output: 256

