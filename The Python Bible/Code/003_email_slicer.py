# A slice is a small peice of something larger.
# Remember: strings are interable.
# Strings are made of elements, and each element has a number, starting at zero
# These numbers are referred to an the index
# Strings are immutable


word = "Supercalifragilisticexpialidocious"

#If we want the first letter, which the the 0th index
print(word[0])

# To get the letter 'p':
# Indexes start at 0, so p is the third letter, at index 2, so
print(word[2])

# To take a slice use the format: variable[start:end:step]
# Let's get the word 'Super'
# Remember, the end index is the end point, plus 1
print(word[0:5:1])

# How get the word 'cali'
print(word[5:9:1])

# If we wanted from 'Cali' right to the end, we can do this like:
print(word[5:])

# Go from 'cali' to the end, in steps of 2
print(word[5::2])

# Get everything up to index 7
print(word[:7])

# We can use negatiive steps to reverse a sting:
print(word[::-1])

# We can index from the end of a strings
print(word[-2])

# We can use the index function to help us find where letters or slices are:
print(word.index('cali'))

print(word[word.index('cali'):word.index('cex')])

# here is a very long word

word = "antidisestablishmentarianism"

# use a slice to take out the word "establishment"
# and store it in the answer variable....

answer = word[word.index("est"):word.index('ari')]
print(answer)
