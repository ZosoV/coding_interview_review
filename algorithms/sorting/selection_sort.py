def selection_sort(arr):
    # space complexity -> O(1)
    # time compelxity -> O(n)

    
    for i in range(len(arr)):
        min_value = arr[i]
        index = i
        for j in range(i+1,len(arr)):
            if arr[j] < min_value:
                min_value = arr[j]
                index = j
        arr[index] = arr[i]
        arr[i] = min_value
        

    return arr

arr1 = [5,2,7,1,464, 121, 64646,25, 12,4]
print(selection_sort(arr1))