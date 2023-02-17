

def ways_to_score(score):
    # Write your code here
    score_points = [2,3,7]
    res = []
    point2letters = {
        2 : "SF",
        3 : "GL",
        7 : "TD"
    }

    def dfs(curr, total):
        
        if total == score:
            res.append(curr.copy())
            return
        
        if total > score:
            return
        
        for point in score_points:
            curr.append(point2letters[point])
            dfs(curr, total + point)
            curr.pop()           

        
    
    dfs([], 0)

    return [ ",".join(arr) for arr in res ]

print(ways_to_score(7))