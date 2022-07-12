# NOTE:
# 1. BFS uses a queue and additional visited array to store the
#    nodes that are already visited
# 2. We have to change to True inmedialy after pushing a new value to the queue
# 3. Complexity -> Time: O(N + E) Space: O(N)

from collections import defaultdict
from queue import Queue

class Graph:
 
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)


def BFS(graph, source = 2):

    queue = Queue()
    visited = [False] * len(graph)
    print(visited)
    
    # Put the start node in queue
    queue.put(source)
    visited[source] = True

    while(not queue.empty()):
            print(list(queue.queue))
            # Take node from queue
            node_idx = queue.get()
            

            # Make an operation
            print(node_idx)

            # Push the neighbor values it that values are not already visited
            
            for idx in graph[node_idx]:
                if visited[idx] == False:
                        queue.put(idx)
                        visited[idx] = True
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

BFS(g.graph, source = 2)
