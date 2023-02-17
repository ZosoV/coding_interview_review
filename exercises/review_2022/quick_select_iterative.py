def partition(points, low, high):
    
    mid = low + (high - low) // 2
    
    points[high], points[mid] = points[mid], points[high]
    
    pivot = get_distance(points[high])
        
    left_idx = low
    
    for i in range(low, high):
        
        if get_distance(points[i]) < pivot:
            points[left_idx], points[i] = points[i], points[left_idx]
            left_idx += 1
            
    points[left_idx], points[high] = points[high], points[left_idx]
    
    return left_idx


def quick_select(points, k):
    
    l, r = 0, len(points)-1
    # initialize pivot to the right 
    # if pivot_index == k, that means k == len(points), all points return
    pivot_index = len(points)
    while pivot_index != k:
        pivot_index = partition(points, l ,r)
        # narrowing the range of l & r, keeping index k inside
        if pivot_index < k:
            # points smaller than pivot index is in correct place
            # move left pointer to pivot index: ->
            l = pivot_index + 1
        else:
            # points greater than pivot index is in correct place
            # move right pointer to pivot index -1: <-
            r = pivot_index - 1
    return points[:k]
    
quick_select(points, k)
        