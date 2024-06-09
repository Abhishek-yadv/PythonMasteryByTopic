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

from symbol import decorator
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
8. Write a Python program that implements a decorator to add logging functionality to a function.
"""
import logging
def add_logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@add_logger
def add_numbers(a, b):
    return a+b

# Call the decorated function
result = add_numbers(200, 300)
print("Result:", result)

""" 
*Question 9
Write a Python program that implements a decorator to handle exceptions
raised by a function and provide a default response.
"""
def handle_exceptions(default_response):
    def decorator(func):
        def wrapper(*arg, **kargs):
            try:
                return func(*arg, **kargs)
            except Exception as e:
                print(f"Exception occurred: {e}")
                return default_response
        return wrapper
    return decorator
@handle_exceptions(default_response="An error occurred!")
def division(a,b):
    return a/b
result = division(5,0)
print(result)


""" 
*Question 10
10. Write a Python program that implements a decorator
to enforce type checking on the arguments of a function.
"""
def my_datatype(datatype):
    def my_decorator(func):
        def wrapper(*arg, **kwargs):
            if type(arg[0]) == datatype:
                return "Ye nhi chalega re"
            else:
                return func(*arg, **kwargs)
        return wrapper
    return my_decorator

@my_datatype(str)
def func(a, b):
    return a+b
result = func(1,2)
print(result)

""" 
*Question 11
11. Write a Python program that implements a decorator to
measure the memory usage of a function. 
"""
import tracemalloc
def measure_memory_usage(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        snapshot = tracemalloc.take_snapshot()
        top_stats = snapshot.statistics("lineno")
        # Print the top memory-consuming lines
        print(f"Memory usage of {func.__name__}:")
        for stat in top_stats[:5]:
            print(stat)
        return result
    return wrapper

@measure_memory_usage
def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

result = calculate_factorial(5)
print("Factorial:", result)

""" 
*Question 12
# 12. Write a Python program that implements a decorator
to provide caching with expiration time for a function.
"""
import time
def cache_with_expiry(expiry_time):
    def decorator(func):
        cache = {}
        def wrapper(*args, **kwargs):
            # Create a cache key from function arguments
            key = (args, frozenset(kwargs.items()))
            current_time = time.time()
            if key in cache:
                value, timestamp = cache[key]
                if current_time - timestamp < expiry_time:
                    print("Retrieving result from cache...")
                    return value
            # Calculate the result and cache it
            result = func(*args, **kwargs)
            cache[key] = (result, current_time)
            return result
        return wrapper
    return decorator

# Example usage
@cache_with_expiry(expiry_time=3)  # Cache expiry time set to 5 seconds
def calculate_multiply(x, y):
    """Calculate the product of two numbers."""
    print("Calculating product of two numbers...")
    return x * y

# Call the decorated function multiple times
print(calculate_multiply(23, 5))  # Calculation is performed
print(calculate_multiply(23, 5))  # Result is retrieved from cache
time.sleep(3)
print(calculate_multiply(23, 5))  # Calculation is performed (cache expired)

def func(*args, **kwargs):
    result = (args, kwargs.items())
    for k in args:
        print(k)
func(2,3)
            


