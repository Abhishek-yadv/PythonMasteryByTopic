####################################################################
######################################################## Itertools
####################################################################

# Infinite iterators:
# count, cycle, repeat
import itertools as it
import heapq
from heapq import merge
import datetime
from operator import itemgetter
import os
from collections import UserDict
from collections import UserList
from collections import UserString
from collections import ChainMap
import itertools
from itertools import accumulate
import operator
from itertools import count
import time
lst = count(10, 2)
for k in lst:
    print(k)
    time.sleep(1)

import time
from itertools import cycle
itr = cycle('ABCD')
for k in itr:
    print(k)
    time.sleep(1)

import time
from itertools import repeat
itr = repeat('ABCD', 4)
for k in itr:
    print(k, end = " ")
    time.sleep(1)

# Iterators terminating on the shortest input sequence:
from itertools import accumulate
itr = accumulate([1, 2, 3, 4, 5])
print(list(itr))

from itertools import batched
itr = batched('abhishek', 2)
print(list(itr))

from itertools import chain
itr = chain('ABC', 'DEF')
print(list(itr))

from itertools import chain
itr = chain.from_iterable(['ABC', 'DEF'])
print(list(itr))

from itertools import compress
itr = compress('ABCDEF', [1, 0, 1, 0, 1, 1])
print(list(itr))

from itertools import dropwhile
itr = dropwhile(lambda x: x < 5, [1, 4, 6, 3, 8])
print(list(itr))

from itertools import filterfalse
itr = filterfalse(lambda x: x < 5, [1, 4, 6, 3, 8])
print(list(itr))

from itertools import groupby
words = ['apple', 'apricot', 'banana', 'blueberry', 'cherry', 'citrus']
grouped_words = groupby(words, key=lambda x: x[0])
for key, group in grouped_words:
    print(f"Group {key}:")
    for word in group:
        print(f"  {word}")

from itertools import islice
itr = islice('ABCDEFG', 2, None)
print(list(itr))

from itertools import pairwise
itr = pairwise('ABCDEFG')
print(list(itr))

from itertools import starmap
itr = starmap(pow, [(2, 5), (3, 2), (10, 3)])
print(list(itr))

def func(x,y): return x+y
from itertools import starmap
itr = starmap(func, [(2, 5), (3, 2), (10, 3)])
print(list(itr))

from itertools import takewhile
itr = takewhile(lambda x: x < 5, [1, 4, 6, 3, 8])
print(list(itr))

from itertools import zip_longest
itr = zip_longest('ABCD', 'xy', fillvalue='-')
print(list(itr))

# Combinatoric iterators:
from itertools import product
itr = product('ABCD', repeat=2)
print(list(itr))
# AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD

from itertools import permutations
itr = permutations('ABCD', 2)
print(list(itr))
# AB AC AD BA BC BD CA CB CD DA DB DC

from itertools import combinations
itr = combinations('ABCD', 2)
print(list(itr))
# AB AC AD BC BD CD

from itertools import combinations_with_replacement
itr = combinations_with_replacement('ABCD', 2)
print(list(itr))
# AA AB AC AD BB BC BD CC CD DD

###################################################################
"""
1. Write a Python program to create an iterator from several iterables in
a sequence and display the type and elements of the new iterator.
"""
from itertools import chain
def chain_func(l1, l2, l3):
    return chain(l1, l2, l3)

# List
result = chain_func([1, 2, 3], ['a', 'b', 'c', 'd'], [4, 5, 6, 7, 8, 9])
print("Type of the new iterator:")
print(type(result))
print("Elements of the new iterator:")
for i in result:
    print(i)

# Tuple
result = chain_func((10, 20, 30, 40), ('A', 'B', 'C', 'D'), (40, 50, 60, 70, 80, 90))
print("Type of the new iterator:")
print(type(result))
print("Elements of the new iterator:")
for i in result:
    print(i)

###################################################################
"""
2. Write a Python program that generates the running product of elements in an iterable.
"""
from itertools import accumulate
import operator
def running_product(it):
    return accumulate(it, operator.mul)

result = running_product([1, 2, 3, 4, 5, 6, 7])
print("Running product of a list:")
for i in result:
    print(i)

result = running_product((1, 2, 3, 4, 5, 6, 7))
print("Running product of a Tuple:")
for i in result:
    print(i)

###################################################################
"""
3. Write a Python program to generate the maximum and 
minimum values of the elements of an iterable.
"""
from itertools import accumulate
def func(itr):
    return (accumulate(itr, func=max))

from itertools import accumulate
def func(itr):
    return (accumulate(itr, func=min))

result = func([1,3,2,7,9,8,10,11,12,14,11,12,7])
print("Running maximum value of a list:")
for i in result:
    print(i)


###################################################################
"""
4. Write a Python program to construct an infinite iterator that returns
evenly spaced values starting with a specified number and step.
"""
k = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
# >>> [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
print(k)

k = {x: x**2 for x in (2, 4, 6)}
print(k)

###################################################################
"""
5. Write a Python program to generate an infinite cycle of elements from an iterable.
"""
import itertools
def func(itr):
    return itertools.cycle(itr)

result = func([1, 2, 3, 4, 5])
print("Infinite cycle of a list:")
for i in result:
    print(i)
    
###################################################################
"""
6. Write a Python program to make an iterator that drops elements
from the iterable as soon as an element is a positive number. """
from itertools import dropwhile
def func(itr):
    return list(dropwhile(lambda x: x > 0, itr))
result = func([1, -2, 3, -4, 5, -6, 7, -8])
print(result)

###################################################################
"""
7. Write a Python program to make an iterator that drops elements from the
iterable as long as the elements are negative; afterwards, it returns every element. """
from itertools import dropwhile
def func(itr):
    return dropwhile(lambda x : x< 0, itr)
result = func([1, -2, 3, -4, 5, -6, 7, -8])
print(list(result))

###################################################################
"""
8. Write a Python program to create an iterator that returns
consecutive keys and groups from an iterable.. """
from itertools import groupby
print("Iterate over characters of a string and display\nconsecutive keys and groups from the iterable:")
str1 = 'AAAAJJJJHHHHNWWWEERRRSSSOOIIU'
data_groupby = groupby(str1)
for key, group in data_groupby:
    print('Key:', key)
    print('Group:', list(group))
    
print("\nIterate over elements of a list and display\nconsecutive keys and groups from the iterable:")
str1 = 'AAAAJJJJHHHHNWWWEERRRSSSOOIIU'
str1 = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 7, 8]
data_groupby = groupby(str1)
for key, group in data_groupby:
    print('Key:', key)
    print('Group:', list(group))


###################################################################
"""
9. Write a Python program to split an iterable and
generate iterables a specified number of times... """
from itertools import tee
def tee_data(iter, n):
    return tee(iter, n)

# List
result = tee_data(['A', 'B', 'C', 'D'], 5)
print("Generate iterables specified number of times:")
for i in result:
    print(list(i))

# String
result = tee_data("Python itertools", 4)
print("\nGenerate iterables specified number of times:")
for i in result:
    print(list(i))

###################################################################
"""
10. Write a Python program to create an iterator to get
a specified number of permutations of elements.... 
"""
from itertools import permutations
def func(itr, num):
    return list(permutations(itr, num))
num = int(input("Enter your input: "))
print(func(['A', 'B', 'C', 'D'], num))


"""
11. Write a Python program to generate combinations
of a given length of a given iterable.
"""
from itertools import combinations
def func(itr, num):
    return list(combinations(itr, num))

num = int(input("Enter your input: "))
print(func(['A', 'B', 'C', 'D'], num))

"""
12. Write a Python program to compute the Cartesian product
of two or more given lists using itertools.
"""
from itertools import product
def cartesian_product(lists):
    return list(product(*lists))

ls = [[1, 2], [3, 4]]
print("Original Lists:", ls)
print("Cartesian product of the said lists: ", cartesian_product(ls))

"""
13. Write a Python program that will select a specified number of colours
from three different colours, and then generate all the combinations with repetitions.
"""
from itertools import combinations_with_replacement
def combinations_colors(l, n):
    return combinations_with_replacement(l,n)
l = ["Red","Green","Blue"]
print("Original List: ",l)
n=1
print("\nn = 1")
print(list(combinations_colors(l, n)))
n=2
print("\nn = 2")
print(list(combinations_colors(l, n)))
n=3
print("\nn = 3")
print(list(combinations_colors(l, n)))

"""
14. Write a Python program to generate permutations of
specified elements drawn from specified values.
"""
from itertools import product 
def permutations_colors(inp, n):
    for x in product(inp, repeat=n):
        c = ''.join(x)
        print(c,end=', ')

str1 = "Red"
print("Original String: ",str1)
print("Permutations of specified elements, drawn from specified values:")
n=1
print("\nn = 1")
permutations_colors(str1,n)
n=2
print("\nn = 2")
permutations_colors(str1,n)
n=3
print("\nn = 3")
permutations_colors(str1,n)

"""
15. Write a Python program to generate all
possible permutations of n different objects.
"""
from itertools import permutations
def func(itr):
    for value in permutations(itr):
        print(value)
result = func([1])
print("\n")
result = func([1, 2])
print("\n")
result = func([1, 2, 3])

"""
16. Write a Python program to find the sorted sequence
from a set of permutations of a given input.
"""
from itertools import permutations
def is_sorted(sequence):
    return all(a <= b for a, b in zip(sequence, sequence[1:]))

def permutation_sort(lst):
    for perm in permutations(lst):
        if is_sorted(perm):
            return perm

print("All the sequences:")
print("\nSorted sequence:", permutation_sort([12, 10, 9]))

print("\n\nAll the sequences:")
print("\nSorted sequence:", permutation_sort([2, 3, 1, 0]))

"""
17. Write a Python program to read a given string character by character
and compress repeated characters by storing the length of those character(s).
"""
from itertools import groupby
def encode_str(input_str):
    return [(len(list(n)), m) for m,n in groupby(input_str)]

str1 = "AAASSSSKKIOOOORRRREEETTTTAAAABBBBBBDDDDD" 
print("Original string:")
print(str1)
print("Result:")
print(encode_str(str1))

str1 = "jjjjiiiiooooosssnssiiiiwwwweeeaaaabbbddddkkkklll" 
print("\nOriginal string:")
print(str1)
print("Result:")
print(encode_str(str1))

"""
18. Write a Python program to generate permutations of n items in which
successive permutations differ from each other by the swapping of any two items.
"""
DEBUG = False  # like the built-in __debug__

def spermutations(n):
    """Permutations by swapping. Yields: perm, sign"""
    sign, p = 1, [[i, 0 if i == 0 else -1] for i in range(n)]
    if DEBUG:
        print(' #', p)
    yield tuple(pp[0] for pp in p), sign

    while any(pp[1] for pp in p):
        i1, (n1, d1) = max(((i, pp) for i, pp in enumerate(p) if pp[1]), key=itemgetter(1))
        sign *= -1
        i2 = i1 + (1 if d1 == 1 else -1)
        p[i1], p[i2] = p[i2], p[i1]
        p[i2][1] = 0 if i2 in {0, n - 1} or p[i2 + (1 if d1 == 1 else -1)][0] > n1 else d1
        if DEBUG:
            print(' #', p)
        yield tuple(pp[0] for pp in p), sign
        for pp in p:
            if pp[0] > n1:
                pp[1] = 1 if p.index(pp) < i2 else -1

if __name__ == '__main__':
    for n in (3, 4):
        print(f'\nPermutations and sign of {n} items')
        sp = set(spermutations(n))
        for perm, sgn in sp:
            print(f'Permutation: {perm} Sign: {sgn}')
        assert sp == set((tuple(p), 1)
                        for p in permutations(range(n))), 'Methods do not agree'

"""
19. Write a Python program that iterates the integers from 1 to a given number and 
prints "Fizz" for multiples of three, prints "Buzz" for multiples of five, and prints
"FizzBuzz" for multiples of both three and five using the itertools module.
"""
from itertools import cycle
def fizz_buzz(n):
    fizzes = cycle([""] * 2 + ["Fizz"])
    buzzes = cycle([""] * 4 + ["Buzz"])
    fizzes_buzzes = (fizz + buzz for fizz, buzz in zip(fizzes, buzzes))
    result = (word or n for word, n in zip(fizzes_buzzes, count(1)))
    for i in islice(result, 100):
        print(i)
n = 50
fizz_buzz(n)

"""
20. Write a Python program to find the factorial of a number using the itertools module.
""" 
from itertools import accumulate
from itertools import chain
import operator as op
def factorials_nums(n):
    result = list(accumulate(chain([1], range(1, 1 + n)), op.mul))
    return result;
print("Factorials of 5 :", factorials_nums(5))
print("Factorials of 9 :", factorials_nums(9))


"""
21. Write a Python program to find the years between 2000 
and 2150 when the 25th of December is a Sunday.
"""
# Function to find years where December 25th is a Sunday
import datetime
def find_christmas_sundays(start_year, end_year):
    christmas_sundays = []
    for year in range(start_year, end_year + 1):
        if datetime.date(year, 12, 25).weekday() == 6:  # 6 corresponds to Sunday
            christmas_sundays.append(year)
    return christmas_sundays

# Define the range of years
start_year, end_year = 2000, 2150
sundays_on_christmas = find_christmas_sundays(start_year, end_year)
print("Years when December 25th is a Sunday between 2000 and 2150:")
for year in sundays_on_christmas:
    print(year)

# OR
from datetime import date
from itertools import islice
# xmasIsSunday :: Int -> Bool
def xmasIsSunday(y):
    '''True if Dec 25 in the given year is a Sunday.'''
    return 6 == date(y, 12, 25).weekday()

# main :: IO ()
def main():
    '''Years between 2000 and 2150 with 25 December on a Sunday'''
    xs = list(filter(xmasIsSunday, range(2000, 2151)))
    total = len(xs)
    print(fTable(main.__doc__ + ':\n\n' + '(Total ' + str(total) + ')\n')(lambda i: str(1 + i)
        )(str)(index(xs))(range(total)))

# GENERIC -------------------------------------------------
# index (!!) :: [a] -> Int -> a
def index(xs):
    '''Item at given (zero-based) index.'''
    return lambda n: None if 0 > n else (
        xs[n] if hasattr(xs, "__getitem__") else next(islice(xs, n, None)))

# unlines :: [String] -> String
def unlines(xs):
    """
    Concatenates a list of strings with the newline character in between.
    Parameters:
        xs (list): A list of strings.
    Returns:
        str: A single string formed by the intercalation of the list of strings with the newline character.
    """

    # Join the strings in the list with the newline character in between
    # to form a single string
    return '\n'.join(xs)

def unlines(xs):
    '''A single string formed by the intercalation of a list of strings with the newline character.'''
    return '\n'.join(xs)

# FORMATTING ---------------------------------------------
# fTable :: String -> (a -> String) -> (b -> String) -> (a -> b) -> [a] -> String
def fTable(s):
    '''Heading -> x display function -> fx display function -> f -> xs -> tabular string.'''
    def go(xShow, fxShow, f, xs):
        ys = [xShow(x) for x in xs]
        w = max(map(len, ys))
        return s + '\n' + '\n'.join(map(lambda x, y: y.rjust(w, ' ') + ' -> ' + fxShow(f(x)), xs, ys))
    return lambda xShow: lambda fxShow: lambda f: lambda xs: go(xShow, fxShow, f, xs)
# MAIN --
if __name__ == '__main__':
    main()

"""
22. Write a Python program to create a 24-hour time format (HH:MM) using the 4 given digits.
Display the latest time and do not use any digit more than once.
"""
import itertools 
import datetime
def func(lst):
    return datetime.datetime(*lst)
print(func([1,2,3,4]))

"""
23. Write a Python program to find the shortest distance from a specified
character a given string. Return the shortest distances through a list
and use rtoan itertools component to solve the problem.
"""
import itertools
def shortest_distance(s, c):
    return min(itertools.zip_longest(s, s[1:], fillvalue=c), key=lambda x: x.count(c))
print(shortest_distance("hello", 'l'))

"""
24. Write a Python program to find the maximum length of a substring
in a given string where all the characters of the substring are the same.
Use the itertools module to solve the problem.
"""
from itertools import chain
def char_shortest_distancer(str1, char1):
    result = [len(str1)] * len(str1)
    prev_char = -len(str1)
    for i in chain(range(len(str1)), reversed(range(len(str1)))):
        if str1[i] == char1:
            prev_char = i
        result[i] = min(result[i], abs(i-prev_char))
    return result

str1 = "w3resource"
chr1 = 'r'
print("Original string:", str1, ": Specified character:", chr1)
print(char_shortest_distancer(str1, chr1))


"""
25. Write a Python program to find the first two elements of a given list
whose sum is equal to a given value. Use the itertools module to solve the problem.
"""
from itertools import combinations
def sum_pairs_list(nums, n):
    for num2, num1 in list(combinations(nums[::-1], 2))[::-1]:
        if num2 + num1 == n:
            return [num1, num2]
nums = [1,2,3,4,5,6,7]     
n = 10
print("Original list:",nums,": Given value:",n)   
print("Sum of pair equal to ",n,"=",sum_pairs_list(nums,n))

"""
26. Write a Python program to find the nth Hamming number. Use the itertools module.
"""
import itertools
import heapq
def nth_hamming_number(n):
    def num_recur():
        last = 1
        yield last
        x, y, z = itertools.tee(num_recur(), 3)
        for n in heapq.merge((2 * i for i in x), (3 * i for i in y), (5 * i for i in z)):
            if n != last:
                yield n
                last = n
    result = itertools.islice(num_recur(), n)
    return list(result)[-1]
print(nth_hamming_number(8))   # Should print 9


"""
27. Create a Python program that chooses a specified number of colors
from three different colors and generates unique combinations.    
"""
import itertools
def func(lst, num):
    return [" and ".join(items) for items in itertools.combinations(lst, num)]

colors = ["Red", "Green", "Blue"]
print("Original List: ", colors)
n = 1
print("\nn = 1")
print(list(func(colors, n)))
n = 2
print("\nn = 2")
print(list(func(colors, n)))
n = 3
print("\nn = 3")
print(list(func(colors, n)))

"""
28. Write a Python program to find the maximum,
minimum aggregation pair in a given list of integers.    
"""
from itertools import combinations
def max_aggregate(l_data):
    max_pair = max(combinations(l_data, 2), key=lambda pair: pair[0] + pair[1])
    min_pair = min(combinations(l_data, 2), key=lambda pair: pair[0] + pair[1])
    return max_pair, min_pair

nums = [1, 3, 4, 5, 4, 7, 9, 11, 10, 9]
print("Original list:")
print(nums)
result = max_aggregate(nums)
print("\nMaximum aggregation pair of the said list of tuple pair:")
print(result[0])
print("\nMinimum aggregation pair of the said list of tuple pair:")
print(result[1])

"""
29. Write a Python program to interleave multiple lists of the same length.
Use the itertools module.
"""
import itertools
def interleave(*lists):
    return list(itertools.chain(*zip(*lists)))
print(interleave([1, 2, 3], [4, 5, 6], [7, 8, 9]))

"""
30. Write a Python program to create non-repeated combinations
of the Cartesian product of a given list of four numbers.
"""
import itertools as it
mums1 = [1, 2, 3, 4]
mums2 = [5, 6, 7, 8]
mums3 = [9, 10, 11, 12]
mums4 = [13, 14, 15, 16]
print("Original lists:")
print(mums1)
print(mums2)
print(mums3)
print(mums4)
print("\nSum of the specified range:")
for i in it.product([tuple(mums1)], it.permutations(mums2), it.permutations(mums3), it.permutations(mums4)):
    print(i)

"""
31. Write a Python program to count the frequency of consecutive duplicate
elements in a given list of numbers. Use the itertools module.
"""
import itertools
def func(lst):
    return [len(list(group)) for key, group in itertools.groupby(lst)]
nums = [1, 2, 2, 3, 4, 4, 5, 5, 5]
my_lst = func(nums)
print("Original list:", my_lst)

"""
32. Write a Python program to count the frequency of the elements of a given unordered list..
"""
import itertools
def func(lst):
    return [len(list(group)) for key, group in itertools.groupby(sorted(lst))]
nums = [1, 2, 2, 3, 4, 4, 5, 5, 5]
my_lst = func(nums)
print("Original list:", my_lst)

"""
33. Write a Python program to find pairs of maximum and
minimum products from a given list. Use the itertools module.
"""
import itertools as it
def list_max_min_pair(nums):
    result_max = max(it.combinations(nums, 2), key=lambda sub: sub[0] * sub[1])
    result_min = min(it.combinations(nums, 2), key=lambda sub: sub[0] * sub[1])
    return result_max, result_min

nums = [2, 5, 8, 7, 4, 3, 1, 9, 10, 1]
print("The original list: ")
print(nums)
print("\nPairs of maximum and minimum product from the said list:")
print(list_max_min_pair(nums))

"""
34. Write a Python program to compute the sum of digits
of each number in a given list of positive integers.
"""
def sum_of_digits(lst):
    return sum(map(int, (''.join(str(x) for x in lst))))
lst = [10, 2, 53]
print(sum_of_digits(lst))

# or
from itertools import chain
def sum_of_digits(nums):
    return sum(int(y) for y in (chain(*[str(x) for x in nums])))
nums = [10,2,56]
print(sum_of_digits(nums))

"""
35. Write a Python program to get all possible combinations of
the elements of a given list using the itertools module..
"""
import itertools
def combinations_list(list1):
    temp = []
    for i in range(0, len(list1)+1):
        temp.append(list(itertools.combinations(list1, i)))
    return temp

colors = ['orange', 'red', 'green', 'blue']
print("Original list:")
print(colors)
print("\nAll possible combinations of the said list’s elements:")
print(combinations_list(colors))

"""
36. Write a Python program to add two given lists of different lengths,
starting from the right, using the itertools module. 
"""
import itertools
def add_lists(list1, list2):
    result = [a + b for a, b in itertools.zip_longest(reversed(list1), reversed(list2), fillvalue=0)][::-1]
    return result

list1 = [2, 4, 6, 9, 23, 12]
list2 = [21, 42, 6, 9, 23, 20]
print(add_lists(list1, list2))

"""
37. Write a Python program to add two given lists of different lengths,
starting from the left, using the itertools module. 
"""
import itertools
def func(lst1, lst2):
    result = [a+b for a,b in itertools.zip_longest(list1, list2, fillvalue=0)]
    return result

list1 = [2, 4, 6, 9, 23, 12]
list2 = [21, 42, 6, 9, 23, 20]
print(func(list1, list2))

"""
38. Write a Python program to interleave a number of lists of different lengths
using the itertools module.. 
"""
import itertools
def interleave(*lists):
    return list(itertools.chain(*zip(*lists)))

list1 = [2, 4, 6, 9, 23, 12]
list2 = [21, 42, 6, 9, 23, 20]
print(interleave(list1, list2, list1, list2))

"""
39. Write a Python program to get the index of the first element that is greater than
a specified element using the itertools module... 
"""
from itertools import takewhile
def first_index(l1, n):
    return len(list(takewhile(lambda x: x[1] <= n, enumerate(l1))))

nums = [12,45,23,67,78,90,100,76,38,62,73,29,83]
print("Original list:")
print(nums)
n = 73
print("\nIndex of the first element which is greater than",n,"in the said list:")
print(first_index(nums,n))
n = 21

"""
40. Write a Python program to split a given list into specified
sized chunks using the itertools module.... 
"""
from itertools import islice
def split_list(lst, n):
    lst = iter(lst)
    result = iter(lambda: tuple(islice(lst, n)), ())
    return list(result)

nums = [12,45,23,67,78,90,45,32,100,76,38,62,73,29,83]
print(split_list(nums, 3))

"""
41. Write a Python program to find all lower and upper mixed case combinations of a given string.
"""
import itertools
def combination(str1):
    result = map(''.join, itertools.product(*((c.lower(), c.upper()) for c in str1)))
    return list(result)
st ="abc"
print(st)
print(combination(st))

from itertools import product
def combination(str1):
    return [''.join(p) for p in product(*((c.lower(), c.upper()) for c in str1))]

st = "abc"
print(st)
print(combination(st))


"""
42. Write a Python program to create groups of similar items from a given list.
"""
from itertools import groupby
def group_similar_items(seq):
    result =  [list(el) for _, el in groupby(seq, lambda x: x.split('_')[0])]
    return result 

colors = ['red_1', 'red_2', 'green_1', 'green_2', 'green_3', 'orange_1', 'orange_2']
print("Original list:")
print(colors)
print("\nGroup similar items of the said list:")
print(group_similar_items(colors))

"""
43. Write a Python program to find the maximum difference between pairs in a given list.
"""
from itertools import combinations
from heapq import nlargest
def test(lst):
    result = nlargest(1, combinations(lst, 2), key=lambda sub: abs(sub[0] - sub[1]))
    return result

marks = [32,14,90,10,22,42,31]
print("\nOriginal list:")
print(marks)
print("\nFind maximum difference pair of the said list:")
print(test(marks))

# 2nd 
from itertools import combinations
def max_difference(lst):
    return max(abs(a - b) for a, b in combinations(lst, 2))

marks = [32, 14, 90, 10, 22, 42, 31]
print(max_difference(marks))

"""
44. Write a Python program to extract a non-zero block from a given integer list.
"""
import itertools as it
def test(lst):
    result = [list(x[1]) for x in it.groupby(lst, lambda x: x == 0) if not x[0]]
    return result
nums = [3,4,6,2,0,0,0,0,0,0,6,7,6,9,10,0,0,0,0,0,7,4,4,0,0,0,0,0,0,5,3,2,9,7,1]
print("\nOriginal list:")
print(nums)
print("\nExtract non_zero block from a given integers of list:")
print(test(nums))
















