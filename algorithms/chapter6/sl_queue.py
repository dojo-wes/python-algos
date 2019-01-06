class EmptyQueueError(Exception):
  def __init__(self):
    self.expression = "Queue Empty"
    self.message = "Cannot finish operation"

class Node():
  def __init__(self, val):
    self.val = val
    self.next = None

class SLQueue():
  def __init__(self):
    # nodes get removed from the head, it's the "front of the queue"
    self.head = None
    # nodes get added to the tail, it's the "back of the queue"
    self.tail = None
    self.length = 0
  
  def enqueue(self, val):
    new_node = Node(val)
    if self.head == None:
      self.head = new_node
    else:
      self.tail.next = new_node
    self.tail = new_node
    self.length += 1
    return self

  def dequeue(self):
    if self.head == None:
      raise EmptyQueueError()
    temp = self.head
    self.head = self.head.next
    self.length -= 1
    return temp.val
  
  def display(self):
    result = []
    curr_node = self.head
    while curr_node:
      result.append(curr_node.val)
      curr_node = curr_node.next
    print(result)
    return self

q = SLQueue()

q.enqueue('A').enqueue('B').enqueue('C').display()