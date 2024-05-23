###########################################################
##################################################### OOP
###########################################################

##########################################################
""" 
*Question 1:
1. Write a Python program to create a class representing a Circle.
Include methods to calculate its area and perimeter.
"""
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius**2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

circle_obj = Circle(5)
print(circle_obj.area())
print(circle_obj.perimeter())

####################################################################
""" 
*Question 2:
2. Write a Python program to create a person class. Include attributes like name,
country and date of birth. Implement a method to determine the person's age.
"""
from datetime import date
class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
        
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        # Or if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
        # age = age - 1
        return age

person1 = Person("Ferdi Odilia", "France", date(1962, 7, 12))
person2 = Person("Shweta Maddox", "Canada", date(1982, 10, 20))
person3 = Person("Elizaveta Tilman", "USA", date(2000, 1, 1))

print(person1.name, "is", person1.age(), "years old.")
print(person2.name, "is", person2.age(), "years old.")
print(person3.name, "is", person3.age(), "years old.")


from datetime import date
class Person:
    # Initialize the Person object with a name, country, and date of birth
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    # Calculate the age of the person based on their date of birth
    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if date.today().day > self.date_of_birth.day:
            return today.year - self.date_of_birth.year - 1
        else:
            return today.year - self.date_of_birth.year
        
# Example usage
# Create three Person objects with different attributes
person1 = Person("Ferdi Odilia", "France", date(1962, 7, 12))
person2 = Person("Shweta Maddox", "Canada", date(1982, 10, 20))
person3 = Person("Elizaveta Tilman", "USA", date(2000, 1, 1))

# Access and print the attributes and calculated age for each person
print("Person 1:")
print("Name:", person1.name)
print("Country:", person1.country)
print("Date of Birth:", person1.date_of_birth)
print("Age:", person1.calculate_age())

print("\nPerson 2:")
print("Name:", person2.name)
print("Country:", person2.country)
print("Date of Birth:", person2.date_of_birth)
print("Age:", person2.calculate_age())

print("\nPerson 3:")
print("Name:", person3.name)
print("Country:", person3.country)
print("Date of Birth:", person3.date_of_birth)
print("Age:", person3.calculate_age())

####################################################################
""" 
Question 3:
Write a Python program to create a calculator class.
Include methods for basic arithmetic operations.
"""
# Define a class called Calculator to perform basic arithmetic operations
class Calculator:
    def add(self, x, y):
        return x + y
    def subtract(self, x, y):
        return x - y
    def multiply(self, x, y):
        return x * y
    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return ("Cannot divide by zero.")
calculator = Calculator()
result = calculator.add(7, 5)
print("7 + 5 =", result)
result = calculator.subtract(34, 21)
print("34 - 21 =", result)
result = calculator.multiply(54, 2)
print("54 * 2 =", result)
result = calculator.divide(144, 2)
print("144 / 2 =", result)
result = calculator.divide(45, 0)
print("45 / 0 =", result)

#####################################################################
""" 
Question 4:
4. Write a Python program to create a class that represents a shape. Include methods
to calculate its area and perimeter.Implement subclasses for different shapes like circle, 
triangle, and square.
"""
import math
class Shape:
    def __init__(self, name):
        self.name = name

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, name, base, height, side1, side2, side3):
        super().__init__(name)
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

class Square(Shape):
    def __init__(self, name, side_length):
        super().__init__(name)
        self.side_length = side_length
    
    def area(self):
        return self.side_length ** 2
    
    def perimeter(self):
        return 4 * self.side_length

# Example usage:
circle = Circle("Circle", 5)
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())

triangle = Triangle("Triangle", 6, 8, 10, 10, 10)
print("Triangle Area:", triangle.area())
print("Triangle Perimeter:", triangle.perimeter())

square = Square("Square", 4)
print("Square Area:", square.area())
print("Square Perimeter:", square.perimeter())


#####################################################################
""" 
5. Write a Python program to create a class representing a binary search tree.
Include methods for inserting and searching for elements in the binary tree.
"""
# Define a class called Node to represent a node in a binary search tree (BST)
class Node:
    # Initialize the Node object with a value, and set the left and right child pointers to None
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Define a custom __str__ method to convert the node's value to a string
    def __str__(self):
        return str(self.value)

# Define a class called BinarySearchTree to represent a binary search tree
class BinarySearchTree:
    # Initialize the BST with an empty root node
    def __init__(self):
        self.root = None

    # Insert a value into the BST
    def insert(self, value):
        # If the root is None, create a new node with the given value as the root
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    # Helper method to recursively insert a value into the BST
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    # Search for a value in the BST
    def search(self, value):
        return self._search_recursive(self.root, value)

    # Helper method to recursively search for a value in the BST and return the node if found
    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

# Example usage
# Create an instance of BinarySearchTree
bst = BinarySearchTree()

# Insert values into the BST
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

# Search for elements in the BST and print the results
print("Searching for elements:")
print(bst.search(4))  # Found, returns the node (4)
print(bst.search(9))  # Not found, returns None 

#####################################################################
""" 
6. Write a Python program to create a class representing a stack data structure.
Include methods for pushing and popping elements.
"""
# Define a class called Stack to implement a stack data structure
class Stack:
    # Initialize the stack with an empty list to store items
    def __init__(self):
        self.items = []

    # Push an item onto the stack
    def push(self, item):
        self.items.append(item)

    # Pop (remove and return) an item from the stack if the stack is not empty
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Cannot pop from an empty stack."

    # Check if the stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # Get the number of items in the stack
    def size(self):
        return len(self.items)

    # Peek at the top item of the stack without removing it, if the stack is not empty
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Empty stack."

# Example usage
# Create an instance of the Stack class
stack = Stack()

# Push items onto the stack
stack.push(0)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

# Print the size of the stack and the top element
print("Stack size:", stack.size())
print("Top element:", stack.peek())

# Pop an item from the stack, and print the popped item, and the updated size and top element
popped_item = stack.pop()
print("\nPopped item:", popped_item)
print("\nStack size:", stack.size())
print("Top element:", stack.peek())

# ----------------------------------------
# Create another instance of the Stack class
stack1 = Stack()

# Print the size of the empty stack and attempt to pop an item (with an error message)
print("\nStack size:", stack1.size())
popped_item = stack1.pop()
print("\nPopped item:", popped_item)

#####################################################################
""" 
8. Write a Python program to create a class representing a shopping cart.
Include methods for adding and removing items, and calculating the total price.
"""
class Cart:
    def __init__(self):
        self.items = {}
    def add(self):
        while True:
            key = input("Enter item: ")
            value = input("Enter item price: ")
            # Validate if the price is a number
            try:
                value = float(value)
            except ValueError:
                print("Invalid price. Please enter a numeric value.")
                continue
            self.items[key] = value
            more_items = input(
                "Do you want to add one more item (Y/N): ").strip().upper()
            if more_items == "N":
                break
    def remove(self):
        item_to_remove = input("Enter item to remove: ")
        if item_to_remove in self.items:
            del self.items[item_to_remove]
            print(f"Item '{item_to_remove}' removed.")
        else:
            print(f"Item '{item_to_remove}' not found in the cart.")
    def calculate_total(self):
        total = sum(self.items.values())
        return total
    def show_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Your cart contains:")
            for item, price in self.items.items():
                print(f"{item}: ${price:.2f}")

# Example usage:
my_instance = Cart()
my_instance.add()
my_instance.show_cart()
print(f"Total price: ${my_instance.calculate_total():.2f}")
my_instance.remove()
my_instance.show_cart()
print(f"Total price: ${my_instance.calculate_total():.2f}")


#####################################################################
""" 
9. Write a Python program to create a class representing a stack data structure.
Include methods for pushing, popping and displaying elements.
"""
# Define a class called Stack to implement a stack data structure
class Stack:
    # Initialize the stack with an empty list to store items
    def __init__(self):
        self.items = []
    # Push an item onto the stack
    def push(self, item):
        self.items.append(item)
    # Pop (remove and return) an item from the stack if the stack is not empty
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Cannot pop from an empty stack.")
    # Check if the stack is empty
    def is_empty(self):
        return len(self.items) == 0
    # Display the items in the stack
    def display(self):
        print("Stack items:", self.items)
# Example usage
# Create an instance of the Stack class
stack = Stack()

# Push items onto the stack
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

# Display the items in the stack
stack.display()

# Pop items from the stack and print the popped items
popped_item = stack.pop()
print("Popped item:", popped_item)
popped_item = stack.pop()
print("Popped item:", popped_item)

# Display the updated items in the stack
stack.display()

#####################################################################
""" 
10. Write a Python program to create a class representing a queue data structure. 
Include methods for enqueueing and dequeueing elements.
"""
# Define a class called Queue to implement a queue data structure
class Queue:
    # Initialize the queue with an empty list to store items
    def __init__(self):
        self.items = []

    # Add (enqueue) an item to the end of the queue
    def enqueue(self, item):
        self.items.append(item)

    # Remove and return (dequeue) an item from the front of the queue if the queue is not empty
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Cannot dequeue from an empty queue.")

    # Check if the queue is empty
    def is_empty(self):
        return len(self.items) == 0

# Create an instance of the Queue class
queue = Queue()

# Enqueue (add) items to the queue
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

# Print the current items in the queue
print("Current Queue:", queue.items)

# Dequeue (remove) items from the front of the queue and print the dequeued items
dequeued_item = queue.dequeue()
print("Dequeued item:", dequeued_item)
dequeued_item = queue.dequeue()
print("Dequeued item:", dequeued_item)

# Print the updated items in the queue
print("Updated Queue:", queue.items)

#####################################################################
""" 
11. Write a Python program to create a class representing a bank.
Include methods for managing customer accounts and transactions.
"""
# Define a class called Bank to implement a simple banking system
class Bank:
    # Initialize the bank with an empty dictionary to store customer accounts and balances
    def __init__(self):
        self.customers = {}
    # Create a new account with a given account number and an optional initial balance (default to 0)
    def create_account(self, account_number, initial_balance=0):
        if account_number in self.customers:
            print("Account number already exists.")
        else:
            self.customers[account_number] = initial_balance
            print("Account created successfully.")

    # Make a deposit to the account with the given account number
    def make_deposit(self, account_number, amount):
        if account_number in self.customers:
            self.customers[account_number] += amount
            print("Deposit successful.")
        else:
            print("Account number does not exist.")

    # Make a withdrawal from the account with the given account number
    def make_withdrawal(self, account_number, amount):
        if account_number in self.customers:
            if self.customers[account_number] >= amount:
                self.customers[account_number] -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient funds.")
        else:
            print("Account number does not exist.")

    # Check and print the balance of the account with the given account number
    def check_balance(self, account_number):
        if account_number in self.customers:
            balance = self.customers[account_number]
            print(f"Account balance: {balance}")
        else:
            print("Account number does not exist.")

# Example usage
# Create an instance of the Bank class
bank = Bank()

# Create customer accounts and perform account operations
acno1 = "SB-123"
damt1 = 1000
print("New a/c No.: ", acno1, "Deposit Amount:", damt1)
bank.create_account(acno1, damt1)

acno2 = "SB-124"
damt2 = 1500
print("New a/c No.: ", acno2, "Deposit Amount:", damt2)
bank.create_account(acno2, damt2)
wamt1 = 600
print("\nDeposit Rs.", wamt1, "to A/c No.", acno1)
bank.make_deposit(acno1, wamt1)
wamt2 = 350
print("Withdraw Rs.", wamt2, "From A/c No.", acno2)
bank.make_withdrawal(acno2, wamt2)
print("A/c. No.", acno1)
bank.check_balance(acno1)
print("A/c. No.", acno2)
bank.check_balance(acno2)
wamt3 = 1200
print("Withdraw Rs.", wamt3, "From A/c No.", acno2)
bank.make_withdrawal(acno2, wamt3)
acno3 = "SB-134"
print("A/c. No.", acno3)
bank.check_balance(acno3)  # Non-existent account number

            
