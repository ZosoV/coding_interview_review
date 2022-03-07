def coinChange(coins, amount): 
# n: len(coints)
# m: amount + 1
# Time Complexity: O(nm)
# Space Complexity: O(m)
    
    # dp stores the number of ways to count that amount
    dp = [0] * (amount+1)
    
    dp[0] = 1
    
    #coins should be the first and outer 'for' loop to avoid counting duplicate combinations with different order(permutations)
    for coin in coins:

        # take the coin a check the rest with the current coin
        # eg: [1,2,4] amount = 3 
        # amount + 1    coin
        # 4               1 -> Loop val from 0-2
        # val    coin
        # 0      1

        for val in range( (amount+1) - coin):
            if dp[val]:
                dp[val + coin] += dp[val]



    return dp[-1] 

def count(coins, amount):
 
    # table[i] will be storing the number of solutions for
    # value i. We need n+1 rows as the table is constructed
    # in bottom up manner using the base case (n = 0)
    # Initialize all table values as 0
    table = [0] * (amount+1)
 
    # Base case (If given value is 0)
    table[0] = 1
 
    # Pick all coins one by one and update the table[] values
    # after the index greater than or equal to the value of the
    # picked coin
    for coin in coins:
        for val in range(coin,amount+1):
            print(val, val-coin, table[val-coin])
            table[val] += table[val-coin] # mi valor actual es lo que val 
                                          # val menos una moneda usada
 
    return table[-1]
                  
arr = [1, 2, 5]
amount = 5
print(coinChange(arr, amount))

print(count(arr, amount))