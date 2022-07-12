

def mergeKarray(lists):

    while len(lists) > 1:
        
        tmp = [] # Space: O(n*k)
        for i in range(0,len(lists),2): # Time: O(log(k))
            list1 = lists[i]
            list2 = lists[i+1] if i+1 < len(lists) else None
            
            tmp.append(merge2arrays(list1,list2)) #Time: O(n)
            
        lists = tmp
        
    # Time: O(nlog(k))
    # Space: O(n*k)
        
    return lists[0] if len(lists) > 0 else None


def merge2arrays(arr1, arr2):

    res = [] # Space O(n + m)

    i = j = 0
    while(i < len(arr1) and j < len(arr2)): # Time O(n + m)

        if arr1[i] <= arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1

    return res

