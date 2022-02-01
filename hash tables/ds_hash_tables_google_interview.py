# Google Question
# Given an array = [2,5,1,2,3,5,1,2,4]
# It should return 2

# Given an array = [2,1,1,2,3,5,1,2,4]
# It should return 1

#Given an array = [2,3,4,5]
# It should return undefined

def firsOcurrennce1(arr): # -> O(1) in space but O(n^2) in time
    for i in range(1, len(arr)):
        for j in range(0,i):
            if (arr[i] == arr[j]):
                return arr[i]


print(firsOcurrennce1([2,5,1,2,3,5,1,2,4]))
print(firsOcurrennce1([2,1,1,2,3,5,1,2,4]))
print(firsOcurrennce1([2,3,4,5]))

def firsOcurrennce(arr):

    ocurrences = set() # -> O(n) in space

    for num in arr: # -> O(n) in time
        if num in ocurrences:
            return num
        else:
            ocurrences.add(num)
    
    return None

print(firsOcurrennce([2,5,1,2,3,5,1,2,4]))
print(firsOcurrennce([2,1,1,2,3,5,1,2,4]))
print(firsOcurrennce([2,3,4,5]))
