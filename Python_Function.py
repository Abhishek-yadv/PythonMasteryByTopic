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

##########################################################################
################ Question #*(Get Students with Names and Top Notes II)
"""
Out Of contest:-
Create a function that takes a single Hexadecimal number as an argument and returns the equivalent
six-digit binary number to light the display. Consider the six-digit binary number as an incoming
input from a serial port. The segment display is a common cathode segment display that means you
need to give a logical 1 to light up each segment.

Notes
Bit order is as follows MSB [dp, g, f, e, d, c, b, a] LSB.
This is something that comes up in FPGA work a lot, where you have to make some kind of conversion
between numerical values and bits controlling hardware. These conversions often have no simple algorithm
and require hard coding. If you do hard code this challenge you can try to determine the correct values
by yourself but in industry if you can just look up a reference, you do.
In this case the code tests have all the required values.
"""
# 1st method
D = {0x0: 0x3F, 0x1: 0x06, 0x0: 0x3F, 0x1: 0x06, 0x2: 0x5B, 0x3: 0x4F, \
	0x4: 0x66, 0x5: 0x6D, 0x6: 0x7D, 0x7: 0x07, 0x8: 0x7F, 0x9: 0x6F, \
	0xA: 0x77, 0xB: 0x7C, 0xC: 0x39, 0xD: 0x5E, 0xE: 0x79, 0xF: 0x71}
def to_display(hexIn):
	return D.get(hexIn, None)

# 2nd method
# Concept
"""
Note: The characters in the segment strings are lowercase letters from 'a' to 'g',
and the formula 2**(ord(c) - 97) is used to convert each letter to its corresponding bit
in a binary representation (assuming ASCII values, where 'a' has ASCII value 97).
"""
segments = {0: "abcdef", 1: "bc", 2: "abged", 3: "abcdg", 4: "fgbc",
            5: "afgcd", 6: "afedcg", 7: "abc", 8: "abcdefg", 9: "afgbcd",
            10: "abcefg", 11: "fedcg", 12: "afed", 13: "bcdeg",
            14: "afedg", 15: "agef"}

def to_display(hexIn):
    k = int(hexIn)
    b = 0
    for c in segments[k]:
        b += 2**(ord(c) - 97)
    return b

# 3rd method
def to_display(hi):
    questions = [str(i) for i in range(16)]
    answers = [63, 6, 91, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 0x7F, 0x6F, 0x77, 0x7C, 0x39, 0x5E, 0x79, 0x71]

    dic = {questions[n]:answers[n] for n in range(len(questions))}    
    return dic[str(hi)]

# 4th method
# Concept
#* Convert integer to hex representation
my_int = 4
print(hex(my_int)) # Output : 0x4

print(my_int.to_bytes(4, byteorder='big')) # Output : b'\x00\x00\x00\x04'

#* Convert integer to byte representation (variable length, big-endian)
# this method : This way, you get the byte representation with the minimum number of bytes required to represent the integer.
my_int = 4
byte_length = (my_int.bit_length() + 7) // 8
byte_representation = my_int.to_bytes(byte_length, byteorder='big')
print(byte_representation) # Output : b'\x04'

#* Convert integer to bit representation
print(bin(my_int)) # Output : 0b100


#* Convert hex into bytes and bit by using bytes.fromhex(), and format method
# Hexadecimal string
hex_string = "1a3f"

# Convert hex to bytes
byte_representation = bytes.fromhex(hex_string)
print(f"Hex to Bytes: {byte_representation}")

# Convert bytes to binary
binary_representation = ''.join(format(byte, '08b') for byte in byte_representation)
print(f"Bytes to Binary: {binary_representation}")

#* Convert a hexadecimal string to its binary representation directly
# Hexadecimal string
hex_string = "1a3f"

# Convert hex to binary directly
binary_representation = bin(int(hex_string, 16))[2:]
print(f"Hex to Binary: {binary_representation}")




for i in range(1, 16):
    binary_representation = (hex(i))
    print(f"{i}: {binary_representation}")
# >>> 1: 0x1
#     2: 0x2 
#     3: 0x3 
#     4: 0x4 
#     5: 0x5 
#     6: 0x6 
#     7: 0x7 
#     8: 0x8 
#     9: 0x9 
#     10: 0xa
#     11: 0xb
#     12: 0xc
#     13: 0xd
#     14: 0xe
#     15: 0xf






########################################################################
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
    if my_list[k]:
        print(k)


my_tup = set(pattern)
print(my_tup)
my_list_tup = set(lst)
print(my_list_tup)


my_dict = {k:v for k in my_pattern for v in lst}
print(my_dict) # In dictioary each key must be unique.


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
# 1.st method
automaton = {
	'S%s' % k: ['S%s' % ((2*k + n) % 5) for n in [0, 1]] for k in range(5)
}

# 2nd method
automaton = {
	'S0': ['S0', 'S1'],
	'S1': ['S2', 'S3'],
	'S2': ['S4', 'S0'],
	'S3': ['S1', 'S2'],
	'S4': ['S3', 'S4']
}


#####################################################################
######################################## Question : (Paul Cipher)
"""
Task :Paul Cipher
In Paul Cipher, only alpha characters will be encoded with the following rules:

All alpha characters will be treated as uppercase letters.
The first alpha character will not change (except for switching to upper case).
All subsequent alpha characters will be shifted toward "Z" by the alphabetical position of the previous alpha character (wrap back to "A" if "Z" is passed).
he1lo would be encoded as follows:

paul_cipher("he1lo") ➞ "HM1QA"

h -> H (First character to be changed to uppercase)
e -> M (H is the previous alpha character and 8th letter in the alphabets. E + 8 = M)
1 -> 1 (Keep all characters other than alphabets as it is)
l -> Q (E is the previous alpha character and 5th letter in the alphabets. L + 5 = Q)
o -> A (L is the previous alpha character and 12th letter in the alphabets. O + 12 = A)

Given a string txt, return the encoded message. See the below examples for a better understanding:

Examples :
paul_cipher("muBas41r") ➞ "MHWCT41K"
paul_cipher("a1rForce") ➞ "A1SXUGUH"
paul_cipher("MATT") ➞ "MNUN"

"""
# Key concept
"""
* ord() :
the ord() function is used to get the Unicode code point of a given character.
The Unicode code point is a unique numeric identifier assigned to each character
in the Unicode standard,which is a standardized character encoding that supports
a wide range of characters from various writing systems around the world.

* Unicode
Unicode is a standardized character encoding system that assigns a unique numeric identifier, called a code point,
to every character used in the world's writing systems. it has diffrence encoding schema "UTF-8, UTF-16, and UTF-32"
UTF-8( variable-length encoding scheme different characters may require different numbers of bytes to represent.),
UTF-16(var2to4), and UTF-32 (fix 4 byte).
it's backword compactbility first 128 is ASCII 

"""
import string
upper_case = string.ascii_uppercase
unicode_indentifer = [ord(k) for k in upper_case]
print(unicode_indentifer) #Output [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]

import string
digit_to_encode = string.digits
unicode_indentifer = [ord(k) for k in digit_to_encode]
print(unicode_indentifer) #[48, 49, 50, 51, 52, 53, 54, 55, 56, 57]


"""
The chr() function in Python is used to convert an ASCII code or Unicode code point into a character.
It returns a string representing a character whose Unicode code point is the integer passed as an argument.

ascii_code = 65
character = chr(ascii_code)

print(f"The character with ASCII code {ascii_code} is '{character}'")

"""
# example
ascii_code = 65
character = chr(ascii_code)
print(f"The character with ASCII code {ascii_code} is '{character}'") #The character with ASCII code 65 is 'A'

# Convert text string to bytes (UTF-8 encoding)
# Text string
text_string = "Hello, World!"
byte_representation = text_string.encode('utf-8')
print(f"Text to Bytes: {byte_representation}") # Output : Text to Bytes: b'Hello, World!'


# Decode bytes back into a string
decoded_string = byte_representation.decode('utf-8')
print(f"Bytes to Text: {decoded_string}") # Output : Bytes to Text: Hello, World!

# Integer
my_int = 42

# Encode integer to bytes
byte_representation = my_int.to_bytes(4, byteorder='big')  # Assuming a 4-byte representation
print(f"Integer to Bytes: {byte_representation}") # Output : Integer to Bytes: b'\x00\x00\x00*'

# Decode bytes back to integer
decoded_int = int.from_bytes(byte_representation, byteorder='big')
print(f"Bytes to Integer: {decoded_int}") # Output : Bytes to Integer: 42




import string
upper_case = string.ascii_uppercase
def paul_cipher(txt):
    my_string = ""
    my_index = 0
    if txt[0].isdigit():
        my_string += txt[0]
    elif txt[0].islower():
        my_string += txt[0].upper()
        my_index = upper_case.index(txt[0].upper())
    else:
        my_string += txt[0].upper()
        my_index = upper_case.index(txt[0].upper())
        
    for k in txt[1:]:
        if k.isdigit():
            my_string += k
        elif k.islower():
            indx = upper_case.index(k.upper() + my_index)
            my_string += upper_case.index(indx)
        else:
            indx = upper_case.index(k.upper()) + my_index
            my_string += upper_case.index(indx)
            
    return my_string
            
            

import string
upper_case = string.ascii_uppercase
lower_case = string.ascii_lowercase
my_string = ""
my_index = 0
def paul_cipher(txt):
    global my_string  # Declare my_string as a global variable
    global my_index
    if txt[0].islower():
        my_string = my_string + k.upper()
        my_index = my_index + lower_case.index(k)
        
    else:
        my_string = my_string + k
        my_index = my_index + upper_case.index(k)
        
    for k in txt[1:]:
        if k.islower():
            my_index = my_index + lower_case.index(k)
            my_string = my_string + lower_case[my_index]
        elif k.isupper():
            my_index = my_index + upper_case.index(k)
            my_string = my_string + upper_case[my_index]
            
        elif k.isdigit():
            my_string = k + my_string

    return my_string

# 1st method
def paul_cipher(txt):
    import string
    upper_case = string.ascii_uppercase
    my_string, my_index = "", 0
    for i in txt.upper():
        if i.isalpha():
            my_string += upper_case[(upper_case.index(i) + my_index) % 26]
            my_index = upper_case.index(i) + 1
        else:
            my_string += i
    return my_string

# 2nd method using chr and ord method
def paul_cipher(txt):
    my_list, my_index = [], 0
    for c in txt.upper():
        if c.isalpha():
            c_pos = ord(c) - 65
            new_c = chr((c_pos + my_index) % 26 + 65)
            my_index = c_pos + 1
        else:
            new_c = c
        my_list.append(new_c)
    return "".join(my_list)

# 3rd method
def paul_cipher(txt):
    my_index = 0
    my_string = ""
    for c in txt.upper():
        if c.isalpha():
            my_string += chr(65 + ((ord(c) - 65) + my_index) % 26)
            my_index = ord(c) - 64
        else:
            my_string += c
    return my_string


# 4th method
import re
def paul_cipher(txt):
    txt= txt.capitalize()    
    a = re.findall(r'[a-zA-Z]',txt)
    ans = [a[0]]    
    for i,w in enumerate(a[1:]):
        n = ord(w.lower()) -96 + ord(a[i].lower()) -96
        if n>26:n-=26
        ans.append(chr(int(n)+96).upper())    
    return ''.join(list(map(lambda x: ans.pop(0) if x.isalpha() else x,list(txt)))).upper()

# 5th method
def paul_cipher(txt):
    import string
    alphabets = list(string.ascii_uppercase)
    textList = [t.upper() for t in txt]
    finalString = []
    index = 0
    for i in range(0, len(textList)):
        current = textList[i]
        if current.isdigit() == True:
            finalString.append(current)
        elif current.isalpha() == True:
            currentIndex = alphabets.index(current) + index
            index = alphabets.index(textList[i]) + 1
            if currentIndex >= 26:
                currentIndex = currentIndex - 26
                finalString.append(alphabets[currentIndex])
            else:
                finalString.append(alphabets[currentIndex])
        else: 
            finalString.append(current)
    return "".join(finalString)

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
                my_string = upper_case.index(l.upper()) + k
                    

##################################################################################
################################### Question : (Sort by Number of Calls)
# Key Concept: callable
"""
Task :Create a function that takes a list of functions and sorts them in ascending order
based on how many calls are needed for them to return a non-function.

Examples
f1 = lambda: "hello"
# f1() ➞ "hello"

f2 = lambda: lambda: "edabit"
# f2()() ➞ "edabit"

f3 = lambda: lambda: lambda: "user"
# f3()()() ➞ "user"

func_sort([f2, f3, f1]) ➞ [f1, f2, f3]
# [f2, f3, f1] ➞ [2, 3, 1] ➞ [1, 2, 3] ➞ [f1, f2, f3]

func_sort([f1, f2, f3]) ➞ [f1, f2, f3]
# [f1, f2, f3] ➞ [1, 2, 3] ➞ [1, 2, 3] ➞ [f1, f2, f3]

func_sort([f2, "func"]) ➞ ["func", f2]
# [f2, "func"] ➞ [2, 0] ➞ [0, 2] ➞ ["func", f2]

Notes
Treat non-functions as needing zero calls.
Every function will be called with empty parameters.
Every function will need to be called at least once.
The potentially returned values include ints, floats, and lists, among others.

"""

#* callable
"""
"callable" refers to an object that can be called as a function. It means you can use the function call syntax,
using parentheses (), on the object. There are several types of objects that are callable in Python:
"""
# 1. Functions: Traditional functions defined using the def keyword.
def my_function():
    print("Hello, World!")
my_function()  # This is a callable object

# 2. Built-in Functions: Functions that are built into the Python language.
len("Hello")  # len is a built-in function and is callable

# 3. Methods: Functions associated with an object, accessed using dot notation.
my_list = [1, 2, 3]
my_list.append(4)  # append is a method of the list object and is callable

# 4. Classes: Instances of classes can be callable if the class defines a __call__ method.
class CallableClass:
    def __call__(self):
        print("Instance of CallableClass called")

obj = CallableClass()
obj()  # Calling the instance as if it were a function

# 5.Callable Objects: Objects that implement the __call__ method can be called.
class CallableObject:
    def __call__(self):
        print("CallableObject called")

obj = CallableObject()
obj()  # Calling the object as if it were a function

#* You can check if an object is callable using the callable() function:

print(callable(my_function))  # True
print(callable(len))          # True
print(callable(my_list.append))  # True
print(callable(obj))  # True if __call__ is defined in the class or the object

""" 
exec() function : is a built-in function that is used for the dynamic execution of Python programs,
which can be either a string or object code. It allows you to dynamically execute Python code at runtime.

#* exec(object[, globals[, locals]])

#* object: This parameter can be a string containing Python code or a code object (compiled code).
#* globals (optional): A dictionary representing the global namespace. If provided, the code will be executed within this namespace.
#* locals (optional): A dictionary representing the local namespace. If provided, the code will be executed within this namespace.

"""
code = """
def greet(name):
    print("Hello, " + name + "!")
"""
# Execute the code
exec(code)

# Call the function defined in the executed code
# func_invoking = greet("John")

"""
exec() is suitable for executing multiple statements or code blocks,
while eval() is designed for evaluating single expressions. 
Both functions take optional globals and locals dictionaries,
allowing you to specify the namespaces in which the code is executed, similar to exec().
"""

# 1st method
def func_sort(lst):
    f = lambda g, n=0: f(g(), n+1) if callable(g) else n
    return sorted(lst, key=f)

# 2nd method
calls = lambda x: calls(x()) + 1 if callable(x) else 0
func_sort = lambda l: sorted(l, key = calls)

# 3rd method
def func_sort(lst):
    inner_num = 0
    def calls(i):
        while True:
            if callable(i):
                inner_num = inner_num  + 1
                i = i()
            else:
                return inner_num
    return sorted(lst, key=calls)

# 4th method
def func_sort(lst):
    d = dict()
    for i in range(len(lst)):
        d[i] = 0
        f = lst[i]
        while callable(f) is True:
            d[i] += 1
            f = f()
    return sorted(lst, key=lambda x:d[lst.index(x)])

#  5th method
def counter(f):
	return 1 if not callable(f) else 1 + counter(f())

def func_sort(lst):
	return sorted(lst, key=counter)

# 6th method
def numCalls(fn):
	count = 0
	while callable(fn):
		fn = fn()
		count += 1
	return count

def func_sort(lst):
	return sorted(lst, key=numCalls)

# 7th method
def func_sort(lst):
	depth = lambda x: 1 + depth(x()) if callable(x) else 0
	return sorted(lst, key=depth)

# 8th method
def getcalls(fun): 
	outlist = 0
	while callable(fun): 
		outlist += 1
		fun = fun()
	return outlist
def func_sort(lst):
	funlist = [getcalls(i) for i in lst]
	zlist = zip(lst,funlist)
	outlist = sorted(zlist,key = lambda x: x[1])
	outlist = [i[0] for i in outlist]
	return outlist

# 9th method
def func_sort(lst):
	func_type = type(func_sort)
	def call_count(f):
		if type(f) != func_type:
			return 0
		return call_count(f()) + 1
	return sorted(lst, key = lambda f: call_count(f))

# 10th method
def func_sort(lst):
	return sorted(lst, key=calls_for_non_func)	
def calls_for_non_func(x):
	calls = 0
	while True:
		try:
			x = x()
			calls += 1
		except TypeError:
			return calls

# 11th method
def func_sort(lst):
	def calls(f, c=0):
		return calls(f(), c+1) if callable(f) else c
	return sorted(lst, key=calls)


# 12th method
def count_func_call(f):
    if type(f).__name__ == 'function':
        return 1 + count_func_call(f())
    else:
        return 0
def func_sort(lst):
    return sorted(lst, key=count_func_call)


##################################################################################
################################### Question : (Mountains or Valleys)
"""
Mountains or Valleys
A mountain is a list with exactly one peak.

All numbers to the left of the peak are increasing.
All numbers to the right of the peak are decreasing.
The peak CANNOT be on the boundary.
A valley is a list with exactly one trough.

All numbers to the left of the trough are decreasing.
All numbers to the right of the trough are increasing.
The trough CANNOT be on the boundary.
Some examples of mountains and valleys:

Mountain A:  [1, 3, 5, 4, 3, 2]   # 5 is the peak
Mountain B:  [-1, 0, -1]   # 0 is the peak
Mountain B:  [-1, -1, 0, -1, -1]   # 0 is the peak (plateau on both sides is okay)

Valley A: [10, 9, 8, 7, 2, 3, 4, 5]   # 2 is the trough
Valley B: [350, 100, 200, 400, 700]  # 100 is the trough
Neither mountains nor valleys:

Landscape A: [1, 2, 3, 2, 4, 1]  # 2 peaks (3, 4), not 1
Landscape B: [5, 4, 3, 2, 1]  # Peak cannot be a boundary element
Landscape B: [0, -1, -1, 0, -1, -1]  # 2 peaks (0)
Based on the rules above, write a function that takes in a list and returns either "mountain", "valley", or "neither".

Examples
landscape_type([3, 4, 5, 4, 3]) ➞ "mountain"

landscape_type([9, 7, 3, 1, 2, 4]) ➞ "valley"

landscape_type([9, 8, 9]) ➞ "valley"

landscape_type([9, 8, 9, 8]) ➞ "neither"

*Notes :A peak is not exactly the same as the max of a list. The max is a unique number, but a list may have multiple peaks. However, if there exists only one peak in a list, then it is true that the peak = max.
"""
# 1st method
def landscape_type(lst):
    # Find the maximum and minimum values and their positions
    max_value, min_value = max(lst), min(lst)
    max_index, min_index = lst.index(max_value), lst.index(min_value)

    # Check for a mountain
    is_mountain = all(lst[i] >= lst[i - 1] for i in range(1, max_index)) and all(lst[i] <= lst[i - 1] for i in range(max_index + 1, len(lst)))
    if is_mountain and max_value not in (lst[0], lst[-1]):
        return "mountain"

    # Check for a valley
    is_valley = all(lst[i] <= lst[i - 1] for i in range(1, min_index)) and all(lst[i] >= lst[i - 1] for i in range(min_index + 1, len(lst)))
    if is_valley and min_value not in (lst[0], lst[-1]):
        return "valley"

    # If neither mountain nor valley, return "neither"
    return "neither"

# 2nd method
def landscape_type(lst):
	if any((sorted(lst[:i+1]) == lst[:i+1] and sorted(lst[i:], reverse=True) == lst[i:]) for i in range(1,len(lst)-1)): return 'mountain'
	elif any((sorted(lst[:i+1], reverse=True) == lst[:i+1] and sorted(lst[i:]) == lst[i:]) for i in range(1,len(lst)-1)): return 'valley'
	return 'neither'

# 3rd method
def landscape_type(lst):
	largest, smallest = max(lst),min(lst)
	peak,trough = 0, 0
	left,right = [], []
	if largest != lst[0] and largest != lst[-1] and lst.count(largest) == 1:
		peak = largest   # must be unique and not on boundaries in order to qualify as a peak
	if smallest != lst[0] and smallest != lst[-1] and lst.count(smallest) == 1:
		trough = smallest   # must be unique and not on boundaries in order to qualify as trough
	if peak == largest:   # confirmed peak, check if it is a mountain
		left = lst[0 : lst.index(peak)]
		right = lst[ lst.index(peak) :]
		if left == sorted(left) and right == sorted(right, reverse=True):
			return 'mountain'
	if trough == smallest:   # confirmed trough, check if it is a valley
		left = lst[0 : lst.index(trough)]
		right = lst[lst.index(trough) :]
		if left == sorted(left, reverse=True) and right == sorted(right):
			return 'valley'
	return 'neither'


# 4th method
def landscape_type(lst):
    for i in range(1, len(lst)-1):        
        if max(lst[:i] + lst[i+1:]) < lst[i]:
            if lst[:i] == sorted(lst[:i]) and lst[i+1:] == sorted(lst[i+1:], reverse = True):
                return 'mountain'            
        if min(lst[:i] + lst[i+1:]) > lst[i]:
            if lst[:i] == sorted(lst[:i], reverse = True) and lst[i+1:] == sorted(lst[i+1:]):
                return 'valley'
    return 'neither'


# 5th method
def landscape_type(lst):
    if [lst[i-1] < lst[i] and lst[i] > lst[i+1] for i in range(1, len(lst)-1)].count(True) == 1 and lst[0]<=lst[1] and lst[-2]>=lst[-1]: return 'mountain'
    if [lst[i-1] > lst[i] and lst[i] < lst[i+1] for i in range(1, len(lst)-1)].count(True) == 1 and lst[0]>=lst[1] and lst[-2]<=lst[-1]: return 'valley'
    return 'neither'


# 6th method
from itertools import groupby
def landscape_type(lst):
	up = [a < b for a, b in zip(lst, lst[1:]) if a != b]
	if len(list(groupby(up))) == 2:
		return 'mountain' if up[0] else 'valley'
	return 'neither'

# 7th method
def landscape_type(lst):
    mode = 0
    hist = []
    for elem, prev in zip(lst[1:], lst):
        # newMode = (elem > prev) - (elem < prev) is a concise way to determine the trend of the current pair of elements (prev, elem) in the list.
        newMode = (elem > prev) - (elem < prev)
        if mode == 0 or newMode == 0:
            mode = mode + newMode
        elif newMode != mode:
            hist.append(mode)
            mode = newMode
    if len(hist) != 1:
        return "neither"
    else:
        if hist[0] == 1:
            return "mountain"
        else:
            return "valley"


##################################################################################
########################################### Question : (Sudoku Validation)
# key concept
def all(iterable):
    for k in iterable:
        if not k:
            return False
    return True
        
def any(iterable):
    for k in iterable:
        if k:
            return True
    return False


list = [[ 1, 5, 2, 4, 8, 9, 3, 7, 6 ],
        [ 7, 3, 9, 2, 5, 6, 8, 4, 1 ],
        [ 4, 6, 8, 3, 7, 1, 2, 9, 5 ],
        [ 3, 8, 7, 1, 2, 4, 6, 5, 9 ],
        [ 5, 9, 1, 7, 6, 3, 4, 2, 8 ],
        [ 2, 4, 6, 8, 9, 5, 7, 1, 3 ],
        [ 9, 1, 4, 6, 3, 7, 5, 8, 2 ],
        [ 6, 2, 5, 9, 4, 8, 1, 3, 7 ],
        [ 8, 7, 3, 5, 1, 2, 9, 6, 4 ]]

print(list[3][6]) # Output : 6
def sudoku_validator(game):

    target = 45  # first 9 numbers sums 45

    # row checking
    for row in game:
        if sum(row) != target:
            return False

    # column cheking
    for i in range(9):  # colums control
        column_sum = 0
        for j in range(9):  # rows control
            column_sum += game[j][i]
        if column_sum != target:
            return False

    # 3x3 box checking
    for i in [0, 3, 6]:  #columns control
        for j in [0, 3, 6]:  # rows control
            box_sum = 0
            for k in range(3):  # block control
                box_sum = box_sum + sum(game[k+j][i:i+3])
            if box_sum != target:
                return False
    return True


# 1st method
def sudoku_validator(x):
    mem = []
    for i in [3, 6, 9]:
        for j in [3, 6, 9]:
            subgrid = []
            for k in range(i-3, i):
                for l in range(j-3, j):
                    subgrid.append(x[k][l])
            mem.append(subgrid)
    print(mem)
    a = all([len(set(i)) == 9 for i in x])
    b = all([len(set(i)) == 9 for i in zip(*x)])
    c = all([len(set(i)) == 9 for i in mem])
    return a and b and c


# 2nd method
def sudoku_validator(x):
    mem = []
    for i in [3, 6, 9]:
        for j in [3, 6, 9]:
            mem = mem + [[x[k][l] for k in range(i-3, i) for l in range(j-3, j)]]
    print(mem)
    a = all([len(set(i)) == 9 for i in x])
    b = all([len(set(i)) == 9 for i in zip(*x)])
    c = all([len(set(i)) == 9 for i in mem])
    return a and b and c

k = sudoku_validator([
        [ 1, 5, 2, 4, 8, 9, 3, 7, 6 ],
        [ 7, 3, 9, 2, 5, 6, 8, 4, 1 ],
        [ 4, 6, 8, 3, 7, 1, 2, 9, 5 ],
        [ 3, 8, 7, 1, 2, 4, 6, 5, 9 ],
        [ 5, 9, 1, 7, 6, 3, 4, 2, 8 ],
        [ 2, 4, 6, 8, 9, 5, 7, 1, 3 ],
        [ 9, 1, 4, 6, 3, 7, 5, 8, 2 ],
        [ 6, 2, 5, 9, 4, 8, 1, 3, 7 ],
        [ 8, 7, 3, 5, 1, 2, 9, 6, 4 ]])

mem = [[1, 5, 2, 7, 3, 9, 4, 6, 8],
        [4, 8, 9, 2, 5, 6, 3, 7, 1],
        [3, 7, 6, 8, 4, 1, 2, 9, 5],
        [3, 8, 7, 5, 9, 1, 2, 4, 6],
        [1, 2, 4, 7, 6, 3, 8, 9, 5],
        [6, 5, 9, 4, 2, 8, 7, 1, 3],
        [9, 1, 4, 6, 2, 5, 8, 7, 3],
        [6, 3, 7, 9, 4, 8, 5, 1, 2],
        [5, 8, 2, 1, 3, 7, 9, 6, 4]]

# 3rd method
def sudoku_validator(arr):
	rows = [len(set(i)) for i in arr]
	cols = [len(set(i)) for i in zip(*arr)]
	squares = [len(set(arr[r][c] for r in range(i//3*3, i//3*3+3) for c in range(i%3*3, i%3*3+3))) for i in range(9)]
	return set(rows + cols + squares) == {9}

# 4th method
def sudoku_validator(bo):
    for row in range(9):
        if not sum(bo[row]) == 45:
            return False
		
    for col in range(9):
        if not sum(list(zip(*bo))[col]) == 45:
            return False
    
    list_box =[0, 3, 6]
    new_list = []
    for x in list_box:
        for num in list_box:
            for i in range(x,x+3):
                for j in range (num, num + 3):
                    new_list.append(bo[i][j])
    data = [new_list[t:t+9] for t in range(0,len(new_list),9)]
    for n in range(9):
        if not sum(data[n]) == 45:
            return False                        
    return True

# 5th method
def sudoku_validator(x):
    return all(len(set(x[i])) == 9 for i in range(9)) and all(len(set(x[j][i] for j in range(9))) == 9 for i in range(9)) and all(len(set(x[3*j][3*i:3+3*i]+x[1+3*j][3*i:3+3*i]+x[2+3*j][3*i:3+3*i])) == 9 for i in range(3) for j in range(3))

# 6th method
def sudoku_validator(x):

	def checker(lst):
		return len(set(lst))==len(lst)
	
	#check the rows
	rowChk = []
	rowChk = [checker(n) for n in x]
	
	#check the columns
	colChk = []
	for c in range(9):
		col = [row[c] for row in x]
		colChk.append(checker(col))
	
	#check the 3X3 boxes
	boxChk = []
	for j in range(0,9,3):
		for i in range(0,9,3):
			box = [x[r][c] for c in range(0+j,3+j) for r in range(0+i,3+i)]
			boxChk.append(checker(box))
	
	
	return all(rowChk)==True and all(colChk)==True and all(boxChk)==True

# 7th method
def sudoku_validator(x):
    valid9 = (lambda lst9: all(dig in lst9 for dig in range(1,10)))

    sqr = (lambda top, left: [x[3*top + r][3*left + c] for r in range(3) for c in range(3)])
    row = (lambda top: [x[top][c] for c in range(9)])
    col = (lambda left: [x[r][left] for r in range(9)])
    
    sqrs_valid = all(valid9(sqr(top, left)) for top in range(3) for left in range (3))
    rows_valid = all(valid9(row(top)) for top in range(9))
    cols_valid = all(valid9(col(left)) for left in range(9))

    return sqrs_valid and rows_valid and cols_valid

# 8th method
def sudoku_validator(x):
	ch = {i for i in range(1,10)}
	if not all([set(i) == ch for i in x]): return False
	if not all([set(i) == ch for i in zip(*x)]): return False
	boxes = [[i[3*j:3*j+3] for i in x[3*i:3*i+3]] for i in range(3) for j in range(3)]
	for i in boxes:
		e=set()
		for j in i: e|=set(j)
		if e!=ch: return False
	return True

# 9th method
def sudoku_validator(board):
    valid = {1,2,3,4,5,6,7,8,9}
    zipped = [list(x) for x in zip(*board)]
    if any(set(valid).difference(x) for x in board):
        return False
    if any(set(valid).difference(x) for x in zipped):
        return False
    threes = [board[x:x+3] for x in range(0,8,3)]
    threes = sum([list(zip(*x))for x in threes], [])
    threes = [sum(threes[x:x+3], ()) for x in range(0,len(threes),3)]
    if any(set(valid).difference(x) for x in threes):
        return False
    return True

# 10th method
def sudoku_validator(x):
	chk = list(range(1,10))
	hoz = all(sorted(row)==chk for row in x)
	ver = all(sorted(col)==chk for col in list(map(list,zip(*x))))
	arr = []
	for i in range(0,len(x),3):
		for j in range(0,len(x),3):
			tmp = []
			for a in range(3):
				for b in range(3):
					tmp.append(x[i+a][j+b])
			arr.append(tmp)
	squ = all(sorted(row) == chk for row in arr)
	return hoz and ver and squ

# 11h method
def sudoku_validator(x):
    bag = lambda x: sorted(x) == [1,2,3,4,5,6,7,8,9]
    rows = [bag(row) for row in x]
    cols = [bag([row[y] for row in x]) for y in range(9)]
    sections = []
    combos = [(0,3),(3,6),(6,9)]
    for i in combos:
        for j in combos:
            sections.append(bag([z for y in [[row[col] for row in x[i[0]:i[1]]]for col in range(j[0],j[1])] for z in y]))
    return all(rows) and all(cols) and all(sections)

# 12th method
def sudoku_validator(x):
	import numpy as np
	matrix = np.array(x)
	box = []
	check_box = []
	for i in range(9):
		if sorted(matrix[i, :]) != [1,2,3,4,5,6,7,8,9]:  
			print('row error')
			return False
		if sorted(matrix[:, i]) != [1,2,3,4,5,6,7,8,9]:  
			print('column error')
			return False
	for row in range(0, 9, 3):
		for col in range(0, 9, 3):
			box = matrix[row : row + 3, col : col + 3]   
			for number in range(1, 10):
				check_box.append(np.count_nonzero(box == number))
			if check_box != [1]*9:
				return False
			else:
				check_box = []
				box = []
	return True

# 13th method
def sudoku_validator(x):
    rows, cols, sqrs = [s for s in [set() for _ in range(9)]], [s for s in [set() for _ in range(9)]], [s for s in [set() for _ in range(9)]]
    for i in range(81):
        r, c = i // 9, i % 9
        s = (r // 3) * 3 + (c // 3)
        rows[r].add(x[r][c])
        cols[c].add(x[r][c])
        sqrs[s].add(x[r][c])
    return all(len(v) == 9 for v in rows + cols + sqrs)

# 14th method
def sudoku_validator(x):
    for i in range(len(x)):
        row = x[i]
        col = [r[i] for r in x]
        if len(row) != len(set(row)) or len(col) != len(set(col)): return False

    for i in range(len(x) // 3):
        ans = []
        for j in range(0, len(x)):
            ans.extend(x[j][i * 3:i * 3 + 3])
            if j % 3 == 2 and j > 0:
                if len(ans) != len(set(ans)): return False
                ans = []
    return True

# 15th method
def sudoku_validator(x):
	for i in x:
		if len(set(i))!=9: 
			return False
	for i in range(9):
		if len(set([x[a][i] for a in range(9)]))!=9: 
			return False
	for i in range(0,9,3):
		for j in range(0,9,3):
			temp=x[i][j:j+3]+x[i+1][j:j+3]+x[i+2][j:j+3]
			if len(set(temp))!=9:
				return False
	return True



##################################################################################
################################ Question : (Lambda Expressions All the Way Down)
"""
Create a function which takes a parameter n and returns a function such that it, when called n times, returns the string "edabit".

Examples
lambda_depth(0) ➞ "edabit"

lambda_depth(1)() ➞ "edabit"

lambda_depth(2)()() ➞ "edabit"

type(lambda_depth(2)()) ➞ <class: "function">
Notes
num will always be a non-negative integer.
If num == 0, return "edabit".
If num > 0, return a function.
All non-example test cases come in two forms: checking whether lambda_depth(k), after being called k times, returns a string, and checking whether lambda_depth(k) returns a function.
"""
# 1st method
lambda_depth = lambda num: (lambda: lambda_depth(num-1)) if num else 'edabit'


# 2nd method
def lambda_depth(num):
    if num == 0:
        return "edabit"
    else:
        return lambda: lambda_depth(num-1) # getting  TypeError: 'str' object is not callable if lambda
    
# 3rd method
lambda_depth = lambda n: eval('lambda: '*n + '"edabit"')

# 4th method
def lambda_depth(num):
    def inner():
        nonlocal num
        if num == 0:
            return "edabit"
        num = num - 1
        return inner
    return inner()

# 
def lambda_depth(num):
    return 'edabit' if not num else lambda: lambda_depth(num-1)
	# Or :return (lambda: lambda_depth(num - 1)) if num else "edabit"




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
