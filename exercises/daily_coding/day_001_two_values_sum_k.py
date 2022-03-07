# Good morning! Here's your coding interview problem for today.

# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

def TwoNumberSumK(arr, k):

    hashmap = set()

    for num in arr:
        if k-num in hashmap:
            return True
        
        hashmap.add(num)

    return False

print(TwoNumberSumK([10, 15, 3, 7], 17))
print(TwoNumberSumK([10, 15, 3, 7], 20))