

import queue

import queue

def level_traversal(root):

    q = queue.Queue()
    q.put(root)

    while not q.empty():
            
        # TODO: something to gather in the level

        for i in range(q.size()):
            node = q.get()

            if node.left:
                q.put(node.left)

            if node.right:
                q.put(node.right)
        
            

def ways_to_score(score):
    # Write your code here
    score_points = [2,3,7]
    counter = [0]
    
    def dfs(i, curr, total):
        
        if total == score:
            counter[0] += 1
            return
        
        if i >= len(score_points) or total > score:
            return
        
        curr.append(score_points[i])
        dfs(i, curr, total + score_points[i])
        
        curr.pop()
        dfs(i + 1, curr,  total)
        
    
    dfs(0, [], 0)


def ways_to_score(score):
    # Write your code here
    score_points = [2,3,7]
    counter = [0]


    def dfs(curr, total):
        
        if total == score:
            counter[0] += 1
            return
        
        if total > score:
            return
        
        for point in score_points:
            dfs(curr, total + point)
            dfs(curr,  total)
        
    
    dfs([], 0)

    return counter[0]