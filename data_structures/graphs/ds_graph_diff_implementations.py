
# Edge List 
graph = [[0, 2], [2,3], [2,1], [1,3]] #connections

# Ajacent List -> the index is the node and the value is the neighbor 
graph = [[2], [2,3] , [0,1,3], [1,2]]

# as hash table
#graph = { 0: [2], 1: [2,3], 2: [0,1,3], 3: [1,2]} # useful if you don't have sequential values

# Adjacent Matrix

# of the connections
graph = [
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]

# as a dict
graph = {
    "0": [0, 0, 1, 0],
    "1": [0, 0, 1, 1],
    "2": [1, 1, 0, 1],
    "3": [0, 1, 1, 0] 
}