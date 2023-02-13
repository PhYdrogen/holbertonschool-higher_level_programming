# Python - Almost a circle

In this readme, you will find information about:

- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- What is ``*args`` and how to use it
- What is ``**kwargs`` and how to use it
- How to handle named arguments in a function

## Unit Testing
Unit testing is a software testing technique in which individual units or components of the code are tested in isolation from the rest of the system. The goal is to validate that each unit of the software application is working as intended. In a large project, it's important to implement unit tests to ensure that changes to the code do not break existing functionality.

To implement unit testing in a large project, you can use a testing framework such as unittest in Python. The framework provides tools for writing and organizing tests, and for reporting results. Here's an example of how to write a simple test using unittest:

```python
import unittest

def add(a, b):
	return a + b

class TestAdd(unittest.TestCase):
	def test_add(self):
		result = add(3, 4)
		self.assertEqual(result, 7)

if __name__ == '__main__':
	unittest.main()
```
You can run this test by running the file from the command line. The unittest framework will discover and run the test, and report the results.
## Serialization and Deserialization of a Class
Serialization is the process of converting an object's state to a byte stream, and deserialization is the reverse process of recreating the object from the byte stream. This is useful when you want to persist an object's state, or send it over the network.

To serialize and deserialize a class in Python, you can use the pickle module. Here's an example:
```python
import pickle

class Person:
    def __init__(self, name, age):
	        self.name = name
			        self.age = age

# Serialize the object
person = Person("John Doe", 30)
with open("person.pkl", "wb") as f:
    pickle.dump(person, f)

# Deserialize the object
with open("person.pkl", "rb") as f:
    person = pickle.load(f)

	print(person.name)
	print(person.age)
```

## JSON
JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write and easy for machines to parse and generate. In Python, you can use the json module to write and read JSON files.

Here's an example of how to write a JSON file:
```python
import json

data = {"name": "John Doe", "age": 30}

with open("data.json", "w") as f:
    json.dump(data, f)

print(data["age"])
```

## *args and **kwargs

In Python, the `*` and `**` syntax are used to pass a variable number of arguments to a function.

`*args` is used to pass a non-keyworded, variable length argument list to a function. The syntax for using `*args` is to prefix the parameter name with an asterisk (`*`). Here's an example:

```python
def print_args(*args):
    for arg in args:
        print(arg)

print_args(1, 2, 3)
```

``**kwargs`` is used to pass keyworded, variable length of arguments to a function. The syntax for using ``**kwargs`` is to prefix the parameter name with two asterisks (**). Here's an example:

```python
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="John Doe", age=30)
```

Handling Named Arguments in a Function
When defining a function, you can specify default values for arguments by assigning them in the function definition. If an argument is not provided when the function is called, the default value will be used. Here's an example:

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("John Doe")
greet("Jane Doe", "Hi")
```
When calling the function, you can also specify the arguments by name, which is called named arguments. This allows you to specify the arguments in any order. Here's an example:

```python
greet(greeting="Hi", name="John Doe")
```
