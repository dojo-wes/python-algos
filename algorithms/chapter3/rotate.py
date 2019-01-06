def rotate_arr(arr, num_rotations):
  num_rotations = num_rotations % len(arr)
  if num_rotations <= len(arr) / 2:
    rotate_right(arr, num_rotations)
  else:
    rotate_left(arr, num_rotations)
  return arr

def rotate_right(arr, num_rotations):
  while num_rotations > 0:
    temp = arr[len(arr) - 1]
    for i in range(len(arr) - 1, 0, -1):
      arr[i] = arr[i - 1]
    arr[0] = temp
    num_rotations -= 1
  return arr

def rotate_left(arr, num_rotations):
  num_rotations = len(arr) - num_rotations
  while num_rotations > 0:
    temp = arr[0]
    for i in range(0, len(arr) - 1, 1):
      arr[i] = arr[i + 1]
    arr[len(arr) - 1] = temp
    num_rotations -= 1
  return arr

print rotate_arr([1, 2, 3, 4, 5], -3)