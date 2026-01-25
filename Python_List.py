################################################################
########################################################## (List)
################################################################
"""1.  Write a Python program to sum all the items in a list."""
from functools import reduce
lst = [1, 2, 3, 4, 5] # type: ignore
print(sum(lst))

# OR
def sum_list(lst):
    total = 0
    for item in lst:
        total += item
    return total
print(sum_list(lst))

# OR
sm = 0
for k in lst:
    sm += k
print(sm)

"""2.  Write a Python program to multiply all the items in a list."""
lst = [1, 2, 3, 4, 5]
print(reduce((lambda x, y: x * y), lst))

# OR
def multiply_list(lst):
    total = 1
    for item in lst:
        total *= item
    return total
print(multiply_list(lst))

sm = 1
for k in lst:
    sm *= k
print(sm)

"""3.  Write a Python program to get the largest number from a list."""
lst = [1, 2, 3, 4, 5]
print(max(lst))

def max_list(lst):
    return max(lst)
print(max_list(lst))

Max_num = lst[0]
for k in lst:
    if k > Max_num:
        Max_num = k
print(Max_num)

"""4.Write a Python program to get the smallest number from a list."""
lst = [1, 2, 3, 4, 5]
print(min(lst))

def min_list(lst):
    return min(lst)
print(max_list(lst))

Min_num = lst[0]
for k in lst:
    if k < Min_num:
        Min_num = k
print(Min_num)

"""5.Write a Python program to count the number of strings from a given list of strings.
The string length is 2 or more and the first and last characters are the same.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2 """
def count_strings(lst):
    count = 0
    for item in lst:
        if len(item) >= 2 and item[0] == item[-1]:
            count += 1
    return count
print(count_strings(['abc', 'xyz', 'aba', '1221']))

"""
6.Write a Python program to get a list, sorted in increasing order by
the last element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
"""
def sort_by_last(tuples):
    return sorted(tuples, key=lambda x: x[-1])
print(sort_by_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

# OR
List = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
new_list = []
for k,v in list.enumerate(List):
    new_list.append((v[1], k))
print(new_list)

""" 7.  Write a Python program to remove duplicates from a list."""
lst = [1, 2, 3, 4, 5, 1, 2, 3]
lst_new = [k for k in lst if lst.count(k) == 1]
print(lst_new)
# or 
print(list(set(lst)))


""" 8.Write a Python program to check if a list is empty or not ."""
lst = [1,2,""]
def is_empty(lst):
    if len(lst) == 0:
        return True
    else:
        return False
print(is_empty(lst))

# OR
def is_empty(lst):
    return all(lst)
print(is_empty(lst))
"""9.Write a Python program to clone or copy a list."""
lst =  [1, 2, 3, 4, 5]
print(lst.copy())

""" 10. Write a Python program to find the list of words that are longer than n from a given list of words."""
def longer_than_n(lst, n):
    return [word for word in lst if len(word) > n]
print(longer_than_n(['abc', 'xyz', 'aba', '1221'], 3))

lambda_func = lambda lst, n: [word for word in lst if len(word) > n]
print(lambda_func(['abc', 'xyz', 'aba', '1221'], 3))

""" 11. Write a Python function that takes two lists & returns True if they have at least one common member."""
def common_memb(l1,l2):
    return any(i in l2 for i in l1)
print(common_memb([1,2,3,4,5],[4,5,6,7,8]))
# OR
l1 = [1,2,3,4,5]
l2 = [6,7,8]
def common_memb(l1,l2):
    for i in l1:
        if i in l2:
            return True
    return False
print(common_memb(l1,l2))

"""
12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
    Sample List: ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    Expected Output: ['Green', 'White', 'Black']"""
def remove_elements(lst):
    return [item for index, item in enumerate(lst) if index not in [0, 4, 5]]
print(remove_elements(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))

# OR
def remove_elements(lst):
    for i in [0, 4, 5]:
        lst.pop(i)
    return lst
print(remove_elements(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))

# OR
def remove_elements(lst):
    ind = [0, 4, 5]
    asj = []
    for k in ind:
        asj.append(lst[k])
    for k in asj:
        lst.remove(k)
    return lst
print(remove_elements(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))

"""
13. Write a Python program to generate a 3\*4\*6 3D array whose each element is *.
"""
import numpy as np
array = np.full((3, 4, 6), '*')
print(array)
# OR
def arr(element):
    for i in range(3):        # 3 "pages"
        print(f"Page {i + 1}:")
        for j in range(4):    # 4 "rows"
            for k in range(6):  # 6 "columns"
                print(element, end=' ')
            print()
        print()  # extra newline between "pages"
arr('*')

"""14. Write a Python program to print the numbers of a specified list after removing even numbers from it."""
def remove_even_numbers(lst):
    return [num for num in lst if num % 2 != 0]
print(remove_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""15. Write a Python program to shuffle and print a specified list."""
import random
def shuffle_list(lst):
    random.shuffle(lst)
    return lst
print(shuffle_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""16. Write a Python program to generate and print a list of the first and last 5
elements where the values are square numbers between 1 and 30 (both included)."""
def square_numbers():
    lst = [num ** 2 for num in range(1, 31)]
    return lst[:5] + lst[-5:]
print(square_numbers())

"""17. Write a Python program to check if each number is prime in a given list of numbers.
Return True if all numbers are prime otherwise False.
    Sample Data:
    ([0, 3, 4, 7, 9]) -> False
    ([3, 5, 7, 13]) -> True
    ([1, 5, 3]) -> False
"""
def is_prime(lst):
   return all(all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)) for num in lst)
   print(is_prime([0, 3, 4, 7, 9]))

"""18. Write a Python program to generate all permutations of a list in Python."""
def permutations(lst):
    import itertools
    return list(itertools.permutations(lst))
print(permutations([1, 2, 3]))

def custom_permutation(lst):
   result = []
   for i in range(len(lst)):
       for j in range(len(lst)):
           if i != j:
               for k in range(len(lst)):
                   if i != k and j != k:
                       result.append([lst[i], lst[j], lst[k]])
   return result
   print(custom_permutation([1, 2, 3]))


"""19. Write a Python program to calculate the difference between the two lists."""
def diffrence(lst1, lst2):
   return list(set(lst1) - set(lst2))
print(diffrence([1, 2, 3], [2, 3, 4]))

"""20. Write a Python program to access the index of a list."""
def access_index(lst, index):
   return lst[index]
print(access_index([1, 2, 3], 1))

"""21. Write a Python program to convert a list of characters into a string."""
def list_to_string(lst):
   return ''.join(lst)
print(list_to_string(['H', 'e', 'l', 'l', 'o']))

"""22. Write a Python program to find the index of an item in a specified list."""
def find_index(lst, item):
    return lst.index(item)
print(find_index([1, 2, 3], 2))

"""23. Write a Python program to flatten a shallow list."""
def flatten_list(lst):
    return [item for sublist in lst for item in sublist]
print(flatten_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

"""24. Write a Python program to append a list to the second list."""
def append_list(lst1, lst2):
    lst1.extend(lst2)
    return lst1
print(append_list([1, 2, 3], [4, 5, 6]))

"""25. Write a Python program to select an item randomly from a list."""
import random
def select_random(lst):
    return random.choice(lst)
print(select_random([1, 2, 3, 4, 5]))

"""26. Write a Python program to check whether two lists are circularly identical."""
def circularly_identical(lst1, lst2):
    return lst1 == lst2 or lst1 == lst2[::-1]
print(circularly_identical([1, 2, 3], [3, 2, 1]))

"""27. Write a Python program to find the second smallest number in a list."""
def smallest_number(lst):
    return sorted(lst)[1]
print(smallest_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""28. Write a Python program to find the second largest number in a list."""
def second_largest(lst):
    return sorted(lst)[-2]
print(second_largest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""29. Write a Python program to get unique values from a list."""
def unique_values(lst):
    return list(set(lst))
print(unique_values([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""30. Write a Python program to get the frequency of elements in a list."""
def frequency(lst):
    return {item: lst.count(item) for item in lst}
print(frequency([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""31. Write a Python program to count the number of elements in a list within a specified range."""
def count_range(lst, start, end):
    return sum(1 for item in lst if start <= item <= end)
print(count_range([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2, 8))

"""32. Write a Python program to check whether a list contains a sublist."""
def check_sublist(lst1, lst2):
    return any(sublist == lst2 for sublist in lst1)
print(check_sublist([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [4, 5, 6]))

# OR
def check_sublist(lst1, lst2):
    for k in lst1:
        if k == lst2:
            return True
    return False
print(check_sublist([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [4, 5, 6]))

"""33. Write a Python program to generate all sublists of a list."""
def gen_sublists(lst):
    return [lst[i:j] for i in range(len(lst)) for j in range(i+1, len(lst)+1)]
print(gen_sublists([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# OR
def gen_sublists(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            print(lst[i:j])
print(gen_sublists([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""34. Write a Python program that uses the Sieve of Eratosthenes method to compute prime numbers up to a specified number.
    Note: In mathematics, the sieve of Eratosthenes, (Ancient Greek: κόσκινον Ἐρατοσθένους, kóskinon Eratosthénous) one of a number of prime number sieves, is a simple, ancient algorithm for finding all prime numbers up to any given limit.
"""
def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(2, n + 1) if primes[i]]
print(sieve_of_eratosthenes(10))

"""35. Write a Python program to create a list by concatenating a given list with a range from 1 to n.
    Sample list : ['p', 'q']
    n =5
    Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
"""
def concat(lst, n):
    my_lst = []
    [my_lst.append(f"{i}{j}") for i in lst for j in range(1, n+1)]
    return my_lst
print(concat(['p', 'q'], 5))

import concurrent.futures
import urllib.request

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://nonexistent-subdomain.python.org/']

# Retrieve a single page and report the URL and contents
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('%r page is %d bytes' % (url, len(data)))

"""36. Write a Python program to get a variable with an identification number or string."""
def get_var(var_id):
    return globals()[var_id]
print(get_var('x'))

"""37. Write a Python program to find common items in two lists."""
def common_items(list1, list2):
    return [value for value in list1 if value in list2]
print(common_items([1, 2, 3, 7], [4, 3, 2, 1]))

"""38. Write a Python program to change the position of every n-th value to the (n+1)th in a list.
    Sample list: [0,1,2,3,4,5]
    Expected Output: [1, 0, 3, 2, 5, 4]"""
def change_item(lst):
    return [lst[i] for i in range(1, len(lst), 2)] + [lst[i] for i in range(0, len(lst), 2)]
print(change_item([0, 1, 2, 3, 4, 5]))

"""39. Write a Python program to convert a list of multiple integers into a single integer.
    Sample list: [11, 33, 50]
    Expected Output: 113350 """
import asyncio
async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    print(f'[{cmd!r} exited with {proc.returncode}]')
    if stdout:
        print(f'[stdout]\n{stdout.decode()}')
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')

asyncio.run(run('ls /zzz'))
    
    
"""40. Write a Python program to split a list based on the first character of a word."""
# Import the 'groupby' function from the 'itertools' module and the 'itemgetter' function from the 'operator' module
from itertools import groupby
from operator import itemgetter

# Define a list 'word_list' containing words
word_list = ['be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'take', 'see', 'come', 'think',
            'look', 'want', 'give', 'use', 'find', 'tell', 'ask', 'work', 'seem', 'feel', 'leave', 'call']
for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
    print(letter)
    for word in words:
        print(word)

"""41. Write a Python program to create multiple lists."""
def multiple_list(lst, n):
    return [lst[i::n] for i in range(n)]
print(multiple_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))

"""42. Write a Python program to find missing and additional values in two lists.
    Sample data : Missing values in second list: b,a,c
    Additional values in second list: g,h """
def find_missing_and_additional_values(list1, list2):
    return [item for item in list1 if item not in list2], [item for item in list2 if item not in list1]
print(find_missing_and_additional_values([1, 2, 3, 4, 5, 6, 7], [1, 2, 4, 5, 6, 7, 8, 9, 10]))

"""43. Write a Python program to split a list into different variables."""
def split_list(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]
print(split_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))

"""44. Write a Python program to generate groups of five consecutive numbers in a list."""
def generate_groups(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]
print(generate_groups([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))

"""45. Write a Python program to convert a pair of values into a sorted unique array."""
def convert_pair_to_sorted_array(pair):
    return sorted(set(pair))
print(convert_pair_to_sorted_array((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))

# OR
l = [[5*i + j for j in range(1, 6)] for i in range(5)]
print(l)

"""46. Write a Python program to select the odd items from a list."""
def odd():
    return [x for x in range(20) if x % 2 == 1]
print(odd())

"""47. Write a Python program to insert an element before each element of a list."""
def insert_before(lst, element):
    return [element] + lst
print(insert_before([1, 2, 3, 4, 5], 0))

"""48. Write a Python program to print nested lists (each list on a new line) using the print() function."""# Define a list 'colors' containing sublists, each with a single color name
colors = [['Red'], ['Green'], ['Black']]
print('\n'.join([str(lst) for lst in colors])) 

"""49. Write a Python program to convert a list to a list of dictionaries.
    Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
    Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]
"""
def dictn(lst1, lst2):
    return {i:j for i, j in zip(lst1, lst2)}
print(dictn(["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]))
"""50. Write a Python program to sort a list of nested dictionaries."""
def sort_list(lst):
    return sorted(lst, key=lambda x: x['name'])
print(sort_list([{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 20}]))

"""51. Write a Python program to split a list every Nth element.
    Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
    Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
"""
def split(lst, n):
    return [lst[i::n] for i in range(n)]
print(split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 3))

"""52. Write a Python program to compute the difference between two lists.
    Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
    Expected Output:
    Color1-Color2: ['white', 'orange', 'red']
    Color2-Color1: ['black', 'yellow']
"""
def compute_diff(lst1, lst2):
    return list(set(lst1) - set(lst2)), list(set(lst2) - set(lst1))
lst1 = ["red", "orange", "green", "blue", "white"]
lst2 = ["black", "yellow", "green", "blue"]
print(compute_diff(lst1, lst2))

"""53. Write a Python program to create a list with infinite elements."""
lst = []
while True:
    item = input("Enter an item (or 'done' to finish): ")
    if item == "done":
        break
    lst.append(item)
print(lst)

"""54. Write a Python program to concatenate elements of a list."""
def concatenate(lst):
    return ''.join(lst)
print(concatenate(['a', 'b', 'c', 'd', 'e']))

"""55. Write a Python program to remove key-value pairs from a list of dictionaries."""
def remove_key_value(lst, key, value):
    return [item for item in lst if item.get(key) != value]
print(remove_key_value([{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 20}], 'name', 'Alice'))

"""56. Write a Python program to convert a string to a list."""
def string_to_list(string):
    return list(string)
print(string_to_list('hello'))

"""57. Write a Python program to check if all items in a given list of strings are equal to a given string."""
def check_equal(lst, string):
    return all(item == string for item in lst)
print(check_equal(['hello', 'hello', 'hello'], 'hello'))

"""58. Write a Python program to replace the last element in a list with another list.
    Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
    Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8] """
def concatenate(lst1, lst2):
    return lst1[:-1] + lst2
print(concatenate([1, 3, 5, 7, 9, 10], [2, 4, 6, 8]))

"""59. Write a Python program to check whether the n-th element exists in a given list."""
def check(lst, n):
    return n < len(lst)
print(check([1, 2, 3, 4, 5], 3))
# OR
def check(lst, n):
    return n in range(len(lst))
print(check([1, 2, 3, 4, 5], 3))
# OR
def check(lst, n):
    try:
        return lst[n]
    except IndexError:
        return False
print(check([1, 2, 3, 4, 5], 3))

"""60. Write a Python program to find a tuple, the smallest second index value from a list of tuples."""
def smallest_second_index(lst):
    return min(lst, key=lambda x: x[1])
print(smallest_second_index([(1, 2), (3, 4), (5, 6)]))

"""61. Write a Python program to create a list of empty dictionaries."""
def empty_dict_list(n):
    return [{} for _ in range(n)]
print(empty_dict_list(3))
# OR
def empty_dict_list(n): 
    return [dict() for _ in range(n)]
print(empty_dict_list(3))

"""62. Write a Python program to print a list of space-separated elements."""
def space_separated(lst):
    return ' '.join(lst)
print(space_separated(['a', 'b', 'c', 'd', 'e']))
# OR
def space_separated(lst):
    return ' '.join(map(str, lst))
print(space_separated(['a', 'b', 'c', 'd', 'e']))
# OR
def space_separated(lst):
    return ' '.join(str(item) for item in lst)
print(space_separated(['a', 'b', 'c', 'd', 'e']))

"""63. Write a Python program to insert a given string at the beginning of all items in a list.
    Sample list : [1,2,3,4], string : emp
    Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
"""
def insert_string(lst, string):
    return [string + str(item) for item in lst]
print(insert_string([1, 2, 3, 4], 'emp'))

"""64. Write a Python program to iterate over two lists simultaneously."""
def iterate_two_lists(lst1, lst2):
    for item1, item2 in zip(lst1, lst2):
        print(item1, item2)
iterate_two_lists([1, 2, 3], ['a', 'b', 'c'])

"""65. Write a Python program to move all zero digits to the end of a given list of numbers.
    Expected output:
    Original list:
    [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
    Move all zero digits to end of the said list of numbers:
    [3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
"""
def adjust_zero(lst):
    zero_count = lst.count(0)
    non_zero = [x for x in lst if x != 0]
    return non_zero + [0] * zero_count
print(adjust_zero([3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]))
# OR
def adjust_zero(lst):
    zero =  []
    non_zero = []
    for k,v in enumerate(lst):
        if v != 0:
            non_zero.append(v)
        else:
            zero.append(v)
    return non_zero + zero
print(adjust_zero([3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]))

"""66. Write a Python program to find the list in a list of lists whose sum of elements is the highest.
    Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
    Expected Output: [10, 11, 12]
"""
import asyncio
async def main():
    print('Hello ...')
    await asyncio.sleep(10)
    print('... World!')
asyncio.run(main())

"""67. Write a Python program to find all the values in a list that are greater than a specified number."""
def greater_than(lst, num):
    return [x for x in lst if x > num]
print(greater_than([1, 2, 3, 4, 5], 3))

"""68. Write a Python program to extend a list without appending.
    Sample data: [10, 20, 30]
    [40, 50, 60]
    Expected output : [40, 50, 60, 10, 20, 30]
"""
def extend_list(lst1, lst2):
    return lst1 + lst2
print(extend_list([10, 20, 30], [40, 50, 60]))

"""69. Write a Python program to remove duplicates from a list of lists.
    Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    New List : [[10, 20], [30, 56, 25], [33], [40]]
"""
def remove_duplicates(lst):
    return list(set(lst))
print(remove_duplicates([[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]))

"""70. Write a Python program to find items starting with a specific character from a list.
    Expected Output:
    Original list:
    ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
    Items start with a from the said list:
    ['abcd', 'abc', 'acjd']
    Items start with d from the said list:
    ['dagfa']
    Items start with w from the said list:
    []
"""
def start_with(lst, char):
    return [x for x in lst if x.startswith(char)]
print(start_with(['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd'], 'a'))

"""
71. Write a Python program to check whether all dictionaries in a list are empty or not.
    Sample list : [{},{},{}]
    Return value : True
    Sample list : [{1,2},{},{}]
    Return value : False
"""
def all_empty(lst):
    return all(not d for d in lst)
print(all_empty([{},{},{}]))

"""72. Write a Python program to flatten a given nested list structure.
    Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
    Flatten list:
    [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
"""
def flat(lst):
    return [k for k in lst if isinstance(k, list) for k in k]
print(flat([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]))
# or
lambda_func = lambda lst: [k for k in lst if isinstance(k, list) for k in k]

"""73. Write a Python program to remove consecutive (following each other continuously) duplicates (elements) from a given list.
    Original list:
    [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
    After removing consecutive duplicates:
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
"""
def remove_consecutive_duplicates(lst):
    
    return list(dict.fromkeys(lst))
print(remove_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]))

"""74.Write a Python program to pack consecutive duplicates of a given list of elements into sublists.
    Original list:
    [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
    After packing consecutive duplicates of the said list elements into sublists:
    [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
"""
from itertools import groupby
def sublist(lst):
    return [list(g) for k, g in groupby(lst)]
print(sublist([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]))

# Original list
original_list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# Result list to store packed sublists
packed_list = []
# Temporary list to keep track of current group
temp = []
for item in original_list:
    if not temp or item == temp[-1]:
        temp.append(item)
    else:
        packed_list.append(temp)
        temp = [item]
# Don't forget to add the last group
if temp:
    packed_list.append(temp)
# Output
print("Original list:")
print(original_list)
print("After packing consecutive duplicates into sublists:")
print(packed_list)

"""75. Write a Python program to create a list reflecting the run-length encoding from a given list of integers or a given list of characters.
    Original list:
    [1, 1, 2, 3, 4, 4.3, 5, 1]
    List reflecting the run-length encoding from the said list:
    [[2, 1], [1, 2], [1, 3], [1, 4], [1, 4.3], [1, 5], [1, 1]]
    Original String:
    automatically
    List reflecting the run-length encoding from the said string:
    [[1, 'a'], [1, 'u'], [1, 't'], [1, 'o'], [1, 'm'], [1, 'a'], [1, 't'], [1, 'i'], [1, 'c'], [1, 'a'], [2, 'l'], [1, 'y']]
"""
from itertools import groupby
def rle(lst):
    return [[len(list(g)), k] for k, g in groupby(lst)]
print(rle([1, 1, 2, 3, 4, 4.3, 5, 1]))

# OR
from collections import Counter
def rle(lst):
    return [[count, item] for item, count in Counter(lst).items()]
print(rle([1, 1, 2, 3, 4, 4.3, 5, 1]))


"""77. Write a Python program to decode a run-length message.
    Original encoded list:
    [[2, 1], 2, 3, [2, 4], 5, 1]
    Decode a run-length encoded said list:
    [1, 1, 2, 3, 4, 4, 5, 1]
"""
def decode_run(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend([item[1]] * item[0])
        else:
            result.append(item)
    return result
print(decode_run([[2, 1], 2, 3, [2, 4], 5, 1]))

"""78. Write a Python program to split a given list into two parts where the length
of the first part of the list is given.
    Original list:
    [1, 1, 2, 3, 4, 4, 5, 1]
    Length of the first part of the list: 3
    Splited the said list into two parts:
    ([1, 1, 2], [3, 4, 4, 5, 1])
"""
def split_list(lst, n):
    return lst[:n], lst[n:]
print(split_list([1, 1, 2, 3, 4, 4, 5, 1], 3))
# OR
lst = [1, 1, 2, 3, 4, 4, 5, 1]
n = 3
print(lst[:n], lst[n:])

"""79. Write a Python program to remove the K'th element from a given list, and print the updated list.
    Original list:
    [1, 1, 2, 3, 4, 4, 5, 1]
    After removing an element at the kth position of the said list:
    [1, 1, 3, 4, 4, 5, 1]
"""
def remove_kth_element(lst, k):
    return lst[:k] + lst[k+1:]
print(remove_kth_element([1, 1, 2, 3, 4, 4, 5, 1], 2))
# OR
lst = [1, 1, 2, 3, 4, 4, 5, 1]
del lst[2]
print(lst)

"""80. Write a Python program to insert an element at a specified position into a given list.
    Original list:
    [1, 1, 2, 3, 4, 4, 5, 1]
    After inserting an element at kth position in the said list:
    [1, 1, 12, 2, 3, 4, 4, 5, 1]
"""
def insert_element(lst, element, position):
    lst.insert(position, element)
    return lst
print(insert_element([1, 1, 2, 3, 4, 4, 5, 1], 12, 2))
# OR
lst = [1, 1, 2, 3, 4, 4, 5, 1]
lst.insert(2, 12)
print(lst)

"""81. Write a Python program to extract a given number of randomly selected elements from a given list.
    Original list:
    [1, 1, 2, 3, 4, 4, 5, 1]
    Selected 3 random numbers of the above list:
    [4, 4, 1]
"""
import random
def selection(lst, n):
    random.shuffle(lst)
    return lst[:n]
print(selection([1, 1, 2, 3, 4, 4, 5, 1], 3))

# OR
import random
def selection(lst, n):
    return random.sample(lst, n)
print(selection([1, 1, 2, 3, 4, 4, 5, 1], 3))

"""
82. Write a Python program to generate combinations of n distinct objects taken from the elements
of a given list. Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9] 
Combinations of 2 distinct objects:
    [1, 2] [1, 3] [1, 4] [1, 5] .... [7, 8] [7, 9] [8, 9] """
from itertools import combinations
def generate_combinations(lst, n):
    return list(combinations(lst, n))
print(generate_combinations([1, 2, 3, 4, 5, 6, 7, 8, 9], 2))

"""83. Write a Python program to round every number in a given list of numbers and 
    print the total sum multiplied by the length of the list.
    Original list: [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
    Result: 243
"""
def run(list):
    return round(sum(list) * len(list))
print(run([22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]))

"""84. Write a Python program to round the numbers in a given list, print the minimum and maximum
numbers and multiply the numbers by 5. Print the unique numbers in ascending order separated by space.
    Original list: [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
    Minimum value: 4
    Maximum value: 22
    Result: 20 25 45 55 60 70 80 90 110
"""
def run(lst):
    print(f'Minimum value {min(lst)}')
    print(f'Maximum value {max(lst)}')
    new_lst = [k*5 for k in list(map(round, lst))]
    print(f'Result:{sorted(new_lst)}')
    return
lst = [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
print(run(lst))

"""
85. Write a Python program to create a multidimensional list (lists of lists) with zeros.
    Multidimensional list: [[0, 0], [0, 0], [0, 0]]
"""
def multi_dim(lst):
    return [[0 for _ in range(lst)] for _ in range(lst)]
print(multi_dim(3))
# OR
def multi_dim(lst):
    return [[0] * lst for _ in range(lst)]
print(multi_dim(3)) 

"""86. Write a Python program to create a 3X3 grid with numbers.
    3X3 grid with numbers:
    [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
"""
def grid(lst):
    return [[i for i in range(1, lst+1)] for _ in range(lst)]
print(grid(3))
# OR
def grid(lst):
    return [[1, 2, 3] for _ in range(lst)]
print(grid(3))

"""87. Write a Python program to read a matrix from the console and print the sum for each column.
    As input from the user, accept matrix rows, columns, and elements separated by a space (each row).
    Input rows: 2
    Input columns: 2
    Input number of elements in a row (1, 2, 3):
    1 2
    3 4
    sum for each column:
    4 6
"""
def matrix_sum(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f'Input number of elements in a row ({i+1}): ').split()))
        matrix.append(row)
    col_sum = [sum(col) for col in zip(*matrix)]
    print('Sum for each column:')
    print(' '.join(map(str, col_sum)))
    return
rows = int(input('Input rows: '))
cols = int(input('Input columns: '))
matrix_sum(rows, cols)

"""88. Write a Python program to read a square matrix from the console and print 
the sum of the matrix's primary diagonal. Accept the size of the square matrix and elements 
for each column separated with a space (for every row) as input from the user.
    Input the size of the matrix: 3
    2 3 4
    4 5 6
    3 4 7
    Sum of matrix primary diagonal:
    14
"""
def matrix():
    size = int(input("Enter the size of the matrix: "))
    raw = input(f"Enter {size*size} digits (e.g., 123456789): ").strip()
    if len(raw) != size * size or not raw.isdigit():
        raise ValueError(f"Expected {size*size} digits, but got '{raw}'")
    mat = list(map(int, raw))
    my_mat = [mat[i:i+size] for i in range(0, len(mat), size)]
    return my_mat
print(matrix())

# OR
def matrix():
    size = int(input("Enter the size of the matrix: "))
    mat = []
    for i in range(size):
        row = list(map(int, input(f"Enter {size} digits for row {i+1}: ").split()))
        mat.append(row)
    return mat
print(matrix())

"""89. Write a Python program to Zip two given lists of lists.
    Original lists:
    [[1, 3], [5, 7], [9, 11]]
    [[2, 4], [6, 8], [10, 12, 14]]
    Zipped list:
    [[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12, 14]]
"""
def zip_lists(lst1, lst2):
    return [x+y for x, y in zip(lst1,lst2)]
print(zip_lists([[1, 3], [5, 7], [9, 11]], [[2, 4], [6, 8], [10, 12, 14]]))

"""90. Write a Python program to count the number of lists in a given list of lists.
    Original list:
    [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
    Number of lists in said list of lists:
    4
    Original list:
    [[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
    Number of lists in said list of lists:
    3
"""
def count_lists(lst):
    return len(lst)
print(count_lists([[1, 3], [5, 7], [9, 11], [13, 15, 17]]))

"""91.Write a Python program to find a list with maximum and minimum lengths.
    Original list:
    [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
    List with maximum length of lists:
    (3, [13, 15, 17])
    List with minimum length of lists:
    (1, [0])
"""
def max_min_length(lst):
    max_list = max(lst, key=len)
    min_list = min(lst, key=len)
    return (len(max_list), max_list), (len(min_list), min_list)
print(max_min_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]))

"""92. Write a Python program to check if a nested list is a subset of another nested list.
    Original list:
    [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
    [[1, 3], [13, 15, 17]]
    If the one of the said list is a subset of another.:
    True
"""
def is_subset(lst1, lst2):
    return all(item in lst1 for item in lst2)
print(is_subset([[1, 3], [5, 7], [9, 11], [13, 15, 17]], [[1, 3], [13, 15, 17]]))


"""93. Write a Python program to count the number of sublists that contain a particular element.
    Original list:
    [[1, 3], [5, 7], [1, 11], [1, 15, 7]]
    Count 1 in the said list:
    3
"""
def count_sublists(lst, element):
    return sum(1 for sublist in lst if element in sublist)
print(count_sublists([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 1))
# OR
def count_sublists(lst, element):
    count = 0
    for sublist in lst:
        if element in sublist:
            count += 1
    return count
print(count_sublists([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 1))
# OR
def count_sublists(lst, element):
    return len([sublist for sublist in lst if element in sublist])
print(count_sublists([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 1))
# OR
def count_sublists(lst, element):
    return len(list(filter(lambda x: element in x, lst)))
print(count_sublists([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 1))

"""94. Write a Python program to count the number of unique sublists within a given list.
    Original list:
    [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
    Number of unique lists of the said list:
    {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
    Original list:
    [['green', 'orange'], ['black'], ['green', 'orange'], ['white']]
    Number of unique lists of the said list:
    {('green', 'orange'): 2, ('black',): 1, ('white',): 1}
"""
def count_unique_sublists(lst):
    from collections import Counter
    return dict(Counter(tuple(sorted(sublist)) for sublist in lst))
print(count_unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]))
# OR
def count_unique_sublists(lst):
    unique_sublists = {}
    for sublist in lst:
        key = tuple(sorted(sublist))
        if key in unique_sublists:
            unique_sublists[key] += 1
        else:
            unique_sublists[key] = 1
    return unique_sublists
print(count_unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]))

# OR
def count_unique_sublists(lst):
    unique_sublists = {}
    for sublist in lst:
        key = tuple(sorted(sublist))
        unique_sublists[key] = unique_sublists.get(key, 0) + 1
    return unique_sublists
print(count_unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]))

"""95. Write a Python program to sort each sublist of strings in a given list of lists.
    Original list:
    [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
    Sort the list of lists by length and value:
    [[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]
"""
def sort_sublists(lst):
    return sorted(lst, key=lambda x: (len(x), x))  # or     [sorted(sublist) for sublist in lst]
print(sort_sublists([[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]))

"""96. Write a Python program to sort a given list of lists by length and value.
    Original list:
    [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
    Sort the list of lists by length and value:
    [[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]
"""
def sort_list(lst):
    lst = [sorted(sub) for sub in lst]
    return sorted(lst, key=lambda x: (len(x), x))
# Test input
print(sort_list([[2], [0], [1, 3], [0, 7], [9, 11], [15, 17, 13, 14, 11]]))

"""97. Write a Python program to remove sublists from a given list of lists that contain an element
    outside a given range.
    Original list:
    [[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
    After removing sublists from a given list of lists, which contains an element outside the given range:
    [[13, 14, 15, 17]]
"""
def del_sublist(lst, start, end):
    return [sublist for sublist in lst if all(start <= item <= end for item in sublist)]
print(del_sublist([[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]], 0, 10))

"""98. Write a Python program to scramble the letters of a string in a given list.
    Original list:
    ['Python', 'list', 'exercises', 'practice', 'solution']
    After scrambling the letters of the strings of the said list:
    ['tnPhyo', 'tlis', 'ecrsseiex', 'ccpitear', 'noiltuos']
"""
def scramble_string(lst):
    import random
    return [''.join(random.sample(string, len(string))) for string in lst]
print(scramble_string(['Python', 'list', 'exercises', 'practice', 'solution']))

"""99. Write a Python program to find the maximum and minimum values in a given heterogeneous list.
    Original list:
    ['Python', 3, 2, 4, 5, 'version']
    Maximum and Minimum values in the said list:
    (5, 2)
"""
def max_min(lst):
    numbers = [x for x in lst if isinstance(x, (int, float))]
    return max(numbers), min(numbers)
print(max_min(['Python', 3, 2, 4, 5, 'version']))


"""100. Write a Python program to extract common index elements from more than one given list.
    Original lists:
    [1, 1, 3, 4, 5, 6, 7]
    [0, 1, 2, 3, 4, 5, 7]
    [0, 1, 2, 3, 4, 5, 7]
    Common index elements of the said lists:
    [1, 7]
"""

def common_index(lst1, lst2, lst3):
    common_elements = []
    for i in range(len(lst1)):
        if lst1[i] == lst2[i] == lst3[i]:
            common_elements.append(lst1[i])
    return common_elements
print(common_index([1, 1, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 7], [0, 1, 2, 3, 4, 5, 7]))
# OR
def common_index(lst1, lst2, lst3):
    return [i for i, j, k in zip(lst1, lst2, lst3) if i == j == k]
print(common_index([1, 1, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 7], [0, 1, 2, 3, 4, 5, 7]))



"""101. Write a Python program to sort a given matrix in ascending order according to the sum of its rows.
    Original Matrix:
    [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
    Sort the said matrix in ascending order according to the sum of its rows
    [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
    Original Matrix:
    [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
    Sort the said matrix in ascending order according to the sum of its rows
    [[-2, 4, -5], [1, -1, 1], [1, 2, 3]]
"""
def sort_matrix(matrix):
    return sorted(matrix, key=lambda x:sum(x))
print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]]))

"""102. Write a Python program to extract specified size of strings from a give list of string values.
    Original list:
    ['Python', 'list', 'exercises', 'practice', 'solution']
    length of the string to extract:
    8
    After extracting strings of specified length from the said list:
    ['practice', 'solution']
"""
def extract_strings(lst, length):
    return [string for string in lst if len(string) >= length]
print(extract_strings(['Python', 'list', 'exercises', 'practice', 'solution'], 8))
    
"""103. Write a Python program to extract specified number of elements from a given list,
    which follows each other continuously.
    Original list:
    [1, 1, 3, 4, 4, 5, 6, 7]
    Extract 2 number of elements from the said list which follows each other continuously:
    [1, 4]
    Original lists:
    [0, 1, 2, 3, 4, 4, 4, 4, 5, 7]
    Extract 4 number of elements from the said list which follows each other continuously:
    [4]
"""
def extract_continuous(lst, n):
    result = []
    for i in range(len(lst) - n + 1):
        if len(set(lst[i:i+n])) == 1:
            result.append(lst[i])
    return result
print(extract_continuous([1, 1, 3, 4, 4, 5, 6, 7], 2))

"""104. Write a Python program to find the difference between consecutive numbers in a given list.
    Original list:
    [1, 1, 3, 4, 4, 5, 6, 7]
    Difference between consecutive numbers of the said list:
    [0, 2, 1, 0, 1, 1, 1]
    Original list:
    [4, 5, 8, 9, 6, 10]
    Difference between consecutive numbers of the said list:
    [1, 3, 1, -3, 4]
"""
def consecutive_difference(lst):
    return [lst[i] - lst[i-1] for i in range(1, len(lst))]
print(consecutive_difference([1, 1, 3, 4, 4, 5, 6, 7]))

"""105. Write a Python program to compute average of two given lists.
    Original list:
    [1, 1, 3, 4, 4, 5, 6, 7]
    [0, 1, 2, 3, 4, 4, 5, 7, 8]
    Average of two lists:
    3.823529411764706
"""
def average_of_lists(lst1, lst2):
    return (sum(lst1) + sum(lst2)) / (len(lst1) + len(lst2))
print(average_of_lists([1, 1, 3, 4, 4, 5, 6, 7], [0, 1, 2, 3, 4, 4, 5, 7, 8]))

"""106. Write a Python program to count integers in a given mixed list.
    Original list:
    [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
    Number of integers in the said mixed list:
    6
"""
def count_int(lst):
    return sum(1 for item in lst if isinstance(item, (float, int)))
print(count_int([1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]))

"""107. Write a Python program to remove a specified column from a given nested list.
    Original Nested list:
    [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
    After removing 1st column:
    [[2, 3], [4, 5], [1, 1]] 
"""
def function(lst, col):
    return [row[:col] + row[col+1:] for row in lst]
print(function([[1, 2, 3], [2, 4, 5], [1, 1, 1]], 2))


"""108. Write a Python program to extract a specified column from a given nested list.
    Original Nested list:
    [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
    Extract 1st column:
    [1, 2, 1]
"""
def extract(lst, col):
    return [k[col] for k in lst]
print(extract([[1, 2, 3], [-2, 4, -5], [1, -1, 1]], 1))

"""109. Write a Python program to rotate a given list by a specified number of items in the right
    or left direction.
    original List:
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Rotate the said list in left direction by 4:
    [4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
"""
def rotate(lst, num):
    return lst[num:] + lst[:num]
print(rotate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4))

"""110. Write a Python program to find the item with the most occurrences in a given list.
    Original list:
    [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
    Item with maximum occurrences of the said list:
    2
"""
def most_occr(lst):
    return max(set(lst), key=lst.count)
print(most_occr([2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]))
# OR
def most_occr(lst):
    from collections import Counter
    return Counter(lst).most_common(1)[0][0]
print(most_occr([2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]))
# OR
def most_occr(lst):
    from collections import defaultdict
    count = defaultdict(int)
    for item in lst:
        count[item] += 1
    return max(count, key=count.get)
print(most_occr([2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]))
# OR
def most_occr(lst):
    list_count = {}
    for k in lst:
        lst.count[k] = lst.count(k)
    max_count = max(list_count.values())
    return [k for k, v in list_count.items() if v == max_count]
print(most_occr([2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]))

"""111. Write a Python program to access multiple elements at a specified index from a given list.
    Original list:
    [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
    Index list:
    [0, 3, 5, 7, 10]
    Items with specified index of the said list:
    [2, 4, 9, 2, 1]
"""
def access_multiple(lst, index):
    return [lst[i] for i in index]
print(access_multiple([2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2], [0, 3, 5, 7, 10]))
# OR
def access_multiple(lst, index):    
    return [lst[i] for i in range(len(lst)) if i in index]
print(access_multiple([2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2], [0, 3, 5, 7, 10]))

"""112. Write a Python program to check whether a specified list is sorted or not.
    Original list:
    [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
    Is the said list is sorted!
    True
"""
def is_sorted(lst):
    return lst == sorted(lst)
print(is_sorted([1, 2, 4, 6, 8, 10, 12, 14, 16, 17]))

"""113. Write a Python program to remove duplicate dictionary entries from a given list.
    Original list with duplicate dictionary:
    [{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]
    After removing duplicate dictionary of the said list:
    [{'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]
"""
def remove_duplicates(lst):
    seen = set()
    result = []
    for d in lst:
        t = tuple(d.items())
        if t not in seen:
            seen.add(t)
            result.append(d)
    return result
print(remove_duplicates([{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]))
"""114. Write a Python program to extract the nth element from a given list of tuples.
    Original list:
    [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
    Extract nth element ( n = 0 ) from the said list of tuples:
    ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
"""
def extract_element(lst, n):
    return [k[n] for k in lst]
print(extract_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)], 0))

"""115. Write a Python program to check if the elements of a given list are unique or not.
    Original list:
    [1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]
    Is the said list contains all unique elements!
    False
"""
def unique(lst, n):
    return len(lst) == len(set(lst))
print(unique([1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17], 0))

"""116. Write a Python program to sort a list of lists by a given index of the inner list.
    Original list:
    [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
    Sort the said list of lists by a given index ( Index = 0 ) of the inner list
    [('Beau Turnbull', 94, 98), ('Brady Kent', 97, 96), ('Greyson Fulton', 98, 99), ('Wyatt Knott', 91, 94)]
"""
def sort_by_index(lst, index):
    return sorted(lst, key= lambda x:x[index])
print(sort_by_index([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)], 0))

"""117. Write a Python program to remove all elements from a given list that are present in another list.
    Original lists:
    list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list2: [2, 4, 6, 8]
    Remove all elements from 'list1' present in 'list2:
    [1, 3, 5, 7, 9, 10]
"""
def remove_elements(lst1, lst2):
    return [x for x in lst1 if x not in lst2]
print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]))
# or
def remove_elements(lst1, lst2):
    return list(filter(lambda x: x not in lst2, lst1))
# or
def remove_elements(lst1, lst2):
    return [x for x in lst1 if x not in set(lst2)]

# or
def remove_elements(lst1, lst2):
    return [x for x in lst1 if not any(x == y for y in lst2)]

"""118. Write a Python program to find the difference between elements (n+1th - nth)
    of a given list of numeric values.
    Original list:
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Dfference between elements (n+1th - nth) of the said list :
    [1, 1, 1, 1, 1, 1, 1, 1, 1]
"""
def difference(lst):
    return [lst[i+1] - lst[i] for i in range(len(lst)-1)]
print(difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""119. Write a Python program to check if a substring appears in a given list of string values.
    Original list:
    ['red', 'black', 'white', 'green', 'orange']
    Substring to search:
    ack
"""
def check_substring(lst, substring):
    return any(substring in string for string in lst)
print(check_substring(['red', 'black', 'white', 'green', 'orange'], 'ack'))

"""120. Write a Python program to create a list taking alternate elements from a given list.
    Original list:
    ['red', 'black', 'white', 'green', 'orange']
    List with alternate elements from the said list:
    ['red', 'white', 'orange']
"""
def alt_lst(lst):
    return lst[::2]
print(alt_lst(['red', 'black', 'white', 'green', 'orange']))

"""121. Write a Python program to find nested list elements that are present in another list.
    Original lists:
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
    Intersection of said nested lists:
    [[12], [7, 11], [1, 5, 8]]
"""

"""122. Write a Python program to find common elements in a nested list.
    Original lists:
    [[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
    Common element(s) in nested lists:
    [18, 12]
"""
def common_elements(lst):
    from functools import reduce
    return list(reduce(lambda x, y: set(x) & set(y), lst))
print(common_elements([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))
    
def common_elements(lst):
    new_lst = [set(x) for x in lst]
    common = set.intersection(*new_lst)
    return list(common)
print(common_elements([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))

def common_elements(lst):
    return list(set.intersection(*map(set, lst)))
print(common_elements([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))

"""123. Write a Python program to reverse strings in a given list of string values.
    Original lists:
    ['Red', 'Green', 'Blue', 'White', 'Black']
    Reverse strings of the said given list:
    ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
"""
def reverse_str(lst):
    return list(map(lambda x: x[::-1], lst))
print(reverse_str(['Red', 'Green', 'Blue', 'White', 'Black']))

# OR
def reverse_str(lst):
    return [s[::-1] for s in lst]

"""124. Write a Python program to find the maximum and minimum product of pairs of tuples within a given list.
    The original list, tuple :
    [(2, 7), (2, 6), (1, 8), (4, 9)]
    Maximum and minimum product from the pairs of the said tuple of list:
    (36, 8)
"""
def max_min_product(lst):
    products = [a * b for a, b in lst]
    return max(products), min(products)

"""125. Write a Python program to calculate the product of the unique numbers in a given list.
    Original List : [10, 20, 30, 40, 20, 50, 60, 40]
    Product of the unique numbers of the said list: 720000000
"""
from itertools import reduce
def product_of_unique(lst):
    return reduce(lambda x, y: x * y, set(lst))
"""126. Write a Python program to interleave multiple lists of the same length.
    Original list:
    list1: [1, 2, 3, 4, 5, 6, 7]
    list2: [10, 20, 30, 40, 50, 60, 70]
    list3: [100, 200, 300, 400, 500, 600, 700]
    Interleave multiple lists:
    [1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]
"""
def lst_interleave(*args):
    from itertools import chain
    return list(chain.from_iterable(zip(*args)))
print(lst_interleave([1, 2, 3, 4, 5, 6, 7], [10, 20, 30, 40, 50, 60, 70], [100, 200, 300, 400, 500, 600, 700]))

# OR
def lst_interleave(*args):
    return [x for pair in zip(*args) for x in pair]

"""127. Write a Python program to remove words from a given list of strings containing a character or string.
     Original list:
     list1: ['Red color', 'Orange#', 'Green', 'Orange @', 'White']
     Character list:
     ['#', 'color', '@']
     New list:
     ['Red', '', 'Green', 'Orange', 'White']
"""
def remove_words(lst, chars):
    return [x for x in lst if not any(c in x for c in chars)]
print(remove_words(['Red color', 'Orange#', 'Green', 'Orange @', 'White'], ['#', 'color', '@']))

"""128. Write a Python program to calculate the sum of the numbers in a list between
    the indices of a specified range.
    Original list:
    [2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]
    Range: 8 , 10
    Sum of the specified range:
    29
"""
def sum_in_range(lst, start, end):
    return sum(lst[start:end+1])
"""129. Write a Python program to reverse each list in a given list of lists.
    Original list of lists:
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
"""
def reverse_each_list(lst):
    reversed_lists = [sublist[::-1] for sublist in lst]
    return reversed_lists
# OR
def reverse_each_list(lst):
    return [list(reversed(sublist)) for sublist in lst]
print(reverse_each_list([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))

"""130. Write a Python program to count the same pair in three given lists.
    Original lists:
    [1, 2, 3, 4, 5, 6, 7, 8]
    [2, 2, 3, 1, 2, 6, 7, 9]
    [2, 1, 3, 1, 2, 6, 7, 9]
    Number of same pair of the said three given lists:
    3
"""
def count_same_pair(lst1, lst2, lst3):
    count = 0
    for i in range(len(lst1)):
        if lst1[i] == lst2[i] == lst3[i]:
            count += 1
    return count
# OR
def count_same_pair(lst1, lst2, lst3):
    return sum(1 for a, b, c in zip(lst1, lst2, lst3) if a == b == c)
# OR
def count_same_pair(lst1, lst2, lst3):
    return len([1 for a, b, c in zip(lst1, lst2, lst3) if len(set([a, b, c])) == 1])
print(count_same_pair([1, 2, 3, 4, 5, 6, 7, 8], [2, 2, 3, 1, 2, 6, 7, 9], [2, 1, 3, 1, 2, 6, 7, 9]))

"""131. Write a Python program to count the frequency of consecutive duplicate elements
    in a given list of numbers.
    Original lists:
    [1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5]
    Consecutive duplicate elements and their frequency:
    ([1, 2, 4, 5], [1, 3, 3, 4])
"""
from collections import Counter
def dup_freq(lst):
    from itertools import groupby
    grouped = [(key, len(list(group))) for key, group in groupby(lst)]
    return [key for key, _ in grouped], [count for _, count in grouped]
print(dup_freq([1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5]))
# OR
from collections import Counter
def dup_freq(lst):
    counts = Counter(lst)
    return list(counts.keys()), list(counts.values())   
print(dup_freq([1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5]))
# or
def dup_freq(lst):
    cnt = []
    for k in lst:
        cnt.append(lst.count(k) if k not in cnt else 0)
    lst = [k for k in lst if k not in cnt]
    return lst, cnt
print(dup_freq([1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5]))


"""132. Write a Python program to find all index positions of the maximum and minimum values in a given list of numbers.
    Original list:
    [12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]
    Index positions of the maximum value of the said list:
    7
    Index positions of the minimum value of the said list:
    3, 11
"""
def max_min_index(lst):
    max_value = max(lst)
    min_value = min(lst)
    max_indices = [i for i, x in enumerate(lst) if x == max_value]
    min_indices = [i for i, x in enumerate(lst) if x == min_value]
    return max_indices, min_indices
print(max_min_index([12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]))

"""133. Write a Python program to check if two lists have the same elements in them in same order or not.
    Original lists:
    ['red', 'green', 'black', 'orange']
    ['red', 'pink', 'green', 'white', 'black']
    ['white', 'orange', 'pink', 'black']
    Test common elements between color1 and color2 are in same order?
    True
"""
def same_order(lst1, lst2):
    """a normal function """
    x = 10
    all(1 for k in set(lst1) if k in lst2 and lst1.index(k) == lst2.index(k))
print(same_order(['red', 'green', 'black', 'orange'], ['red', 'pink', 'green', 'white', 'black']))

"""134. Write a Python program to find the difference between two lists including duplicate elements.
    Original lists:
    [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
    [1, 1, 2, 4, 5, 6]
    Difference between two said list including duplicate elements):
    [3, 3, 4, 7]
"""
def lst_diff(lst1, lst2):
    for k in lst2:
        if k in lst1:
            lst1.remove(k)
        else:
            lst1
    return lst1

lst1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
lst2 = [1, 1, 2, 4, 5, 6,12,12,23,45,63,1]
print(lst_diff(lst1, lst2))

"""135. Write a Python program to iterate over all pairs of consecutive items in a given list.
    Original lists:
    [1, 1, 2, 3, 3, 4, 4, 5]
    Iterate over all pairs of consecutive items of the said list:
    [(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
"""
def iterlst(lst):
    return [(lst[i], lst[i+1]) for i in range(len(lst)-1)]
print(iterlst([1, 1, 2, 3, 3, 4, 4, 5]))

# OR
def iterlst(lst):
    return list(zip(lst, lst[1:]))
print(iterlst([1, 1, 2, 3, 3, 4, 4, 5]))

"""136. Write a Python program to remove duplicate words from a given list of strings.
    Original String:
    ['Python', 'Exercises', 'Practice', 'Solution', 'Exercises']
    After removing duplicate words from the said list of strings:
    ['Python', 'Exercises', 'Practice', 'Solution']
"""
def remove_duplicates(lst):
    return list(dict.fromkeys(lst))
print(remove_duplicates(['Python', 'Exercises', 'Practice', 'Solution', 'Exercises']))
# OR
def remove_duplicates(lst):
    return list(set(lst))
print(remove_duplicates(['Python', 'Exercises', 'Practice', 'Solution', 'Exercises']))
    
"""137. Write a Python program to find the first even and odd number in a given list of numbers.
    Original list:
    [1, 3, 5, 7, 4, 1, 6, 8]
    First even and odd number of the said list of numbers:
    (4, 1)
"""
def first_even_odd(lst):
    even = next((x for x in lst if x % 2 == 0), None)
    odd = next((x for x in lst if x % 2 != 0), None)
    return even, odd
print(first_even_odd([1, 3, 5, 7, 4, 1, 6, 8]))

"""138. Write a Python program to sort a given mixed list of integers and strings.
    Numbers must be sorted before strings.
    Original list:
    [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
    Sort the said mixed list of integers and strings:
    [1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']
"""
def sort_mixed_list(lst):
    return sorted([x for x in lst if isinstance(x, int)]) + sorted([x for x in lst if isinstance(x, str)])
print(sort_mixed_list([19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]))

""" 139. Write a Python program to sort a given list of strings(numbers) numerically.
    Original list:
    ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
    Sort the said list of strings(numbers) numerically:
    [-500, -12, 0, 4, 7, 12, 45, 100, 200]
"""
def sort_numerically(lst):
    return sorted(lst, key=lambda x: int(x))
print(sort_numerically(['4', '12', '45', '7', '0', '100', '200', '-12', '-500']))

"""140. Write a Python program to remove a specific item from a given list of lists.
    Original list of lists:
    [['Red', 'Maroon', 'Yellow', 'Olive'], ['#FF0000', '#800000', '#FFFF00', '#808000'], ['rgb(255,0,0)', 'rgb(128,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']]
    Remove 1st list from the saod given list of lists:
    [['Maroon', 'Yellow', 'Olive'], ['#800000', '#FFFF00', '#808000'], ['rgb(128,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']]
    Remove 2nd list from the saod given list of lists:
    [['Red', 'Yellow', 'Olive'], ['#FF0000', '#FFFF00', '#808000'], ['rgb(255,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']]
    Remove 4th list from the saod given list of lists:
    [['Red', 'Maroon', 'Yellow'], ['#FF0000', '#800000', '#FFFF00'], ['rgb(255,0,0)', 'rgb(128,0,0)', 'rgb(255,255,0)']]
"""
def remove_item(lst, index):
    """Remove a specific item from a given list of lists."""
    return [row[:index] + row[index+1:] for row in lst]
print(remove_item([['Red', 'Maroon', 'Yellow', 'Olive'], ['#FF0000', '#800000', '#FFFF00', '#808000'], ['rgb(255,0,0)', 'rgb(128,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']], 0))

"""141. Write a Python program to remove empty lists from a given list of lists.
    Original list:
    [[], [], [], 'Red', 'Green', [1, 2], 'Blue', [], []]
    After deleting the empty lists from the said lists of lists
    ['Red', 'Green', [1, 2], 'Blue']
"""
def remove_emplty_list(lst):
    return [x for x in lst if len(x)!=0]
print(remove_emplty_list([[], [], [], 'Red', 'Green', [1, 2], 'Blue', [], []]))
# OR
def remove_emplty_list(lst):
    return list(x for x in lst if len(x)!=0)
# OR
def remove_emplty_list(lst):
    return [x for x in lst if x]
# OR
def remove_emplty_list(lst):
    return list(filter(None, lst))
print(remove_emplty_list([[], [], [], 'Red', 'Green', [1, 2], 'Blue', [], []]))

"""142. Write a Python program to sum a specific column of a list in a given list of lists.
    Original list of lists:
    [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
    Sum: 1st column of the said list of lists:
    12
"""
def sum_column(lst, col):
    return sum(row[col] for row in lst)
print(sum_column([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]], 0))    

"""143. Write a Python program to get the frequency of elements in a given list of lists.
    Original list of lists:
    [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
    Frequency of the elements in the said list of lists:
    {1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
"""
from collections import Counter
def freq_count(lst):
    flat = [item for sublist in lst for item in sublist]
    return dict(Counter(flat))
print(freq_count([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]))

def freq_count(lst):
    return {k: sum(sublist.count(k) for sublist in lst) for k in {item for sublist in lst for item in sublist}}
print(freq_count([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]))

"""144. Write a Python program to extract every first or specified element from a given two-dimensional list.
    Original list of lists:
    [[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]
    Extract every first element from the said given two dimensional list:
    [1, 4, 7]
    Extract every third element from the said given two dimensional list:
    [3, 6, 9]
"""
def extract(lst, index):
    indx = index-1
    return [k[indx] for k in lst]
print(extract([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]], 1))

"""145. Write a Python program to generate a number in a specified range except for some specific numbers.
    Generate a number in a specified range (1, 10) except [2, 9, 10]
    7
    Generate a number in a specified range (-5, 5) except [-5,0,4,3,2]
    -4
"""
def generate_number(start, end, exclude):
    return random.randint(start, end) if random.randint(start, end) not in exclude else generate_number(start, end, exclude)
print(generate_number(1, 10, [2, 9, 10]))
print(generate_number(-5, 5, [-5, 0, 4, 3, 2]))

"""146. Write a Python program to compute the sum of digits of each number in a given list.
    Original tuple:
    [10, 2, 56]
    Sum of digits of each number of the said list of integers:
    14
"""
from pathlib import Path
p = Path('.')
print([x for x in p.iterdir() if x.is_dir()])
print(list(p.glob('**/*.py')))

"""147. Write a Python program to combine two lists into another list randomly.
    Original lists:
    [1, 2, 7, 8, 3, 7]
    [4, 3, 8, 9, 4, 3, 8, 9]
    Interleave two given list into another list randomly:
    [4, 1, 2, 3, 8, 9, 4, 3, 7, 8, 9, 8, 3, 7]
"""
def interleave(lst1, lst2):
    return [x for pair in zip(lst1, lst2) for x in pair]
print(interleave([1, 2, 7, 8, 3, 7], [4, 3, 8, 9, 4, 3, 8, 9]))

"""148. Write a Python program to remove specific words from a given list.
    Original list:
    ['red', 'green', 'blue', 'white', 'black', 'orange']
    Remove words:
    ['white', 'orange']
    After removing the specified words from the said list:
    ['red', 'green', 'blue', 'black']
"""
def remove_word(lst, ord):
    return [k for k in lst if k not in ord]
print(remove_word(['red', 'green', 'blue', 'white', 'black', 'orange'], ['white', 'orange']))

"""149. Write a Python program to get all possible combinations of the elements of a given list.
    Original list:
    ['orange', 'red', 'green', 'blue']
    All possible combinations of the said list's elements:
    [[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]
"""


from multiprocessing import Process, current_process, parent_process, active_children, cpu_count
import time
import os

def worker():
    print(f"[Child] PID: {os.getpid()}")
    print(f"[Child] Name: {current_process().name}")
    print(f"[Child] Parent PID: {parent_process().pid}")
    time.sleep(2)
    print(f"[Child] Done!")

if __name__ == "__main__":
    print(f"[Main] PID: {os.getpid()}")
    print(f"[Main] CPU count: {cpu_count()}")
    
    # Create multiple child processes
    processes = [Process(target=worker, name=f"Worker-{i}") for i in range(3)]

    for p in processes:
        p.start()

    # Show active children
    print(f"[Main] Active children: {active_children()}")

    # Wait for all to finish
    for p in processes:
        p.join()

    # After join, active_children should be empty
    print(f"[Main] Active children after join: {active_children()}")


"""150. Write a Python program to reverse a given list of lists.
    Original list:
    [['orange', 'red'], ['green', 'blue'], ['white', 'black', 'pink']]
    Reverse said list of lists:
    [['white', 'black', 'pink'], ['green', 'blue'], ['orange', 'red']]
"""
def reverse_list(lst):
    return lst[::-1]
print(reverse_list([[1, 2, 3, 4], [0, 2, 4, 5], [2, 3, 4, 2, 4]]))
print(reverse_list([['orange', 'red'], ['green', 'blue'], ['white', 'black', 'pink']]))

# OR
def reverse_list(lst):
    return list(reversed(lst))# or lst[::-1]
# OR
def reverse_list(lst):
    return lst[-1: -len(lst) - 1: -1] #or lst
print(reverse_list([['orange', 'red'], ['green', 'blue'], ['white', 'black', 'pink']]))

"""151. Write a Python program to find the maximum and minimum values in a given list within a specified
index range.
    Original list:
    [4, 3, 0, 5, 3, 0, 2, 3, 4, 2, 4, 3, 5]
    Index range:
    3 to 8
    Maximum and minimum values of the said given list within index range:
    (5, 0)
"""
def max_min(lst, start, end):
    return max(lst[start:end+1]), min(lst[start:end+1])

"""152. Write a Python program to combine two sorted lists using the heapq module.
    Original sorted lists:
    [1, 3, 5, 7, 9, 11]
    [0, 2, 4, 6, 8, 10]
    After merging the said two sorted lists:
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
"""
import heapq
def merge_lists(lst1, lst2):
    return list(heapq.merge(lst1, lst2))
# OR
def merge_lists(lst1, lst2):
    return sorted(lst1 + lst2)

"""153. Write a Python program to check if a given element occurs at least n times in a list.
    Original list:
    [0, 1, 3, 5, 0, 3, 4, 5, 0, 8, 0, 3, 6, 0, 3, 1, 1, 0]
    Check if 3 occurs at least 4 times in a list:
    True
    Check if 0 occurs at least 5 times in a list:
    True
    Check if 8 occurs at least 3 times in a list:
    False
"""
def check_occurrence(lst, element, n):
    """Check if a given element occurs at least n times in a list."""
    return lst.count(element) >= n
print(check_occurrence([0, 1, 3, 5, 0, 3, 4, 5, 0, 8, 0, 3, 6, 0, 3, 1, 1, 0], 3, 4))

"""154. Write a Python program to join two given list of lists of the same length, element wise.
    Original lists:
    [[10, 20], [30, 40], [50, 60], [30, 20, 80]]
    [[61], [12, 14, 15], [12, 13, 19, 20], [12]]
    Join the said two lists element wise:
    [[10, 20, 61], [30, 40, 12, 14, 15], [50, 60, 12, 13, 19, 20], [30, 20, 80, 12]]
    Original lists:
    [['a', 'b'], ['b', 'c', 'd'], ['e', 'f']]
    [['p', 'q'], ['p', 's', 't'], ['u', 'v', 'w']]
    Join the said two lists element wise:
    [['a', 'b', 'p', 'q'], ['b', 'c', 'd', 'p', 's', 't'], ['e', 'f', 'u', 'v', 'w']]
"""
def merge_list(lst1, lst2):
    return [a+b for a,b in zip(lst1, lst2)]
print(merge_list([[10, 20], [30, 40], [50, 60], [30, 20, 80]], [[61], [12, 14, 15], [12, 13, 19, 20], [12]]))
    
# OR
def merge_list(lst1, lst2):
    """Join two given list of lists of the same length, element wise."""
    from itertools import zip_longest
    return [list(filter(None, x)) for x in zip_longest(lst1, lst2, fillvalue=[])]
print(merge_list([['a', 'b'], ['b', 'c', 'd'], ['e', 'f']], [['p', 'q'], ['p', 's', 't'], ['u', 'v', 'w']]))
# or
def merge_list(lst1, lst2):
    """Join two given list of lists of the same length, element wise."""
    from itertools import chain
    return [list(chain.from_iterable(x)) for x in zip(lst1, lst2)]
print(merge_list([[10, 20], [30, 40], [50, 60], [30, 20, 80]], [[61], [12, 14, 15], [12, 13, 19, 20], [12]]))

"""155. Write a Python program to add two given lists of different lengths, starting on the left.
    Original lists:
    [2, 4, 7, 0, 5, 8]
    [3, 3, -1, 7]
    Add said two lists from left:
    [5, 7, 6, 7, 5, 8]
    Original lists:
    [1, 2, 3, 4, 5, 6]
    [2, 4, -3]
    Add said two lists from left:
    [3, 6, 0, 4, 5, 6]
"""
def add_lists_left(lst1, lst2):
    copy_lst1 = lst1.copy()
    copy_lst2 = lst2.copy() 
    min_len = min(len(lst1), len(lst2))
    lst11 = copy_lst1[:min_len]  # Take the last 'min_len' elements from lst1
    lst22 = copy_lst2[:min_len]  # Take the last 'min_len' elements from lst2
    lst1r = lst1[min_len:]  # Take the last 'min_len' elements from lst1
    lst2r = lst2[min_len:]  # Take the last 'min_len' elements from lst2
    
    result = [x + y for x, y in zip(lst11, lst22)]
    result = result + lst1r + lst2r
    return result
print(add_lists_left([2, 4, 7, 0, 5, 8], [3, 3, -1, 7]))

# or
def add_lists_left(lst1, lst2):
    """Add two given lists of different lengths, starting on the left."""
    from itertools import zip_longest
    return [sum(x) for x in zip_longest(lst1, lst2, fillvalue=0)]
print(add_lists_left([2, 4, 7, 0, 5, 8], [3, 3, -1, 7]))
# OR
def add_lists_left(lst1, lst2):
    """Add two given lists of different lengths, starting on the left."""
    return [x + y for x, y in zip(lst1, lst2)]
print(add_lists_left([1, 2, 3, 4, 5, 6], [2, 4, -3]))
# OR
def add_lists_left(lst1, lst2):
    """Add two given lists of different lengths, starting on the left."""
    max_len = max(len(lst1), len(lst2))
    lst1 = lst1 + [0] * (max_len - len(lst1))
    lst2 = lst2 + [0] * (max_len - len(lst2))
    return [x + y for x, y in zip(lst1, lst2)]
print(add_lists_left([2, 4, 7, 0, 5, 8], [3, 3, -1, 7]))

"""156. Write a Python program to add two given lists of different lengths, starting on the right.
    Original lists:
    [2, 4, 7, 0, 5, 8]
    [3, 3, -1, 7]
    Add said two lists from left:
    [2, 4, 10, 3, 4, 15]
    Original lists:
    [1, 2, 3, 4, 5, 6]
    [2, 4, -3]
    Add said two lists from left:
    [1, 2, 3, 6, 9, 3]
"""
def add_lists_right(lst1, lst2):
    """Add two given lists of different lengths, starting on the right."""
    from itertools import zip_longest
    return [sum(x) for x in zip_longest(lst1[::-1], lst2[::-1], fillvalue=0)][::-1]
print(add_lists_right([2, 4, 7, 0, 5, 8], [3, 3, -1, 7]))
# OR
def add_lists_right(lst1, lst2):
    """Add two given lists of different lengths, starting on the right."""
    max_len = max(len(lst1), len(lst2))
    lst1 = [0] * (max_len - len(lst1)) + lst1
    lst2 = [0] * (max_len - len(lst2)) + lst2
    return [x + y for x, y in zip(lst1, lst2)]
print(add_lists_right([1, 2, 3, 4, 5, 6], [2, 4, -3]))

"""157. Write a Python program to interleave lists of varying lengths.
    Original lists:
    [2, 4, 7, 0, 5, 8]
    [2, 5, 8]
    [0, 1]
    [3, 3, -1, 7]
    Interleave said lists of different lengths:
    [2, 2, 0, 3, 4, 5, 1, 3, 7, 8, -1, 0, 7, 5, 8]
"""
def interleave_lists(*lists):
    return [item for sublist in zip(*lists) for item in sublist] + [item for sublist in lists[len(lists[0]):] for item in sublist   ]

"""158. Write a Python program to find the maximum and minimum values in a given list of tuples.        
    Original list with tuples:
    [('V', 60), ('VI', 70), ('VII', 75), ('VIII', 72), ('IX', 78), ('X', 70)]
    Maximum and minimum values of the said list of tuples:
    (78, 60)
"""
def max_min_tuples(lst):
    """Find the maximum and minimum values in a given list of tuples."""
    max_value = max(t[1] for t in lst)
    min_value = min(t[1] for t in lst)
    return max_value, min_value
print(max_min_tuples([('V', 60), ('VI', 70), ('VII', 75), ('VIII', 72), ('IX', 78), ('X', 70)]))
# or
def max_min_tuples(lst):return max(lst, key=lambda x: x[1])[1], min(lst, key=lambda x: x[1])[1]
print(max_min_tuples([('V', 60), ('VI', 70), ('VII', 75), ('VIII', 72), ('IX', 78), ('X', 70)]))

"""159. Write a Python program to append the same value/a list multiple times to a list/list-of-lists.
    Add a value(7), 5 times, to a list:
    ['7', '7', '7', '7', '7']
    Add 5, 6 times, to a list:
    [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]
    Add a list, 4 times, to a list of lists:
    [[1, 2, 5], [1, 2, 5], [1, 2, 5], [1, 2, 5]]
    Add a list, 3 times, to a list of lists:
    [[5, 6, 7], [1, 2, 5], [1, 2, 5], [1, 2, 5], [1, 2, 5]]
"""
def append_val(lst, val):
    return [val] * lst if isinstance(lst, int) else [lst] * val
print(append_val(7, 5))  # ['7', '7', '7', '7', '7']
print(append_val(5, 6))  # [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]

"""160. Write a Python program to remove the first specified number of elements from a given list
    satisfying a condition. Remove the first 4 number of even numbers from the following list:
    Original list:
    [3,10,4,7,5,7,8,3,3,4,5,9,3,4,9,8,5]
    Output:
    [3, 7, 5, 7, 3, 3, 5, 9, 3, 4, 9, 8, 5]
"""
from typing import List
def rem(lst: list[int], n: int) -> list[int]:
    """Remove the first n even numbers from the list."""
    return [x for x in lst if x % 2 != 0 or n <= 0 or (n := n - 1) < 0]
print(rem([3, 10, 4, 7, 5, 7, 8, 3, 3, 4, 5, 9, 3, 4, 9, 8, 5], 4))

def rem(lst, n):                                                   
    return [x for x in lst if x % 2 != 0 or n <= 0 or (n := n - 1) < 0]
print(rem([3, 10, 4, 7, 5, 7, 8, 3, 3, 4, 5, 9, 3, 4, 9, 8, 5], 4))

"""161. Write a Python program to check if a given list increases strictly. Moreover,
if removing only one element from the list results in a strictly increasing list,
we still consider the list true.
    True
    True
    True
    True
    True
    True
    True
    True
    True
    True
    True
    False
    False
    False
    False
    False
"""





"""162. Write a Python program to find the last occurrence of a specified item in a given list.
    Original list:
    ['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
    Last occurrence of f in the said list:
    7
    Last occurrence of c in the said list:
    15
"""
def last_occ(lst, occr):
    return (len(lst)-1) - lst[::-1].index(occr) if occr in lst else -1
print(last_occ(['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c'], 'f'))
print(last_occ(['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c'], 'c'))
# OR
def lst_occr(lst, occr):
    for i in range(len(lst)-1, -1, -1):
        if lst[i] == occr:
            return i
    return -1
print(lst_occr(['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c'], 'f'))
print(lst_occr(['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c'], 'c'))

# or
def last_occurrence(lst, item):
    """Find the last occurrence of a specified item in a given list."""
    try:
        return len(lst) - 1 - lst[::-1].index(item)
    except ValueError:
        return -1
# OR
lst_occr = lambda lst, occr: (len(lst)-1) - lst[::-1].index(occr) if occr in lst else -1
"""163. Write a Python program to get the index of the first element that is greater than a specified element.
    Original list:
    [12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83]
    Index of the first element which is greater than 73 in the said list:
    4
    Index of the first element which is greater than 21 in the said list:
    1
"""
def first_greater_index(lst, elem):
    for k in lst:
        if k > elem:
            return lst.index(k)
    return -1
print(first_greater_index([12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83], 73))
print(first_greater_index([12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83], 21))   

"""164. Write a Python program to get items from a given list with specific conditions.
    Original list:
    [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
    Number of Items of the said list which are even and greater than 45
    5
"""
def count_even_greater(lst, num):
    return len([x for x in lst if x % 2 == 0 and x > num])
print(count_even_greater([12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83], 45))

"""165. Write a Python program to split a given list into specified-sized chunks.
    Original list:
    [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
    Split the said list into equal size 3
    [[12, 45, 23], [67, 78, 90], [45, 32, 100], [76, 38, 62], [73, 29, 83]]
"""
def split_list(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst),n)]
print(split_list([12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83],4))

# OR
split_list = lambda lst, n:[lst[i:i+n] for i in range(0, len(lst),n)]
print(split_list([12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83],4))

"""166. Write a Python program to remove the None value from a given list.
    Original list:
    [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
    Remove None value from the said list:
    [12, 0, 23, -55, 234, 89, 0, 6, -12]
"""
def remove_none(lst):
    return [k for k in lst if k!= None]
print(remove_none([12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]))

"""167. Write a Python program to convert a given list of strings into a list of lists.
    Original list of strings:
    ['Red', 'Maroon', 'Yellow', 'Olive']
    Convert the said list of strings into list of lists:
    [['R', 'e', 'd'], ['M', 'a', 'r', 'o', 'o', 'n'], ['Y', 'e', 'l', 'l', 'o', 'w'], ['O', 'l', 'i', 'v', 'e']]
"""
def str_to_list(lst):
    return [list(s) for s in lst]

"""168. Write a Python program to display vertically each element of a given list, list of lists.
    Original list:
    ['a', 'b', 'c', 'd', 'e', 'f']
    Display each element vertically of the said list:
    a
    b
    c
    d
    e
    f
    Original list:
    [[1, 2, 5], [4, 5, 8], [7, 3, 6]]
    Display each element vertically of the said list of lists:
    1 4 7
    2 5 3
    5 8 6
"""
def display_vertically(lst):
    return '\n'.join(' '.join(str(x) for x in row) for row in zip(*lst))
print(display_vertically(['a', 'b', 'c', 'd', 'e', 'f']))
print(display_vertically([[1, 2, 5], [4, 5, 8], [7, 3, 6]]))


"""169. Write a Python program to convert a given list of strings and characters to a single list of characters.
    Original list:
    ['red', 'white', 'a', 'b', 'black', 'f']
    Convert the said list of strings and characters to a single list of characters:
    ['r', 'e', 'd', 'w', 'h', 'i', 't', 'e', 'a', 'b', 'b', 'l', 'a', 'c', 'k', 'f']
"""
def sing_st(lst):
    return [j for k in lst for j in k]
print(sing_st(['red', 'white', 'a', 'b', 'black', 'f']))

"""170. Write a Python program to insert an element in a given list after every nth position.
    Original list:
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    Insert a in the said list after 2 nd element:
    [1, 2, 'a', 3, 4, 'a', 5, 6, 'a', 7, 8, 'a', 9, 0]
    Insert b in the said list after 4 th element:
    [1, 2, 3, 4, 'b', 5, 6, 7, 8, 'b', 9, 0]
"""
def insert_after_nth(lst, element, n):
    result = []
    for i, val in enumerate(lst, 1):
        result.append(val)
        if i % n == 0:
            result.append(element)
    return result

# Test case 1
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("Insert 'a' after every 2nd element:")
print(insert_after_nth(original_list, 'a', 2))

# Test case 2
print("\nInsert 'b' after every 4th element:")
print(insert_after_nth(original_list, 'b', 4))

insert_after_nth = lambda lst, e, n: [x for i, x in enumerate(lst, 1) for x in ([x, e] if i % n == 0 else [x])]
from itertools import chain

insert_after_nth = lambda lst, e, n: list(chain.from_iterable((x, e) if (i + 1) % n == 0 else (x,) for i, x in enumerate(lst)))

"""171. Write a Python program to concatenate element-wise three given lists.
    Original lists:
    ['0', '1', '2', '3', '4']
    ['red', 'green', 'black', 'blue', 'white']
    ['100', '200', '300', '400', '500']
    Concatenate element-wise three said lists:
    ['0red100', '1green200', '2black300', '3blue400', '4white500']
"""
def concat(l1,l2,l3):
    return ["".join((k)) for k in list(zip(l1,l2,l3))]
print(concat(['0', '1', '2', '3', '4'],
    ['red', 'green', 'black', 'blue', 'white'],
    ['100', '200', '300', '400', '500']))

"""172. Write a Python program to remove the last N number of elements from a given list.
    Original lists:
    [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
    Remove the last 3 elements from the said list:
    [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34]
    Remove the last 5 elements from the said list:
    [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34]
    Remove the last 1 element from the said list:
    [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3]
"""
def rem(lst):
    return [lst[:-n] for n in range(1, len(lst)+1)]
print(rem([2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]))
# OR
def remove_last_n(lst, n):
    """Remove the last N number of elements from a given list."""
    return lst[:-n] if n <= len(lst) else []    
print(remove_last_n([2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5], 3))

"""173. Write a Python program to merge some list items in a given list using the index value.
    Original lists:
    ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    Merge items from 2 to 4 in the said List:
    ['a', 'b', 'cd', 'e', 'f', 'g']
    Merge items from 3 to 7 in the said List:
    ['a', 'b', 'c', 'defg']
"""
def merge_items(lst, start, end):
    """Merge items from start to end in the given list."""
    return lst[:start] + [''.join(lst[start:end+1])] + lst[end+1:]
print(merge_items(['a', 'b', 'c', 'd', 'e', 'f', 'g'], 2, 4))

"""174. Write a Python program to add a number to each element in a given list of numbers.
    Original lists:
    [3, 8, 9, 4, 5, 0, 5, 0, 3]
    Add 3 to each element in the said list:
    [6, 11, 12, 7, 8, 3, 8, 3, 6]
    Original lists:
    [3.2, 8, 9.9, 4.2, 5, 0.1, 5, 3.11, 0]
    Add 0.51 to each element in the said list:
    [3.71, 8.51, 10.41, 4.71, 5.51, 0.61, 5.51, 3.62, 0.51]
"""
def add_element(lst):
    return list(map(lambda x:x+3, lst))
print(add_element([3, 8, 9, 4, 5, 0, 5, 0, 3]))

def add_element(lst):
    return list(x+3 for x in lst)
print(add_element([3, 8, 9, 4, 5, 0, 5, 0, 3]))

"""175. Write a Python program to find the minimum and maximum value for each tuple position in a given list of tuples.
    Original list:
    [(2, 3), (2, 4), (0, 6), (7, 1)]
    Maximum value for each tuple position in the said list of tuples:
    [7, 6]
    Minimum value for each tuple position in the said list of tuples:
    [0, 1]
"""
def lst(lst):
    return [[max(x) for x in zip(*lst)], [min(x) for x in zip(*lst)]]
print(lst([(2, 3), (2, 4), (0, 6), (7, 1)]))

# OR
def max_min_tuples(lst):
    """Find the maximum and minimum value for each tuple position in a given list of tuples."""
    max_values = [max(t[i] for t in lst) for i in range(len(lst[0]))]
    min_values = [min(t[i] for t in lst) for i in range(len(lst[0]))]
    return max_values, min_values
print(max_min_tuples([(2, 3), (2, 4), (0, 6), (7, 1)]))
# OR
def max_min_tuples(lst):
    """Find the maximum and minimum value for each tuple position in a given list of tuples."""
    return [[max(t[i] for t in lst) for i in range(len(lst[0]))], [min(t[i] for t in lst) for i in range(len(lst[0]))]]
print(max_min_tuples([(2, 3), (2, 4), (0, 6), (7, 1)]))

"""176. Write a Python program to create a new list by dividing two given lists of numbers.
    Original list:
    [7, 2, 3, 4, 9, 2, 3]
    [9, 8, 2, 3, 3, 1, 2]
    [0.7777777777777778, 0.25, 1.5, 1.3333333333333333, 3.0, 2.0, 1.5]
"""
def divide_lists(lst1, lst2):
    """Create a new list by dividing two given lists of numbers."""
    return [x / y if y != 0 else None for x, y in zip(lst1, lst2)]
print(divide_lists([7, 2, 3, 4, 9, 2, 3], [9, 8, 2, 3, 3, 1, 2]))

"""177. Write a Python program to find common elements in a given list of lists.
    Original list:
    [[7, 2, 3, 4, 7], [9, 2, 3, 2, 5], [8, 2, 3, 4, 4]]
    Common elements of the said list of lists:
    [2, 3]
    Original list:
    [['a', 'b', 'c'], ['b', 'c', 'd'], ['c', 'd', 'e']]
    Common elements of the said list of lists:
    ['c']
"""
def common_elements(lst):
    """Find common elements in a given list of lists."""
    from functools import reduce
    return list(reduce(lambda x, y: set(x) & set(y), lst))
print(common_elements([[7, 2, 3, 4, 7], [9, 2, 3, 2, 5], [8, 2, 3, 4, 4]]))
# OR
def common_elements(lst):
    """Find common elements in a given list of lists."""
    return list(set.intersection(*map(set, lst)))
print(common_elements([['a', 'b', 'c'], ['b', 'c', 'd'], ['c', 'd', 'e']]))

# or
def common_elements(lst):
    """Find common elements in a given list of lists."""
    from collections import Counter
    return [item for item, count in Counter(item for sublist in lst for item in sublist).items() if count == len(lst)]
print(common_elements([[7, 2, 3, 4, 7], [9, 2, 3, 2, 5], [8, 2, 3, 4, 4]]))
    
"""178. Write a Python program to insert a specified element in a given list after every nth element.
    Original list:
    [1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
    Insert 20 in said list after every 4 th element:
    [1, 3, 5, 7, 20, 9, 11, 0, 2, 20, 4, 6, 8, 10, 20, 8, 9, 0, 4, 20, 3, 0]
    Original list:
    ['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd']
    Insert Z in said list after every 3 th element:
    ['s', 'd', 'f', 'Z', 'j', 's', 'a', 'Z', 'j', 'd', 'f', 'Z', 'd']
"""
def indert_element(lst, element):
    my_lst = []
    for i, val in enumerate(lst, 1):
        my_lst.append(val)
        if i%4 == 0:
            my_lst.append(element)
    return my_lst
print(indert_element([1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0], 20))
print(indert_element(['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd'], 'Z'))

# or
def insert_after_nth(lst, element, n):
    my_lst = []
    i = n
    """Insert a specified element in a given list after every nth element."""
    while i < len(lst):
        my_lst.insert(i + n, element)
        i += n + 1
    return my_lst
print(insert_after_nth([1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0], 20, 4))

"""179. Write a Python program to create the largest possible number using the elements of a given list of positive integers.
    Original list:
    [3, 40, 41, 43, 74, 9]
    Largest possible number using the elements of the said list of positive integers:
    9744341403
    Original list:
    [10, 40, 20, 30, 50, 60]
    Largest possible number using the elements of the said list of positive integers:
    605040302010
"""
# 1st
def largest_num(lst):
    """Create the largest possible number using the elements of a given list of positive integers."""
    from functools import cmp_to_key
    def compare(x, y):
        return (y + x) > (x + y)  # Compare concatenated strings
    sorted_lst = sorted(map(str, lst), key=cmp_to_key(compare))
    return int(''.join(sorted_lst))

# 2nd
from functools import cmp_to_key
def largest_num(lst):
    def compare(a, b):
        return (a + b < b + a) - (a + b > b + a)
    return int(''.join(sorted(map(str, lst), key=cmp_to_key(compare))))
# 3rd        
def largest_num(lst):
    return int("".join(list(reversed("".join(sorted("".join(map(str, lst))))))))
print(largest_num([3, 40, 41, 43, 74, 9]))
print(largest_num([10, 40, 20, 30, 50, 60]))

"""180. Write a Python program to create the smallest possible number using the elements of a given list of positive integers.
    Original list:
    [3, 40, 41, 43, 74, 9]
    Smallest possible number using the elements of the said list of positive integers:
    3404143749
    Original list:
    [10, 40, 20, 30, 50, 60]
"""
def smallest_poss(lst):
    
    return int(''.join(map(str, sorted(lst))))
print(smallest_poss([3, 40, 41, 43, 74, 9]))    

def smallest_number(nums):
    str_nums = list(map(str, nums))
    # Sort using a key that repeats the string to compare properly
    sorted_nums = sorted(str_nums)
    return ''.join(sorted_nums)
# Test cases
print(smallest_number([3, 40, 41, 43, 74, 9]))      # Output: 3404143749
print(smallest_number([10, 40, 20, 30, 50, 60]))    # Output: 102030405060
print(smallest_number([3, 30, 34, 5, 9]))    # Output: 102030405060

print(smallest_number([10, 2]))          # ❌ "102"
print(smallest_number([3, 30, 34, 5, 9])) # ❌ "3033459" is correct here by luck
print(smallest_number([121, 12]))        # ❌ "12112"

"""181. Write a Python program to iterate a given list cyclically at a specific index position.
    Original list:
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    Iterate the said list cyclically on specific index position 3 :
    ['d', 'e', 'f', 'g', 'h', 'a', 'b', 'c']
    Iterate the said list cyclically on specific index position 5 :
    ['f', 'g', 'h', 'a', 'b', 'c', 'd', 'e']
"""
def cyclic_iterate(lst, index):
    """Iterate a given list cyclically at a specific index position."""
    if not lst or index < 0 or index >= len(lst):
        return lst
    else:
        return [lst[(i + index) % len(lst)] for i in range(len(lst))]
print(cyclic_iterate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], 3))
print(cyclic_iterate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], 5))

"""182. Write a Python program to calculate the maximum and minimum sum of a sublist in a given list of lists.
    Original list:
    [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
    Maximum sum of sub list of the said list of lists:
    [2, 3, 5, 4]
    Minimum sum of sub list of the said list of lists:
    [1, 2, 1, 2]
"""
def max_min(sublst):
    return max(sublst, key=sum), min(sublst, key=sum)
print(max_min([[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]))

"""183. Write a Python program to get the unique values in a given list of lists.
    Original list:
    [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
    Unique values of the said list of lists:
    [0, 1, 2, 3, 4, 5, 7]
    Original list:
    [['h', 'g', 'l', 'k'], ['a', 'b', 'd', 'e', 'c'], ['j', 'i', 'y'], ['n', 'b', 'v', 'c'], ['x', 'z']]
    Unique values of the said list of lists:
    ['e', 'd', 'c', 'b', 'x', 'k', 'n', 'h', 'g', 'j', 'i', 'a', 'l', 'y', 'v', 'z']
"""
def unique_values(lst):
    return list(set(value for sublist in lst for value in sublist))
print(unique_values([[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]))

"""184. Write a Python program to generate Bigrams of words from a given list of strings.
    From Wikipedia:
    A bigram or digram is a sequence of two adjacent elements from a string of tokens, which are typically letters, syllables, or words. A bigram is an n-gram for n=2. The frequency distribution of every bigram in a string is commonly used for simple statistical analysis of text in many applications, including in computational linguistics, cryptography, speech recognition, and so on.
    Original list:
    ['Sum all the items in a list', 'Find the second smallest number in a list']
    Bigram sequence of the said list:
    [('Sum', 'all'), ('all', 'the'), ('the', 'items'), ('items', 'in'), ('in', 'a'), ('a', 'list'), ('Find', 'the'), ('the', 'second'), ('second', 'smallest'), ('smallest', 'number'), ('number', 'in'), ('in', 'a'), ('a', 'list')]
"""
def bigrams(lst):
    my_lst = []
    new_list = lst.split()
    for i, v in enumerate(new_list):
        if i == 0:
            my_lst.append((v, new_list[i+1]))
        else:
            my_lst.append((new_list[i-1], new_list[i]))

    return my_lst[1:]  # Exclude the last element to :void index error
print(bigrams('Sum all the items in a list Find the second smallest number in a list'))

# 2nd  ways
def generate_bigrams(texts):
    words = texts.split()
    return list(zip(words, words[1:]))
print(generate_bigrams('Sum all the items in a list Find the second smallest number in a list'))

# 3rd ways
from itertools import pairwise
def generate_bigrams(texts):
    """Generate Bigrams of words from a given list of strings."""
    words = texts.split()
    return list(pairwise(words))
print(generate_bigrams('Sum all the items in a list Find the second smallest number in a list'))

"""185. Write a Python program to convert a given decimal number to a binary list.
    Original Number: 8
    Decimal number ( 8 ) to binary list:
    [1, 0, 0, 0]
    Original Number: 45
    Decimal number ( 45 ) to binary list:
    [1, 0, 1, 1, 0, 1]
    Original Number: 100
    Decimal number ( 100 ) to binary list:
    [1, 1, 0, 0, 1, 0, 0]
"""
def decimal_to_binary_list(num):
    return [int(k) for k in list((bin(num)))[2:]]

# OR
def decimal_to_binary_list(num):
    """Convert a given decimal number to a binary list."""
    return [int(bit) for bit in bin(num)[2:]]
print(decimal_to_binary_list(8))
print(decimal_to_binary_list(45))
print(decimal_to_binary_list(100))

"""186. Write a Python program to swap two sublists in a given list.
    Original list:
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    Swap two sublists of the said list:
    [0, 6, 7, 8, 9, 3, 4, 5, 1, 2, 10, 11, 12, 13, 14, 15]
    Swap two sublists of the said list:
    [0, 9, 3, 8, 6, 7, 4, 5, 1, 2, 10, 11, 12, 13, 14, 15]
"""
def swap_sublists(lst, start1, end1, start2, end2):
    pass

""" 187. Write a Python program to convert a given list of tuples to a list of strings.
    Original list of tuples:
    [('red', 'green'), ('black', 'white'), ('orange', 'pink')]
    Convert the said list of tuples to a list of strings:
    ['red green', 'black white', 'orange pink']
    Original list of tuples:
    [('Laiba', 'Delacruz'), ('Mali', 'Stacey', 'Drummond'), ('Raja', 'Welch'), ('Saarah', 'Stone')]
    Convert the said list of tuples to a list of strings:
    ['Laiba Delacruz', 'Mali Stacey Drummond', 'Raja Welch', 'Saarah Stone']
"""
def my_string(tup_lst):
    return [' '.join(tup) for tup in tup_lst]
print(my_string([('red', 'green'), ('black', 'white'), ('orange', 'pink')]))
print(my_string([('Laiba', 'Delacruz'), ('Mali', 'Stacey')]))  


"""188. Write a Python program to sort a given list of tuples by a specified element.
    Original list of tuples:
    [('item2', 10, 10.12), ('item3', 15, 25.1), ('item1', 11, 24.5), ('item4', 12, 22.5)]
    Sort on 1st element of the tuple of the said list:
    [('item1', 11, 24.5), ('item2', 10, 10.12), ('item3', 15, 25.1), ('item4', 12, 22.5)]
    Sort on 2nd element of the tuple of the said list:
    [('item2', 10, 10.12), ('item1', 11, 24.5), ('item4', 12, 22.5), ('item3', 15, 25.1)]
    Sort on 3rd element of the tuple of the said list:
    [('item2', 10, 10.12), ('item4', 12, 22.5), ('item1', 11, 24.5), ('item3', 15, 25.1)]
"""
def sort_lst(lst,n):
    return list(sorted(lst, key = lambda x:x[n]))
print(sort_lst([('item2', 10, 10.12), ('item3', 15, 25.1), ('item1', 11, 24.5), ('item4', 12, 22.5)], 0))
sort_lst = lambda lst, n: sorted(lst, key=lambda x: x[n])

"""189. Write a Python program to shift last element to first position and first element to last position in a given list.
    Original list:
    [1, 2, 3, 4, 5, 6, 7]
    Shift last element to first position and first element to last position of the said list:
    [7, 2, 3, 4, 5, 6, 1]
    Original list:
    ['s', 'd', 'f', 'd', 's', 's', 'd', 'f']
    Shift last element to first position and first element to last position of the said list:
    ['f', 'd', 'f', 'd', 's', 's', 'd', 's']
"""
def shift_elements(lst):
    """Shift last element to first position and first element to last position in a given list."""
    if len(lst) < 2:
        return lst
    return [lst[-1]] + lst[1:-1] + [lst[0]]
print(shift_elements([1, 2, 3, 4, 5, 6, 7]))

"""190. Write a Python program to find the specified number of largest products from two given lists,
    multiplying an element from each list.
    Original lists:
    [1, 2, 3, 4, 5, 6]
    [3, 6, 8, 9, 10, 6]
    3 Number of largest products from the said two lists:
    [60, 54, 50]
    4 Number of largest products from the said two lists:
    [60, 54, 50, 48]
"""
def largest_products(lst1, lst2, n):
    """Find the specified number of largest products from two given lists, multiplying an element from each list."""
    products = sorted([x * y for x in lst1 for y in lst2], reverse=True)
    return products[:n]
print(largest_products([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10, 6], 3))

"""191. Write a Python program to find the maximum and minimum values of the three given lists.
    Original lists:
    [2, 3, 5, 8, 7, 2, 3]
    [4, 3, 9, 0, 4, 3, 9]
    [2, 1, 5, 6, 5, 5, 4]
    Maximum value of the said three lists:
    9
    Minimum value of the said three lists:
    0
"""
def max_min_values(lst1, lst2, lst3):
    return max(max(lst1), max(lst2), max(lst3)), min(min(lst1), min(lst2), min(lst3))
print(max_min_values([2, 3, 5, 8, 7, 2, 3], [4, 3, 9, 0, 4, 3, 9], [2, 1, 5, 6, 5, 5, 4]))

def max_min_values(*args):
    return max([k for l in [*args] for k in l]), min([k for l in [*args] for k in l])
print(max_min_values([2, 3, 5, 8, 7, 2, 3], [4, 3, 9, 0, 4, 3, 9], [2, 1, 5, 6, 5, 5, 4]))

"""192. Write a Python program to remove all strings from a given list of tuples.
    Original list:
    [(100, 'Math'), (80, 'Math'), (90, 'Math'), (88, 'Science', 89), (90, 'Science', 92)]
    Remove all strings from the said list of tuples:
    [(100,), (80,), (90,), (88, 89), (90, 92)]
"""
def rem_str(lst):
    return [(k,) for x in lst for k in x if not isinstance(k, str)]
print(rem_str([(100, 'Math'), (80, 'Math'), (90, 'Math'), (88, 'Science', 89), (90, 'Science', 92)]))
# OR
def remove_strings_from_tuples(lst):
    """Remove all strings from a given list of tuples."""
    return [tuple(x for x in t if not isinstance(x, str)) for t in lst]

"""193. Write a Python program to find the dimension of a given matrix.
    Original list:
    [[1, 2], [2, 4]]
    Dimension of the said matrix:
    (2, 2)
    Original list:
    [[0, 1, 2], [2, 4, 5]]
    Dimension of the said matrix:
    (2, 3)
    Original list:
    [[0, 1, 2], [2, 4, 5], [2, 3, 4]]
    Dimension of the said matrix:
    (3, 3)
"""
def dim(lst):
    return (len(lst), len(lst[0]))
print(dim([[1, 2], [2, 4]]))

"""194. Write a Python program to sum two or more lists. The lengths of the lists may be different.
    Original list:
    [[1, 2, 4], [2, 4, 4], [1, 2]]
    Sum said lists with different lengths:
    [4, 8, 8]
    Original list:
    [[1], [2, 4, 4], [1, 2], [4]]
    Sum said lists with different lengths:
    [8, 6, 4]
"""
from itertools import zip_longest
def sum_lst(lst):
    return [sum(list(x)) for x in zip_longest(*lst, fillvalue=0)]
print(sum_lst([[1, 2, 4], [2, 4, 4], [1, 2]]))

"""195. Write a Python program to traverse a given list in reverse order,
and print the elements with the original index.
    Original list:
    ['red', 'green', 'white', 'black']
    Traverse the said list in reverse order:
    black
    white
    green
    red
    Traverse the said list in reverse order with original index:
    3 black
    2 white
    1 green
    0 red
"""
def traverse(lst):
    """Traverse a given list in reverse order and print the elements with the original index."""
    for i, val in enumerate(reversed(lst)):
        print(val)
    for i, val in enumerate(reversed(lst)):
        print(f"{len(lst) - 1 - i} {val}")

"""196. Write a Python program to move a specified element in a given list.
    Original list:
    ['red', 'green', 'white', 'black', 'orange']
    Move white at the end of the said list:
    ['red', 'green', 'black', 'orange', 'white']
    Original list:
    ['red', 'green', 'white', 'black', 'orange']
    Move red at the end of the said list:
    ['green', 'white', 'black', 'orange', 'red']
    Original list:
    ['red', 'green', 'white', 'black', 'orange']
    Move black at the end of the said list:
    ['red', 'green', 'white', 'orange', 'black']
"""
def remv(lst,  element):
    if element in lst:
        lst.remove(element)
        lst.append(element)
    else:
        print(f"{element} not found in the list.")
    return lst  
print(remv(['red', 'green', 'white', 'black', 'orange'], 'white'))
    
"""197. Write a Python program to compute the average of the n-th element in a given
list of lists with different lengths.
    Original list:
    [[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
    Average of n-th elements in the said list of lists with different lengths:
    [4.8, 5.8, 6.8, 8.0, 11.0]
"""
def compute_average(lst, n):
    """Compute the average of the n-th element in a given list of lists with different lengths."""
    total = 0
    count = 0
    for sublist in lst:
        if n < len(sublist):
            total += sublist[n]
            count += 1
    return total / count if count > 0 else None
print(compute_average([[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]], 2))

"""198. Write a Python program to compare two given lists and find the indices of the values present in both lists.
    Original lists:
    [1, 2, 3, 4, 5, 6]
    [7, 8, 5, 2, 10, 12]
    Compare said two lists and get the indices of the values present in both lists:
    [1, 4]
    Original lists:
    [1, 2, 3, 4, 15, 6]
    [7, 8, 5, 7, 10, 12]
    Compare said two lists and get the indices of the values present in both lists:
    []
"""
def compare_lists(lst1, lst2):
    common_element = set(lst1) & set(lst2)  # Find common elements
    indices = [i for i,value in enumerate(lst1) if value in common_element]
    return indices
print(compare_lists([1, 2, 3, 4, 5, 6], [7, 8, 5, 2, 10, 12]))

"""199. Write a Python program to convert a Unicode list to a list of strings.
    Original lists:
    ['S001', 'S002', 'S003', 'S004']
    Convert the said unicode list to a list contains strings:
    ['S001', 'S002', 'S003', 'S004']
"""
def unicode_to_string(lst):
    """Convert a Unicode list to a list of strings."""
    return [str(item) for item in lst]

"""200. Write a Python program to pair consecutive elements of a given list.
    Original lists:
    [1, 2, 3, 4, 5, 6]
    Pair up the consecutive elements of the said list:
    [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
    Original lists:
    [1, 2, 3, 4, 5]
    Pair up the consecutive elements of the said list:
    [[1, 2], [2, 3], [3, 4], [4, 5]]
"""
def pair_consecutive(lst):
    for i in enumerate(lst):
        if i[0] < len(lst) - 1:
            yield [lst[i[0]], lst[i[0] + 1]]    
print(pair_consecutive([1, 2, 3, 4, 5, 6]))

def pair_consecutive(lst):
    result = []
    for i in range(len(lst) - 1):
        result.append([lst[i], lst[i + 1]])
    return result
print(pair_consecutive([1, 2, 3, 4, 5, 6]))

"""201. Write a Python program to check if a given string contains an element that is present in a list.
    The original string and list:
    https://www.w3resource.com/python-exercises/list/
    ['.com', '.edu', '.tv']
    Check if https://www.w3resource.com/python-exercises/list/ contains an element, which is present in the list ['.com', '.edu', '.tv']
    True
    The original string and list: https://www.w3resource.net
    https://www.w3resource.net
    ['.com', '.edu', '.tv']
    Check if https://www.w3resource.net contains an element, which is present in the list ['.com', '.edu', '.tv']
    False
"""
def check_element(str, lst):
    """Check if a given string contains an element that is present in a list."""
    return any(substring in str for substring in lst)
print(check_element('https://www.w3resource.com/python-exercises/list/', ['.com', '.edu', '.tv']))

"""202. Write a Python program to find the indexes of all None items in a given list.
    Original list:
    [1, None, 5, 4, None, 0, None, None]
    Indexes of all None items of the list:
    [1, 4, 6, 7]
"""
def none_indexes(lst):
    return [i for i, val in enumerate(lst) if val is None]
print(none_indexes([1, None, 5, 4, None, 0, None, None]))
# 2nd method
def find_index(lst):
    return [i for i in range(len(lst)) if lst[i] is None]
print(find_index([1, None, 5, 4, None, 0, None, None]))

"""203. Write a Python program to join adjacent members of a given list.
    Original list:
    ['1', '2', '3', '4', '5', '6', '7', '8']
    Join adjacent members of a given list:
    ['12', '34', '56', '78']
    Original list:
    ['1', '2', '3']
    Join adjacent members of a given list:
    ['12']
"""
def join_adj(lst):
    return [lst[i] + lst[i+1] for i in range(0, len(lst)-1, 2)]
print(join_adj(['1', '2', '3', '4', '5', '6', '7', '8']))
print(join_adj(['1', '2', '3']))

"""204. Write a Python program to check if the first digit or character of each element in a list is the same.
    Original list:
    [1234, 122, 1984, 19372, 100]
    Check if first digit in each element of the said given list is same or not!
    True
    Original list:
    [1234, 922, 1984, 19372, 100]
    Check if first digit in each element of the said given list is same or not!
    False
    Original list:
    ['aabc', 'abc', 'ab', 'a']
    Check if first character in each element of the said given list is same or not!
    True
"""
def chack_first(lst):
    first_elem = str(lst[0])[0]
    return all(str(item)[0] == first_elem for item in lst)
print(chack_first([1234, 122, 1984, 19372, 100]))
"""205. Write a Python program to find the indices of elements in a given list that are greater than a specified value.
    Original list:
    [1234, 1522, 1984, 19372, 1000, 2342, 7626]
    Indices of elements of the said list, greater than 3000
    [3, 6]
    Original list:
    [1234, 1522, 1984, 19372, 1000, 2342, 7626]
    Indices of elements of the said list, greater than 20000
    []
"""
def indices(lst, num):
    for i, value in enumerate(lst):
        if value > num:
            yield i
print(list(indices([1234, 1522, 1984, 19372, 1000, 2342, 7626], 3000)))
# 2nd method
def find_indices_greater_than(lst, threshold):
    return [i for i, value in enumerate(lst) if value > threshold]
print(find_indices_greater_than([1234, 1522, 1984, 19372, 1000, 2342, 7626], 3000))

"""206. Write a Python program to remove additional spaces from a given list.
    Original list:
    ['abc ', ' ', ' ', 'sdfds ', ' ', ' ', 'sdfds ', 'huy']
    Remove additional spaces from the said list:
    ['abc', '', '', 'sdfds', '', '', 'sdfds', 'huy']
"""
def remove_spaces(lst):
    return [item.strip() for item in lst]
print(remove_spaces(['abc ', ' ', ' ', 'sdfds ', ' ', ' ', 'sdfds ', 'huy']))

"""207. Write a Python program to find the common tuples between two given lists.
    Original lists:
    [('red', 'green'), ('black', 'white'), ('orange', 'pink')]
    [('red', 'green'), ('orange', 'pink')]
    Common tuples between two said lists
    [('orange', 'pink'), ('red', 'green')]
    Original lists:
    [('red', 'green'), ('orange', 'pink')]
    [('red', 'green'), ('black', 'white'), ('orange', 'pink')]
    Common tuples between two said lists
    [('orange', 'pink'), ('red', 'green')]
"""
def common_tuples(lst1, lst2):
    return list(set(lst1) & set(lst2))
print(common_tuples([('red', 'green'), ('black', 'white'), ('orange', 'pink')], [('red', 'green'), ('orange', 'pink')]))
# 2nd method
def find_common_tuples(lst1, lst2):
    return [tup for tup in lst1 if tup in lst2]
print(find_common_tuples([('red', 'green'), ('black', 'white'), ('orange', 'pink')], [('red', 'green'), ('orange', 'pink')]))

"""208. Sum a list of numbers. Write a Python program to sum the first number with the second
and divide it by 2, then sum the second with the third and divide by 2, and so on.
    Original list:
    [1, 2, 3, 4, 5, 6, 7]
    Sum the said list of numbers:
    [1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
    Original list:
    [0, 1, -3, 3, 7, -5, 6, 7, 11]
    Sum the said list of numbers:
    [0.5, -1.0, 0.0, 5.0, 1.0, 0.5, 6.5, 9.0]
"""
def summatn(lst):
    return [(lst[i] + lst[i+1]) / 2 for i in range(len(lst)-1)]
print(summatn([1, 2, 3, 4, 5, 6, 7]))

"""209. Write a Python program to count the number of groups of non-zero numbers separated by zeros in a given list of numbers.
    Original list:
    [3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 5, 9, 9, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1]
    Number of groups of non-zero numbers separated by zeros of the said list: 4
"""
def count_non_zero_groups(lst):
    return [len([group for group in ''.join(['1' if num != 0 else '0' for num in lst]).split('0') if group]) for group in ''.join(['1' if num != 0 else '0' for num in lst]).split('0') if group][0]
# 2nd method
def count_non_zero_groups(lst):
    count = 0
    in_group = False
    for num in lst:
        if num != 0 and not in_group:
            count += 1
            in_group = True
        elif num == 0:
            in_group = False
    return count
print(count_non_zero_groups([3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 5, 9, 9, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1]))
# 3rd method
def count_non_zero_groups(lst):
    count = 0
    i = 0
    while i < len(lst):
        if lst[i] != 0:
            count += 1
            while i < len(lst) and lst[i] != 0:
                i += 1
        i += 1
    return count
print(count_non_zero_groups([3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 5, 9, 9, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1]))   

"""210. Write a Python program to compute the sum of non-zero groups (separated by zeros) of a given list of numbers.
    Original list:
    [3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1, 0, 0, 0]
    Compute the sum of non-zero groups (separated by zeros) of the said list of numbers: [15, 38, 15, 27]
"""



"""211. Write a Python program to remove an element from a given list.
    Original list:
    ['Ricky Rivera', 98, 'Math', 90, 'Science']
    After deleting an element:, using index of the element: [98, 'Math', 90, 'Science']
"""
"""212. Write a Python program to remove all values except integer values from a given array of mixed values.
    Original list: [34.67, 12, -94.89, 'Python', 0, 'C#']
    After removing all the values except integer values from the said array of mixed values: [12, 0]
"""
"""213. Write a Python program to calculate the sum of two lowest negative numbers in a given array of integers.
    An integer (from the Latin integer meaning "whole") is colloquially defined as a number that can be written without a fractional component. For example, 21, 4, 0, and -2048 are integers.
    Original list elements: [-14, 15, -10, -11, -12, -13, 16, 17, 18, 19, 20]
    Sum of two lowest negative numbers of the said array of integers: -27
    Original list elements: [-4, 5, -2, 0, 3, -1, 4, 9]
    Sum of two lowest negative numbers of the said array of integers: -6
"""
"""214. Write a Python program to sort a given positive number in descending/ascending order.
    Descending -> Highest to lowest.
    Ascending -> Lowest to highest
    Original Number: 134543
    Descending order of the said number: 544331
    Ascending order of the said number: 133445
    Original Number: 43750973
    Descending order of the said number: 97754330
    Ascending order of the said number: 3345779
"""
"""215. Write a Python program to merge two or more lists into a list of lists, combining elements from each of the input lists based on their positions.
    Sample Output:
    After merging lists into a list of lists:
    [['a', 1, True], ['b', 2, False]]
    [['a', 1, True], [None, 2, False]]
    [['a', 1, True], ['_', 2, False]]
"""
"""216. Write a Python program to group the elements of a list based on the given function and return the count of elements in each group.
    Sample Output:
    {6: 2, 4: 1}
    {3: 2, 5: 1}
"""
"""217. Write a Python program to split values into two groups, based on the result of the given filtering function.
    Sample Output:
    [['white'], ['red', 'green', 'black']]
"""
"""218. Write a Python program to sort one list based on another list containing the desired indexes.
    Sample Output:
    ['apples', 'bread', 'eggs', 'jam', 'milk', 'oranges']
    ['oranges', 'milk', 'jam', 'eggs', 'bread', 'apples']
"""
"""219. Write a Python program to build a list, using an iterator function and an initial seed value.
    Sample Output:
    [-10, -20, -30, -40]
"""
"""220. Write a Python program to map the values of a list to a dictionary using a function, where the key-value pairs consist of the original value as the key and the result of the function as the value.
    Sample Output:
    {1: 1, 2: 4, 3: 9]
"""
"""221. Write a Python program to randomize the order of the values of a list, returning a new list.
    Sample Output:
    Original list: [1, 2, 3, 4, 5, 6]
    Shuffle the elements of the said list:
    [3, 2, 4, 1, 6, 5]
"""
"""222. Write a Python program to get the difference between two given lists, after applying the provided function to each list element of both.
    Sample Output:
    [1.2]
    [{'x': 2}]
"""
"""223. Write a Python program to create a list with non-unique values filtered out.
    Sample Output:
    [1, 3, 5]
"""
"""224. Write a Python program to create a list with unique values filtered out.
    Sample Output:
    [2, 4]
"""
"""225. Write a Python program to retrieve the value of the nested key indicated by the given selector list from a dictionary or list.
    Sample Output:
    Harwood
    2
"""
"""226. Write a Python program to get a list of elements that exist in both lists, after applying the provided function to each list element of both.
    Sample Output:
    [2.1]
"""
"""227. Write a Python program to get the symmetric difference between two lists, after applying the provided function to each list element of both.
    Sample Output:
    [1.2, 3.4]
"""
"""228. Write a Python program to get every element that exists in any of the two given lists once, after applying the provided function to each element of both.
    Sample Output:
    [2.2, 4.1]
"""
"""229. Write a Python program to find the index of the first element in the given list that satisfies the provided testing function.
    Sample Output:
    0
"""
"""230. Write a Python program to find the indexes of all elements in the given list that satisfy the provided testing function.
    Sample Output:
    [0, 2]
"""
"""231. Write a Python program to split values into two groups, based on the result of the given filter list.
    Sample Output:
    [['red', 'green', 'pink'], ['blue']]
"""
"""232. Write a Python program to chunk a given list into smaller lists of a specified size.
    Sample Output:
    [[1, 2, 3], [4, 5, 6], [7, 8]]
"""
"""233. Write a Python program to chunk a given list into n smaller lists.
    Sample Output:
    [[1, 2], [3, 4], [5, 6], [7]]
"""
"""234. Write a Python program to convert a given number (integer) to a list of digits.
    Sample Output:
    [1, 2, 3]
    [1, 3, 4, 7, 8, 2, 3]
"""
"""235. Write a Python program to find the index of the last element in the given list that satisfies the provided testing function.
    Sample Output:
    2
"""
"""236. Write a Python program to find items that are parity outliers in a given list.
    Sample Output:
    [1, 3]
    [2, 4, 6]
"""
"""237. Write a Python program to convert a given list of dictionaries into a list of values corresponding to the specified key.
    Sample Output:
    [8, 36, 34, 10]
"""
"""238. Write a Python program to calculate the average of a given list, after mapping each element to a value using the provided function.
    Sample Output:
    5.0
    15.0
"""
"""239. Write a Python program to find the value of the first element in the given list that satisfies the provided testing function.
    Sample Output:
    1
    2
"""
"""240. Write a Python program to find the value of the last element in the given list that satisfies the provided testing function.
    Sample Output:
    3
    4
"""
"""241. Write a Python program to create a dictionary with the unique values of a given list as keys and their frequencies as values.
    Sample Output:
    {'a': 4, 'b': 2, 'f': 2, 'c': 1, 'e': 2}
    {3: 4, 4: 2, 7: 1, 5: 2, 9: 1, 0: 1, 2: 1}
"""
"""242. Write a Python program to get the symmetric difference between two iterables, without filtering out duplicate values.
    Sample Output:
    [30, 40]
"""
"""243. Write a Python program to check if a given function returns True for every element in a list.
    Sample Output:
    True
    False
    False
"""
"""244. Write a Python program to initialize a list containing the numbers in the specified range where start and end are inclusive and the ratio between two terms is step. Return an error if step equals 1.
    Sample Output:
    [1, 2, 4, 8, 16, 32, 64, 128, 256]
    [3, 6, 12, 24, 48, 96, 192]
    [1, 4, 16, 64, 256]
"""
"""245. Write a Python program that takes any number of iterable objects or objects with a length property and returns the longest one.
    Sample Output:
    Green
    [1, 2, 3, 4, 5]
    [1, 2, 3, 4]
"""
"""246. Write a Python program to check if a given function returns True for at least one element in the list.
    Sample Output:
    True
    False
"""
"""247. Write a Python program to calculate the difference between two iterables, without filtering duplicate values.
    Sample Output:
    [3]
"""
"""248. Write a Python program to get the maximum value of a list, after mapping each element to a value using a given function.
    Sample Output:
    8
"""
"""249. Write a Python program to get the minimum value of a list, after mapping each element to a value using a given function.
    Sample Output:
    2
"""
"""250. Write a Python program to calculate the sum of a list, after mapping each element to a value using the provided function.
    Sample Output:
    20
"""
"""251. Write a Python program that fills a list with the specified value.
    Sample Output:
    [0, 0, 0, 0, 0, 0, 0]
    [3, 3, 3, 3, 3, 3, 3, 3]
    [-2, -2, -2, -2, -2]
    [3.2, 3.2, 3.2, 3.2, 3.2]
"""
"""252. Write a Python program to get the n maximum elements from a given list of numbers.
    Sample Output:
    Original list elements:
    [1, 2, 3]
    Maximum values of the said list: [3]
    Original list elements:
    [1, 2, 3]
    Two maximum values of the said list: [3, 2]
    Original list elements:
    [-2, -3, -1, -2, -4, 0, -5]
    Threee maximum values of the said list: [0, -1, -2]
    Original list elements:
    [2.2, 2, 3.2, 4.5, 4.6, 5.2, 2.9]
    Two maximum values of the said list: [5.2, 4.6]
"""
"""253. Write a Python program to get the n minimum elements from a given list of numbers.
    Sample Output:
    Original list elements:
    [1, 2, 3]
    Minimum values of the said list: [1]
    Original list elements:
    [1, 2, 3]
    Two minimum values of the said list: [1, 2]
    Original list elements:
    [-2, -3, -1, -2, -4, 0, -5]
    Threee minimum values of the said list: [-5, -4, -3]
    Original list elements:
    [2.2, 2, 3.2, 4.5, 4.6, 5.2, 2.9]
    Two minimum values of the said list: [2, 2.2]
"""
"""254. Write a Python program to get the weighted average of two or more numbers.
    Sample Output:
    Original list elements:
    [10, 50, 40]
    [2, 5, 3]
    Weighted average of the said two list of numbers:
    39.0
    Original list elements:
    [82, 90, 76, 83]
    [0.2, 0.35, 0.45, 32]
    Weighted average of the said two list of numbers:
    82.97272727272727
"""
"""255. Write a Python program to perform a deep flattening of a list.
    Sample Output:
    Original list elements:
    [1, [2], [[3], [4], 5], 6]
    Deep flatten the said list:
    [1, 2, 3, 4, 5, 6]
    Original list elements:
    [[[1, 2, 3], [4, 5]], 6]
    Deep flatten the said list:
    [1, 2, 3, 4, 5, 6]
"""
"""256. Write a Python program to get the powerset of a given iterable.
    Sample Output:
    Original list elements:
    [1, 2]
    Powerset of the said list:
    [(), (1,), (2,), (1, 2)]
    Original list elements:
    [1, 2, 3, 4]
    Powerset of the said list:
    [(), (1,), (2,), (3,), (4,), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4), (1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4), (1, 2, 3, 4)]
"""
"""257. Write a Python program to check if two given lists contain the same elements regardless of order.
    Sample Output:
    Original list elements:
    [1, 2, 4]
    [2, 4, 1]
    Check two said lists contain the same elements regardless of order!
    True
    Original list elements:
    [1, 2, 3]
    [1, 2, 3]
    Check two said lists contain the same elements regardless of order!
    True
    Original list elements:
    [1, 2, 3]
    [1, 2, 4]
    Check two said lists contain the same elements regardless of order!
    False
"""
"""258. Write a Python program to create a flat list of all the keys in a flat dictionary.
    Sample Output:
    Original directory elements:
    {'Laura': 10, 'Spencer': 11, 'Bridget': 9, 'Howard ': 10}
    Flat list of all the keys of the said dictionary:
    ['Laura', 'Spencer', 'Bridget', 'Howard ']
"""
"""259. Write a Python program to check if a given function returns True for at least one element in the list.
    Sample Output:
    False
    True
    False
"""
"""260. Write a Python program to check if all the elements of a list are included in another given list.
    Sample Output:
    True
    False
"""
"""261. Write a Python program to get the most frequent element in a given list of numbers.
    Sample Output:
    2
    Original list:
    [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]
    Item with maximum frequency of the said list:
    2
    Original list:
    [1, 2, 3, 1, 2, 3, 2, 1, 4, 3, 3]
    Item with maximum frequency of the said list:
    3
"""
"""262. Write a Python program to move the specified number of elements to the end of the given list.
    Sample Output:
    [4, 5, 6, 7, 8, 1, 2, 3]
    [6, 7, 8, 1, 2, 3, 4, 5]
    [1, 2, 3, 4, 5, 6, 7, 8]
    [1, 2, 3, 4, 5, 6, 7, 8]
    [8, 1, 2, 3, 4, 5, 6, 7]
    [2, 3, 4, 5, 6, 7, 8, 1]
"""
"""263. Write a Python program to move the specified number of elements to the start of the given list.
    Sample Output:
    [4, 5, 6, 7, 8, 1, 2, 3]
    [6, 7, 8, 1, 2, 3, 4, 5]
    [1, 2, 3, 4, 5, 6, 7, 8]
    [1, 2, 3, 4, 5, 6, 7, 8]
    [8, 1, 2, 3, 4, 5, 6, 7]
    [2, 3, 4, 5, 6, 7, 8, 1]
"""
"""264. Write a Python program to create a two-dimensional list from a given list of lists.
    Sample Output:
    [(1, 4, 7, 10), (2, 5, 8, 11), (3, 6, 9, 12)]
    [(1, 4), (2, 5)]
"""
"""265. Write a Python program to generate a list containing the Fibonacci sequence, up until the nth term.
    Sample Output:
    First 7 Fibonacci numbers:
    [0, 1, 1, 2, 3, 5, 8, 13]
    First 15 Fibonacci numbers:
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    First 50 Fibonacci numbers:
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025]
"""
"""266. Write a Python program to cast the provided value as a list if it's not one.
    Sample Output:
    <class 'list'>
    [1]
    <class 'tuple'>
    ['Red', 'Green']
    <class 'set'>
    ['Green', 'Red']
    <class 'dict'>
    [1, 2, 3]
"""
"""267. Write a Python program to get the cumulative sum of the elements of a given list.
    Sample Output:
    Original list elements:
    [1, 2, 3, 4]
    Cumulative sum of the elements of the said list:
    [1, 3, 6, 10]
    Original list elements:
    [-1, -2, -3, 4]
    Cumulative sum of the elements of the said list:
    [-1, -3, -6, -2]
"""
"""268. Write a Python program to get a list with n elements removed from the left and right.
    Sample Output:
    Original list elements:
    [1, 2, 3]
    Remove 1 element from left of the said list:
    [2, 3]
    Remove 1 element from right of the said list:
    [1, 2]
    Original list elements:
    [1, 2, 3, 4]
    Remove 2 elements from left of the said list:
    [3, 4]
    Remove 2 elements from right of the said list:
    [1, 2]
    Original list elements:
    [1, 2, 3, 4, 5, 6]
    Remove 7 elements from left of the said list:
    [2, 3, 4, 5, 6]
    Remove 7 elements from right of the said list:
    [1, 2, 3, 4, 5]
"""
"""269. Write a Python program to get every nth element in a given list.
    Sample Output:
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    [2, 4, 6, 8, 10]
    [5, 10]
    [6]
"""
"""270. Write a Python program to check if the elements of the first list are contained in the second one regardless of order.
    Sample Output:
    True
    True
    False
    True
"""
"""271. Write a Python program to check if there are duplicate values in a given flat list.
    Sample Output:
    Original list:
    [1, 2, 3, 4, 5, 6, 7]
    Check if there are duplicate values in the said given flat list:
    False
    Original list:
    [1, 2, 3, 3, 4, 5, 5, 6, 7]
    Check if there are duplicate values in the said given flat list:
    True
"""
"""272. Write a Python program to generate a list of numbers in the arithmetic progression starting with the given positive integer and up to the specified limit.
    Sample Output:
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
    [5, 10, 15, 20, 25]
"""
"""273. Write a Python program to find an element that divides a given list of integers with the same sum value.
    Sample Output:
    Original list:
    [0, 9, 2, 4, 5, 6]
    Element that devides the said list of integers with the same sum value:
    4
    Original list:
    [-4, 0, 6, 1, 0, 2]
    Element that devides the said list of integers with the same sum value:
    1
    Original list:
    [1, 2, 3, 4]
    Element that devides the said list of integers with the same sum value:
    No such element!
    Original list:
    [-4, 0, 5, 1, 0, 1]
    Element that devides the said list of integers with the same sum value:
    1
"""
"""274. Write a Python program to count the lowercase letters in a given list of words.
    Sample Data:
    (["Red", "Green", "Blue", "White"]) -> 13
    (["SQL", "C++", "C"]) -> 0
"""
"""275. Write a Python program to add all elements of a list of integers except the number at index. Return the updated string.
    Sample Data:
    ([0, 9, 2, 4, 5, 6] -> [26, 17, 24, 22, 21, 20]
    ([-4, 0, 6, 1, 0, 2]) -> [9, 5, -1, 4, 5, 3]
    ([1, 2, 3]) -> [5, 4, 3]
    ([-4, 0, 5, 1, 0, 1]) -> [7, 3, -2, 2, 3, 2]
"""
"""276. Write a Python program to find the largest odd number in a given list of integers.
    Sample Data:
    ([0, 9, 2, 4, 5, 6]) -> 9
    ([-4, 0, 6, 1, 0, 2]) -> 1
    ([1, 2, 3]) -> 3
    ([-4, 0, 5, 1, 0, 1]) -> 5
"""
"""277. Write a Python program to calculate the largest and smallest gap between sorted elements of a list of integers.
    Sample Data:
    {1, 2 ,9, 0, 4, 6} -> 3
    {23, -2, 45, 38, 12, 4, 6} -> 15
"""
"""278. Write a Python program to sum the missing numbers in a given list of integers.
    Sample Data:
    ([0, 3, 4, 7, 9]) -> 22
    ([44, 45, 48]) -> 93
    ([-7, -5, -4, 0]) -> -12
"""
"""279. Write a Python program to extract the first specified number of vowels from a given string. If the specified number is less than the number of vowels present in the string then display "n is less than the number of vowels present in the string".
    Sample Data:
    ("Python", 2) -> "n is less than number of vowels present in the string."
    ("Python Exercises", 3) -> "oEe"
    ("aeiou") -> "AEI"
"""
"""280. Write a Python program that takes a list of integers and finds all pairs of integers that differ by three. Return all pairs of integers in a list.
    Sample Data:
    ([0, 3, 4, 7, 9]) -> [[0, 3], [4, 7]]
    [0, -3, -5, -7, -8] -> [[-3, 0], [-8, -5]]
    ([1, 2, 3, 4, 5]) -> [[1, 4], [2, 5]]
    ([100, 102, 103, 114, 115]) -> [[100, 103]]
"""
