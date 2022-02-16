

def quick_sort(arr, low, high):
    if low < high:

        pi = partition2(arr, low, high)

        quick_sort(arr, 0, pi-1)
        quick_sort(arr, pi + 1, high)

    return arr

def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    
    for j in range(low, high):

        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i] #swap
    
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i+1

def partition2(arr, low, high):
    pivot = arr[high]
    pivot_idx = high

    for i in range(low, high):

        if arr[i] >= pivot:
            arr[pivot_idx] = arr[i]
            arr[i] = arr[pivot_idx - 1]
            arr[pivot_idx - 1] = pivot
            pivot_idx -= 1

    return pivot_idx

arr = [5,2,7,9,1,4]
print(quick_sort(arr, 0, len(arr)-1))
print(arr)