# Ask the user for their name
name = input("What is your name?: ")
# print(name)
# Ask the user for their age
age = input("What is your age?: ")

print(type(name))
print(type)
# Ask the user where they live
city = input("Where do you live?: ")

# Ask the user what the enjoy
love = input("What do you enjoy doing?: ")

# Create output text
string = "Your name is {} and you are {} years old. You live in {} and you enjoy {}."
output = string.format(name,age,city,love)

# Print the output to the screen
print(output)
