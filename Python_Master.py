####################################################################
################################################ (Mastering Python)
####################################################################
"""1.Create a list with values ranging from 0 to 9. """
import pandas as pd
import string
import numpy
from collections import Counter
from functools import reduce
from itertools import starmap
import numpy as np
import math
import random
my_list = list(range(1, 10))
my_list = [k for k in range(1, 10)]
my_list = []
while len(my_list) < 10:
    my_list.append(len(my_list))
# Or
i = 0
my_list = []
while i < 10:
    my_list.append(i)
    i += 1

"""2.Convert a list of integers to a list of strings."""
my_list = list(range(0, 10))
lst = list(map(str, my_list))
lst = [str(i) for i in my_list]
def lst(my_list): return [str(i) for i in my_list]

"""3.Multiply all elements in a list by 2."""
my_list = list(range(0, 10))
lst = list(map(lambda x: x*2, my_list))
lst = [i*2 for i in my_list]
print(lst)

"""4.Extract all odd numbers from a list of integers."""
my_list = list(range(0, 10))
lst = list(filter(lambda x: x % 2 != 0, my_list))
lst = [i for i in my_list if i % 2 != 0]
print(lst)

"""5.Replace all odd numbers in a list with -1."""
my_list = list(range(0, 10))
lst = list(map(lambda x: -1 if x % 2 != 0 else x, my_list))
lst = [i if i % 2 == 0 else -1 for i in my_list]

"""6. Convert a list of integers to a list of booleans where all non-zero values become True."""
my_list = list(range(0, 10))
my_list = [False if k == 0 else True for k in my_list]
my_list = [bool(k) for k in my_list]
my_list = list(map(bool, my_list))
my_list = list(map(lambda x: x != 0, my_list))

"""7.Replace all even numbers in a list with their negative."""
my_list = list(range(0, 10))
lst = list(map(lambda x: -x if x % 2 == 0 else x, my_list))
lst = [-i if i % 2 == 0 else i for i in my_list]

"""8. Create a 3x3 list of lists with random values and normalize it."""
lst = [[random.randint(0, 10) for _ in range(3)] for _ in range(3)]
lst = [[i/sum(j) if sum(j) != 0 else 0 for i in j] for j in lst]
# Or
matrix = [[random.random() for _ in range(3)] for _ in range(3)]
mean = sum(sum(row) for row in matrix) / 9
std = (sum((x - mean) ** 2 for row in matrix for x in row) / 9) ** 0.5
normalized_matrix = [[(x - mean) / std for x in row] for row in matrix]
print(normalized_matrix)

"""9. Calculate the sum of the diagonal elements of a 3x3 matrix (list of lists)."""
my_matrix = [[random.randint(0, 10) for k in range(0, 3)] for _ in range(0, 3)]
sum_diag = sum(my_matrix[i][i] for i in range(3))

"""10.Find the indices of non-zero elements in a list."""
my_matrix = [random.randint(0, 1) for _ in range(0, 10)]
my_matrix = [i for i, x in enumerate(my_matrix) if x != 0]

"""11.Reverse a list."""
my_list = list(range(0, 9))
print(list(reversed(my_list)))
print(my_list[::-1])
my_list = [my_list[k] for k in range(len(my_list)-1, -1, -1)]
print(my_list)

"""12.Create a 3x3 identity matrix as a list of lists."""
my_list = [[1 for k in range(0, 3)] for _ in range(0, 3)]
print(my_list)

"""13.Reshape a 1D list to a 2D list with 2 rows."""
my_list = list(range(10))
my_list = [my_list[i:i+5] for i in range(0, len(my_list), 5)]
my_list = [my_list[:len(my_list)//2], my_list[len(my_list)//2:]]
print(my_list)  # Improved code for all tasks

"""14.Stack two lists vertically."""
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
stacked_lst = [lst1, lst2]
print(stacked_lst)

"""15: Get the common items between two lists."""
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_items = list(set(list1) & set(list2))
common_items = [i for i in list1 if i in list2]

"""16. Create a 5x5 list of lists with row values ranging from 0 to 4. """
my_list = [[i for i in range(5)] for _ in range(5)]
print(my_list)

"""17.Find the index of the maximum value in a list."""
my_list = list(range(4))
print(my_list.index(max(my_list)))
my_list, m = list(range(4, 9)), None
for i, x in enumerate(my_list):
    if m is None or x > my_list[m]:
        m = i  # Store the index instead of the value
print(m)  # Print the index of the maximum value

my_list = list(range(4, 9))
m = max(range(len(my_list)), key=lambda i: my_list[i])
print(m)

# OR
my_list = list(range(4, 9))
max_value = my_list[0]  # Initialize with the first element
max_index = 0
for i, k in enumerate(my_list):
    if k > max_value:
        max_value, max_index = k, i
print(max_index)
print(max_value)

"""18.Normalize the values in a list between 0 and 1."""
my_list = list(range(4, 9))
max_v, min_v = max(my_list), min(my_list)
normalized_matrix = [((i - min_v) / (max_v - min_v)) for i in my_list]
print(normalized_matrix)

"""19.Calculate the dot product of two lists."""
lst_1 = list(range(4))
lst_1 = list(range(4, 8))
dot_product = sum(x * y for x, y in zip(lst_1, lst_1))
print(dot_product)

"""20.Count the number of elements in a list within a specific range."""
my_list = list(range(2, 9))


def num(lst, r):
    return len(lst[:r])
print(num(my_list, 6))

"""21.Find the mean of each row in a 2D list."""
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mean = [sum(row) / len(row) for row in my_list]
print(mean)

"""22.Create a random 4x4 list of lists and extract the diagonal elements."""
my_matrix = [[random.randint(0, 10) for k in range(4)] for _ in range(4)]
diagonal_elements = [my_matrix[i][i] for i in range(4)]
print(diagonal_elements)

"""23.Count the number of occurrences of a specific value in a list."""
my_list = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
count = my_list.count(4)
print(count)

"""24.Replace all values in a list with the mean of the list."""
my_list = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
my_mean = sum(my_list)/len(my_list)
my_list = [my_mean for i in my_list]
print(my_list)

"""25.Find the indices of the maximum and minimum values in a list."""
my_list = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
max_index = my_list.index(max(my_list))
min_index = my_list.index(min(my_list))
print(max_index)
print(min_index)

"""26.Create a 2D list with 1 on the border and 0 inside. """
my_list = [[1 if i == 0 or i == 4 or j == 0 or j ==
            4 else 0 for j in range(5)] for i in range(5)]
print(my_list)

"""27.Find the unique values and their counts in a list."""
my_list = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
unique_values = list(set(my_list))  # get unique values
unique_values_count = {i: my_list.count(i) for i in unique_values}
print(unique_values_count)

"""28.Create a 3x3 list of lists with values ranging from 0 to 8."""
my_list = [[random.randint(0, 8) for _ in range(3)] for _ in range(3)]
print(my_list)

matrix = [[i + j*3 for i in range(3)] for j in range(3)]
print(matrix)

"""29.Calculate the exponential of all elements in a list."""
my_list = [1, 2, 3, 4, 5]
my_list = [math.exp(i) for i in my_list]
print(my_list)

"""30.Swap two rows in a 2D list."""
lst1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lst1[0], lst1[1] = lst1[1], lst1[0]  # swap rows
print(lst1)

"""31.Create a random 3x3 list of lists and replace all values greater than 0.5 with 1 and all others with 0.."""
my_list = [[random.random() for _ in range(3)] for _ in range(3)]
my_list = [[1 if x > 0.5 else 0 for x in row]for row in my_list]  # replace values
print(my_list)

"""32.Find the indices of the top N maximum values in a list."""
my_list = [8, 3, 1, 9, 7, 1, 3, 2, 4, 5]
N = 3
new_list = sorted(my_list, reverse=True)
max_indices = [my_list.index(i) for i in new_list[:N]][::-1]
print(max_indices)

my_list = [8, 3, 1, 9, 7, 1, 3, 2, 4, 5]
N = 3
max_indices = sorted(range(len(my_list)), key=lambda i: my_list[i])[-N:]
print(max_indices)

# OR
my_list = [8, 3, 1, 9, 7, 1, 3, 2, 4, 5]
N = 3
max_indices = sorted(range(len(my_list)), key=my_list.__getitem__)[-N:]
print(max_indices)

"""33.Calculate the mean of each column in a 2D list."""
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def mean_lambda(lst): return [sum(row[i] for row in lst) / len(lst) for i in range(len(lst[0]))]
print(mean_lambda(my_list))

# OR
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def main():
    lst_sum = [sum(row[i] for row in my_list) for i in range(3)]
    lst_len = len(my_list)  # number of rows
    mean = [i/lst_len for i in lst_sum]
    print(mean)
main()

# OR
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lst_sum = [sum(row[i] for row in my_list) for i in range(3)]
lst_len = len(my_list)  # number of rows
mean = [i/lst_len for i in lst_sum]
print(mean)

# OR
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mean = [sum(row[i] for row in my_list) / len(my_list) for i in range(3)]
print(mean)

# OR
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mean = [sum(row)/len(my_list) for row in list(zip(*my_list))]
print(mean)

"""34.Normalize the values in each column of a 2D list."""
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
normalized_matrix = [[(x - min(col)) / (max(col) - min(col))for x in col] for col in zip(*my_list)]
print(normalized_matrix)
print(list(zip(*normalized_matrix)))
print(list(map(list, zip(*normalized_matrix))))

# OR
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
normalized_matrix = [[(x - min(col)) / (max(col) - min(col))
                for x in col] for col in zip(*my_list)]
normalized_matrix = list(map(list, zip(*normalized_matrix)))
print(normalized_matrix)

matrix = [[random.random() for _ in range(3)] for _ in range(4)]
normalized_matrix = [[(x - min(col)) / (max(col) - min(col))
                for x in col] for col in zip(*matrix)]
normalized_matrix = list(map(list, zip(*normalized_matrix)))
print(normalized_matrix)

"""35.Concatenate two lists."""
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst1.extend(lst2)
print(lst1)

# OR
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst1 = lst1 + lst2
print(lst1)

"""36.Create a 2D list with random values and sort each row."""
my_list = [[random.int(0, 10) for _ in range(3)] for _ in range(3)]
new_list = [sorted(row) for row in my_list]
new_list = list(map(lambda x: sorted(x), my_list))
print(new_list)

"""37.Check if all elements in a list are non-zero."""
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
all_non_zero = all(my_list)
print(all_non_zero)

""" 38.Find the indices of the maximum value in each row of a 2D list."""
my_list = [[random.randint(0, 10) for _ in range(3)] for _ in range(3)]
print(my_list)
max_indices = [max(range(len(row)), key=row.__getitem__) for row in my_list]
print(max_indices)

# OR
my_list = [[random.randint(0, 10) for _ in range(3)] for _ in range(3)]
print(my_list)
max_indices = [max(range(len(row)), key=lambda i: row[i]) for row in my_list]
print(max_indices)

# OR
max_indices = []
for row in my_list:
    max_index, max_value = max(enumerate(row), key=lambda x: x[1])
    max_indices.append(max_index)
print(max_indices)  # Output: [1, 0, 2]

# OR
my_list = [[random.randint(0, 10) for _ in range(4)] for _ in range(3)]
max_index = [max(row).index() for row in my_list]
print(max_index)

"""39:Create a 2D list and replace all nan values with the mean of the list."""
my_list = [[1, 2, np.nan], [4, 5, 6], [7, np.nan, 9]]
new_list = [[np.nanmean(row) if np.isnan(x) else x for x in row]
            for row in my_list]
print(new_list)

matrix = [[1, float('nan'), 3], [4, 5, float('nan')], [7, 8, 9]]
mean_val = sum(x for row in matrix for x in row if not math.isnan(
    x)) / sum(not math.isnan(x) for row in matrix for x in row)
matrix = [[mean_val if math.isnan(x) else x for x in row] for row in matrix]
print(matrix)

# OR
matrix = [[1, float('nan'), 3], [4, 5, float('nan')], [7, 8, 9]]
valid_values = [x for row in matrix for x in row if not math.isnan(x)]
mean_val = sum(valid_values) / len(valid_values)
matrix = [[mean_val if math.isnan(x) else x for x in row] for row in matrix]
print(matrix)


"""40:Calculate the mean of each row in a 2D list ignoring nan values."""
my_list = [[1, 2, np.nan], [4, 5, 6], [7, np.nan, 9]]
mean = [np.nanmean(row) for row in my_list]
print(mean)

# Or
matrix = [[1, float('nan'), 3], [4, 5, float('nan')], [7, 8, 9]]
def valid_value(row): return [x for x in row if not math.isnan(x)]
mean = [sum(valid_value(row)) / len(valid_value(row)) for row in matrix]
print(mean)

# OR
matrix = [[1, float('nan'), 3], [4, 5, float('nan')], [7, 8, 9]]
mean = [sum(x for x in row if not math.isnan(x)) /
        sum(not math.isnan(x) for x in row) for row in matrix]
print(mean)

"""41:Compute the sum of diagonal elements in a 2D list."""
my_list = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]
sum_diag = sum(my_list[i][i] for i in range(3))
print(sum_diag)

"""42:Convert radians to degrees for each element in a list."""
lst = [math.pi / 2, math.pi, 3 * math.pi / 2]
degrees_lst = [math.degrees(x) for x in lst]
print(degrees_lst)

"""43:Calculate the pairwise Euclidean distance between two lists. """
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
Eucl_dist = np.linalg.norm(np.array(lst1) - np.array(lst2))
print(Eucl_dist)

# OR
Eucl_dist = math.sqrt(sum((x - y) ** 2 for x, y in zip(lst1, lst2)))
print(Eucl_dist)

"""44:Create a list and set the values between the 25th and 75th percentile to 0."""
lst = [10, 20, 30, 40, 50]
percentile_25th = sorted(lst)[int(len(lst) * 0.25)]
percentile_75th = sorted(lst)[int(len(lst) * 0.75)]
lst = [0 if percentile_25th <= x <= percentile_75th else x for x in lst]
print(lst)

"""45:Calculate the element-wise square of the difference between two lists."""
lst1 = [1, 2, 3]
lst2 = [5, 6, 7]
squared_diff = [(x - y) ** 2 for x, y in zip(lst1, lst2)]
print(squared_diff)

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
squared_diff = list(map(lambda x, y: (x-y)**2, lst1, lst2))
print(squared_diff)

"""46:Replace all even numbers in a list with the next odd number."""
lst1 = [1, 2, 3, 4, 5, 6, 7]
my_list = [x+1 if x % 2 == 0 else x for x in lst1]
print(my_list)

"""47:Create a 2D list and normalize each column by its range."""
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
normalised_lst = [[(x - min(col)) / (max(col) - min(col)) for x in col] for col in zip(*lst)]
print(normalised_lst)

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed1 = [list(x) for x in zip(*lst)]
transposed2 = [[lst[i][j]
                for i in range(len(lst))] for j in range(len(lst[0]))]
transposed3 = []
for j in range(len(lst[0])):
    transposed3.append([lst[i][j] for i in range(len(lst))])
transposed4 = np.array(lst).T.tolist()
transposed5 = list(map(list, zip(*lst)))
transposed6 = list(starmap(list, zip(*lst)))
transposed7 = pd.DataFrame(lst).T.values.tolist()
transposed8 = reduce(lambda acc, row: [x + [y] for x, y in zip(acc, row)], lst, [[] for _ in lst[0]])
transposed9 = [[row[i] for row in lst] for i, _ in enumerate(lst[0])]

"""48:Compute the cumulative sum of elements along a given axis in a 2D list."""
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def Cum(lst, axis):
    return np.cumsum(lst, axis=axis).tolist()  # print(Cum(lst, 0))


lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def Cum(lst, axis):
    cum_lst = [[sum(l[:k+1]) for k in range(len(l))] for l in lst]
    return cum_lst if axis == 0 else list(map(list, zip(*cum_lst)))
print(Cum(lst, 0))


"""49:Check if any element in a list is non-zero."""
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
any_non_zero = any(any(row) for row in lst)
print(any_non_zero)

"""50:Compute the correlation matrix of a 2D list."""


"""51.Find the median of a list of numbers."""
lst = [1, 2, 3, 4, 5]
lst = sorted(lst)
n = len(lst)
median = (lst[n//2] + lst[~n//2]) / 2
print(median)

# OR
lst = [2, 5, 1, 3, 4]
lst.sort()
n = len(lst)
median = (lst[n//2] if n % 2 != 0 else (lst[n//2 - 1] + lst[n//2]) / 2)
print(median)

"""52:Convert a list of numbers to a list of their logarithms."""
lst = [1, 2, 3, 4, 5]
log_lst = [math.log(x) for x in lst]
lag_list = list(map(math.log, lst))
log_list = list(map(lambda x: math.log(x), lst))
print(log_lst)

"""53:Find the mode of a list of numbers."""
lst1 = [1, 2, 3, 3, 4, 5, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
mode = max(set(lst1), key=lst1.count)
print(mode)

# OR
lst1 = [1, 2, 3, 3, 4, 5, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
mode = Counter(lst1).most_common(1)[0][0]
print(mode)

"""54:Flatten a list of lists.."""
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_row = [x for row in lst for x in row]
print(flat_row)
# OR
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_row = sum(lst, [])
print(flat_row)

"""55:Transpose a 2D list."""
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = numpy.transpose(lst)
print(transposed)

# OR
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpesed = list(map(list, zip(*lst)))
transposed = [list[x] for x in zip(*lst)]
print(transposed)
# OR
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lst = [[lst[i][j] for i in range(len(lst))] for j in range(len(lst[0]))]
print(lst)

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
my_list = []
tran_lst = []
for j in range(len(lst[0])):
    tran_lst.append([lst[i][j] for i in range(len(lst))])
print(tran_lst)


"""56:Remove duplicates from a list while preserving order."""
lst = [1, 2, 3, 3, 4, 5, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
set_lst = set(lst)
print(set_lst)
unique_lst = []
for i in lst:
    if i not in unique_lst:
        unique_lst.append(i)
print(unique_lst)

lst = [1, 2, 2, 3, 4, 4, 5]
seen = set()
unique_lst = [x for x in lst if not (x in seen or seen.add(x))]
print(unique_lst)

# OR
"""57:Find the intersection of two lists."""
lst1 = [1, 2, 3, 4, 5]
lst2 = [4, 5, 6, 7, 8]
intersection = list(set(lst1) & set(lst2))
print(intersection)
# OR
lst1 = [1, 2, 3, 4, 5]
lst2 = [4, 5, 6, 7, 8]
lst3 = []
for i in lst1:
    if i in lst2:
        lst3.append(i)
print(lst3)

"""58:Merge two dictionaries.."""
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
# Method 1
dict1.update(dict2)
print(dict1)
# Method 2
dict1 = {**dict1, **dict2}
print(dict1)

"""59:Sort a list of dictionaries by a key."""
my_dict = [{'name': 'Alice', 'age': 40}, {
    'name': 'Bob', 'age': 30}, {'name': 'Carl', 'age': 20}]
sorted_dict = sorted(my_dict, key=lambda x: x['age'])
print(sorted_dict)

"""60:Filter a dictionary based on its values."""
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filter_dict = {k: v for k, v in my_dict.items() if v > 2}
print(filter_dict)

"""61:Create a dictionary from two lists."""
lst1 = [1, 2, 3, 4]
lst2 = ['a', 'b', 'c', 'd']
my_dict = dict(zip(lst2, lst1))
print(my_dict)

"""62:Find the maximum value in a dictionary."""
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Method 1
max_value = max(dict1.value(), key=dict1.get)
print(max_value)
# Method 2
max_value = max(dict1.values())
print(max_value)

"""63:Invert a dictionary (swap keys and values)."""
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Method 1
my_dict = {v: k for k, v in dict1.items()}
print(my_dict)
# Method 2
dict2 = dict((v, k) for k, v in dict2.items())
print(dict2)
# method 3

"""64:Create a dictionary with a default value."""
lst1 = [1, 2, 3, 4]
default_value = 0
my_dict = {k: default_value for k, v in dict1.items()}
print(my_dict)

"""65:Convert a dictionary to a list of tuples."""
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
my_list = list(dict1.items())
print(my_list)

"""66:Find the length of the longest string in a list."""
lst = ['apple', 'banana', 'cherry']
print(max(lst, key=len))

"""67:Reverse the words in a sentence."""
sentence = 'Python is cool'
words = sentence.split()
reversed_sentence = ' '.join(reversed(words))
print(reversed_sentence)
# OR
sentence = 'Python is cool'
reversed_sentence = " ".join(sentence.split()[::-1])
print(reversed_sentence)

"""68:Check if a string is a palindrome."""
string = 'madam'
is_palindrome = string == string[::-1]
print(is_palindrome)
# OR


def is_palindrome(string):
    return string == string[::-1]
print(is_palindrome('madam'))

"""69:Remove punctuation from a string."""
sentence = 'Python is cool!'
sentence = sentence.translate(str.maketrans('', '', string.punctuation))
print(sentence)

"""70:Count the occurrences of each character in a string."""
my_string = 'hello'
my_dict = {char: my_string.count(char) for char in set(my_string)}
print(my_dict)

"""71:Find the longest common prefix among a list of strings."""
import os
lst = ['flower', 'flow', 'flowight']
longest_prefix = os.path.commonprefix(lst)
print(longest_prefix)

# OR
lst = ['flower', 'flow', 'flowight']
longest_prefix = ''
for chars in zip(*lst):
    print(chars)
    if len(set(chars)) == 1:
        longest_prefix += chars[0]
    else:
        break   # Stop when the characters are different
print(longest_prefix)

# OR
lst = ['flower', 'flow', 'flowight']
longest_prefix = ''
for i in range(len(min(lst))):
    if len(set([word[i] for word in lst])) == 1:
        longest_prefix += lst[0][i]
    else:
        break   # Stop when the characters are different
print(longest_prefix)
    

"""72:Convert a string to a list of characters."""
my_string = 'hello'
my_list = list(my_string)
print(my_list)

"""73:Generate a list of random integers."""
import random
my_list = [random.randint(0, 10) for _ in range(5)]
print(my_list)

"""74:Shuffle a list."""
import random
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)

"""75:Generate a random password of a given length."""
import random
import string
def random_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password
print(random_password(8))

"""76:Calculate the factorial of a number"""
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
# OR
import functools
@functools.lru_cache()
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1) # Using recursion
print(factorial(5))

"""77:Calculate the Fibonacci sequence up to a given number of terms."""
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
print(list(fibonacci(5)))

"""78:Check if a number is prime.."""
def Is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
print(Is_prime(11))

"""79:Find the greatest common divisor (GCD) of two numbers.."""
import math
def gcd(a, b):
    return math.gcd(a, b)
print(gcd(12, 15))
# OR
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(gcd(12, 15))

"""80:Find the least common multiple (LCM) of two numbers."""
def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)
print(lcm(12, 15))
# OR
def lcm(a, b):
    return abs(a*b) // gcd(a, b)
print(lcm(12, 15))

"""81:Sort a list of tuples by the second element."""
my_list = [(1, 2), (3, 1), (5, 3), (1, 1)]
sorted_list = sorted(my_list, key=lambda x: x[1])
print(sorted_list)

"""82:Find the second largest number in a list."""
my_list = [1, 2, 3, 4, 5]
second_largest = sorted(set(my_list))[-2]
print(second_largest)

# OR
my_list = [1, 2, 3, 4, 5]
max_value = max(my_list)
second_largest = max(x for x in my_list if x != max_value)
print(second_largest)
# OR
my_list = [1, 2, 3, 4, 5]
max_value = None
second_largest = None
for x in my_list:
    if max_value is None or x > max_value:
        second_largest = max_value
        max_value = x
    elif second_largest is None or x > second_largest:
        second_largest = x
print(second_largest)

"""83:Check if a list is a palindrome.."""
my_list = [1, 2, 3, 2, 1]
is_palindrone = my_list == my_list[::-1]
print(is_palindrone)

"""84:Find the sum of the digits of a number."""
number = 12345
sum_digits = sum(int(digit) for digit in str(number))
print(sum_digits)

"""85:Find the product of the digits of a number."""
import math
number = 12345
product_digits = math.prod(int(digit) for digit in str(number))
print(product_digits)

pro_lst = 1
for k in str(number):
    pro_lst = pro_lst*int(k)
print(pro_lst)

"""86:Check if a string is a valid number."""
s = "123.45"
try:
    float(s)
    print("Valid number")
except ValueError:
    print("Invalid number")
    
"""87:Find the length of the longest word in a sentence."""
s = "This is a test sentence"
long_word = max(len(k) for k in s.split())
long = [k for k in s.split() if len(k)==long_word]
print(long)

s = "This is a test sentence"
long_word = max(len(k) for k in s.split())
long = [k for k in s.split() if len(k)==long_word]
print(long)

# OR
s = "This is a test sentence"
long_word = max(s.split(), key=len)
print(long_word)

"""88:Convert a list of tuples to a dictionary."""
my_list = [('a', 1), ('b', 2), ('c', 3)]
my_dict = dict(my_list)
print(my_dict)

"""89:Filter a list of dictionaries based on a key value."""
lst = [{'name': 'Vivek', 'age': 25}, {'name': 'Esther', 'age': 22}, {'name': ' Neassa', 'age': 28}]                            
filtered_lst = [x for x in lst if x['age'] > 23]
print(filtered_lst)

"""90:Sort a list of tuples by multiple keys."""
lst = [(' Aisha', 'A', 25), (' Remy', 'B', 22), ('Meine', 'A', 28)]
sorted_lst = sorted(lst, key=lambda x: (x[1], x[2]))
print(sorted_lst)

"""91:Merge two lists into a dictionary, using one as keys and the other as values."""
lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c']
my_dict = dict(zip(lst1, lst2))

"""92:Create a dictionary with keys as numbers and values as their squares."""
my_dict = {k:k**2 for k in range(1, 11)}
print(my_dict)

"""93:Check if two strings are anagrams."""
s1 = "listen"
s2 = "silent"
is_anagram = sorted(s1) == sorted(s2)
print(is_anagram)

"""94:Count the number of vowels in a string."""
vowels = "aeiouAEIOU"
count = 0
for char in s:
    if char in vowels:
        count += 1
print(count)

s = "hello world"
vowel_count = sum(1 for char in s if char in 'aeiou')
print(vowel_count)

"""95:Check if a string contains only digits.."""
my_str = "12345"
is_digit = my_str.isdigit()

"""96:Find the first non-repeated character in a string."""
s = "hello world"
first_non_repeated = next((char for char in s if s.count(char) == 1), None)
print(first_non_repeated)

"""97:Reverse each word in a sentence."""
s = "hello world"
reversed_words = " ".join(reversed(word) for word in s.split())
print(reversed_words)

"""98:Generate a list of Fibonacci numbers up to a given number."""
n = 10
fibonacci = [0, 1] + [fibonacci[i] + fibonacci[i+1] for i in range(2, n)]
print(fibonacci)

"""99:Remove all whitespaces from a string."""
s = "hello world "
s = s.strip()
print(s)

s = " a b c d "
s_without_whitespace = s.replace(' ', '')
print(s_without_whitespace)

"""100:Replace all occurrences of a substring in a string."""
s = "Hello world, welcome to the world of Python family."
new_s = s.replace('world', 'universe')
print(new_s)



