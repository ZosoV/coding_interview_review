
# 0 1 1 2 3 5 8 13

# Get the n-th fibonacci value


from os import curdir


def fibonacci_recursive(n): # -> O(2^n) # exponencial time  
    if n < 2:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    
    #0 1 2 3 4 5

def fibonacci_loop(n): # -> O(n)

    n1 = 0
    n2 = 1
    for i in range(n-1):
        val = n1 + n2
        n1 = n2
        n2 = val

    return val

def fibonacci_loop2(n): # -> O(n)
    arr = [0,1]
    for i in range(2,n+1): 
        arr.append(arr[i-2] + arr[i-1])

    return arr[n]

print(fibonacci_recursive(5))
print(fibonacci_loop(5))
print(fibonacci_loop2(5))