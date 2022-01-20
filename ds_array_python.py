# For python: http://www.laurentluce.com/posts/python-list-implementation/

# Python -> List -> works as Dynamic Arrays

strings = ['a', 'b', 'c', 'd']

# Lookup -> O(1)
strings[0]

# Push -> O(1) # adding at the end
# Sometimes you can find the situation that is O(n)
strings.append('e')

# Pop -> O(1) # remove the last data item
strings.pop()
strings.pop()

# Insert -> O(n) # add at the begining
# What is happening under the hood?
strings.insert(0,'x')

# At the middle of the array
strings.insert(len(strings)//2,'alien') # O(n) also

# Delete -> O(n) # delete at a position
strings.pop(2)

# Extra: remove an specific item -> O(n)
strings.remove('a')

print(strings)