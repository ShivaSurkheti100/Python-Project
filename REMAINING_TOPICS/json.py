''' JSON is a syntax for storing and exchanging data
JSON is a text, written with JavaScript object notation
python has built-in package(module) "json" to work with JSON data
'''

# Parse JSON - convert from JSON to Python -- using < json.loads() > method

import json

# JSON string
x = '{"name":"Jhon", "age":33, "city":"New York"}'

# parse x: convert x to y
y = json.loads(x)

# the result will be a python dictionary
print(y["age"]) # prints 33... but its not working


## convert from python to JSON 

import json

# a python object(dict):
x = {
    "name": "John",
    "age":30, 
    "city":"New York"
}
# convert into json -- using json.dumps() method
y = json.dumps(x)
# the result is a JSON string
print(y)
## codes are throwing error ... so I have not done much research on it


'''You can convert Python objects of the following types, into JSON strings:

dict
list
tuple
string
int
float
True
False
None

'''

'''When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

Python	JSON
dict	Object
list	Array
tuple	Array
str	    String
int	    Number
float	Number
True	true
False	false
None	null '''