# Algorithm to find the k-th smallest values
# NOTE: for k-ths greater values I think it could also work


# The algorithm instead of searching for both partes after the pivot
# just keeps the smallest k-th elements

# Complexity K-th

# 1. After pivot the smallest values are k-th elements, return them
# 2. Otherwise, search in the right part, until comple k elements

arr = [1,5, 6, 2, 3, 1, 7]

def partition(arr, low, high):

    pivot = arr[high]

    left_idx = low

    for i in range(low, high):

        if arr[i] <= pivot:

            arr[i], arr[left_idx] = arr[left_idx], arr[i]
            left_idx += 1
    
    arr[high], arr[left_idx] = arr[left_idx], arr[high]

    return left_idx

def quick_select(arr, low, high, k):

    if k > len(arr):
        return arr 

    if ( k > 0 and k <= high - low + 1 ):

        pivot = partition(arr, low, high)

        if pivot + 1 - low == k:
            return arr[:pivot+1]

        # if there are more values in the left part
        if pivot + 1 - low > k:
            return quick_select(arr, low, pivot - 1, k)

        # if there are not enough values in the left part
        # check the right part
        return quick_select(arr, pivot + 1, high, k - (pivot + 1))
    
res = quick_select(arr, 0, len(arr)-1, 5)
print(arr)
print(res)

res = quick_select(arr, 0, len(arr)-1, 6)
print(arr)
print(res)

arr = [ 10, 4, 5, 8, 6, 11, 26 ]
res = quick_select(arr, 0, len(arr)-1, 3)
print(arr)
print(res)

arr = [ 10, 4, 5, 8, 6, 11, 26 ]
res = quick_select(arr, 0, len(arr)-1, 6)
print(arr)
print(res)