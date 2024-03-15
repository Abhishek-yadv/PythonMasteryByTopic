##############################################################################
## #* (Find Domain Name From DNS Pointer (PTR) Records Using IP Address)
"""
Task :
Write a function that takes an IP address and returns the domain name using PTR DNS records.

Example
get_domain("8.8.8.8") ➞ "dns.google"
get_domain("8.8.4.4") ➞ "dns.google"
"""
# 1st method
import socket

def get_domain(ip_address):
    try:
        domain_name = socket.gethostbyaddr(ip_address)[0]
        return domain_name
    except socket.herror:
        return None

# OR 
import socket
def get_domain(ip_address):
	return socket.gethostbyaddr(ip_address)[0]

# 2nd method
from socket import getfqdn as get_domain

#####################################################################################
############################ #* (Question The Karaca's Encryption Algorithm)
"""
The Karaca's Encryption Algorithm
Make a function that encrypts a given input with these steps:

Input: "apple"
Step 1: Reverse the input: "elppa"
Step 2: Replace all vowels using the following chart:
a => 0
e => 1
i => 2
o => 2
u => 3
# "1lpp0"

Step 3: Add "aca" to the end of the word: "1lpp0aca"
Output: "1lpp0aca"

Examples
encrypt("banana") ➞ "0n0n0baca"
encrypt("karaca") ➞ "0c0r0kaca"
encrypt("burak") ➞ "k0r3baca"
encrypt("alpaca") ➞ "0c0pl0aca"
"""

# 1st method
import string
def encrypt(word):
    stp_one = word[::-1]
    my_dict = {'a': '0', 'e': '1', 'i': '2', 'o': '2', 'u': '3'}  
    stp_two = ''.join(my_dict[k] if k in my_dict else k for k in stp_one) 
    stp_three = stp_two + 'aca'
    return stp_three

# 2nd method
def encrypt(word):
    word = word[::-1]
    for r in (("a", "0"), ("e", "1"), ("o", "2"), ("u", "3")):
        word = word.replace(*r)
    return word+'aca'

# 3rd method
def encrypt(word):
    return word[::-1].replace("a", "0").replace("e", "1").replace("o", "2").replace("u", "3") + "aca"


#############################################################################
#################################### #*Question *C*ns*r*d Str*ngs
"""
C*ns*r*d Str*ngs
Someone has attempted to censor my strings by replacing every vowel with a *, l*k* th*s. Luckily,
I've been able to find the vowels that were removed.
Given a censored string and a string of the censored vowels, return the original uncensored string.

Example :-
uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") ➞ "Where did my vowels go?"
uncensor("abcd", "") ➞ "abcd"
uncensor("*PP*RC*S*", "UEAE") ➞ "UPPERCASE"
"""
# 1st method
def uncensor(txt, vowels):
    result = ""
    vowel_index = 0
    for char in txt:
        if char == "*":
            result += vowels[vowel_index]
            vowel_index += 1
        else:
            result += char
    return result

# 2nd method
def uncensor(txt, vowels):
	txt = txt.replace('*', '{}')
	return txt.format(*vowels)

# 3rd method by using iterator method
def uncensor(txt, vowels):
	vowels = iter(vowels)
	return ''.join(next(vowels) if i == '*' else i for i in txt)

# 4th method
def uncensor(t, v):
	for c in v: t = t.replace('*', c, 1)
	return t

# 5th method
def uncensor(txt, vowels):
    v = list(vowels)
    return ''.join(v.pop(0) if i == "*" else i for i in txt)

# 6th method
def uncensor(s, V):
	return s.replace('*', '%s') % tuple(V)


# 7th method
def uncensor(t, v): return t.replace('*', '{}').format(*v)


#############################################################################
#################################### #* Censor Words from List
"""
Censor Words from List
Create a function that takes a string txt and censors any word from a given list lst.
The text removed must be replaced by the given character char.

Example :-
censor_string("Today is a Wednesday!", ["Today", "a"], "-") ➞ "----- is - Wednesday!"
censor_string("The cow jumped over the moon.", ["cow", "over"], "*"), "The *** jumped **** the moon.")
censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*") ➞ "Why *** the ******* cross the ****?"
"""
# 1st method
def censor_string(txt, lst, char):
    my_list = txt.split(" ")
    new_list = []
    for k in my_list:
        if k in lst:
            new_list.append(char*len(k))
        else:
            new_list.append(k)
    return ' '.join(new_list)

# 2nd method
import re
def censor_string(text, words, symbol):
    pattern = '|'.join(map(re.escape, words))
    def replace_word(match):
        return symbol * len(match.group(0))
    return re.sub(pattern, replace_word, text)

# 3rd method
def censor_string(txt, lst, char):
    my_list = txt.split(" ")
    new_list = [char*len(k) if k in lst else k for k in my_list]        
    return ' '.join(new_list)

# 4th method
def censor_string(txt, lst, character):
    for word in lst:
        txt = txt.replace(word, character*len(word))
    return txt


#####################################################################
#################################### #* Encoded String Parse
"""
Create a function which takes in an encoded string and returns a dictionary according to the following example:
Examples
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
import re
def parse_code(txt):
	first, second, _id = re.split('0+', txt)
	return {'first_name': first, 'last_name': second, 'id': _id}
	
# 2nd method
import re
def parse_code(lst):
    return {x:y for x,y in zip(["first_name", "last_name", "id"], re.findall(r'[^0]+', lst))}

# 3rd method
def parse_code(txt):
	templist = txt.split("0")
	while "" in templist:
			templist.remove("")
	templist2 = ["first_name", "last_name", "id"]
	return dict(zip(templist2, templist))
