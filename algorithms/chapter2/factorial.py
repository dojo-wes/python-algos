def factorial(num):
  # start at one
  # multiply one and two
  # multiply result and 3
  # multiply result and 4
  result = 1
  for i in range(1, num + 1, 1):
    result = result * i
  return result

print(factorial(5))

#############
# product | 24
#       i | 4