def balancedSplitExists(arr):
                       # left sum    # right sum
  # [1*, 1, 5, 6, 7*]     1              7
  # [1, 1*, 5, 6, 7*]     2              7
  # [1, 1, 5*, 6, 7*]     7              7
  # [1, 1, 5*, 6*, 7]     7              13
  
  arr.sort()
  
  start = 0
  end = len(arr) - 1
  
  left_sum = arr[start] 
  right_sum = arr[end]

  while(end - start > 1):
    print(start, end, left_sum, right_sum)
    
    if left_sum < right_sum:
      start += 1
      left_sum += arr[start]
      
    if left_sum == right_sum and end - start > 1:
      end -= 1
      right_sum += arr[end]
  print(start, end, left_sum, right_sum)

  return left_sum == right_sum and arr[start] != arr[start + 1]


arr1 = [1, 1, 5, 6, 7] 
print(balancedSplitExists(arr1))

arr1 = [2, 1, 2, 5]
print(balancedSplitExists(arr1))

arr2 = [3, 6, 3, 4, 4]
print(balancedSplitExists(arr2))
