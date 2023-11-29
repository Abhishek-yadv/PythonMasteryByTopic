################################################################
"""
# Note : In a list or generator comprehension, the order of the loops is from left to right. 
# This means that the outer loop is specified first, followed by any inner loops. The comprehension is read in the same order.

#* Here's a general structure:
result = [expression for outer_loop in outer_iterable for inner_loop in inner_iterable]
"""
####################################################################
########################################################(Function)
####################################################################
############# Question : (Add the Values of the Symbols in a Matrix)
"""
Write a function that takes a list of lists and returns the value of all of the symbols in it,
where each symbol adds or takes something from the total score. Symbol values:
"""
# 1st method
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

from ctypes import *
# List all names in the ctypes module
print(dir())


####################################################################
################################### Question : (Magic Function)
"""
Create a class with a few functions like these examples.
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
	def replace(self, my_str, replace_it, replace_with): return my_str.replace(replace_it, replace_with)
	def str_length(self, my_str): return len(my_str)
	def trim(self, my_str): return my_str.strip()
	def str_length(self, my_str): return len(my_str)
	def list_slice(self, my_lst, my_tup): return my_lst[my_tup[0]-1:my_tup[1]]

####################################################################
############################# Question : (How Many Unique Styles?)
""" 
There are many different styles of music and many albums exhibit multiple styles.
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


######################################################################
############################# Question : (Oddly or Evenly Positioned)
"""
Create a function that returns the characters from a list or string r on odd or even positions, depending on the specifier s.
The specifier will be "odd" for items on odd positions (1, 3, 5, ...) and "even" for items on even positions (2, 4, 6, ...).
# char_at_pos([2, 4, 6, 8, 10], "even") ➞ [4, 8]
# 4 & 8 occupy the 2nd & 4th positions
"""

# 1st method
def char_at_pos(r, s):
    result = lambda r, s: r[::2] if s == "odd" else r[1::2]
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
################################### Question : (Reorder Digits)
"""
Create a function that reorders the digits of each numerical element in a list based on ascending (asc) or descending (desc) order.
reorder_digits([515, 341, 98, 44, 211], "asc") ➞ [155, 134, 89, 44, 112]
"""
# 1st method using lambda and sorted
def reorder_digits(lst, direction):
    result = lambda lst, direction : sort(lst, key = lambda k:lst[k]) if direction == 'asc' else lst.sort(key = lambda k:lst[k])[::-1]
# wrong

def reorder_digits(lst, direction):
    result = lambda lst, direction: sorted(lst, key=lambda k: int(''.join(sorted(str(k)))) if direction == 'asc' else int(''.join(sorted(str(k), reverse=True))))
    
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
	return [int(''.join(sorted(str(lst[x]), reverse = direction == "desc"))) for x in range(len(lst))]

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
    return [int(y) for y in [''.join(sorted(str(x),reverse=direction=='desc')) for x in lst]]

# 10th method
def reorder_digits(lst, direction):
	return [int("".join(sorted(list(str(num)), reverse={"asc": False, "desc": True}[direction]))) for num in lst]


###############################################
########### Question (Needle in a Hex String)








# Question :Create a function that finds the highest integer in the list using recursion.
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
def find_highest(l): return l[0] if len(l) == 1 else find_highest(
    l[:-1]) if l[0] > l[-1] else find_highest(l[1:])


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


# Question: (Sum of Odd and Even Numbers)
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
