def insert_at(arr, val, index):
  return arr[:index] + [val] + arr[index:]
# print insert_at([1,2,3,4,5], 22, 2)


def insert_at(arr, val, idx):
  arr.append(None)
  i = len(arr) - 1
  while i > idx:
    arr[i] = arr[i - 1]
    i -= 1
  arr[idx] = val
  return arr
print insert_at([1, 2, 3, 4, 5], 22, 2)