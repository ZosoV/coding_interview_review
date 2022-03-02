# The question we'll work through is the following: 
# return a new sorted merged list from K sorted lists, 
# each with size N. Before we move on any further, 
# you should take some time to think about the solution!

# First, go through an example. This buys time, makes 
# sure you understand the problem, and lets you gain some 
# intuition for the problem. 

# For example, if we had [[10, 15, 30], [12, 15, 20], [17, 20, 32]], 
# the result should be [10, 12, 15, 15, 17, 20, 20, 30, 32].

# NOTE: At the end of the interview
# The question we'll work through is the following: return 
# a new sorted merged list from K sorted lists, each with size N. 
# Before we move on any further, you should take some time to 
# think about the solution!

# First, go through an example. This buys time, makes sure you 
# understand the problem, and lets you gain some intuition for the problem. 
# For example, if we had [[10, 15, 30], [12, 15, 20], [17, 20, 32]], the result 
# should be [10, 12, 15, 15, 17, 20, 20, 30, 32].


# HEAP SOLUTION

from queue import PriorityQueue

def merge_list(list_of_list):
    # n : number of list
    # m : size of sublist -> the greater in the worst case

    pq = PriorityQueue()

    for i, sublist in enumerate(list_of_list): # save tuples (value, list_idx, idx)
        pq.put((sublist[0], i, 0)) # O(log(n))

    merged = []
    while(not pq.empty()): # O(m*n)

        value, list_idx, idx = pq.get()
        print(value)
        merged.append(value)

        if idx + 1 < len(list_of_list[list_idx]):
            pq.put((list_of_list[list_idx][idx + 1], list_idx, idx + 1)) # log(n)

    # Final complextity -> O(m*n*log(n))
    return merged


# with points -> Naive solution

def merge_list(arr): # Complexity = n^2*m

    pointers = [0] * len(arr)

    merged = []
    while( sum(pointers) < len(arr)*len(arr[0])): # n*m

        min_idx = 0
        min_value = float("inf")
        for list_idx in range(len(pointers)): # n
            idx = pointers[list_idx]

            if idx < len(arr[list_idx]):
                if arr[list_idx][idx] < min_value:
                    min_value = arr[list_idx][idx]
                    min_idx = list_idx

        pointers[min_idx] += 1
        merged.append(min_value)
        
    return merged


arr1 = [[10, 15, 30], [12, 15, 20], [17, 20, 32]]
print(merge_list(arr1)) 

    