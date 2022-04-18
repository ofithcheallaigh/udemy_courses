#!/usr/bin/env python

# Lists in python are an itterable data type


# Example of a list
our_list = [27,46,-5,17,99]
print(our_list)

print("The type of the our_list variable is: ")
print(type(our_list))

# Lists can contain multiple data types
mixed_list = ["A","B","C",1,2,3,"Do","Rey","Me",True,False]


# Since lists are itterable, each element has an index, which starts at 0
# We can select any of the list by using its index. For example, index 4 below
print(mixed_list[4])

# Another example
print(mixed_list[7])

# We can also count from the end of the list, and the element can be stored
# in a variable
x = mixed_list[-2]
print(x)

# We can also take out a slice of the list. In other words, a number of elemnts
# at once. This in effect makes a sublist of the main list. The format is:
# list_name[start:end:steps]
# Default steps is 1, and the end is "up to, but not including". As an example,
# we will take "A,B,C". Key point: a slide is just a copy of the original
print(mixed_list[0:3])

# Now let's get a more complicated list, from which we want to extract the
# internal list, which is at index 2
new_list = [1,2,[3,4,5],6,7,8]  # This has a kist inside a list
new_list_sub_list = new_list[2]
print(new_list_sub_list)

# But what if we wanted to extract just the number 3?
print(new_list[2][0])

# Now looking at tables
my_table = [[1,2,3],[4,5,6],[7,8,9]]
print(my_table[0])
print(my_table[1])
print(my_table[2])

# To get the number 2:
print(my_table[0][1])

# To get the number 6:
print(my_table[1][2])

# To get the numbers 8 and 9:
print(my_table[2][1:])

# The first set of brackets gets us the row, the second gets the column(s)
