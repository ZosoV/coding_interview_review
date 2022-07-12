
# NOTE:
# 1. DFS in graphs doesn't have preorder or in order variations
# 2. DFS uses an stack to pick values and a visited array to 
#    keep track of the already visited nodes
# 3. Visited nodes of given node_idx is update inmediately after pushing a 
#    to the stack.
# 4. Complexity -> Time: O(N + E) Space: O(N)


from collections import defaultdict


class Graph:
 
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)


def DFS(graph, source = 2):

    stack = []
    visited = [False] * len(graph)

    stack.append(source)
    visited[source] = True

    while (len(stack) != 0):
            print(stack)
            # get the element
            node_ix = stack.pop()

            print(node_ix)

            for idx in graph[node_ix]:
                    if not visited[idx]:
                        stack.append(idx)
                        visited[idx] = True

def recursive_DFS(graph, source = 2):
    
        def aux_func(node_idx, visited):
                
                visited[node_idx] = True
                print(node_idx)

                for idx in graph[node_idx]:
                        if not visited[idx]:
                                aux_func(idx, visited)
   
        aux_func(source, [False]*len(graph))

g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,0)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(2,4)
g.addEdge(3,2)
g.addEdge(4,2)
g.addEdge(3,1)
g.addEdge(3,4)
g.addEdge(1,3)
g.addEdge(4,3)

DFS(g.graph, source = 2)

print("----")
recursive_DFS(g.graph, source=2)