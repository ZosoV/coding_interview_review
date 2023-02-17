
arr = [7, 8, 2, 3, 6, 5]

# Quick select is used to get the k-th greatest or smallest values
# in O(n) average time

# To get the k-th smallest values
# The idea is to apply quick sort but instead of analazing both partitions
# just analyze the left partition until get the k-th elements
# because the pivot ensure us that the left partition have values less than the 
# pivot. If the pivoth places in the k-th element then all the left part 
# (including the pivot) are the k-th smallest elements

# Quick sort = partition + recursion

def partition(arr, low, high):

    # pivot the high value

    pivot = arr[high]

    left_idx = low

    for i in range(low, high):

        if arr[i] < pivot:
            arr[i], arr[left_idx] = arr[left_idx], arr[i]
            left_idx += 1

    arr[left_idx], arr[high] = arr[high], arr[left_idx]

    return left_idx


def quick_select(arr, low, high, k):

    if low <= high:

        pivot = partition(arr, low, high)
        

        if pivot == k:
            return arr[:pivot]
        elif pivot < k:
            return quick_select(arr, pivot + 1, high, k)
        else:
            return quick_select(arr, low, pivot - 1, k)



for i in range(len(arr)+1):
    k_min_vals = quick_select(arr, 0, len(arr) - 1, i)

    print(arr)
    print(k_min_vals)
