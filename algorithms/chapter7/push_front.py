# def push_front(arr, val):
#   result = [val]
#   for value in arr:
#     result.append(value)
#   return result

def push_front(arr, val):
  if not isinstance(arr, list):
    raise TypeError('first argument must be a list')

  arr.append(None)
  for i in range(len(arr) - 1, 0, -1):
    arr[i] = arr[i - 1]
  arr[0] = val
  return arr