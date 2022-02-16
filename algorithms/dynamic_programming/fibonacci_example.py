
# fib(n) -> 0 1 1 2 3 5 8
# n      -> 0 1 2 3 4 5 6

calculations = 0
def fib(n): # Time Complexity -> O(2^n)
            # Space Complexity -> O(h) the stack is as deep as the height of the tree
    global calculations
    calculations += 1
    if n <= 1:
        return n

    return fib(n-1) + fib(n-2)

print(fib(10))
print("Calculation:", calculations)


calculations = 0
def fibMaster(): # Time Complexity -> O(n) 
    cache = {}   # Space Complexity -> O(n) # where are saving the evaluation for each fib(n)
                 # Trade off between time and space complexity
    def fib(n):
        global calculations
        calculations += 1
        if n <= 1:
            return n

        if not (n-1) in cache:
            cache[n-1] = fib(n-1)

        if not (n-2) in cache:
            cache[n-2] = fib(n-2)

        return cache[n-1] + cache[n-2]

    return fib


dp_fib = fibMaster()

print(dp_fib(10))
print("Calculation:", calculations)

calculations = 0
def fib_bottom_up_approach(n):
    global calculations
    answer = [0,1]
    for i in range(2, n-1):
        calculations += 1
        answer.append(answer[i-1]+answer[i-2])

    return answer.pop()


print(fib_bottom_up_approach(10))
print("Calculation", calculations)