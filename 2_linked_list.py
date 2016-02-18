# Can we use the computer to keep track of a list of things
# without using Python's built-in abilities?
#
# Let's try to replicate the following functionality:
#
# groceries = []
# groceries.append("Apples")
# groceries.append("Bananas")
# groceries.append("Cookies")
# groceries[0]   # => "Apples"
# groceries[1]   # => "Bananas"
# groceries[2]   # => "Cookies"
#
# Remember, no built-in lists or dictionaries may be used.
#
# Let's start by mapping out a solution on paper.
#
# Then we can try to teach the computer to do the same.

groceries = GroceryList()
assert 0 == groceries.length()

groceries.append("Apples")
assert 1 == groceries.length()
assert "Apples" == groceries[0]

groceries.append("Bananas")
assert 2 == groceries.length()
assert "Bananas" == groceries[1]

groceries.append("Cookies")
assert 3 == groceries.length()
assert "Cookies" == groceries[2]
