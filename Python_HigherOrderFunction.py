####################################################################
######################################### #*(HigherOrderFunction)
####################################################################
# Just fow know: sockets(interface/way) are not protocols themselves,
# they are built upon communication protocols like TCP/IP and UDP.

####################################################################
######################################### (Tallest Skyscraper)
"""
Tallest Skyscraper
A city skyline can be represented as a 2-D list with 1s representing buildings. In the example below, the height of the tallest building is 4 (second-most right column).
[[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 0],
[0, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1]]
Create a function that takes a skyline (2-D list of 0's and 1's) and returns the height of the tallest skyscraper.

tallest_skyscraper([
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [1, 1, 1, 1]
]) ➞ 3
"""
# 1st method
def tallest_skyscraper(lst):
    max_h = 0
    for col in zip(*lst):
        height = len(list(filter(lambda x: x == 1, col)))
        if height > max_h:
            max_h = height
    return max_h

# 2nd method
def tallest_skyscraper(lst):
	return max(sum(i) for i in zip(*lst))

# 3rd method
def tallest_skyscraper(A):
	return sum(1 in R for R in A)
"""
for R in A: This iterates over each row R in the list A.
1 in R: This checks if the value 1 is present in the current row R.
(1 in R for R in A): This creates a generator expression that yields True if 1 is present in the row R, and False otherwise, for each row R in the list A.
sum(...): This calculates the sum of the generator expression, where True values are counted as 1 and False values are counted as 0.
return ...: This returns the result of the sum, which represents the total number of rows in A that contain the value 1.
"""

# OR
def tallest_skyscraper(A):
    count = 0  # Initialize a counter variable to count occurrences of 1
    for R in A:  # Iterate through each element in list A
        if 1 in R:  # Check if 1 is present in the current element R
            count += 1  # If yes, increment the count


# 4th method
def tallest_skyscraper(lst):
	return sum(1 for i in lst if sum(i)>0)

# 1 for i in lst if sum(i)>0 could be also written as
def tallest_skyscraper(lst):
    result = []
    for i in lst: 
        if sum(i) > 0:
            result.append(1)
    return sum(result)

# 5th method
def tallestSkyscraper(lst):
	for i in range(len(lst)):
		if lst[i].count(1):
			return len(lst) - i

# 6th method
def tallest_skyscraper(lst):
    return len([row for row in lst if 1 in row])

# Or
def tallest_skyscraper(lst):
    result = []  # Initialize an empty list to store the filtered rows
    for row in lst:  # Iterate through each row in the list
        if 1 in row:  # Check if the value 1 is present in the current row
            result.append(row)  # If yes, add the row to the result list


# 7th method
def tallest_skyscraper(lst):
	for i in range(0, len(lst)):
		if 1 in lst[i]:
			return len(lst) - i

# 8th method
def tallest_skyscraper(lst):
    return max(len(lst) - lst.index(l) for l in lst if 1 in l)













