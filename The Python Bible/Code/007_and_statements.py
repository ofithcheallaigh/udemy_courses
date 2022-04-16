c = 10
d = 5

if c > 10 and d > 1:        # This comes out to "False AND True", which is False
    # Both above need to be true to enter the loops
    print("it worked")

if c >= 10 and d > 1:        # This comes out to "True AND True", which is True
    # Both above need to be true to enter the loops
    print("it worked")

# We can get the top example to work as follows:
if not (c > 10 and d > 1):  # Inside brackets done fist, which comes to false, then negate it to get true
    print("It works now")
