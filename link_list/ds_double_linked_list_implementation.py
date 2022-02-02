class DoubleLinkedList():
    def __init__(self, value):
        self.head = {
            "value": 10,
            "next": None,
            'previous': None
        }
        self.tail = self.head
        self.length = 1

    def __str__(self) -> str:
        
        current_node = self.head
        string = "x <- "
        while(current_node):
            string += str(current_node['value']) + " <-> "
            current_node = current_node['next']

        string += "x"

        return string

    def append(self, value): # -> O(1)
        new_node = {
            "value" : value,
            "next" : None,
            'previous': None
        }
        new_node['previous'] = self.tail
        self.tail['next'] = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value): # -> O(1)
        new_node = {
            "value" : 1,
            "next" : None,
            "previous" : None,
        }
        new_node["next"] = self.head
        self.head["previous"] = new_node
        self.head = new_node
        self.length += 1

    def traverseToIndex(self, index): 
        current_node = self.head
        i = 0
        while i < index: 
            current_node = current_node['next']
            i += 1

        return current_node

    def insert(self, index, value): # -> O(n)
        if index >= self.length:
            self.append(value)
        elif index == 0:
            self.prepend(value)
        else:
            new_node = {
                "value": value,
                "next" : None,
                "previous": None
            }

            # index -1 because we want the previous node, the "leader"
            leader = self.traverseToIndex(index - 1) # -> O(n)
            follower = leader['next']

            new_node['next'] = follower
            new_node['previous'] = leader
            leader['next'] = new_node
            follower['previous'] = new_node

            self.length += 1

    def remove(self, index): # -> O(n)
        if index >= self.length:
            index = self.length - 1
        if index == 0:
            self.head = self.head['next']
            self.length -= 1
        else:
            
            leader = self.traverseToIndex(index - 1) # -> O(n)
            follower2 = leader['next']['next']
            leader['next'] = follower2

            if index != self.length - 1:
                follower2['previous'] = leader

            #del node2remove

            if index == self.length - 1:
                self.tail = leader
            
            self.length -= 1

myLinkedList = DoubleLinkedList(10)
myLinkedList.append(5)                  # 10 <-> 5
myLinkedList.prepend(1)                 # 1  <-> 10 <-> 5
myLinkedList.insert(2,99)               # 1  <-> 10 <-> 99 <-> 5
myLinkedList.remove(1)                  # 1  <-> 99 <-> 5
myLinkedList.remove(2)                  # 1  <-> 99 <-> 5

print(myLinkedList)