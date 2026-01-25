################################################################
################################################ (Advance List)
################################################################
"""1. Write a Python function to reverse a list at a specific location.
    Sample Data:
    ([10, 20, 30, 40, 50], 2) -> [10, 20, 50, 40, 30]
    ([1, 2, 3, 4, 5], 0) -> [5, 4, 3, 2, 1]
    ([1, 2, 3, 4], 3) -> [1, 2, 3, 4]
"""
def change(lst):
    print("inside, lst id:", id(lst))
    lst.append(4)
    print("inside after append, lst id:", id(lst))
a = [1, 2, 3]
print("before, a id:", id(a))
change(a)
print("after, a id:", id(a), "value:", a)

"""2. Write a Python function find the length of the longest increasing sub-sequence in a list.
    Sample Data:
    ([10, 9, 2, 5, 3, 7, 101, 18]) -> 4
    ([0, 1, 0, 3, 2, 3]) -> 4
    ([7, 7, 7, 7]) -> 1
"""
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role
User('Abhi')        # ❌ BROKEN
User(name='Abhi')   # ❌ missing role (clear error)

print(list(b'still allows embedded "double" quotes'))

"""3. Write a Python function that finds all the permutations of the members of a list.
    Sample Data:
    ([1, 2]) -> [[1, 2], [2, 1]]
    ([1, 2, 3]) -> [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
"""
import asyncio
import contextvars

client_addr_var = contextvars.ContextVar('client_addr')

def render_goodbye():
    # The address of the currently handled client can be accessed
    # without passing it explicitly to this function.

    client_addr = client_addr_var.get()
    return f'Good bye, client @ {client_addr}\r\n'.encode()

async def handle_request(reader, writer):
    addr = writer.transport.get_extra_info('socket').getpeername()
    client_addr_var.set(addr)

    # In any code that we call is now possible to get
    # client's address by calling 'client_addr_var.get()'.

    while True:
        line = await reader.readline()
        print(line)
        if not line.strip():
            break

    writer.write(b'HTTP/1.1 200 OK\r\n')  # status line
    writer.write(b'\r\n')  # headers
    writer.write(render_goodbye())  # body
    writer.close()

# To test it you can use telnet or curl:
#     telnet 127.0.0.1 8081
#     curl 127.0.0.1:8081

"""4. Write a Python function to find the kth smallest element in a list.
    Sample Data:
    ([7, 10, 4, 3, 20, 15], 3) -> 7
    ([7, 10, 4, 3, 20, 15], 4) -> 10
    ([1, 2, 3, 4, 5], 1) -> 1
"""
def smal_element(data, ele):
    print()
    return sorted(data, reverse=True)[ele]
print(smal_element([7, 10, 4, 3, 20, 15], 4))
"""5. Write a Python function to find the kth largest element in a list.
    Sample Data:
    ([1, 2, 3, 4, 5], 2) -> 4
    ([3, 2, 1, 5, 6, 4], 2) -> 5
    ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) -> 4
"""
import asyncio
import datetime

async def display_date():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)

asyncio.run(display_date())

"""6. Write a Python function to check if a list is a palindrome or not. Return true otherwise false.
    Sample Data:
    ([1, 2, 3, 2, 1]) -> True
    ([1, 2, 3, 4]) -> False
    (['r', 'a', 'c', 'e', 'c', 'a', 'r']) -> True
"""
def is_palindrome(lst):
    return lst == lst[::-1]
print(is_palindrome([1, 2, 3, 2, 1]))  # True
# 2nd method
def is_palindrome2(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        if lst[left] != lst[right]:
            return False
        left += 1
        right -= 1
    return True
print(is_palindrome2([1, 2, 3, 2, 1]))  # True

"""7. Write a Python a function to find the union and intersection of two lists.
    Sample Data:
    ([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]) -> Union: [1, 2, 3, 4, 5, 6, 7, 8], Intersection: [4, 5]
    ([1, 2, 3], [4, 5, 6]) -> Union: [1, 2, 3, 4, 5, 6], Intersection: []
"""
def union_intesecction(lst1,lst2):
    union_lst = list(set(lst1)| set(lst2))
    intersection_lst = list(set(lst1)&set(lst2))
    return union_lst, intersection_lst
# 2nd method
def union_intesecction2(lst1,lst2):
    union_lst = []
    intersection_lst = []
    for item in lst1:
        if item not in union_lst:
            union_lst.append(item)
    for item in lst2:
        if item not in union_lst:
            union_lst.append(item)
    for item in lst1:
        if item in lst2 and item not in intersection_lst:
            intersection_lst.append(item)
    return union_lst, intersection_lst

"""8. Write a Python function to remove duplicates from a list while preserving the order.
    Sample Data:
    ([1, 2, 3, 1, 2, 4, 5]) -> [1, 2, 3, 4, 5]
    (['a', 'b', 'a', 'c', 'b']) -> ['a', 'b', 'c']
"""
def remove_dupl(lst):
    seen = set()
    for k in lst:
        seen.append(k)
    return list(seen)
print(remove_dupl([1, 2, 3, 1, 2, 4, 5]))  # [1, 2, 3, 4, 5]
# 3rd method
def remove_dupl3(lst):
    return list(dict.fromkeys(lst))
print(remove_dupl3([1, 2, 3, 1, 2, 4, 5]))  # [1, 2, 3, 4, 5]

"""9. Write a Python a function to find the maximum sum sub-sequence in a list.
Return the maximum value.
    Sample Data:
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4]) -> 6
    ([1, 2, 3, 4, -10]) -> 10
    ([-1, -2, -3, -4]) -> -1
"""
def max_sum(lst):
    max_current = max_global = lst[0]
    for i in range(1, len(lst)):
        max_current = max(lst[i], max_current + lst[i])
        if max_current > max_global:
            max_global = max_current
    return max_global
print(max_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
# 2nd method
def max_sum2(lst):
    max_sum = float('-inf')
    n = len(lst)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += lst[j]
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum
print(max_sum2([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
"""10. Write a Python a function to find the minimum sum sub-sequence in a list.
Return the sub-sequence.
    Sample Data:
    ([1, 2, 3, -2, 5]) -> [-2]
    ([10, -5, -3, 20]) -> [-5, -3]
    ([1, 2, 3, 4]) -> [1]
"""
def min_sum(lst):
    min_current = min_global = lst[0]
    start = end = s = 0
    for i in range(1, len(lst)):
        if lst[i] < min_current + lst[i]:
            min_current = lst[i]
            s = i
        else:
            min_current += lst[i]
        if min_current < min_global:
            min_global = min_current
            start = s
            end = i
    return lst[start:end+1]
print(min_sum([1, 2, 3, -2, 5]))  # [-2]
# 2nd method
def min_sum2(lst):
    min_sum = float('inf')
    n = len(lst)
    start = end = 0
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += lst[j]
            if current_sum < min_sum:
                min_sum = current_sum
                start = i
                end = j
    return lst[start:end+1]
print(min_sum2([1, 2, 3, -2, 5]))  # [-2]

"""11. Write a Python function to find the longest common sub-sequence in two lists.
    Sample Data:
    ("AGGTAB", "GXTXAYB") -> "GTAB"
    ([1, 2, 3, 4, 1], [3, 4, 1, 2, 1, 3]) -> [3, 4, 1]
    ("abcdef", "acf") -> "acf"
"""
def lcs(X , Y):
    m = len(X)
    n = len(Y)
    L = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    index = L[m][n]
    lcs_seq = [''] * (index + 1)
    lcs_seq[index] = ''
    i = m
    j = n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs_seq[index-1] = X[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
    return ''.join(lcs_seq)
print(lcs("AGGTAB", "GXTXAYB"))  # "GTAB"
# 2nd method
def lcs2(X , Y):
    m = len(X)
    n = len(Y)
    L = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    index = L[m][n]
    lcs_seq = [''] * (index + 1)
    lcs_seq[index] = ''
    i = m
    j = n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs_seq[index-1] = X[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
    return ''.join(lcs_seq)
print(lcs2("AGGTAB", "GXTXAYB"))  # "GTAB"

"""12. Write a Python program to find the first non-repeated element in a list.
    Sample Data:
    ([1, 1, 2, 2, 3, 4, 5]) -> 3
    (['a', 'a', 'b', 'c', 'c', 'd']) -> 'b'
    ([1, 2, 3]) -> 1
"""
def non_repeated(lst):
    count = {}
    for item in lst:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    for item in lst:
        if count[item] == 1:
            return item
print(non_repeated([1, 1, 2, 2, 3, 4, 5]))  # 3
# 2nd method
def non_repeated2(lst):
    for i in range(len(lst)):
        if lst.count(lst[i]) == 1:
            return lst[i]
print(non_repeated2([1, 1, 2, 2, 3, 4, 5]))  # 3

"""13. Write a Python a function to implement a LRU cache.
    Sample Data:
    (Capacity: 2, Ops: [Put(1, 1), Put(2, 2), Get(1), Put(3, 3), Get(2)]) -> [1, -1]
    (Capacity: 3, Ops: [Put(1, 10), Put(2, 20), Put(3, 30), Get(1), Put(4, 40), Get(2)]) -> [10, -1]
"""
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.order = []

    def get(self, key: int) -> int:
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) >= self.capacity:
            lru_key = self.order.pop(0)
            del self.cache[lru_key]
        self.cache[key] = value
        self.order.append(key)
lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))  # 1
    
"""14. Write a Python function to sort a list of dictionaries based on values of a key.
    Sample Data:
    ([{'name': 'item1', 'price': 10}, {'name': 'item2', 'price': 5}], 'price') -> [{'name': 'item2', 'price': 5}, {'name': 'item1', 'price': 10}]
    ([{'id': 3}, {'id': 1}, {'id': 2}], 'id') -> [{'id': 1}, {'id': 2}, {'id': 3}]
"""
def sort_dicts(lst, key):
    return sorted(lst, key= lambda x:x[key])

"""15. Write a Python program to find all the pairs in a list whose sum is equal to a given value.
    Sample Data:
    ([1, 2, 3, 4, 5], 5) -> [[1, 4], [2, 3]]
    ([10, 20, 30, 40], 50) -> [[10, 40], [20, 30]]
    ([1, 2, 3, 4, 5, 6], 10) -> [[4, 6]]
"""
def find_pairs(lst, target_sum):
    pairs = []
    seen = set()
    for num in lst:
        complement = target_sum - num
        if complement in seen:
            pairs.append([complement, num])
        seen.add(num)
    return pairs
print(find_pairs([1, 2, 3, 4, 5], 5))  # [[1, 4], [2, 3]]
# 2nd method
from itertools import combinations
def find_pairs2(lst, target_sum):
    pairs = []
    for combo in combinations(lst, 2):
        if sum(combo) == target_sum:
            pairs.append(list(combo))
    return pairs
print(find_pairs2([1, 2, 3, 4, 5], 5))  # [[1, 4], [2, 3]]
