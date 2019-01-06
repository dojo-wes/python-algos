# Given an array of numbers, print the max, min and average values for that array.
# loop through all numbers
# sum all of them
# avg = sum / number_of_items
# if the number I'm looking at < current min store new min
# if the number I'm looking at > current max store new max

my_list = [10, 5, 6, 7, 11, 15]
def max_min_avg(li):
  min_val = li[0]
  max_val = li[0]
  total = 0
  for val in li:
    total += val
    if val < min_val:
      min_val = val
    elif val > max_val:
      max_val = val
  
  print ("min_val => ", min_val, "max_val => ", max_val, "avg =>", total / len(li))

max_min_avg(my_list)