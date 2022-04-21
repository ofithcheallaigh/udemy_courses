# Tuples are data types which work similar to lists.
# The only difference is when a tuple is created, it cannot be changed.
# They are immuatable

our_tuple = 1,2,3,'A','B','C'
print(our_tuple)

# More typically, tuples are created with brackets:
our_tuple = (1,2,3,'A','B','C')
print(type(our_tuple))

# We can slice tuples, in the same way as lists:
sliced_tuple = our_tuple[0:3]
print(sliced_tuple)

# We can use the tuple function to turn other data into a tuple
a_list = [1,2,3]
print(type(a_list))
a_list = tuple(a_list)
print(type(a_list))
