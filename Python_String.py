####################################################################
########################################################## (String)
####################################################################

###################################################################
############## #* (Basic Arithmetic Operations on a String Number)
"""
Task : Create a function to perform basic arithmetic operations that includes addition, subtraction,
multiplication and division on a string number (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").
Here, we have 1 followed by a space, operator followed by another space and 2.

For the challenge, we are going to have only two numbers between 1 valid operator. The return value should be a number.
eval() is not allowed. In case of division, whenever the second number equals "0" return -1.

For example:
"15 // 0"  ➞ -1
"""

#* Answer
# 1st method
def arithmetic_operation(n):
	try:
		return eval(n)
	except ZeroDivisionError as e:
		return -1

# 2nd method
def arithmetic_operation(equation):
    from operator import add, sub, floordiv, mul
    my_oper = {'+': add, '-': sub, '*': mul, '//': floordiv}
    a, oper, b = equation.split()
    try:
        return my_oper[oper](int(a), int(b))
    except ZeroDivisionError:
        return -1

# 3rd method
def arithmetic_operation(equation):
    from operator import add, sub, floordiv, mul
    my_oper = {'+': add, '-': sub, '*': mul, '//': floordiv}
    a, oper, b = equation.split()
    # Useing getfor retrieval of operator function from the my_oper dictionary
    operator_function = my_oper.get(oper)

    # Check if the operator function is found in the dictionary
    if operator_function is not None:
        try:
            return operator_function(int(a), int(b))
        except ZeroDivisionError:
            return -1
    else:
        # Handle the case when the operator is not supported
        return "Unsupported operator: {}".format(oper)


# 4th method
Oper = {'+': int.__add__,  '-': int.__sub__,  '*': int.__mul__, '//': lambda m, n: m//n if n else -1}
def arithmetic_operation(n):
    m, oper, n = n.split()
    return Oper[oper](int(m), int(n))

# 5th method
def arithmetic_operation(n):
    m, oper, n = n.split()
    if oper == '//' and n == '0':
        return -1
    if oper == '+':
        return int(m) + int(n)
    elif oper == '-':
        return int(m) - int(n)
    elif oper == '*':
        return int(m) * int(n)
    else:
        return int(m) // int(n)

# Or
def arithmetic_operation(n):
    m, oper, n = n.split()
    m, n = int(m), int(n)
    if oper == '//' and n == '0': return -1
    if oper == '+': return (m) + (n)
    elif oper == '-': return (m) - (n)
    elif oper == '*': return (m) * (n)
    else: return (m) // (n)
    
# Or oops throuwig error will figure letter
def arithmetic_operation(n):
    m, oper, n = n.split()
    m, n = int(m), int(n)
    return -1 if (oper == '//' and n == 0) else (m + n) if oper == '+' else (m - n) if oper == '-' else (m * n)


def arithmetic_operation(n):
    m, oper, n = n.split()
    m, n = int(m), int(n)
    return -1 if (oper == '//' and n == 0) else (m + n) if oper == '+' else (m - n) if oper == '-' else (m * n) if oper == '*' else (m // n)


# 6th method
def arithmetic_operation(n):
	n, Oper, m = n.split()
	n, m = int(n), int(m)
	return n+m if Oper =='+' else n*m if Oper=='*' else n-m if Oper=='-' else n/m if Oper=='/' and m != 0 else -1

###################################################################
########################################## #* (Disarium Number)
"""
A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.
Create a function that determines whether a number is a Disarium or not.
"""
# 1st method
def is_disarium(n):
    return sum(int(digit) ** (index + 1) for index, digit in enumerate(str(n))) == n

# 2nd method
def is_disarium(n):
    my_list = []
    for k in range(len(str(n))):
        value = int(str(n)[k]) ** (k + 1)
        my_list.append(value)
    return sum(my_list) == n

# 3rd method
def is_disarium(n):
    func = lambda n: sum(int(digit) ** (index + 1) for index, digit in enumerate(str(n))) == n
    return func(n)

# 4th method
from functools import reduce
def is_disarium(n):
    digit_list = list(map(int, str(n)))
    power_sum = reduce(lambda acc, digit: acc + digit ** len(digit_list), digit_list, 0)
    return power_sum == n

###################################################################
########################################## #* (Convert to Hex)
"""
Task : Create a function that takes a string's characters as ASCII and returns each character's hexadecimal value as a string.
Examples
convert_to_hex("hello world") ➞ "68 65 6c 6c 6f 20 77 6f 72 6c 64"
convert_to_hex("Big Boi") ➞ "42 69 67 20 42 6f 69"
convert_to_hex("Marty Poppinson") ➞ "4d 61 72 74 79 20 50 6f 70 70 69 6e 73 6f 6e"
* Notes:=
Each byte must be seperated by a space.
All alpha hex characters must be lowercase.
"""
# 1st method
def convert_to_hex(txt):
    return " ".join(hex(ord(x))[2:] for x in str(txt))

# 2nd method
def convert_to_hex(txt):
	return ' '.join([format(ord(i), 'x') for i in txt])

# 3rd method



#########################################################################
####################### #* (Add the Values of the Symbols in a Matrix)
"""
Write a function that takes a list of lists and returns the value of all of the symbols in it, where each symbol adds or takes something from the total score. Symbol values:

# = 5
O = 3
X = 1
! = -1
!! = -3
!!! = -5
A list of lists containing 2 #s, a O, and a !!! would equal (0 + 5 + 5 + 3 - 5) 8.
If the final score is negative, return 0 (e.g. 3 #s, 3 !!s, 2 !!!s and a X would be (0 + 5 + 5 + 5 - 3 - 3 - 3 - 5 - 5 + 1) -3, so return 0.

Examples
check_score([
    ["#", "!"],
    ["!!", "X"]
]) ➞ 2

check_score([
    ["!!!", "O", "!"],
    ["X", "#", "!!!"],
    ["!!", "X", "O"]
]) ➞ 0

check_score([
    ["#", "O", "#", "!!", "X", "!!", "#", "O", "O", "!!", "#", "X", "#", "O"],
    ["!!!", "!!!", "!!", "!!", "!", "!", "X", "!", "!!!", "O", "!", "!!!", "X", "#"],
    ["#", "X", "#", "!!!", "!", "!!", "#", "#", "!!", "X", "!!", "!!!", "X", "O"],
    ["!!", "X", "!!", "!!", "!!!", "#", "O", "O", "!!!", "#", "O", "O", "#", "!!"],
    ["O", "X", "#", "!", "!", "X", "!!!", "O", "!!!", "!!", "O", "!", "O", "X"],
    ["!!", "!!!", "X", "!!!", "!!", "!!", "!!!", "X", "O", "!", "#", "!!", "!!", "!!!"],
    ["!!", "!!", "#", "O", "!", "!!", "!", "!!!", "#", "O", "#", "!", "#", "!!"],
    ["X", "X", "O", "X", "!!!", "#", "!!!", "!!!", "X", "X", "X", "!", "#", "!!"],
    ["O", "!!!", "!", "O", "#", "!", "!", "#", "X", "X", "#", "O", "!!", "!"],
    ["X", "!", "!!", "#", "#", "X", "!!", "O", "!!", "X", "X", "!!", "#", "X"],
    ["!", "!!", "!!", "O", "!!", "!!", "#", "#", "!", "!!!", "O", "!", "#", "#"],
    ["!", "!!!", "!!", "X", "!!", "!!", "#", "!!!", "O", "!!", "!!!", "!", "!", "!"],
    ["!!!", "!!!", "!!", "O", "!", "!", "!!!", "!!!", "!!", "!!", "X", "!", "#", "#"],
    ["O", "O", "#", "O", "#", "!", "!!!", "X", "X", "O", "!", "!!!", "X", "O"]
]) ➞ 12
Notes : Strings in the lists will only be #, O, X, !, !! and !!!.
"""

# 1st method
def check_score(s):
	my_dict = {'#': 5, 'O': 3, 'X': 1, '!': -1, '!!': -3, '!!!': -5}
	my_list = []
	for x in s:
		for k in x:
			my_list.append(my_dict.get(k))
	return sum(my_list) if sum(my_list) > 0 else 0

# Or
def check_score(s):
	my_dict = {'#': 5, 'O': 3, 'X': 1, '!': -1, '!!': -3, '!!!': -5}
	my_list = [my_dict.get(k) for x in s for k in x]
	return sum(my_list) if sum(my_list) > 0 else 0

# OR it's incorrect
def check_score(s):
	my_dict = {'#': 5, 'O': 3, 'X': 1, '!': -1, '!!': -3, '!!!': -5}
	return sum((my_dict.get(k) for x in s for k in x)) if > 0 else 0

# OR
my_dict = {'#': 5, 'O': 3, 'X': 1, '!': -1, '!!': -3, '!!!': -5}
def check_score(s):
    # return max(0, sum(my_dict[char] for row in s for char in row))
    return max(0, sum(my_dict.get(char, 0) for row in s for char in row))


# 2nd method
def check_score(s):
	pts = {'#':5, 'O':3, 'X':1, '!':-1, '!!':-3, '!!!':-5}
	total = 0
	for row in s:
		for el in row:
			total += pts[el]
	return max(total, 0)


# 3rd method
from collections import Counter
def check_score(s):
	dic = {'#':5,'O':3,'X':1,'!':-1,'!!':-3,'!!!':-5}
	res = sum(sum(dic[k]*v for k,v in Counter(t).items()) for t in s)
	return res if res > 0 else 0


# 4th method
def check_score(s):
	s=sum({'#':5,'O':3,'X':1,'!':-1,'!!':-3,'!!!':-5}[x]for y in s for x in y)
	return(s,0)[s<0]

# 5th method
def check_score(s):
    score = 0
    for i in s:
        for j in i:
            if j == '#':
                score += 5
            elif j == 'O':
                score += 3
            elif j == 'X':
                score += 1
            elif j == '!':
                score -= 1
            elif j == '!!':
                score -= 3
            elif j == '!!!':
                score -= 5
    if str(score).count('-') != 0:
        return 0
    else:
        return score
    
#########################################################################
############################################# #* (C*ns*r*d Str*ngs)
"""
Someone has attempted to censor my strings by replacing every vowel with a *, 
l*k* th*s. Luckily, I've been able to find the vowels that were removed.

Given a censored string and a string of the censored vowels, return the original uncensored string.

Example :
uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") ➞ "Where did my vowels go?"

uncensor("abcd", "") ➞ "abcd"

uncensor("*PP*RC*S*", "UEAE") ➞ "UPPERCASE"

Notes :
The vowels are given in the correct order.
The number of vowels will match the number of * characters in the censored string.

"""
# 1st method
def uncensor(txt, vowels):
    for x in txt:
        if x == "*":
            txt = txt.replace("*", vowels[0], 1)
            vowels = vowels[1:]
    return txt

# Or
def uncensor(txt, vowels):
    for x in vowels:
        txt = txt.replace("*", x, 1)
    return txt

# Or
def uncensor(txt, vowels):
    for x in vowels: txt = txt.replace("*", x, 1)
    return txt

# string has not remove attribute so we can use slicing and some these method
# 1st way Using str.replace() method:
my_string = "Hello, World!"
my_new_string = my_string.replace("o", "")
print(my_new_string) # Output: Hell, Wrld!

# specify counting
my_string = "Hello, World!"
my_new_string = my_string.replace("o", "", 1)
print(my_new_string) # Output: Hell, World!

# 2nd way Using list comprehension and str.join():
my_string = "Hello, World!"
chars_to_remove = {'o', 'l'}
my_new_string = ''.join([char for char in my_string if char not in chars_to_remove])
print(my_new_string) #Output : He, Wrd!

# 3rd way Using a loop to construct a new string:
my_string = "Hello, World!"
chars_to_remove = {'o', 'l'}
my_new_string = ""
for char in my_string:
    if char not in chars_to_remove:
        my_new_string += char
print(my_new_string) #Output He, Wrd!

# my bad practice
def uncensor(txt, vowels):
	my_vowels = ""
	for x in txt:
		if x == "*":
			txt = txt.replace("*", vowels[0],1)
			vowels.replace(vowels[0],'') #Forget to mention quantifier here 1
	return txt

# So correct code is
def uncensor(txt, vowels):
    for x in txt:
        if x == "*":
            txt = txt.replace("*", vowels[0], 1)
            vowels = vowels.replace(vowels[0], '', 1)
    return txt

# 2nd method
def uncensor(txt, vowels):
	txt = txt.replace('*', '{}')
	return txt.format(*vowels)

# 3rd method
def uncensor(txt, vowels):
	vowels = iter(vowels)
	return ''.join(next(vowels) if i == '*' else i for i in txt)

# 4th method
def uncensor(txt, vowels):
    v=list(vowels)
    return ''.join(v.pop(0) if i=="*" else i for i in txt)

# 5th method
def uncensor(s, V):
    return s.replace('*', '%s') % tuple(V)

# 6th method
uncensor=lambda t,v:t.replace('*','{}').format(*v)



###########################################################################
############################################# #* (Censor Words from List)
"""
Create a function that takes a string txt and censors any word from a given list lst.
The text removed must be replaced by the given character char.

censor_string("Today is a Wednesday!", ["Today", "a"], "-") ➞ "----- is - Wednesday!"

censor_string("The cow jumped over the moon.", ["cow", "over"], "*"), "The *** jumped **** the moon.")

censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*") ➞ "Why *** the ******* cross the ****?"

"""
# 1st method
def censor_string(txt, lst, char):
    for word in lst:
        txt = txt.replace(word, char * len(word))
    return txt
# Or
def censor_string(txt, lst, char):
	return ' '.join(char*len(word) if word in lst else word for word in txt.split())

# 2nd method
def censor_string(txt, lst, char):
    words=txt.split(" ")
    for word in words:
        if word in lst:
            replace_index=words.index(word)
            words[replace_index]=char*len(word)
    return " ".join(words)

# 3rd method
def censor_string(txt, lst, char):
	words = txt.split(" ")
	for i, word in enumerate(words):
		if word in lst:
			words[i] = "".join([char for letter in word])
            # Or words[i] = char*len(words[i])
	return " ".join(words)


# 4th method
def censor_string(txt, lst, char):
    words = txt.split()
    returnStr = ''
    for word in words:
        if word in lst:
            word = char * len(word)
        returnStr = returnStr + " " + word  
    return returnStr.strip()


###########################################################################
############################################# #* (Loves Me, Loves Me Not...)
"""
"Loves me, loves me not" is a traditional game in which a person plucks off all the petals of a flower one by one,
saying the phrase "Loves me" and "Loves me not" when determining whether the one that they love, loves them back.

Given a number of petals, return a string which repeats the phrases "Loves me" and "Loves me not" for every alternating petal,
and return the last phrase in all caps. Remember to put a comma and space between phrases.

Examples
loves_me(3) ➞ "Loves me, Loves me not, LOVES ME"
loves_me(1) ➞ "LOVES ME"
"""
# 1st method
from itertools import cycle
def loves_me(n):
    words = cycle(["Loves me", "Loves me not"])
    result = []
    for i in range(n):
        if i != n - 1:
            result.append(next(words))
        elif i == n - 1:
            result.append(next(words).upper())
    return ', '.join(result)

# getting StopIteration error. This error occurs when you try to call next() on an iterator that has reached the end.
# To fix this, you can use the cycle function from the itertools module to cycle through the words continuously.
def loves_me(n):
    words = ["Loves me", "Loves me not"]
    my_words = iter(words)
    result = []
    for i in range(n):
        if i != n - 1:
            result.append(next(my_words))
        elif i == n - 1:
            result.append(next(my_words).upper())
    return ', '.join(result)

# 2nd method
# testing
word = ['Loves me', 'Loves me not']
n = 4
sample_result = word*n
print(sample_result) #Output: ['Loves me', 'Loves me not', 'Loves me', 'Loves me not', 'Loves me', 'Loves me not', 'Loves me', 'Loves me not']
orignal_result = (word*n)[:n]
print(orignal_result) #Output : ['Loves me', 'Loves me not', 'Loves me', 'Loves me not']

# 2nd method
def loves_me(n):
    word = (['Loves me', 'Loves me not']*n)[:n]
    word[-1] = word[-1].upper()
    return ', '.join(word)

# 3rd method
def loves_me(n):
	word = ["Loves me" if i % 2 == 0 else "Loves me not" for i in range(0, n)]
	word[-1] = word[-1].upper()
	return ', '.join(word)


###########################################################################
############################################# #* (Pluralize!...)
"""
Given a list of words in the singular form, return a set of those words in the plural form if they appear more than once in the list.

Examples
pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }

pluralize(["table", "table", "table"]) ➞ { "tables" }

pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }
"""
# 1st method
def pluralize(lst):
    my_dict = {}
    for word in lst:
        my_dict[word] = my_dict.get(word, 0) + 1
    my_list = []
    for k, v in my_dict.items():
        if v > 1:
            n = k + 's'
            my_list.append(n)
        else:
            my_list.append(k)
    return set(my_list)

# 2nd method
from collections import Counter
def pluralize(lst):
    my_dict = Counter(lst)
    my_list = []
    for k, v in my_dict.items():
        if v > 1:
            n = k + 's'
            my_list.append(n)
        else:
            my_list.append(k)
    return set(my_list)

# Or
from collections import Counter
def pluralize(lst):
    return set((k+'s') if v>1 else k for k, v in Counter(lst).items())


# 3rd method
def pluralize(lst):
    return set([i+'s' if lst.count(i) > 1 else i for i in lst])
	#Or return {i+'s' if lst.count(i)>1 else i for i in lst}


# 4th method
def pluralize(lst):
	return set(i + 's'*(lst.count(i)>1) for i in lst)

# 5th method
def pluralize(lst):
    return set('{}s'.format(w) if lst.count(w) >= 2 else w for w in lst)

def pluralize(lst):
	x = set()
	for item in lst:
		if lst.count(item) > 1:
			x.add(item + "s")
		else:
			x.add(item)
	return x

# 6th method
def pluralize(lst):
    return dict.fromkeys([ i if lst.count(i) == 1 else i+"s" for i in lst ]).keys()


###########################################################################
########################################### #* (Encoded String Parse...)
"""
Create a function which takes in an encoded string and returns a dictionary according to the following example:

parse_code("John000Doe000123") ➞ {
    "first_name": "John",
    "last_name": "Doe",
    "id": "123"
}

parse_code("michael0smith004331") ➞ {
    "first_name": "michael",
    "last_name": "smith",
    "id": "4331"
}

parse_code("Thomas00LEE0000043") ➞ {
    "first_name": "Thomas",
    "last_name": "LEE",
    "id": "43"
}
"""
# 1st method 
def parse_code(txt):
    return dict(zip(['first_name', 'last_name', 'id'], txt.replace('0', ' ').split()))

# (testing case)
def parse_code(txt):
	my_list = txt.split("0")
	my_value = [k.replace('0', '') if len(k) >=0 for k in my_list] #wrong
	return my_value

# (testing case)
import re
def parse_code(txt):
    my_keys = ["first_name", "last_name", "id"]
    pattern = r"([a-zA-Z]+)[0]*([a-zA-Z]+)[0]*([1-9]+)"
    my_list = re.split(pattern, txt,)
    main_value = [k for k in my_list if not k.find("0")]
    my_dict = {k: v for k, v in zip(my_keys, main_value)}
    return my_dict

# * zero or more + one or more and ? is for one or two
# >>> corrected
import re
def parse_code(txt):
    pattern = re.compile(r'([a-zA-Z]+)0*([a-zA-Z]+)0*([1-9]+)$')   
    if pattern.match(txt) :
        first_name, last_name, id_number = pattern.match(txt).groups()
        my_dict = {
            "first_name": first_name,
            "last_name": last_name,
            "id": id_number}
        return my_dict
    else:
        return None


# 2nd method
my_string = "John000Doe000123"
my_list = my_string.split("0")
print(my_list) #Output : ['John', '', '', 'Doe', '', '', '123']

my_string = "John000Doe000123"
my_list = my_string.split("0",2)
print(my_list) #Output : ['John', '', '0Doe000123']


# 2nd method
def parse_code(txt):
    my_keys = ["first_name", "last_name", "id"]
    main_value = [k for k in txt.split("0") if len(k) > 0]
    my_dict = {k: v for k, v in zip(my_keys, main_value)}
    return my_dict

# OR
def parse_code(txt):
    first_name, last_name, id = [k for k in txt.split('0') if len(k)]
    return {'first_name': first_name, 'last_name': last_name, 'id': id}

# Or
def parse_code(txt):
    first_name, last_name, id = [k for k in txt.split('0') if k]
    return {'first_name': first_name, 'last_name': last_name, 'id': id}


# 3rd method
import re
def parse_code(txt):
	first, second, _id = re.split('0+', txt)
	return {'first_name': first, 'last_name': second, 'id': _id}

# 4th method
import re
def parse_code(txt):
	return dict(zip(('first_name', 'last_name', 'id'), re.split('0+', txt)))

parse_code=lambda txt:dict(zip(['first_name','last_name','id'],re.split('0+',txt)))

# 5th method
def parse_code(txt):
	f_name, l_name, ID = filter(None, txt.split('0'))
	return {'first_name':f_name, 'last_name':l_name, 'id':ID}


# 6th method
def parse_code(txt):
	templist = txt.split("0")
	while "" in templist:
			templist.remove("")
	templist2 = ["first_name", "last_name", "id"]
	return dict(zip(templist2, templist))


# 7th method
def parse_code(s: str) -> dict:
    s = list(filter(lambda e: len(e), s.replace("0", " ").split(" ")))
    return {"first_name": s[0], "last_name": s[1], "id": s[2]}

# Or
def parse_code(txt):
	d = {}
	txt = list(filter(None, txt.split("0")))
	return {"first_name": txt[0], "last_name": txt[1], "id": txt[2]}

# 8th method
import re
def parse_code(txt):
    keys = ['first_name', 'last_name', 'id']
    s = re.sub('0+', ' ', txt)
    return dict(zip(keys, s.split()))

# 9th method
def parse_code(txt):
	txt = [i for i in txt.split("0") if bool(i)==True]
	return {"first_name": txt[0] ,"last_name": txt[1] ,"id": txt[2]}

# 10th method
import re
def parse_code(txt):
	m = re.match(r'([a-zA-Z]+)0+([a-zA-Z]+)0+([1-9]+)', txt)
	return  {"first_name": m.group(1), "last_name": m.group(2),"id": m.group(3)}


###########################################################################
########################################### #* (Secret Function 4.0...)
"""
Create a function based on the input and output. Look at the examples, there is a pattern.

Examples :-
secret("p.one.two.three") ➞ "<p class='one two three'></p>"

secret("p.one") ➞ "<p class='one'></p>"

secret("p.four.five") ➞ "<p class='four five'></p>"
Notes
Input is a string.
"""
txt = "p.one.two.three"
class_value = ' '.join(txt.split('.')[1:])
print(type(class_value)) # Output : <class 'str'>
print(class_value) # Output : one two three

# 1st method
def secret(txt):
	tag, *class_value = txt.split('.')
	return "<{} class='{}'></{}>".format(tag, ' '.join(class_value), tag)

# 2nd method
def secret(txt):
    txt = txt.split('.')
    return  "<{0} class='{1}'></{0}>".format(txt[0],' '.join(txt[1:]))

# 3rd method
def secret(txt):
    txt = txt.split('.')
    tag = txt.pop(0)
    return "<" + tag + " class='" + ' '.join(txt) + "'></" + tag + ">"

# 4th method
def secret(txt):
    tag, *class_value = txt.split('.')
    return "<{tag} class='{' '.join(class_value)}'></{tag}>"

###########################################################################
########################################### #* (Remove The Word!...)
"""
Create a function that takes a list and string. The function should remove the letters in the string from the list, and return the list.

Examples
remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string") ➞ ["w"]

remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon") ➞ ["b", "g", "w"]

remove_letters(["d", "b", "t", "e", "a", "i"], "edabit") ➞ []
Notes
If number of times a letter appears in the list is greater than the number of times the letter appears in the string, the extra letters should be left behind (see example #2).
If all the letters in the list are used in the string, the function should return an empty list (see example #3).
"""
# 1st method
def remove_letters(letters, word):
	for w in word:
		if w in letters:
			letters.remove(w)
	return letters

# 2nd method
def remove_letters(lst, s):
    [lst.remove(x) for x in s if x in lst]
    return lst

# 3rd method
def remove_letters(st,c):
    for a in c:
        if a in st:
            st.pop(st.index(a))
    return st

###########################################################################
########################################### #* (Number Pairs!...)
calculater = (lambda a,b:a+b)(3,4)
print(calculater) # Output : 7
"""
Task: Create a function that determines how many number pairs are there embedded in a space-separated string. 
The first numeric value in the space-separated string represents the count of the numbers,
thus, excluded in the pairings.

Examples
number_pairs("7 1 2 1 2 1 3 2") ➞ 2
# (1, 1), (2, 2)

number_pairs("9 10 20 20 10 10 30 50 10 20") ➞ 3
# (10, 10), (20, 20), (10, 10)

number_pairs("4 2 3 4 1") ➞ 0
# although two 4's are present but
# the first one is discounted
Notes
Always take into consideration the first number in the string is not part of the pairing,
thus, the count. It may not seem so useful as most people see it,
but it's mathematically significant if you deal with set operations.

"""
# 1st method
from collections import Counter
def number_pairs(txt):
	my_list = [int(v) for v in txt.split()]
	my_count  = Counter(my_list[1:])
	count = 0
	for key, value in my_count.items():
		if value >=2 :
			count= value//2 + count
	return count

# Or 
from collections import Counter
def number_pairs(txt):
    return sum([v // 2  for k,v in Counter(txt.split()[1:]).items() if v > 1])

my_string = "9 10 20 20 10 10 30 50 10 20"
for k in my_string:
    print(k) # Output : 9 1 0 2 0 2 0 1 0 1 0 3 0 5 0 1 0 2 0


# 2nd method
def number_pairs(txt):
    my_list = [int(v) for v in txt.split()]
    my_dict = {}
    for k in my_list:
        my_dict[k] = my_dict.get(k, 0) + 1
    
    count = 0
    for key, value in my_dict.items():
        if value >= 2:
            count = count + value // 2
    return count


# 3rd method
def number_pairs(txt):
    nums = {}
    my_list = txt.split()[1:]
    pairs = 0
    for i in set(my_list):
        nums[i] = my_list.count(i)
    for key, value in nums.items():
        pairs += value // 2
    return pairs

my_string = 'abhishekyadav'
print(my_string.find('a')) #Output : 0


# 4th method
number_pairs=lambda txt:(lambda l:sum(l.count(x)//2 for x in set(l)))(txt.split()[1:])


# 5th method
def number_pairs(txt):
	mems = txt.split()[1:]
	return sum([mems.count(a)//2 for a in sorted(set(mems)) if mems.count(a)>1])

###########################################################################
########################################### #* (Tidy Hyperlinks...)
"""
Task :
Using markdown, it's possible to format links such as https://edabit.com/challenges, into something tidier like this. Notice how the text "Go to the challenges!" appears when hovering over the link.

This was achieved by using this code:

[this](https://edabit.com/challenges "Go to the challenges!")
Given the url, the new name and optionally the hover_text, return the tidied up hyperlink as a string.

Examples
tidy_link("https://edabit.com/challenges", "this", "Go to the challenges!") ➞ "[this](https://edabit.com/challenges "Go to the challenges!")"

tidy_link("https://www.google.com", "Google", "Google Search") ➞ "[Google](https://www.google.com "Google Search")"

tidy_link("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "Click Me!") ➞ "[Click Me!](https://www.youtube.com/watch?v=dQw4w9WgXcQ)"

Notes :
Supply double quotes for the hover text.
Keep in mind that some tests will not include an argument for hover_text.
"""
# 1st method
def tidy_link(url, name, *args):
    if args:
        return '[{}]({} "{}")'.format(name,url,args[0])
    return '[{}]({})'.format(name, url)

# 2nd method
def tidy_link(url, name, hover_text=None):
	if hover_text != None:
		return '[{}]({} \"{}\")'.format(name,url,hover_text)
	else:
		return '[{}]({})'.format(name,url)
# Or
def tidy_link(url, name, hover_text=''):
	return ('[{}]({} "{}")'.format(name, url, hover_text) if hover_text else '[{}]({})'.format(name, url))

# 3rd method
def tidy_link(url, name, hover_text=None):
	if hover_text:
		return '['+name+']('+url+' "'+hover_text+'")'
	else:
		return '['+name+']('+url+')'

# Note :
try:
    1/0
except Exception as e:
    print(e.with_traceback)
# >>> <built-in method with_traceback of ZeroDivisionError object at 0x000002364EFA2A40>

###########################################################################
######################################## #* (Sum of Negative Integers...)
"""
Create a function that takes a string containing integers as well as other characters and
return the sum of the negative integers only.

Examples
negative_sum("-12 13%14&-11") ➞ -23
# -12 + -11 = -23

negative_sum("22 13%14&-11-22 13 12") ➞ -33
# -11 + -22 = -33
Notes
There is at least one negative integer.
"""
# 1st method
import re
def negative_sum(chars):
    pattern = r'-\d+' # r'-[0-9]+'
    negative_numbers = re.findall(pattern, chars)    
    total = sum(map(int, negative_numbers))  
    return total


# 2nd method
import re
negative_sum = lambda chars: sum(map(int, re.findall(r'-\d+', chars)))


# 1st method
def add_bill(money):
	my_list = money.split(',')
	my_sum = 0
	for v in my_list:
		if v.startswith('d'):
			if 'k' in v:
				my_sum = my_sum + int(v[1:-1])*1000
			else:
				my_sum = my_sum + int(v[1:])
	return my_sum

# Or Also we can do
def add_bill(money):
	my_sum = 0
	for i in money.split(','):
		if i.startswith('d'):
			if i.endswith('k'):
				my_sum+=int(i[1:-1])*1000
			else:
				my_sum+=int(i[1:])
	return my_sum

# 2nd method
def add_bill(money):
    result = sum(int(v[1:-1]) * 1000 if 'k' in v else int(v[1:]) for v in money.split(',') if v.startswith('d'))
    return result


# 3rd method
import re
def add_bill(money):
    my_list = re.findall(r'd[^\s,]*', money)
    result = sum(int(k[1:-1]) * 1000 if 'k' in k else int(k[1:]) for k in my_list)
    return result


#4th method
def add_bill(money):
    return sum(int(i[1:]) for i in money.replace('k', '000').split(',') if i.startswith('d'))


# 5th method
def add_bill(money):
    return sum([eval(i[1:].replace("k", "*1000")) for i in money.split(",") if "d" in i])


# 6th method
add_bill = lambda money: sum(map(int,[i[1:] for i in money.replace("k","000").split(",") if i[0]=="d"]))
add_bill = lambda money: sum(map(int,[i[1:] for i in money.replace("k","000").split(",") if i.startswith('d')]))

###########################################################################
######################################## #* (Get the Date...)

"""
Write a function that, given a date (in the format MM/DD/YYYY), returns the day of the week as a string. Each day name must be one of the following strings: "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", or "Saturday".

To illustrate, the day of the week for "12/07/2016" is "Wednesday".
"""

# 1st method
import datetime
def get_day(day):
    # Parse the input string into a datetime object
    dt = datetime.datetime.strptime(day, "%m/%d/%Y")
    # Get the day name
    day_name = dt.strftime("%A")
    return day_name

# 2nd method
import time
def get_day(day):
    return time.strftime("%A", time.strptime(day, "%m/%d/%Y"))

# 3rd method
import datetime
def get_day(day):
	m,d,y = [int(i) for i in day.split('/')]
	days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
	return days[datetime.date(y,m,d).weekday()]

# 4th method
from datetime import*
def get_day(d):
    m,d,y=map(int,d.split("/"));
    return date(y,m,d).strftime('%A')

# 5th method
import datetime
import calendar
def get_day(d):
		month , day , year  = (int(e)  for e in d.split("/"));
		today =  datetime.datetime(year, month, day).weekday();
		return calendar.day_name[today];

# 6th method
from datetime import datetime
import calendar
def get_day(day):
	day = datetime.strptime(day, '%m/%d/%Y')
	return calendar.day_name[day.weekday()]

