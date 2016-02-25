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

# want to define the linked-list structure he drew on the board
class Item:
  def __init__(self):
    # whats in the item?
    self.data = None
    # whats next in the list?
    self.next = None


class GroceryList:
  def __init__(self):
    self.head = None

  def remove_all(self):
    # if you delete the head, the whole list is lost
    self.head = None
    
  def append(self, data):
    # IMPORTANT: this is why all elements are items
    new_item = Item()
    new_item.data = data

    # make the new item the head
    if self.head is None:
      self.head = new_item
    # start at the head, work your way through the list
    # set the new item = the .next item of the last in the list
    else:
      current_item = self.head
      while (current_item.next != None):
        current_item = current_item.next
      current_item.next = new_item

  def at(self, position):
    # start at the head (Apples)
    current_item = self.head
    # count over to the position
    while position > 0 and current_item != None:
      # current_item = apples.next
      current_item = current_item.next
      position -= 1

    if current_item != None:
      # apples.next.data
      return current_item.data
    else:
      return None

  def length(self):
    # start at head and cycle through to find length
    n = 0
    current_item = self.head
    while (current_item != None):
      n += 1
      current_item = current_item.next

    return n


groceries = GroceryList()
assert 0 == groceries.length()

groceries.append("Apples")
assert 1 == groceries.length()
assert "Apples" == groceries.at(0)

groceries.append("Bananas")
assert 2 == groceries.length()
assert "Bananas" == groceries.at(1)

groceries.append("Cookies")
assert 3 == groceries.length()
assert "Cookies" == groceries.at(2)

groceries.remove_all()
assert 0 == groceries.length()
assert None == groceries.at(2)
