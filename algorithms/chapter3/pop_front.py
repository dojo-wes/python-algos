my_list = [10, 2, 3, 4, 5]
# print my_list.pop()
# print my_list

def pop_front(li):
  result = li[0]
  for i in range(len(li) - 1):
    li[i] = li[i + 1]
  li.pop()
  return result

print pop_front(my_list)
print my_list