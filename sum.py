def sum(arr, val = 0):
  if len(arr) == 0:
    return val
  else:
    val += arr.pop()
    return sum(arr, val)
