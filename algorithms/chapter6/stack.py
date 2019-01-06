class Stack:
  def __init__(self):
    self.stack = []

  def push(self, data):
    self.stack.append(data)
    return self

  def pop(self):
    if len(self.stack) <= 0:
      return "nah"
    return self.stack.pop()

  def empty(self):
    if len(self.stack) <= 0:
      return True
    else:
      return False

  def size(self):
    return len(self.stack)

  def display(self):
    print(self.stack)
    return self

  def top(self):
    if len(self.stack) > 0:
      return self.stack[len(self.stack) - 1]
    else:
      return None

my_stack = Stack()

my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
# my_stack.pop()

print my_stack.empty()
print my_stack.size()
my_stack.display()
print my_stack.top()
my_stack.display()