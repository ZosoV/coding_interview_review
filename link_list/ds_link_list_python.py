
# Python does not have linked list
# Linked list: apples --> grapes --> pears
# apples
# 8947  --> grapes
#           8742  --> pears
#                     372 --> null

# Garbage collector and Reference
obj1 = {"a": True}
obj2 = obj1 # reference
print('1', obj1)
print('2', obj2)
obj1['a'] = 'booya'
del obj1

#obj1 and obj2 point to the same object in memory {"a": True}
#print('1', obj1)
print('2', obj2)