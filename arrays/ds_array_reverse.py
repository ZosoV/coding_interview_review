#Create a function that reverses a string:

def reverse(string): # -> time complexity is O(n) and space complexity is O(n)
    # check input # don't assumme
    if not string or type(string) != str or len(string) < 2 :
        return 'that is not good'

    result = ""
    for i in range(len(string)-1,-1,-1):
        result += string[i]
    
    return result

example01 = "Hi My name is Oscar"
print("Simple reverse:",reverse(example01))

#A smarter way to do this , can be taking a pair of elements from either end of the string and swapping them
#We have start at both the ends and continue swapping pairs till the middle of the string
#This way we can avoid having to create a new array and save on space complexity while keeping time complexity at O(n)

def swap(string, a, b): #Function which swaps two characters of a string
    string = list(string)
    temp = string[a]
    string[a] = string[b]
    string[b] = temp
    return ''.join(string)

def smarter_reverse(string): #-> time complexity O(n) yet, but space complexity 1
    for i in range(len(string)//2):
        string = swap(string, i, len(string)-i-1)
    return string

print("Smarter Reverse:",smarter_reverse(example01))


# Other python implementations
# more readable
example01 = "Hi My name is Oscar"
print("Extra 01:",''.join(reversed(example01)))

example01 = "Hi My name is Oscar"
print("Extra 02:",example01[::-1])
