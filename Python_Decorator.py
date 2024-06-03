###########################################################
############################################# Decorator
###########################################################
# Reminder:
def my_dec(fun):
    def wrapper():
        print("*****************")
        fun()
        print("*****************")
    return wrapper
@my_dec
def hello():
    print("Hello world")
hello()

##########################################################
""" 
*Question 1:
1. Write a Python program to create a decorator that logs
the arguments and return value of a function.
"""
def log(func):
    def wrapper(*args, **kwargs):
        print("Arguments:", args, kwargs)
        result = func(*args, **kwargs)
        print("Return Value:", result)
        return result
    return wrapper
def add(a, b):
    return a + b
# Manually apply the decorator to the function
add = log(add)
# Now, when you call the decorated function `add`, it will log its arguments and return value.
add(3, 5)

# 2nd method
def log(func):
    def wrapper(*args, **kwargs):
        print("Arguments:", args, kwargs)
        result = func(*args, **kwargs)
        print("Return Value:", result)
        return result
    return wrapper
@log
def add(a, b, c:4):
    return a+b
add(3,4,5)

##########################################################
""" 
*Question 2:
2. Write a Python program to create a decorator function to measure
the execution time of a function.
"""
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)  # Pass arguments to the decorated function
        end = time.time()
        return end - start, result  # Return both the execution time and the result
    return wrapper
@timer
def add(a, b):
    return a + b

e,r = add(2,3)
print(e)
print(r)

# Now, when you call the decorated function `add`, it will measure the execution time.
execution_time, result = add(26565776634654, 67865434876543)
print("Execution Time:", execution_time)
print("Result:", result)


##########################################################
""" 
*Question 3:
Write a Python program to create a decorator to convert the return value of a function 
to a specified data type.
"""
def my_deco(datatype):
    def Inner_deco(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return datatype(result)
        return wrapper
    return Inner_deco

@my_deco(str)
def add(a, b):
    return a + b

value = add(2,3)
print(value)
print(type(value))

##########################################################
""" 
*Question 4:
4. Write a Python program that implements a decorator to cache the result of a function.
"""
def cache_funct(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = (*args, *kwargs.items())

        if key in cache:
            print("Retrieving result from cache...")
            return cache[key]
        result = func(*args, *kwargs)
        cache[key] = result        
        return result
    return wrapper

@cache_funct
def calculate_multiply(x, y):
    print("Calculating the product of two numbers...")
    return x * y
        
print(calculate_multiply(4, 5))  # Calculation is performed
print(calculate_multiply(4, 5))  # Result is retrieved from cache
print(calculate_multiply(5, 7))  # Calculation is performed
print(calculate_multiply(5, 7))  # Result is retrieved from cache
print(calculate_multiply(-3, 7))  # Calculation is performed

##########################################################
""" 
*Question 5:
5. Write a Python program that implements a decorator to validate function
arguments based on a given condition.
"""
# 1st method manually
def my_decorator(condition):
    def decorator(func):
        def wrappers(*args, **kwargs):
            if condition(*args, **kwargs):
                return func(*args, **kwargs)
            else:
                print("Invalid input")
        return wrappers
    return decorator

def calculate_cube(x):
    return x ** 3
# Applying the decorator manually
calculate_cube = my_decorator(lambda x: x > 0)(calculate_cube)

# Testing the function
print(calculate_cube(5))  # Output: 125
print(calculate_cube(-2))  # Output: Invalid input

# 2nd mehtod
def my_decorator(condition):
    def decorator(func):
        def wrappers(*args, **kwargs):
            if condition(*args, **kwargs):
                return func(*args, **kwargs)
            else:
                print("Invalid input")
        return wrappers
    return decorator
    
@my_decorator(lambda x: x > 0)
def calculate_cube(x):
    return x ** 3

print(calculate_cube(5))  # Output: 125
print(calculate_cube(-2)) # Raises ValueError: Invalid arguments passed to the function


##########################################################
""" 
*Question 7:
7. Write a Python program that implements a decorator to
enforce rate limits on a function.
"""
import time
def rate_limits(max_calls, period):
    """
    A decorator to enforce rate limits on a function.
    Args:
        max_calls (int): The maximum number of allowed calls.
        period (float): The time period in seconds.
    """
    def decorator(func):
        calls = 0
        last_reset = time.time()
        
        def wrapper(*args, **kwargs):
            nonlocal calls, last_reset
            current_time = time.time()
            
            # Calculate time elapsed since last reset
            elapsed = current_time - last_reset
            
            # If elapsed time is greater than the period, reset the call count
            if elapsed > period:
                calls = 0
                last_reset = current_time
            
            # Check if the call count has reached the maximum limit
            if calls >= max_calls:
                raise Exception("Rate limit exceeded. Please try again later.")
            
            # Increment the call count
            calls += 1
            
            # Call the original function
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Example usage
@rate_limits(max_calls=6, period=10)
def api_call():
    print("API call executed successfully...")

# Make API calls
for _ in range(8):
    try:
        api_call()
    except Exception as e:
        print(f"Error occurred: {e}")

##########################################################
""" 
*Question 8:
88. Write a Python program that implements a decorator to add logging functionality to a function.
"""
