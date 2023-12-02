"""
#* Note : In a list or generator comprehension, the order of the loops is from left to right. 
# This means that the outer loop is specified first, followed by any inner loops. The comprehension is read in the same order.

#* Here's a general structure:
result = [expression for outer_loop in outer_iterable for inner_loop in inner_iterable]
"""

####################################################################
######################################################## (Function)
####################################################################

####################################################################
########### Question : (Add the Values of the Symbols in a Matrix)
"""
Task: Write a function that takes a list of lists and returns the value of all of the symbols in it,
where each symbol adds or takes something from the total score. Symbol values:
"""
# 1st method
from ctypes import *
import codecs
def check_score(s):
    symbol_values = {'#': 5, 'O': 3, 'X': 1, '!': -1, '!!': -3, '!!!': -5}
    total_score = 0
    for k in s:
        for symbol in k:
            total_score = total_score + symbol_values.get(symbol, 0)
    return max(total_score, 0)


# 2nd method
def check_score(s):
    total_score = 0
    for k in s:
        for symbol in k:
            if symbol == "#":
                total_score += 5
            elif symbol == "O":
                total_score += 3
            elif symbol == "X":
                total_score += 1
            elif symbol == "!":
                total_score -= 1
            elif symbol == "!!":
                total_score -= 3
            elif symbol == "!!!":
                total_score -= 5
    return max(total_score, 0)

# 3rd method
def check_score(s):
    symbol_values = {'#': 5, 'O': 3, 'X': 1, '!': -1, '!!': -3, '!!!': -5}
    total_score = sum(symbol_values.get(symbol, 0) for k in s for symbol in k)
    return max(total_score, 0)


# List all names in the ctypes module
print(dir())


####################################################################
################################# Question : (Magic Function)
"""
Task : Create a class with a few functions like these examples.
magic.replace("string", 'char', char') is a function that replaces all of the specified characters with different specified characters.
magic.str_length("string") is a function that returns the length of the string.
magic.trim(" string ") is a function that returns a string with truncated spaces at both the beginning and end.
magic.list_slice(list, tuple) is a function that returns the items in the list that are between the specified indexes. If the length of the new list is 0, return -1.
"""
# 1st method
class Magic:
    def replace(self, my_str, replace_it, replace_with):
        return my_str.replace(replace_it, replace_with)

    def str_length(self, my_str):
        return len(my_str)

    def trim(self, my_str):
        return my_str.strip()

    def list_slice(self, my_lst, my_tup):
        return my_lst[my_tup[0]-1:my_tup[1]]

# 2nd method
class Magic:
    def replace(self, my_str, replace_it, replace_with): return my_str.replace(
        replace_it, replace_with)

    def str_length(self, my_str): return len(my_str)
    def trim(self, my_str): return my_str.strip()
    def str_length(self, my_str): return len(my_str)
    def list_slice(self, my_lst, my_tup): return my_lst[my_tup[0]-1:my_tup[1]]


#######################################################################
############################## Question : (How Many Unique Styles?)
""" 
Task : There are many different styles of music and many albums exhibit multiple styles.
Create a function that takes a list of musical styles from albums and returns how many styles are unique.
"""
# 1st method
def unique_styles(albums):
    result = set(style.strip() for album in albums for style in album.split(","))
    return len(result)

# 2nd method
def unique_styles(albums):
    my_list = []
    for album in albums:
        for style in album.split(","):
            my_list.append(style)
        return len(set(my_list))

# 3rd method
def unique_styles(albums):
    return len(set(','.join(albums).split(',')))


########################################################################
########################### Question : (Oddly or Evenly Positioned)
"""
Task : Create a function that returns the characters from a list or string r on odd or even positions, depending on the specifier s.
The specifier will be "odd" for items on odd positions (1, 3, 5, ...) and "even" for items on even positions (2, 4, 6, ...).
# char_at_pos([2, 4, 6, 8, 10], "even") ➞ [4, 8]
# 4 & 8 occupy the 2nd & 4th positions
"""

# 1st method
def char_at_pos(r, s):
    def result(r, s): return r[::2] if s == "odd" else r[1::2]
    return result
# Note : assigning it to the variable result not actually call the lambda function with the provided arguments r and s it's retruning function

# So correct version


def char_at_pos(r, s):
    def result(r, s): return r[::2] if s == "odd" else r[1::2]
    return result(r, s)

# 2nd method
def char_at_pos(sequence, specifier):
    if specifier not in ["odd", "even"]:
        raise ValueError("Specifier must be 'odd' or 'even'")
    if specifier == "odd":
        return sequence[::2]
    elif specifier == "even":
        return sequence[1::2]


####################################################################
#################################### Question : (Reorder Digits)
"""
Task : Create a function that reorders the digits of each numerical element in a list based on ascending (asc) or descending (desc) order.
reorder_digits([515, 341, 98, 44, 211], "asc") ➞ [155, 134, 89, 44, 112]
"""
# 1st method using lambda and sorted
def reorder_digits(lst, direction):
    def result(lst, direction): return sort()
        lst, key=lambda k: lst[k]) if direction == 'asc' else lst.sort(key=lambda k: lst[k])[::-1]
# wrong


def reorder_digits(lst, direction):
    def result(lst, direction): return sorted(lst, key=lambda k: int(''.join(sorted(
        str(k)))) if direction == 'asc' else int(''.join(sorted(str(k), reverse=True))))

# OR using map with custom function
def reorder_digits(lst, direction):
    def reorder_num(k, order):
        if order == 'asc':
            return int(''.join(sorted(str(k))))
        elif order == 'desc':
            return int(''.join(sorted(str(k), reverse=True)))

    return list(map(lambda x: reorder_num(x, direction), lst))


# 2nd method Using sort method
def reorder_digits(lst, direction):
    def reorder_num(k, order):
        digits = [int(digit) for digit in str(k)]

        digits.sort() if order == "asc" else digits.sort(reverse=True)

        reordered_num = int(''.join(map(str, digits)))
        return reordered_num

    reordered_list = [reorder_num(k, direction) for k in lst]
    return reordered_list

# 3rd method
def reorder_digits(lst, direction):
    def reorder_num(k, order):
        if order == 'asc':
            return int(''.join(sorted(str(k))))
        elif order == 'desc':
            return int(''.join(sorted(str(k), reverse=True)))
        else:
            return k

    reordered_list = [reorder_num(k, direction) for k in lst]
    return reordered_list


# 4th method
def reorder_digits(lst, direction):
    return [int(''.join(sorted(list(str(i)), reverse=True))) if direction == "desc" else int(''.join(sorted(list(str(i))))) for i in lst]

# Or
def reorder_digits(lst, direction):
    return [int(''.join(sorted(str(lst[x]), reverse=direction == "desc"))) for x in range(len(lst))]

# 5th method
def reorder_digits(lst, direction):
    return [f(k, direction) for k in lst]

def f(x, d):
    s = ''.join(sorted(str(x)))
    if d == 'desc':
        s = s[::-1]
    return int(s)

# 6th method
def reorder_digits(lst, direction):
    x = True if direction == 'desc' else False
    return [int(''.join(sorted([char for char in str(num)], reverse=x))) for num in lst]


# 7th method
def reorder_digits(lst, direction):
    if direction == "asc":
        return [order(l, False) for l in lst]
    else:
        return [order(l, True) for l in lst]


def order(num, dir):
    return int("".join(sorted(list(str(num)), reverse=dir)))

# 8th method
def reorder_digits(lst, direction):
    new_lst = []
    for i in lst:
        num = ''.join(sorted(str(i)))
        if direction == 'asc':
            new_lst.append(int(num))
        else:
            new_lst.append(int(num[::-1]))
    return new_lst

# 9th method
def reorder_digits(lst, direction):
    return [int(y) for y in [''.join(sorted(str(x), reverse=direction == 'desc')) for x in lst]]

# 10th method
def reorder_digits(lst, direction):
    return [int("".join(sorted(list(str(num)), reverse={"asc": False, "desc": True}[direction]))) for num in lst]


###############################################################
####################### Question #*(Needle in a Hex String)
"""
#* Key Concept 
Hexadecimal is a base-16 numeral system that uses 16 symbols (0-9 and A-F) to represent values : -
"""
# * Encoding (String or Digit to Hex): -

# 1. Encoding a String to Hex:
string_to_encode = "Hello, World!"
hex_encoded_string = string_to_encode.encode('utf-8').hex()
print(hex_encoded_string)  # Output : 48656c6c6f2c20576f726c6421

# 2. Encoding a Digit to Hex:
digit_to_encode = 42
hex_encoded_digit = hex(digit_to_encode)
print(hex_encoded_digit)  # Output : 0x2a

# * Decoding (Hex to String or Digit):-

# 1. Decoding Hex to a String:
# Hex representation of "Hello, World!"
hex_to_decode = "48656c6c6f2c20576f726c6421"
decoded_string = bytes.fromhex(hex_to_decode).decode('utf-8')
print(decoded_string)  # Output : Hello, World!

# 2. Decoding Hex to a Digit:
hex_to_decode_digit = "2a"  # Hex representation of the digit 42
decoded_digit = int(hex_to_decode_digit, 16)
print(decoded_digit)

# chr() function: - The chr() function in Python is used to convert an ASCII code into its corresponding character.
# ord() function: - The ord() function in Python is used to get the ASCII code of a character.


"""
Task : 
Find the index of a string within a hex encoded string.
You will be given a string which needs to be found in another string which has previously been translated into hex.
You will need to return the first index of the needle within the hex encoded string.
"""
# 1st method
def first_index(hex_text, needle):
    # Split the hex text into a list of individual hex values
    hex_values = hex_text.split()
    # Convert hex values to integers
    ascii_characters = [int(hex_value, 16) for hex_value in hex_values]
    # Convert integers to characters
    decoded_string = ''.join(chr(char) for char in ascii_characters)
    # Find the index of the needle in the decoded string
    index = decoded_string.find(needle)
    return index

# 2nd method
def first_index(hex_txt, needle):
    return ''.join(chr(int(i, 16)) for i in hex_txt.split()).index(needle)

# 3rd method
def first_index(hex_txt, needle):
    return bytearray.fromhex(hex_txt).decode('ISO-8859-1').index(needle)

# 4th method
def first_index(hex_txt, needle):
    n = hex(ord(needle[0]))[2:]
    return hex_txt.split().index(n)

# 5th method
def first_index(hex_txt, needle):
    for c in hex_txt.split():
        if chr(int(c, 16)) == needle[0]:
            return hex_txt.split().index(c)

# 6th method
def first_index(hex_txt, needle):
    ch1 = format(ord(needle[0]), "x")
    l = hex_txt.split(" ")
    return (l.index(ch1))


# 7th method
def first_index(hex_txt, needle):
    n = codecs.encode(needle.encode(encoding="utf-8"), 'hex')
    for ind, i in enumerate(hex_txt.split()):
        if i == str(n)[2:4]:
            return ind

# 8th method
def first_index(hex_val, needle):
    bytes_arr = bytearray.fromhex(hex_val)
    decoded = bytes_arr.decode(errors='replace')
    return decoded.find(needle)


"""
n the context of hexadecimal (base-16) notation, 0x3F represents a number. 
The 0x prefix is used to denote that the following characters are in hexadecimal format.
Breaking down 0x3F:

0x: Indicates that the number is in hexadecimal notation.
3: Represents the value of 3 in hexadecimal.
F: Represents the value of 15 in hexadecimal.

"""

######################################################################
################ Question #*(Get Students with Names and Top Notes II)
"""
Task : Create a function that takes a list of dictionaries like [{ "name": "John", "notes": [3, 5, 4]}, 
{ "name": "Mich", "notes": [1, 3, 5]}] and returns a list of dictionaries like [{ "name": "John", "top_note": 5 }, 
{"name": "Mich", "top_note": 5}]. If a student has no notes (an empty list), return top_note: 0.
"""

# 1st method
def get_name_and_top_note(students):
    my_list = []
    for d in students:
        my_dict = {}
        for k, v in d.items():
            if k != 'notes':
                my_dict[k] = v
            elif k == 'notes' and len(v) > 0:
                my_dict['top_note'] = max(v)
            else:
                my_dict['top_note'] = 0
        my_list.append(my_dict)
    return my_list

# Or
def get_name_and_top_note(students):
    my_list = []
    for d in students:
        my_list.append({'name': d['name'], 'top_note': max(d['notes']) if d['notes'] else 0})
    return my_list


# 2nd method
def get_name_and_top_note(students):
    for s in students:
        s['top_note'] = max(s['notes'] + [0])
        s.pop('notes')
    return students

# Or
def get_name_and_top_note(students):
    return [{'name': x['name'], 'top_note': max(x['notes'], default=0)} for x in students]

# Or
def get_name_and_top_note(students):
    return [{'name': i['name'], 'top_note': 0 if len(i['notes']) == 0 else max(i['notes'])} for i in students]

# Or
def get_name_and_top_note(s):
    return [{'name': j['name'], "top_note": 0 if j['notes'] == [] else max(j['notes'])} for j in s]

# Or
def get_name_and_top_note(students):
    student_top_lst = []
    for student in students:
        student_top_lst.append({'name': student['name'], 'top_note': max(
            student['notes']) if student['notes'] else 0})  # or if len(student['notes']) !=0 else 0})
    return student_top_lst


# 3rd method
def get_name_and_top_note(students):
    ret = []
    for i in students:
        temp = {}
        temp['name'] = i['name']
        if i['notes']:
            temp['top_note'] = max(i['notes'])
        else:
            temp['top_note'] = 0
        ret.append(temp)
    return ret


# 4th method
def get_name_and_top_note(lst):
    l = []
    d = {}
    for a in lst:
        d['name'] = a['name']
        try:
            d['top_note'] = max(a['notes'])
        except:
            d['top_note'] = 0
        l.append(d)
        d = {}
    return l

# 5th method
def get_name_and_top_note(lst):
    for item in lst:
        if len(item['notes']) >= 1:
            item['top_note'] = max(item['notes'])
        else:
            item['top_note'] = 0
        del item['notes']
    return lst

# Or
def get_name_and_top_note(students):
    for i in range(len(students)):
        students[i]['top_note'] = max(students[i]['notes']) if len(
            students[i]['notes']) > 0 else 0
        del students[i]['notes']
    return students

# 6th method
def get_name_and_top_note(students):
    return [{'name': x['name'], 'top_note': max(x['notes']) if x['notes']else 0} for x in students]


######################################################################
#################################### Question #*(Funny Numbers)
"""
Task : Create a function which takes a number n and a positive integer p and returns a positive integer k,
such as the sum of the digits of n taken to the successive powers of p is equal to k * n. 
Funny Numbers
89 --> 8¹ + 9² = 89 * 1
695 --> 6² + 9³ + 5⁴ = 1390 = 695 * 2
46288 --> 4³ + 6⁴ + 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

In other words, is there an integer k such as:

(a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ... ) = n * k
# A given number = n
# A given positive integer = p
# Digits of the given number = a, b, c, d ...
# A positive integer = k
"""

# 1st method
def funny_numbers(n, p):
    my_list = [int(x) for x in str(n)]
    my_power = [p + i for i in range(len(my_list))]
    my_sum = sum(x**y for x, y in zip(my_list, my_power))
    if my_sum % n == 0:
        return my_sum // n
    else:
        return None


# 2nd method
my_list = [1, 2, 3, 4]
print((enumerate(my_list)))

def funny_numbers(n, p):
    my_sum = sum(int(digit)**(index + p) for index, digit in enumerate(str(n)))
    if my_sum % n == 0:
        return my_sum // n
    else:
        return None

# 3rd method
def funny_numbers(n, p):
    s = 0
    for i, c in enumerate(str(n)):
        s = s + pow(int(c), p + i)
    return s // n if s % n == 0 else None


# 4th method
def funny_numbers(n, p):
    A = [int(x) for x in str(n)]
    s = sum([A[i]**(p+i) for i in range(len(A))])
    k, r = divmod(s, n)
    return k if r == 0 else None


#########################################################################
############################## Question #*(Matrix Multiplication)
"""
Create a function that multiplies two matricies (n x n each).

Examples :-
matrix_mult([[4, 2],[3, 1]], [[5, 6], [3, 8]]) ➞ [[26, 40], [18, 26]]
"""
# 1st method using numpy
import numpy as np
def matrix_mult(m1, m2):
		return np.dot(m1,m2).tolist()
	
# 2nd methd
def matrix_mult(m1, m2):
    return [[sum(a*b for a,b in zip(row, col)) for col in zip(*m2)] for row in m1]

m = [[4, 2],[3, 1]]
print(*m) #Output : [4, 2] [3, 1]
print(type((*m)))


# 3rd method
def matrix_mult(m1, m2):
	m = [[0,0],[0,0]]
	m2 = list(zip(*m2))
	for i in range(2):
		for j in range(2):
			m[i][j] = sum(a*b for a,b in zip(m1[i],m2[j]))
	return m


#########################################################################
############################## Question #*(Fit the Pattern)
"""
Task : Create a function that checks if the sub-lists in a list adhere to the specified pattern.

Examples
check_pattern([[1, 1], [2, 2], [1, 1], [2, 2]], "ABAB") ➞ True
"""
def check_pattern(lst, pattern):
	lst = list(map(tuple, lst))
	return len(set([(a, b) for a, b in zip(lst, pattern)])) == len(set(pattern)) == len(set(lst))

# we can not store mutable items in set so that list through error TypeError: unhashable type: 'list'
# dictioary each key must be unique. However, different keys can have the same values. 
#check_pattern([[1, 1], [2, 2], [1, 1], [2, 2]], "ABAB") ➞ True
pattern = "ABAB"
lst = [[1, 1], [2, 2], [1, 1], [2, 2]]
my_set = set(tuple(v) for v in lst)

my_pattern = list(pattern)
my_dict = list(zip(my_pattern, lst))

for k in my_list:
    if my_list[k]



my_tup = set(pattern)
print(my_tup)
my_list_tup = set(lst)
print(my_list_tup)


my_dict = {k:v for k in my_pattern for v in lst}
print(my_dict)


import numpy as np
def check_pattern(lst, pattern):
#check_pattern([[1, 1], [2, 2], [1, 1], [2, 2]], "ABAB") ➞ True
		pattern = list(pattern)
		my_dict = {k:v for k,v in zip(pattern, lst)}
		return all(k == m for k in lst for m,n in my_dict.items())

# 2nd method
def all_pos(x):
	return [j for i in x for j in range(len(x)) if i == x[j]]

def check_pattern(lst, pattern):
	return all_pos(lst) == all_pos(pattern)


# 3rd method
def check_pattern(lst, pattern):
	patt = list(pattern)
	return [patt.index(x) for x in patt] == [lst.index(x) for x in lst]

# 4th method
def check_pattern(lst, pattern):
	return all([(lst[i] == lst[j]) == (pattern[i] == pattern[j]) for i in range(len(lst)) for j in range(i)])

# 5th method
from collections import defaultdict
def check_pattern(l, word):
    dic = {''.join([str(i) for i in a]): b for a, b in zip(l, word)}
    res = defaultdict(list)
    for k, v in dic.items():
        res[v].append(k)
    return len(res) == len(set(word)) and all([len(a) == 1 for a in res.values()])

# 6th method
def check_pattern(c,s):
    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic:
            dic[s[i]] = c[i]
    x = []
    for k in dic.values():
        if k not in x:
            x.append(k)
    if len(x) != len(dic):
        return False

    return [dic[k] for k in s] == c

# 7th method
def check_pattern(lst, pattern):
    lst = [tuple(x) for x in lst]
    dic = {key : value for key, value in zip(pattern, lst)}
    lst = [x for x in zip(pattern, lst)]
    one = all([lst[i][1] == dic[lst[i][0]] for i in range (len(pattern))])
    two = len(dic.values()) == len(set([value for value in dic.values()]))
    return one and two

# 8th method
def check_pattern(lst, pattern):
	d = {}
	for i in range(len(lst)):
		if pattern[i] not in d:
			if lst[i] not in lst[:i]:
				d[pattern[i]] = lst[i]
			else: return False
		elif d[pattern[i]] != lst[i]:
			return False
	return True




###################################################################
########################### Question : (FSA: Creating Machines)
"""
Task: Create a finite-state automaton that determines whether a binary number is divisible by five. The finite-state automaton from this challenge can be constructed as follows:

Example FSA
divisible = {
    "S0": ["S0", "S1"],
    "S1": ["S2", "S0"],
    "S2": ["S1", "S2"]
}
Each key is a state, and each value denotes instructions for each type of input. For "S0", the array ["S0", "S1"] indicates that if a 0 is received, the new state is "S0". If 1 is received, the new state is "S1".

Notes :
Remember to create a dictionary, not a function.
In this case, "accept" would mean that the number is divisible by five, whereas "reject" means that it isn't.
The starting and accepting states should both be "S0".
The automaton should read the digits of a binary number from left to right. For example, the first digit for 26 (0b11010) would be 1, since we ignore the 0b.

"""

# Out of my context


###################################################################
########################### Question : (FSA: Creating Machines)



import string
def paul_cipher(txt):
    # paul_cipher("he1lo") ➞ "HM1QA"
    lower_case = list(string.ascii_lowercase(txt))
    upper_case = list(string.ascii_uppercase(txt))
    my_list = []
    my_string = ""
    my_index = {}
    index = None
    first_txt = txt[:1]
    my_txt = txt[1:]
    for k in first_txt:
        if k.islower():
            my_string = my_string + k.upper()
            my_index[k] = (lower_case.index(k))
            index = lower_case.index(k)
        elif k.isupper():
            my_string = k
            my_index.append(upper_case.index(k))
            index = upper_case.index(k)
        else:
            my_string = my_string + k
        
    for l in my_txt:
        if first_txt.islower() or first_txt.isupper():
            if l.islower():
                my_string = upper_case.index(l.upper()) + 
            
            
            


















################################################################################################
###### Question :Create a function that finds the highest integer in the list using recursion.
# 1st method.
def find_highest(lst):
    if len(lst) == 1:
        return lst[0]
    r = find_highest(lst[1:])
    return r if r >= lst[0] else lst[0]


# 2nd method
def find_highest(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        if lst[0] < lst[1]:
            lst.pop(0)
        else:
            lst.pop(1)
        return find_highest(lst)
# OR
def find_highest(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        lst.pop(0) if lst[0] < lst[1] else lst.pop(1)
        return find_highest(lst)


# 3rd method
def find_highest(l):
    return l[0] if len(l) == 1 else find_highest(l[:-1]) if l[0] > l[-1] else find_highest(l[1:])


# 4th method
def find_highest(lst):
    if len(lst) == 1:
        return lst[0]
    a = lst[0]
    b = find_highest(lst[1:])
    if a > b:
        return a
    else:
        return b


# 5th method
def find_highest(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        current = find_highest(lst[1:])
        return current if current > lst[0] else lst[0]


# 6th method
def find_highest(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        m = find_highest(lst[1:])
        return m if m > lst[0] else lst[0]


# 7th method
def find_highest(lst, m=None):
    if not lst:
        return m
    if m is None:
        m = lst[0]
    return find_highest(lst[1:], m if m > lst[0] else lst[0])


# 8th method
def find_highest(lst):
    if len(lst) == 1:
        return lst[0]
    if lst[0] >= lst[-1]:
        return find_highest(lst[0:-1])
    else:
        return find_highest(lst[1:])


# 9th method
def find_highest(lst):
    if len(lst) == 1:
        return lst[0]
    return max(lst[0], find_highest(lst[1:]))


# 10th method
def find_highest(n):
    if len(n) == 1:
        return n[0]
    else:
        if n[0] > n[1]:
            n.remove(n[1])
            return find_highest(n)
        else:
            n.remove(n[0])
            return find_highest(n)


# 11th method
def find_highest(lst):
    if all([lst[0] >= x for x in lst]):
        return lst[0]
    else:
        return find_highest(lst[1:])


###################################################
########## Question: (Sum of Odd and Even Numbers)
"""
# Write a function that takes a list of numbers and returns a list with two elements:
The first element should be the sum of all even numbers in the list.
The second element should be the sum of all odd numbers in the list."""
# 1.
def sum_odd_and_even(lst):
    even_element = (lambda x, y: x + y)(sum(x for x in lst if x % 2 == 0), 0)
    odd_element = (lambda x, y: x + y)(sum(x for x in lst if x % 2 != 0), 0)

    my_list = [even_element, odd_element]
    return my_list


# 2.
def sum_odd_and_even(lst):
    x = lst[::2]
    y = lst[1::2]
    return [sum(y), sum(x)]


# 3.
def sum_odd_and_even(lst):
    return [sum(e for e in lst if e % 2 == i) for i in [0, 1]]
