"""
OR operstor truth table

===============================
|   A   |   B   |   Output    |
===============================
|   0   |   0   |      0      |
|   0   |   1   |      1      |
|   1   |   0   |      1      |
|   1   |   1   |      1      |
==============================
"""

c = 5
d = -1

if c > 1 or d > 1:
    print("it worked")

# We can also do a version of this using "if not"
# This basically creates a nor gate
if not (c > 100 or d > 100):
    print("if not worked too")


# ------------------------------------
c = 6
d = 2

if(c>5 and d>5) or (c>1 and d>1):
    print("final one worked")
