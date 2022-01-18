#" Define a List with a few negative and positive numbers.

# Using list comprehensions, obtain the square values for only the positive numbers from the original list"

"""
  "Define a List with a few negative and positive numbers.

   Using list comprehensions, obtain the square values for only the positive numbers from the original list"
"""

pos_ng = [1, 2, 10, -1, -2, -10]

ret = (x*x for x in pos_ng if x > 0)

print(ret)

