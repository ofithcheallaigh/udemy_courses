# This is a file which some examples of some more advanced list work

# Generate list of users
known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]

# We can get the number of known users as follows
# print(len(known_users))

while True:
    print("Hello, my name is Travis")

    # We can use the capitalize() method to ensure that no matter how the users
    # enters their name it will work, i.e. Alice or alice
    name = input("What is your name?: ").strip().capitalize()

    # Is this name in the list of known users?
    if name in known_users:
        # print("Name recognised")
        print("Hello {}.".format(name))

        remove = input("Would you like to be removed from the system (y/n)? ").lower()
        print(remove)
        if remove == 'y':
            known_users.remove(name)
            print("Your name has been removed")
        elif remove == 'n':
            print("No problem.")

    else:
        print("I don't think I have met you yet, {}".format(name))
        add_me = input("Would you like to be added to the system (y/n)?: ").strip().lower()
        if add_me == 'y':
            known_users.append(name)
            print("You have been added to list {}".format(name))
        elif add_me == 'n':
            print("That's fine, have a nice day")

    print("=======================================")
