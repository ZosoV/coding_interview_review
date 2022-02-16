def insertion_sort(arr):

    # time complexity -> O(n^2)
    # space complexity -> O(1)

    # However if the arr is nearly ordered and have few values
    # the time complexity could become O(n)

    # sorted part first element, unsorted the rest in the beginning.
    for i in range(1,len(arr)):
        # take the first element from unsorted part
        tmp = arr[i]

        # swap the greater values than tmp in the sorted part
        j = i-1
        while j >= 0 and tmp < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        # when there are not more great values
        # insert the value in the current idx
        # Note that here we use j+1 because at the last step of the while loop
        # the algorithm rest 1 to go out from the loop
        arr[j+1] = tmp

    return arr
print(insertion_sort([5,2,7,1]))