def biggie_size(arr):
  for i in range(len(arr)):
    if arr[i] > 0:
      arr[i] = "big"
  return arr

def biggie_size(arr):
  i = 0
  for val in arr:
    if val > 0:
      arr[i] = "big"
    i += 1
  return arr

def biggie_size(arr):
  i = 0
  while i < len(arr):
    if arr[i] > 0:
      arr[i] = "big"
    i += 1
  return arr