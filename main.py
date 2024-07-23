"""To declare an encoding other than the default one (i.e. utf-8), a special comment line should be added as the
first line of the file. The syntax is as follows: # -*- coding: encoding -*-"""

# This is a comment :D

spam = 1  # This is a comment too, but the spam thing is not a comment.

text = "# Hash inside quotes is not considered to be a comment."

print(50 - 6 * 5)
print((50 - 2 * 5) / 5)  # A division always returns a floating point number.
print((50 - 2 * 5) // 6)  # But the floor division returns an int.
print((50 - 2 * 5) % 6)  # Percent operator returns the remainder of the division.
print(6 * 6 + 4)  # This returns the original number before division.

print(f"2 squared = {2 ** 2}")

width = 20
height = 5 * 9
print(width * height)  # Introducing variables.
