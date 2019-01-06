# Zip Arrays into Map

# Associative arrays are sometimes called maps because a key (string) maps to a value. Given two arrays, create an associative array (map) containing keys of the first, and values of the second. For arr1 = ["abc", 3, "yo"] and arr2 = [42, "wassup", true] return {"abc": 42, 3: "wassup", "yo": true}

def zip_arrays_into_map(arr1, arr2):
  result = {}
  for i in range(len(arr1)):
    result[arr1[i]] = arr2[i]
  print result
  return result

test1 = ["abc", 3, "yo"]
test2 = [42, "wassup", True]
zip_arrays_into_map(test1, test2)