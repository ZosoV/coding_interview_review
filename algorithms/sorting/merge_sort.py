
def merge_sort(arr):
    length = int(len(arr))
    if length == 1:
        return arr

    print(arr[0:length//2], arr[length//2:])

    return merge(
        merge_sort(arr[0:length//2]), 
        merge_sort(arr[length//2:]))

def loop_merge(left, right):
    result = []
    i = 0
    j = 0
    while(i < len(left) and j < len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i == len(left):
        result += right[j:]
    elif j == len(right):
        result += left[i:]

    return result

def merge(left,right):
    
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    else:
        return [right[0]] + merge(left, right[1:])

print(merge_sort([5,2,7,1,54,85,12,4,13,56]))