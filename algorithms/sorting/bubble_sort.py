
def bubble_sort(arr):

    # space complexity -> O(1)
    # time compelxity -> O(n)

    # the i-index controls how many start from the beginning
    # I'm going to do
    for i in range(len(arr)-1):
        # the j index the begining to the array
        for j in range(len(arr)-1):
            if arr[j+1] < arr[j]:
                # swap values 
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp

    return arr

arr1 = [5,2,7,1,464, 121, 64646,25, 12,4]
print(bubble_sort(arr1))