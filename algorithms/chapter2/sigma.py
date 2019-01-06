# Implement function sigma(num) that given a number, returns the sum of all positive integers up to number (inclusive). Ex.: sigma(3) = 6 (or 1 + 2 + 3 ); sigma(5) = 15 (or 1 + 2 + 3 + 4 + 5 ).

# def sigma(num):
#   result_sum = num
#   i = num - 1
#   while i > 0:
#     result_sum = result_sum + i
#     i = i - 1
#   return result_sum

# def sigma(num):
#   result_sum = num
#   for i in range(num - 1, 0, -1):
#     result_sum += i
#   return result_sum

def sigma(num):
  result_sum = 0
  for i in range(0, num + 1, 1):
    result_sum = result_sum + i
  return result_sum

# def sigma(num):
#   s = 0
#   for i in range(1, num+1):
#     s += i
#   return s

print(sigma(3))