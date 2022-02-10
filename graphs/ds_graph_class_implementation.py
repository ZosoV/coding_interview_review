class Graph():

    def __init__(self) -> None:
        self.numberOfNode = 0
        self.adjacentList = {} # better to remove objects

    def addVertex(self,node):
        # just add the keys with None value (without connections)
        if not self.adjacentList.get(node):
            self.adjacentList[node] = []
            self.numberOfNode += 1

    def addEdge(self,node1, node2):
        # undirected graph
        # If there are already connections. I need to append the new value
        if not node2 in self.adjacentList[node1]:
            self.adjacentList[node1].append(node2)

        # If there are already connections. I need to append the new value
        if not node1 in self.adjacentList[node2]:
            self.adjacentList[node2].append(node1)

    def __str__(self) -> str:
        return str(self.adjacentList)
    

myGraph = Graph()
myGraph.addVertex(0)
myGraph.addVertex(1)
myGraph.addVertex(2)
myGraph.addVertex(3)

myGraph.addEdge(0,1)
myGraph.addEdge(2,3)
myGraph.addEdge(2,0)
myGraph.addEdge(3,2)

print(myGraph)
