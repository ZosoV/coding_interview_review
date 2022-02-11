from math import factorial


def factorial_recursive(n): # -> O(n)
    if n <= 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

def factorial_loop(n): #-> O(n)

    result = 1
    for i in range(n):
        result *= n-i

    return result

print(factorial_recursive(0))
print(factorial_loop(0))