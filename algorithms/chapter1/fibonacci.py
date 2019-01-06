# Create a function to generate Fibonacci numbers. In this famous mathematical sequence, each number is the sum of the previous two, starting with values 0 and 1. Your function should accept one argument, an index into the sequence (where 0 corresponds to the initial value, 4 corresponds to the value four later, etc). Examples: fibonacci(0) = 0 (given), fibonacci(1) = 1 (given), fibonacci(2) = 1 ( fib(0) + fib(1) , or 0+1), fibonacci(3) = 2 ( fib(1) + fib(2) , or 1+1), fibonacci(4) = 3 (1+2), fibonacci(5) = 5 (2+3), fibonacci(6) = 8 (3+5), fibonacci(7) = 13 (5+8), etc.
[0, 1, 1, 2, 3, 5, 8, 13]
def fibonacci(num):
  a = 0
  b = 1

  while num > 0:
    c = a + b
    a = b
    b = c
    num -= 1
  return a

# def recur_fib(num, a = 0, b = 1):
#   if num == 0:
#     return 0
#   if num == 1:
#     return 1
#   return recur_fib(num - 1, b, a + b)
print("hello " + "world")
my_string = len("r" + "ello")

print("hello" * 80)

# print(fibonacci(10))