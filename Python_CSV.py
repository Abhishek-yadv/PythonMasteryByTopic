#############################################################
########################################## #*CSV
# csv : The csv module implements classes to read and write tabular data in CSV format.
# Importtant function
# * csv.reader(csvfile, dialect='excel', **fmtparams) : Reads data from a CSV file.
"""
csvfile: File object or an iterable of lines (like a list of strings).
dialect: Specifies a dialect for parsing. Default is 'excel'.
**fmtparams: Optional additional formatting parameters.
"""
with open('example.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(row)

# * csv.writer(csvfile, dialect='excel', **fmtparams)¶ :Writes data to a CSV file.
"""
file_object: File object to write to.
dialect: Specifies a dialect for parsing. Default is 'excel'.
**fmtparams: Optional additional formatting parameters.
"""

# Writer Objects
"""
#* csvwriter.writerows(row) : Writes multiple rows to a CSV file at once.
Write all elements in rows (an iterable of row objects as described above) to the writer’s file object,
formatted according to the current dialect.
"""
import csv
data = [
    ['Name', 'Age', 'City'],
    ['John', '25', 'New York'],
    ['Alice', '30', 'Los Angeles'],
    ['Bob', '35', 'Chicago']
]
with open('example_output.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(data)

# * csvwriter.writerow(row) :
"""
Write the row parameter to the writer’s file object, formatted according to the current Dialect.
Return the return value of the call to the write method of the underlying file object.
"""
data = [
    ['Name', 'Age', 'City'],
    ['John', '25', 'New York'],
    ['Alice', '30', 'Los Angeles'],
    ['Bob', '35', 'Chicago']
]

with open('example_output.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    for row in data:
        csvwriter.writerow(row)

with open('example_output.csv', 'r') as file_handle:
    data = csv.reader(file_handle)
    for row in data:
        print(row)

####################################################################################################
#### 1. Write a python program to read each row from a given csv file and print a list of strings.
#  create a sample data
import csv
data = [
    ["Name", "Age", "City"],
    ["John", 25, "New York"],
    ["Alice", 30, "Los Angeles"],
    ["Bob", 35, "Chicago"]]
with open("sample.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(data)

# Answer
def csv_reader(filename):
    import csv
    with open(filename, "r", newline="") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            print(",".join(row))


######################################################################################
#### 2.  Write a Python program to read a given CSV file having tab delimiter.
def csv_reader(filename):
    import csv
    with open(filename, "r", newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter='\t')
        for row in csvreader:
            print(",".join(row))


######################################################################################
#### 3.  Write a Python program to read a given CSV file as a list.
def csv_reader(filename):
    import csv
    with open(filename, "r", newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter='\t')
        print(list(csvreader))
csv_reader('sample.csv')

######################################################################################
#### 4. Write a Python program to read a given CSV file as a dictionary.
def csv_reader(filename):
    import csv
    with open(filename, "r", newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter='\t')
        print(dict(csvreader))
csv_reader('sample.csv')

######################################################################################
#### 5. Write a Python program to read a given CSV files with initial spaces
# after a delimiter and remove those initial spaces.
import csv
with open('sample.csv', 'r') as file_handle:
    csvreader = csv.reader(file_handle, skipinitialspace=False)
    for k in csvreader:
        ', '.join(k)
print("\n\nWithout initial spaces after a delimiter:\n")

with open('sample.csv', 'r') as file_handle:
    csvreader = csv.reader(file_handle, skipinitialspace=True)
    for k in csvreader:
        ', '.join(k)

######################################################################################
#### 6. Write a Python program that reads a CSV file and remove initial spaces
# quotes around each entry and the delimiter.
# 1st method
import csv
def process_csv(input_file, output_file, delimiter='|'):
    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter)
        rows = list(reader)

    for row in rows:
        for i in range(len(row)):
            row[i] = row[i].strip().strip('"')
    
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=delimiter)
        writer.writerows(rows)

input_file = 'sample_file.csv'
output_file = 'temp.csv'
process_csv(input_file, output_file)

# 2nd method
import csv
csv.register_dialect('csv_dialect',delimiter='|',skipinitialspace=True,quoting=csv.QUOTE_ALL)
with open('sample.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, dialect='csv_dialect')
    for row in reader:
        print(row)

######################################################################################
######## 7. Write a Python program to read specific columns of a given CSV file
# and print the content of the columns.
import csv
my_list = []
def column_read(filename,n):
    with open(filename, 'r') as file_handle:
        csvreader = csv.reader(file_handle)
        for row in csvreader:
            my_list.append(row)
    my_column = list(zip(*my_list))
    return my_column[n]

print(column_read("sample.csv",2)) # change filename and number accordingly

# 2nd method more efficient 
import csv
def column_read(filename, column_index):
    with open(filename, 'r', newline='') as file_handle:
        csvreader = csv.DictReader(file_handle)
        for row in csvreader:
            yield row.get(csvreader.fieldnames[column_index])

column_num = 2  # column num you want to read
for value in column_read("sample.csv", column_num):
    print(value)

# 3rd method
import csv
def read_column(filename, column_name):
    with open(filename, 'r', newline='') as file_handle:
        csvreader = csv.DictReader(file_handle)
        for row in csvreader:
            print(row(column_name))
read_column("sample.csv", 'age')


######################################################################################
### 8. Write a Python program that reads each row of a given csv file and skip
# the header of the file. Also print the number of rows and the field names.
import csv
my_list = []
def read_column(filename, column_name):
    with open(filename, 'r', newline='') as file_handle:
        csvreader = csv.reader(file_handle, )
        for row in csvreader:
            my_list.append(row)
    print(*my_list[1:], sep = '\n')
    print('fileds name are {}'.format(*zip(my_list)))
    l = len(my_list)
    return print(l)
read_column("sample.csv", 'age')

# 2nd method
import csv
fields = []
rows = []
with open('sample.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=' ', quotechar=',')
    # Following command skips the first row of the CSV file.
    fields = next(data)
    for row in data:
        print(', '.join(row))
print("\nTotal no. of rows: %d" % (data.line_num))
print('Field names are:')
print(', '.join(field for field in fields))

######################################################################################
#### 9. Write a Python program to create an object for writing and iterate over the rows to print the values.
import csv
def writing_object(filename):
    with open(filename, 'w') as file_handle:
        csvwriter = csv.writer(file_handle)
        lines = [["John Smith","50"], ["Eric Johnson","34"]]
        for line in range(len(lines)):
            csvwriter.writerow(line)
            print(line)
writing_object('sample.csv')
        

######################################################################################
#### 10. Write a Python program to write a Python list of lists to a csv file.
# After writing the CSV file read the CSV file and display the content.
from itertools import zip_longest
import calendar
day_nam = list(calendar.day_name)
month_name = list(calendar.month_name)
my_list = []
for k,v in zip_longest(day_nam,month_name):
    my_list.append([k,v])

import csv
with open('pappu.csv','w') as file_handle:
    writer_object = csv.writer(file_handle)
    writer_object.writerows(my_list)

import csv
with open('pappu.csv', 'r', newline='') as file_handle:
    csv_reader = csv.reader(file_handle)
    for line in csv_reader:
        print(line)

################################################################
# 11. Write a Python program to write a Python dictionary to a csv file.
# After writing the CSV file read the CSV file and display the content.
import calendar
import csv

month_name = list(calendar.month_name)
my_dict = dict()
for k, v in enumerate(month_name):
    my_dict[k] = v

with open('pu.csv', 'w', newline='') as file_handle:
    fieldnames = ['Key', 'Month']  # Specify the fieldnames
    writer_object = csv.DictWriter(file_handle, fieldnames=fieldnames)
    writer_object.writeheader()  # Write the header row
    for key, value in my_dict.items():
        writer_object.writerow({'Key': key, 'Month': value})

# Read the CSV file and print its contents
with open('pu.csv', 'r', newline='') as file_handle:
    csv_reader = csv.DictReader(file_handle)
    for line in csv_reader:
        print(line)
