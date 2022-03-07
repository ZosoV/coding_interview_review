def coinChange(target, coins):

    # I want to save the min number of coins needed to sum target target  
    cache = {}
    
    def dfs(idx, accum):
        
        # cuando se puede sumar
        if accum == target:
            return 0
        
        # cuando no se puede summar
        if accum > target:
            return float('inf')
        
        # si utilice todas las monedas y no se puede sumar
        if idx == len(coins):
            return float('inf')
        
        if (idx, accum) in cache:
            return cache[(idx, accum)]
        
        cache[(idx, accum)] = min(
                        dfs(idx, accum + coins[idx]) + 1, 
                        dfs(idx + 1, accum))
        return cache[(idx, accum)]
    
    result = dfs(0, 0) 
    return result if result != float('inf') else -1

def coinChange2(amount, coins): 
# n: len(coints)
# m: amount + 1
# Time Complexity: O(nm)
# Space Complexity: O(m)
    
    # dp stores the min number of coins to get an amount
    dp = [amount + 1] * (amount+1)
    
    dp[0] = 0
    
    for val in range(1, amount + 1):
        
        for coin in coins:
            remain = val - coin 
            
            if remain >= 0:
                dp[val] = min(dp[val], 1 + dp[remain])
                
    return dp[amount] if  dp[amount] != amount + 1 else -1

arr = [1, 2, 3, 5]
amount = [4, 3, 7, 9, 11]

for a in amount:
    print(coinChange(a, arr))
    print(coinChange2(a, arr))