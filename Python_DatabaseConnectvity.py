############################################################
#################################### Database Connectivity
############################################################

############################################################
############################### Connect sqlite3 database
import pyodbc
import sqlite3
import os
from faker import Faker

faker_object = Faker()
result = list(faker_object.text(300).split())
age = list(range(20, 20 + len(result)))

connection = sqlite3.connect("sample.db")
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS sample")
cursor.execute("CREATE TABLE sample (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)")

cursor.executemany("INSERT INTO sample (name, age) VALUES (?,?)", zip(result, age))
connection.commit()

cursor.execute("DELETE FROM sample WHERE id < 5")
connection.commit()

cursor.execute("UPDATE sample SET AGE = 54 WHERE AGE = 25")
connection.commit()

result = cursor.execute("SELECT * FROM sample")
all_rows = result.fetchall()
for v in all_rows:print(v)
cursor.close()
connection.close()

# Using contest manager method
import sqlite3
import os
from faker import Faker

faker_object = Faker()
result = list(faker_object.text(300).split())
age = list(range(20, 20 + len(result)))

# Using context manager for database connection
with sqlite3.connect("sample.db") as connection:
    cursor = connection.cursor()  # Creating a cursor object
    
    try:
        # Executing SQL commands
        cursor.execute("DROP TABLE IF EXISTS sample")
        cursor.execute("CREATE TABLE sample (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)")
        
        # Executing many insert operations
        cursor.executemany("INSERT INTO sample (name, age) VALUES (?,?)", zip(result, age))
        connection.commit()  # Committing the transaction
        
        # Executing a delete command
        cursor.execute("DELETE FROM sample WHERE id < 5")
        connection.commit()  # Committing the transaction
        
        # Executing a select command and fetching results
        result = cursor.execute("SELECT * FROM sample")
        all_rows = result.fetchall()  # Fetching all rows
        for v in all_rows:
            print(v)
            
    except sqlite3.Error as e:
        # Rolling back in case of an error
        connection.rollback()
        print(f"An error occurred: {e}")

############################################################
############################### Connect Mysql database
# 1st method
import mysql.connector
from faker import Faker

faker_object = Faker()
result = list(faker_object.text(300).split())
age = list(range(20, 20 + len(result)))

# Using context manager for database connection
connection = mysql.connector.connect(host="localhost",user="root",password="Mysql@4900",database="sqlportfolio")
cursor = connection.cursor()  # Creating a cursor object

try:
    cursor.execute("DROP TABLE IF EXISTS sample")
    cursor.execute("CREATE TABLE sample (id INTEGER PRIMARY KEY AUTO_INCREMENT, name TEXT, age INTEGER)")
    cursor.executemany("INSERT INTO sample (name, age) VALUES (%s, %s)", list(zip(result, age)))
    connection.commit()
    
    cursor.execute("DELETE FROM sample WHERE id < 5")
    connection.commit()
    
    cursor.execute("UPDATE sample SET age = 54 WHERE age = 25")
    connection.commit()
    cursor.execute("SELECT * FROM sample")
    all_rows = cursor.fetchall()
    for v in all_rows:
        print(v)

except mysql.connector.Error as error:
    print(f"Error: {error}")

finally:
    cursor.close()
    connection.close()

# 2nd method 
import mysql.connector
from faker import Faker
faker_object = Faker()
result = list(faker_object.text(300).split())
age = list(range(20, 20 + len(result)))

try:
    with mysql.connector.connect(host = 'localhost',user = "root",password = "Mysql@4900",database = "sqlportfolio") as connection:
        cursor = connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS sample")
        cursor.execute("CREATE TABLE sample (id INTEGER PRIMARY KEY AUTO_INCREMENT, name TEXT, age INTEGER)")
        cursor.executemany("INSERT INTO sample (name, age) VALUES (%s, %s)", list(zip(result, age)))
        connection.commit()
        
        cursor.execute("DELETE FROM sample WHERE id < 5")
        connection.commit()
        
        cursor.execute("UPDATE sample SET age = 54 WHERE age = 25")
        connection.commit()
        cursor.execute("SELECT * FROM sample")
        all_rows = cursor.fetchall()
        for v in all_rows:
            print(v)

except mysql.connector.Error as error:
    print(f"Error: {error}")

finally:
    cursor.close()
    connection.close()
        
############################################################
############################### Connect Postgre database
import psycopg2
from faker import Faker
faker_object = Faker()
result = list(faker_object.text(300).split())
age = list(range(20, 20 + len(result)))

# Establishing database connection
connection = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="Postgre@4900",
    database="sample")

cursor = connection.cursor()  # Creating a cursor object

try:
    # Drop table if exists and create a new one
    cursor.execute("DROP TABLE IF EXISTS sample")
    cursor.execute("CREATE TABLE sample (id SERIAL PRIMARY KEY, name TEXT, age INTEGER)")

    # Generating fake data
    faker_object = Faker()
    result = list(faker_object.text(300).split())
    age = list(range(20, 20 + len(result)))

    # Inserting data into the table
    cursor.executemany("INSERT INTO sample (name, age) VALUES (%s, %s)", list(zip(result, age)))
    connection.commit()

    # Deleting rows where id < 5
    cursor.execute("DELETE FROM sample WHERE id < 5")
    connection.commit()

    # Updating age values
    cursor.execute("UPDATE sample SET age = 54 WHERE age = 25")
    connection.commit()

    # Selecting and printing all rows
    cursor.execute("SELECT * FROM sample")
    all_rows = cursor.fetchall()
    for row in all_rows:
        print(row)

except psycopg2.Error as error:
    print(f"Error: {error}")

finally:
    cursor.close()
    connection.close()

# 2nd method With context manager
# Establishing database connection
from faker import Faker
faker_object = Faker()
result = list(faker_object.text(300).split())
age = list(range(20, 20 + len(result)))
try:
    with psycopg2.connect(
    host="localhost",
    user="postgres",
    password="Postgre@4900",
    database="sample") as connection:
        cursor = connection.cursor()  # Creating a cursor object
        # Drop table if exists and create a new one
        cursor.execute("DROP TABLE IF EXISTS sample")
        cursor.execute("CREATE TABLE sample (id SERIAL PRIMARY KEY, name TEXT, age INTEGER)")
        
        # Generating fake data
        faker_object = Faker()
        result = list(faker_object.text(300).split())
        age = list(range(20, 20 + len(result)))
        
        # Inserting data into the table
        cursor.executemany("INSERT INTO sample (name, age) VALUES (%s, %s)", list(zip(result, age)))
        connection.commit()
    
        # Deleting rows where id < 5
        cursor.execute("DELETE FROM sample WHERE id < 5")
        connection.commit()

        # Updating age values
        cursor.execute("UPDATE sample SET age = 54 WHERE age = 25")
        connection.commit()
        
        # Selecting and printing all rows
        cursor.execute("SELECT * FROM sample")
        all_rows = cursor.fetchall()
        for row in all_rows:
            print(row)

except psycopg2.Error as error:
    print(f"Error: {error}")

finally:
    cursor.close()
    connection.close()


faker_object = Faker()
result = list(faker_object.text(300).split())
age = list(range(20, 20 + len(result)))


############################################################
############################## Connect SQL SERVER Database
from faker import Faker
faker_object = Faker()
result = list(faker_object.text(300).split())
age = list(range(20, 20 + len(result)))
# Establishing database connection
connection = pyodbc.connect(
    'DRIVER={ODBC Driver 18 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=sample;'
    'UID=your_username;'
    'PWD=your_password')

cursor = connection.cursor()  # Creating a cursor object

try:
    # Drop table if exists and create a new one
    cursor.execute("IF OBJECT_ID('sample', 'U') IS NOT NULL DROP TABLE sample")
    cursor.execute("""
    CREATE TABLE sample (
        id INT IDENTITY(1,1) PRIMARY KEY, 
        name NVARCHAR(255), 
        age INT
    )
    """)

    # Generating fake data
    faker_object = Faker()
    result = list(faker_object.text(300).split())
    age = list(range(20, 20 + len(result)))

    # Inserting data into the table
    cursor.executemany(
        "INSERT INTO sample (name, age) VALUES (?, ?)", list(zip(result, age)))
    connection.commit()

    # Deleting rows where id < 5
    cursor.execute("DELETE FROM sample WHERE id < 5")
    connection.commit()

    # Updating age values
    cursor.execute("UPDATE sample SET age = 54 WHERE age = 25")
    connection.commit()

    # Selecting and printing all rows
    cursor.execute("SELECT * FROM sample")
    all_rows = cursor.fetchall()
    for row in all_rows:
        print(row)

except pyodbc.Error as error:
    print(f"Error: {error}")

finally:
    cursor.close()
    connection.close()
