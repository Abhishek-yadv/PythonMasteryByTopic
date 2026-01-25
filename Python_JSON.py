################################################################
##################################################### (JSON)
################################################################
"""1.Write a Python program to convert JSON data to Python object."""
import json
def program():
    json_data = """
    {
        "name": "John",
        "age": 30,
        "city": "New York"
    }"""
    python_obj = json.loads(json_data)
    print("Python Object:")
    print(python_obj)
    print("Name:", python_obj["name"])
    print("Age:", python_obj["age"])
    print("City:", python_obj["city"])
program()

"""2. Write a Python program to convert Python object to JSON data."""
import json
def program():
    python_obj = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    json_data = json.dumps(python_obj)
    print("JSON Data:")
    print(json_data)
    print("Name:", python_obj["name"])
    print("Age:", python_obj["age"])
    print("City:", python_obj["city"])
program()

"""3. Write a Python program to convert Python objects into JSON strings. Print all the values."""
import json
def program():
    python_obj = {
        "name": "John",
        "age": 30,
        "city": "New York",
        "is_student": False,
        "courses": ["Math", "Science"],
        "address": {
            "street": "123 Main St",
            "city": "New York"
        }
    }
    json_data = json.dumps(python_obj, indent=4)
    print("JSON Data:")
    print(json_data)
    print("Name:", python_obj["name"])
    print("Age:", python_obj["age"])
    print("City:", python_obj["city"])
    print("Is Student:", python_obj["is_student"])
    print("Courses:", python_obj["courses"])
    print("Street:", python_obj["address"]["street"])
    print("City:", python_obj["address"]["city"])
program()

"""4. Write a Python program to convert Python dictionary object (sort by key) to JSON data.
Print the object members with indent 1"""
import json
def program():
    python_dict = {
        "name": "John",
        "age": 30,
        "city": "New York",
        "is_student": False,
        "courses": ["Math", "Science"],
        "address": {
            "street": "123 Main St",
            "city": "New York"
        }
    }
    json_data = json.dumps(python_dict, indent=1, sort_keys=True)
    print("JSON Data:")
    print(json_data)
    print("Name:", python_dict["name"])
    print("Age:", python_dict["age"])
    print("City:", python_dict["city"])
    print("Is Student:", python_dict["is_student"])
    print("Courses:", python_dict["courses"])
    print("Street:", python_dict["address"]["street"])
    print("City:", python_dict["address"]["city"])
program()

"""5. Write a Python program to convert JSON encoded data into Python objects."""
def program():
    json_data = """
    {
        "name": "John",
        "age": 30,
        "city": "New York",
        "is_student": false,
        "courses": ["Math", "Science"],
        "address": {
            "street": "123 Main St",
            "city": "New York"
        }
    }"""
    python_obj = json.loads(json_data)
    print("Python Object:")
    print(python_obj)
    print("Name:", python_obj["name"])
    print("Age:", python_obj["age"])
    print("City:", python_obj["city"])
    print("Is Student:", python_obj["is_student"])
    print("Courses:", python_obj["courses"])
    print("Street:", python_obj["address"]["street"])
    print("City:", python_obj["address"]["city"])
program()

"""6. Write a Python program to create a new JSON file from an existing JSON file."""
import json
def program():
    try:
        with open("existing_file.json", "r") as file:
            data = json.load(file)
            
        with open("new_file.json", "w") as new_file:
            json.dump(data, new_file, indent=4)

        print("New JSON file created successfully.")
    except Exception as e:
        print("An error occurred:", str(e))
program()

"""7. Write a Python program to check whether an instance is complex or not."""
def program():
    # Define a complex object
    complex_obj = {
        "name": "John",
        "age": 30,
        "city": "New York",
        "is_student": False,
        "courses": ["Math", "Science"],
        "address": {
            "street": "123 Main St",
            "city": "New York"
        }
    }

    # Check if the object is complex (contains nested structures)
    is_complex = isinstance(complex_obj, dict) and any(isinstance(value, (list, dict)) for value in complex_obj.values())
    print("Is the object complex?", is_complex)
program()

"""8. Write a Python program to check whether a JSON string contains complex object or not."""
def program():
    json_data = """
    {
        "name": "John",
        "age": 30,
        "city": "New York",
        "is_student": false,
        "courses": ["Math", "Science"],
        "address": {
            "street": "123 Main St",
            "city": "New York"
        }
    }"""
    python_obj = json.loads(json_data)

    # Check if the object is complex (contains nested structures)
    is_complex = isinstance(python_obj, dict) and any(isinstance(value, (list, dict)) for value in python_obj.values())
    print("Is the JSON string complex?", is_complex)
    print("Python Object:")
    print(python_obj)
    print("Name:", python_obj["name"])
    print("Age:", python_obj["age"])
    print("City:", python_obj["city"])
    print("Is Student:", python_obj["is_student"])
    print("Courses:", python_obj["courses"])
    print("Street:", python_obj["address"]["street"])
    print("City:", python_obj["address"]["city"])
program()

"""9. Write a Python program to access only unique key value of a Python object."""
def program():
    python_obj = {
        "name": "John",
        "age": 30,
        "city": "New York",
        "is_student": False,
        "courses": ["Math", "Science"],
        "address": {
            "street": "123 Main St",
            "city": "New York"
        }
    }

    # Access unique key-value pairs
    unique_keys = set(python_obj.keys())
    print("Unique Key-Value Pairs:")
    for key in unique_keys:
        print(f"{key}: {python_obj[key]}")
program()