arr1 = [0,3,4,31,35]
arr2 = [4,6,18,25,30,33,34,35]

def mergeSortedArrays(arr1,arr2): #(n,m)
    i = 0
    j = 0

    sorted_list = []
    while(i<len(arr1) and j<len(arr2)): # -> O(n+m)
        if arr1[i] < arr2[j]:
            sorted_list.append(arr1[i])
            i += 1
        else:
            sorted_list.append(arr2[j])
            j += 1

    if i >= len(arr1):
        sorted_list += arr2[j:] #-> Slicing has a complexity of O(k) 
    if j >= len(arr2):          #-> where k is the size of the slice
        sorted_list += arr1[i:] #

    return sorted_list

#Better option
def mergeSortedArrays2(arr1,arr2): #(n,m)

    if len(arr2) == 0: # -> O(1)
        return arr1
    if len(arr1) == 0:
        return arr2    # -> O(1)

    i = 0
    j = 0

    sorted_list = []
    while(i<len(arr1) and j<len(arr2)): # -> O(n + m)
        # note here I have to consider the extreme case when
        # a value it is not accesible
        if not arr2[i] or arr1[i] < arr2[j]:
            sorted_list.append(arr1[i])
            i += 1
        else:
            sorted_list.append(arr2[j])
            j += 1

    return sorted_list

print(mergeSortedArrays2(arr1,arr2))     