
arr = [1,5, 6, 2, 3, 1, 7]

# I remember that the idea of this algorithm is to chose a pivot intelligent

# The idea is to place the pivot in the position that it must be in the final
# sorted array

# Then, split the array and repeated the same process to the next arrays

# For positioning the pivot in to its correct position in the final sorted array,
# you need to swap the pivot comparing with each one of the rest until
# the pivot is in the right place.

# there are different way to do this





# The worst pivot is the smallest or largest one -> O(n^2)



# Not optimal Function to perform quicksort
def quick_sort(array):

  length = len(array)

  if length <= 1:
    return array

  pivot = array.pop()

  items_lower = []
  items_greater = []

  for item in array:

    if item > pivot:
      items_greater.append(item)

    else:
      items_lower.append(item)

  return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


def partition(arr, low, high):
  # The idea of this partition is to place the less or equal values to the pivot
  # in the left part of the array until there is not more values 
  # less or equal than the pivot

  pivot = arr[high]

  # Pointer to left position
  left_idx = low

  for i in range(low,high):

    if arr[i] <= pivot:

      arr[i] , arr[left_idx] = arr[left_idx], arr[i]
      left_idx += 1
  
  arr[high], arr[left_idx] = arr[left_idx], arr[high]

  return left_idx

def quick_sort(arr, low,  high):
  if high > low:

    pivot = partition(arr, low, high)

    quick_sort(arr, low, pivot - 1)
    quick_sort(arr, pivot + 1, high)

  return arr

arr = quick_sort(arr, 0, len(arr) - 1)
print(arr)