def count_subarrays(arr):
  n = len(arr)
  res = [1] * n
  stack = [-1]
  #left
  for i in range(n):
    while len(stack) > 1 and arr[stack[-1]] < arr[i]:
      stack.pop()
    res[i] += i - stack[-1] - 1
    stack.append(i)
  
  # from right
  stack = [n]
  for i in range(n - 1, -1, -1):
    while len(stack) > 1 and arr[stack[-1]] < arr[i]:
      stack.pop()
    res[i] += stack[-1] - i - 1
    stack.append(i)
  return res