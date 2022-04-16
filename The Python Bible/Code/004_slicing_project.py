# Get the user email address
email = input("What is your email address?: ").strip() # Stip will remove any whitespaces

# Slice out the user name
username = email[:email.index('@')]


# Slide dmain name
domain_name = email[email.index('@')+1:]

# Format output
output = "Your username is {} and your domain name is {}.".format(username,domain_name)

# Display output
print(output)
