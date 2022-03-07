
def BinarySearch(arr, target):

    start = 0
    end = len(arr) - 1 

    while(end >= start):
        mid = (start + end)//2
        if target == arr[mid]:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
    
    return None
arr = [3, 4, 6, 9, 10,  15, 24]
print(BinarySearch(arr,9))

arr = [3, 4, 6, 8, 10,  15, 24, 25]
print(BinarySearch(arr,9))