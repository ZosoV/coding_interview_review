# [1, 2, 3, 9] sum=8 -> false
# [1, 2, 4, 4] sum=8 -> true

# 1. understand the problem => input -> outputs
# 2. input contraints
#      - how the arrays are given? as integers, allocated in memory? - return none?
#      - Is the array sorted?
#      - Is possible to have repeated number?
#      - Negatives is possible?
#      - The arrays are short or there is not restriction in the length.
#      - input could be null, sum null

# 3. explain the brute force solution, but it would work. -> time consuming

# 4. better than the brute force, explain based on the known information

# [1, 2, 3, 9]
# 2 + 3 = 5
# 

# 5. decompose your solution, see possible problems and if your code solves it.

from operator import truediv


def HasTwoValuesSum(arr, sum):
    # create the low and high variables
    low = 0
    high = len(arr) - 1

    # loop thourgh these two pivots using the indexes, checking if the sum is greated or lesser than the sum
    while( low < high):
        addition = arr[low] + arr[high]
        if addition == sum:
            return True
        elif addition < sum:
            low += 1
        elif addition > sum:
            high -= 1

    # if not just return false
    return False

arr1 = [1, 2, 3, 9]
print(HasTwoValuesSum(arr1, 10))

# 6. Counter question
# [2, 9, 1, 3]
# [6, ]

# [1, 2, 4, 4]

def HasTwoValuesSum2(arr, sum):
    # create a hash set to store the complements to get the sum
    complements = set()

    # loop trought the array, checking if the complement already exists, saving the complements
    for elem in arr:
        if elem in complements:
            return True
        else:
            complements.add(sum - elem)
    
    return False

arr1 = [1, 2, 3, 9]
print(HasTwoValuesSum2(arr1, 10))