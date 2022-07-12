
arr = [1,5, 6, 2, 3, 1, 7]

# I remember that the idea of this algorithm is to use a pivot
# to divide the array in a recursive way
# this pivot is the middle point.

# After divinding the array some times you get just leaves that only contains
# one value

# You have to compare these leaves pair-by-pair 
# an build small sub arrays that are used to build large arrays until
# get the final order array


def merge(arr1, arr2):

    res = []

    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1

    if i == len(arr1): res += arr2[j:]
    if j == len(arr2): res += arr1[i:]

    return res


def merge_sort(arr):

    if len(arr) == 1:
        return arr
        
    m = len(arr) // 2

    left = merge_sort(arr[:m])
    right = merge_sort(arr[m:])

    return merge(
        left,
        right
    )

arr = merge_sort(arr)
print(arr)