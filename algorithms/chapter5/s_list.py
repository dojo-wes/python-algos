class Node:
  def __init__(self, value):
    self.val = value
    self.next = None

  # def __str__(self):
  #   return str(self.val)

class SList:
  def __init__(self):
    self.head = None
    self.length = 0

  def add_front(self, val):
    new_node = Node(val)
    new_node.next = self.head
    self.head = new_node
    self.length += 1
    return self

  def contains(self, value):
    curr = self.head
    while curr:
      if curr.val == value:
        return True
      curr = curr.next
    return False

  def remove_front(self):
    temp = self.head
    self.head = self.head.next
    temp.next = None
    del temp
    self.length -= 1
    return self

  def front(self):
    return self.head.val

  def length(self):
    count = 0
    node = self.head
    while node != None:
      count += 1
      node = node.next
    return count

  def len(self):
    return self.length
  
  def display(self):
    result = []
    curr = self.head
    while curr:
      result.append(curr.val)
      curr = curr.next
    print result
    return self

  def max(self):
    max_val = self.head.val
    curr_node = self.head
    while curr_node != None:
      if max_val < curr_node.val:
        max_val = curr_node.val
      curr_node = curr_node.next
    return max_val

  def avg(self):
    total = 0
    curr_node = self.head
    while curr_node != None:
      total += curr_node.val
      curr_node = curr_node.next
    # returning the average
    return total/self.length

  def remove_back(self):
    prev_node = None
    curr_node = self.head
    while curr_node != None:
      prev_node = curr_node
      curr_node = curr_node.next
      if curr_node.next == None:
        prev_node.next = None
    return self

  def add_back(self, val):
    curr_node = self.head
    new_node = Node(val)
    while curr_node != None:
      if curr_node.next == None:
        curr_node.next = new_node
        self.length += 1
      else:
        curr_node = curr_node.next
    return self

# self is a reference to the instance of the class that is calling the current method
# my_node = Node("A")
# print my_node
my_list = SList()
# print my_list.length()
my_list.add_front("C")
my_list.add_front("B")
print my_list.len()
my_list.add_front("A")
print my_list.max()
# my_list.display()

# print bool(Node('A'))
