my_list = [2, 3, 4, 5]

result = [1, 2, 3, 4, 5]
# len(my_list)
# append_front(my_list, 1)

# my_list == [1, 2, 3, 4, 5]

# my_list[3] = 10
# print my_list

# for val in my_list:
#   print val

# for i in range(len(my_list)):
#   my_list[i] = "something"

# print my_list

# add a new index
# push all old values over to the right
# list[0] = new_val

def append_front(li, val):
  result = []
  result.append(val)
  for idx_val in li:
    result.append(idx_val)
  return result

# print append_front([2, 3, 4, 5], 1)

def append_front_in_place(li, val):
  li.append(None)
  for i in range(len(li) - 1, 0, -1):
    li[i] = li[i - 1]
  li[0] = val
  return li

print append_front_in_place([2,3,4,5], 1)

