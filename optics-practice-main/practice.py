import json

# IDEAS:
#   If data tables can be saved as JSON
#   the method below could easily
#   parse and manipulate the data
#
#

# some JSON:
X =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(X)

# the result is a Python dictionary:
print(y["ages"])
print(y["name"])
print(y["city"])


def function_new():
    """This is the python doc-string to clarify the defined function"""
    #if the json contains int values,
    #they can be grabbed,
    #assigned to variables,
    #and manipulated just like normal
    new_num = y["age"]
    while new_num < 100:
        new_num += 10
        print(new_num)


function_new()
