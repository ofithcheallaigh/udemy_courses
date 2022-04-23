# Dictionaries are key-value pairs
# Items are made of keys and values

students = {"Alice": 25, "Bob":27, "Claire":18, "Dan":21, "Emma":22}

# Find Dan's age:
print(students["Dan"])

# We can add a student to the dictionary. If we want to add Fred who is 25:
students["Fred"] = 25
print(students)

# We can also update items in the dictionary.
# Let's make Alice one year older:
students["Alice"] = 26
print(students)

# We can delete items too:
del students["Fred"]
print(students)

# We can get all the keys in a dictionaryby using the the keys function:
print(students.keys())
print(type(students.keys()))

# We cannot use indexing to access items
# If we want to access the keys, we need to convert them to a list:
a = list(students.keys())
print(a)
print(type(a))

# Same for the values, except we use the values function:
b = list(students.values())
print(b)
print(type(b))

# We can slide while converting to list:
c = list(students.values())[2:]
print(c)

# Somtimes, when printing a dict, the order will not be the same as the order the dict was 
# constructed in -- but the order doesn't matter, the is the key-value pairs that are important
