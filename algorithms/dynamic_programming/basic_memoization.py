def addTo80(n):
    print("Long Time")
    return n + 80


def memoizedAddTo80():
    cache = {}
    def inner_func(n):
        print(cache)
        if n in cache:
            return cache[n]
        else:
            print('long time')
            cache[n] = 5 + 80
            return cache[n]
    
    return inner_func

memoized_func = memoizedAddTo80()

print("1",memoized_func(5))
print("2",memoized_func(5))