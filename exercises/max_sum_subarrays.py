

def max_sum_subarray(arr):

    max_so_far = float("-inf")
    acum = 0

    for num in arr:
        acum += num
        if acum > max_so_far:
            max_so_far = acum
        if acum < 0:
            acum = 0

    return max_so_far

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(max_sum_subarray(arr))
    
arr = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
print(max_sum_subarray(arr))

