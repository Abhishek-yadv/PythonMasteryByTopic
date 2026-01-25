####################################################################
###################################################### (Collections)
####################################################################
"""1. Write a Python program that iterates over elements as many times as its count."""
from collections import Counter
def num(my_list, n):
    return Counter(my_list)[n]

# Test the function
my_list = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
n = 2
print(num(my_list, n))

"""2. Write a Python program to find the most common elements and their counts in a specified text."""
from collections import Counter
def spec_text(text):
    words = text
    word_count = Counter(words)
    most_common = word_count.most_common(1)[0]
    return most_common[0], most_common[1]
# Test the function
text = "Thisisasample text with some common words."
print(spec_text(text))

"""3. Write a Python program to create a new deque with three items and iterate over the deque's elements."""
from collections import deque
def create_deque(items):
    d = deque(items)
    for item in d:
        print(item)
# Test the function
items = [1, 2, 3]
create_deque(items)


"""4. Write a Python program to find the occurrences of the 10 most common words in a given text."""
from collections import Counter
import re
def most_common_words(text):
    # Normalize the text to lowercase and split into words
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = Counter(words)
    return word_count
    
txt = """The Python Software Foundation (PSF) is a 501(c)(3) non-profit corporation that holds the 
intellectual property rights behind the Python programming language. We manage the open source licensing 
for Python version 2.1 and later and own and protect the trademarks associated with Python.
We also run the North American PyCon conference annually,support other Python conferences around the world, and 
fund Python related development with our grants program and by funding special projects."""
print(most_common_words(txt))

"""5. Write a Python program that accepts some words and counts the number of distinct words.
Print the number of distinct 1 words and the number of occurrences of each distinct
word according to their appearance."""
from collections import Counter
def count_distinct_words(text):
    words = text.split()
    word_count = Counter(words)
    distinct_count = len(word_count)
    return distinct_count, word_count
# Test the function
text = "This is a sample text with some sample words and some more words."
distinct_count, word_count = count_distinct_words(text)
print("Number of distinct words:", distinct_count)
print("Occurrences of each distinct word:")
for word, count in word_count.items():
    print(f"{word}: {count}")
    
# 2nd method
from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
# Create an empty list 'word_array' to store words
word_array = []
n = int(input("Input number of words: "))
print("Input the words: ")
for i in range(n):
    word_array.append(input().strip())
word_ctr = OrderedCounter(word_array)
print(len(word_ctr))
for word in word_ctr:
    print(word_ctr[word], end=' ')   

"""6. Write a Python program that accepts the number of subjects, subject names and marks.
Input the number of subjects and then the subject name and marks separated by a space on the next line.
Print the subject name and marks in order of appearance."""
from collections import OrderedDict
def subject_marks(n):
    subjects = OrderedDict()
    for _ in range(n):
        subject, marks = input("Enter subject and marks: ").split()
        subjects[subject] = marks
    return subjects
# Test the function
n = int(input("Enter the number of subjects: "))
subjects = subject_marks(n)
for subject, marks in subjects.items():
    print(f"{subject}: {marks}")

"""7. Write a Python program to create a deque and append a few elements to the left and right.
Next, remove some elements from the left and right sides and reverse the deque."""
from collections import deque
def create_deque():
    d = deque()
    d.appendleft(1)
    d.append(2)
    d.append(3)
    d.append(4)
    d.popleft()
    d.pop()
    d.reverse()
    return d
# Test the function
d = create_deque()
print(d)

"""8. Write a Python program to create a deque from an existing iterable object."""
from collections import deque
def create_deque_from_iterable(iterable):
    d = deque(iterable)
    return d
# Test the function
iterable = [1, 2, 3, 4, 5]
d = create_deque_from_iterable(iterable)
print(d)

"""9. Write a Python program to add more elements to a deque object from an iterable object."""
from collections import deque
def add(d, iterable):
    d.extend(iterable)
    return d
# Test the function
d = deque([1, 2, 3])
iterable = [4, 5, 6]
d = add(d, iterable)
print(d)

"""10. Write a Python program to remove all the elements of a given deque object."""
from collections import deque
def remove_all(d):
    d.clear()
    return d
# Test the function
d = deque([1, 2, 3, 4, 5])
d = remove_all(d)
print(d)

"""11. Write a Python program that copies a deque object and verifies shallow copying."""
from collections import deque
import copy
def copy_deque(d):
    d_copy = copy.copy(d)
    return d_copy
# Test the function
d = deque([1, 2, 3, 4, 5])
d_copy = copy_deque(d)
print("Original deque:", d)
print("Copied deque:", d_copy)
print("Are they the same object?", d is d_copy)  # Should be False for shallow copy

"""12. Write a Python program to count the number of times a specific element appears in a deque object."""
from collections import deque
def count_element(d, element):
    count = d.count(element)
    return count
# Test the function
d = deque([1, 2, 3, 4, 2, 2, 3])
element = 2
count = count_element(d, element)
print(f"The element {element} appears {count} times in the deque.")

"""13. Write a Python program to rotate a Deque Object a specified number (positive) of times."""
from collections import deque
def rotate_deque(d, n):
    d.rotate(n)
    return d
# Test the function
d = deque([1, 2, 3, 4, 5])
n = 2
d = rotate_deque(d, n)
print("Rotated deque:", d)

"""14. Write a Python program to rotate a deque Object a specified number (negative) of times."""
from collections import deque
def rotate_deque_negative(d, n):
    d.rotate(-n)
    return d
# Test the function
d = deque([1, 2, 3, 4, 5])
n = -2
d = rotate_deque_negative(d, n)
print("Rotated deque:", d)

"""15. Write a Python program to find the most common element in a given list."""
from collections import Counter
def most_common_element(lst):
    count = Counter(lst)
    most_common = count.most_common(1)[0]
    return most_common[0], most_common[1]
# Test the function
lst = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
most_common, count = most_common_element(lst)
print(f"The most common element is {most_common} with a count of {count}.")

"""
16.Write a Python program to find the second lowest total marks of any student(s)
from the given names and marks of each student using lists and lambda.
Input number of students, names and grades of each student."""
from collections import defaultdict
def second_lowest_marks(n, students):
    marks = defaultdict(list)
    for student in students:
        name, mark = student.split()
        marks[mark].append(name)
    sorted_marks = sorted(marks.keys())
    if len(sorted_marks) < 2:
        return "Not enough distinct marks"
    second_lowest = sorted_marks[1]
    return second_lowest, sorted(marks[second_lowest])
# Test the function
n = int(input("Enter the number of students: "))
students = []
for _ in range(n):
    name = input("Enter the name of the student: ")
    mark = input("Enter the mark of the student: ")
    students.append(f"{name} {mark}")
second_lowest = second_lowest_marks(n, students)
print("Second lowest marks:", second_lowest)

"""17. Write a Python program to find the majority element from a given array of size n
using the Collections module."""
from collections import Counter
def majority_element(arr):
    count = Counter(arr)
    majority = len(arr) // 2
    for element, freq in count.items():
        if freq > majority:
            return element
    return None
# Test the function
arr = [1, 3, 4, 2, 3, 1, 4, 4, 4]
majority = majority_element(arr)
if majority is not None:
    print(f"The majority element is {majority}.")
else:
    print("There is no majority element.")

"""18. Write a Python program to merge more than one dictionary into a single expression."""
from collections import ChainMap
def merge_dictionaries(dicts):
    merged = ChainMap(*dicts)
    return merged
# Test the function
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'c': 5, 'd': 6}
dicts = [dict1, dict2, dict3]
merged = merge_dictionaries(dicts)
print(merged)
# or
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'c': 5, 'd': 6}
dict1.update(dict2)
dict1.update(dict3)
print(dict1)

"""19. Write a Python program to break a given list of integers into sets of a
given positive number.Return true or false."""
def break_into_sets(lst, n):
    if len(lst) % n != 0:
        return False
    sets = [lst[i:i + n] for i in range(0, len(lst), n)]
    return sets
# Test the function
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 3
sets = break_into_sets(lst, n)
print(sets)

"""20. Write a Python program to find the item with the highest frequency in a given list."""
from collections import Counter
def highest_frequency(lst):
    count = Counter(lst)
    most_common = count.most_common(1)[0]
    return most_common[0], most_common[1]
# Test the function
lst = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
highest, freq = highest_frequency(lst)
print(f"The item with the highest frequency is {highest} with a frequency of {freq}.")

"""21. Write a Python program to count the most and least common characters in a given string."""
from collections import Counter
def count_common_characters(s):
    count = Counter(s)
    most_common = count.most_common(1)[0]
    least_common = count.most_common()[-1]
    return most_common, least_common
# Test the function
s = "hello world"
count = count_common_characters(s)
print(f"Most common character: {count[0][0]} with count {count[0][1]}")
print(f"Least common character: {count[1][0]} with count {count[1][1]}")

"""22. Write a Python program to insert an element at the beginning of a given Ordered Dictionary."""
from collections import OrderedDict

def insert_at_beginning(od, key, value):
    od.update({key: value})
    od.move_to_end(key, last=False)
    return od

# Test the function
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
key = 'x'
value = 10
od = insert_at_beginning(od, key, value)
print("Ordered Dictionary after insertion:", od)

"""23. Write a Python program to get the frequency of the tuples in a given list."""
from collections import Counter
def frequency_of_tuples(lst):
    count = Counter(lst)
    return count
# Test the function
lst = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4), (1, 2)]
count = frequency_of_tuples(lst)
print("Frequency of tuples:", count)

"""24. Write a Python program to calculate the maximum aggregate from the list of tuples (pairs)."""
from collections import defaultdict
def max_aggregate(st_data):
    temp = defaultdict(int)
    for name, marks in st_data:
        temp[name] += marks
    return max(temp.items(), key=lambda x: x[1])
students = [('Juan Whelan', 90), ('Sabah Colley', 88), ('Peter Nichols', 7), ('Juan Whelan', 122), ('Sabah Colley', 84)]
print("Original list:")
print(students)
print("\nMaximum aggregate value of the said list of tuple pair:")
print(max_aggregate(students)) 

"""25. Write a Python program to find the characters in a list of strings that occur more or less
than a given number."""
from collections import Counter
def result(lst,n):
    count_items = Counter(lst)
    more_than = {item: count for item, count in count_items.items() if count > n}
    less_than = {item: count for item, count in count_items.items() if count < n}
    return more_than, less_than

# Test the function
lst = ['a', 'b', 'c', 'a', 'b', 'a', 'd', 'e']
n = 2
more_than, less_than = result(lst, n)
print("Characters occurring more than", n, "times:", more_than)
print("Characters occurring less than", n, "times:", less_than)

"""26. Write a Python program to find the difference between two lists including duplicate elements.
Use the collections module."""
from collections import Counter
def list_difference(list1, list2):
    count1 = Counter(list1)
    count2 = Counter(list2)
    diff = count1 - count2
    return list(diff.elements())
# Test the function
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
print(list_difference(list1, list2))

"""27. Write a Python program to remove duplicate words from a given string. Use the collections module."""
from collections import Counter
def remove_duplicates(s):
    words = s.split()
    count = Counter(words)
    unique_words = list(count.keys())
    return ' '.join(unique_words)
# Test the function
s = "This is a test test string with duplicate duplicate words"
print(remove_duplicates(s))

"""28. Write a Python program to create a dictionary grouping a sequence of key-value pairs
into a dictionary of lists. Use the collections module."""
from collections import defaultdict
def group_by_key(lst):
    grouped = defaultdict(list)
    for key, value in lst:
        grouped[key].append(value)
    return dict(grouped)
# Test the function
lst = [('a', 1), ('b', 2), ('c', 3), ('a', 4), ('b', 5), ('c', 6)]
grouped = group_by_key(lst)
print("Grouped dictionary:", grouped)

"""29. Write a Python program to get the frequency of elements in a given list of lists.
Use the collections module."""
from collections import Counter
def frequency_of_elements(lst):
    count = Counter(tuple(sublist) for sublist in lst)
    return count

"""30. Write a Python program to count the occurrences of each element in a given list."""
from collections import Counter
def count_occurrences(lst):
    count = Counter(lst)
    return count
# Test the function
lst = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
count = count_occurrences(lst)
print("Occurrences of each element:", count)

"""31. Write a Python program to count the most common words in a dictionary."""
from collections import Counter
def count_common_words(d):
    words = []
    for key, value in d.items():
        words.extend(value.split())
    count = Counter(words)
    return count
# Test the function
d = {'a': 'apple banana', 'b': 'banana orange', 'c': 'apple orange'}
count = count_common_words(d)
print("Most common words in the dictionary:", count)

"""32. Write a Python program to find the class wise roll number from a tuple-of-tuples."""
from collections import defaultdict
def class_wise_roll_number(tuples):
    class_roll = defaultdict(list)
    for class_name, roll_number in tuples:
        class_roll[class_name].append(roll_number)
    return dict(class_roll)
# Test the function
tuples = (('A', 1), ('B', 2), ('A', 3), ('B', 4), ('C', 5))
class_roll = class_wise_roll_number(tuples)
print("Class wise roll number:",class_roll)

"""33. Write a Python program to count the number of students in an individual class."""
from collections import defaultdict
def count_students(tuples):
    class_count = defaultdict(int)
    for class_name, _ in tuples:
        class_count[class_name] += 1
    return dict(class_count)
# Test the function
tuples = (('A', 1), ('B', 2), ('A', 3), ('B', 4), ('C', 5))
class_count = count_students(tuples)
print("Number of students in each class:", class_count)

"""34. Write a Python program to create an instance of an OrderedDict using a given dictionary.
Sort the dictionary during the creation and print the members of the dictionary in reverse order."""
from collections import OrderedDict
def create_ordered_dict(d):
    ordered_dict = OrderedDict(sorted(d.items()))
    return ordered_dict
# Test the function
d = {'b': 2, 'a': 1, 'c': 3}
ordered_dict = create_ordered_dict(d)
print("Ordered Dictionary:", ordered_dict)

"""35. Write a Python program to group a sequence of key-value pairs into a dictionary of lists."""
from collections import defaultdict
def group_by_key(lst):
    grouped = defaultdict(list)
    for key, value in lst:
        grouped[key].append(value)
    return dict(grouped)
# Test the function
lst = [('a', 1), ('b', 2), ('c', 3), ('a', 4), ('b', 5), ('c', 6)]
grouped = group_by_key(lst)
print("Grouped dictionary:", grouped)

"""36. Write a Python program to compare two unordered lists (not sets)."""
from collections import Counter
def compare_unordered_lists(list1, list2):
    if len(list1) != len(list2):
        return False
    count1 = Counter(list1)
    count2 = Counter(list2)
    return count1 == count2
# Test the function
list1 = [1, 2, 3, 4]
list2 = [4, 3, 2, 1]
print("Are the lists equal?", compare_unordered_lists(list1, list2))

"""37. Write a Python program to find the most common elements in a list."""
from collections import Counter
def most_common_elements(lst):
    count = Counter(lst)
    most_common = count.most_common(1)[0]
    return most_common[0], most_common[1]
lst = [1,2,3,4,3,2,1,1]
print(most_common_elements(lst))
