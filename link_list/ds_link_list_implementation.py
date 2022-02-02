# 10-> 5 -> 16

# You can use this class for nodes also
class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self, value):
        self.head = {
            "value": 10,
            "next": None
        }
        self.tail = self.head
        self.length = 1

    def __str__(self) -> str:
        
        current_node = self.head
        string = ""
        while(current_node):
            string += str(current_node['value']) + " -> "
            current_node = current_node['next']

        string += "x"

        return string

    def append(self, value): # -> O(1)
        new_node = {
            "value" : value,
            "next" : None
        }
        self.tail['next'] = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value): # -> O(1)
        new_node = {
            "value" : 1,
            "next" : None
        }
        new_node["next"] = self.head
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
                "next" : None
            }

            # index -1 because we want the previous node, the "leader"
            leader_node = self.traverseToIndex(index - 1)

            holder_node = leader_node['next']
            leader_node['next'] = new_node
            new_node['next'] = holder_node
           
            self.length += 1

    def remove(self, index): # -> O(n)
        if index >= self.length:
            index = self.length - 1
        if index == 0:
            self.head = self.head['next']
            self.length -= 1
        else:
            
            leader = self.traverseToIndex(index - 1)
            node2remove = leader['next']
            leader['next'] = node2remove['next']
            node2remove['next'] = None
            #del node2remove

            if index == self.length - 1:
                self.tail = leader
            
            self.length -= 1

    def reverse(self):

    # TODO: Review again

        if self.head['next']:
            self.tail = self.head
            first = self.head
            second = self.head['next']

            while(second):
                temp = second['next']
                second['next'] = first

                first = second
                second = temp

            self.head['next'] = None
            self.head = first            


    # def lookup(self, index):
    #     while (i < index):

myLinkedList = LinkedList(10)
myLinkedList.append(5)                  # 10 ->5
myLinkedList.append(16)                 # 10 -> 5 -> 16
myLinkedList.prepend(1)                 # 1 -> 10 -> 5 -> 16
myLinkedList.insert(2,99)               # 1 -> 10 -> 99 -> 5 -> 16
myLinkedList.insert(100,88)             # 1 -> 10 -> 99 -> 5 -> 16 -> 88
myLinkedList.remove(3)                  # 1 -> 10 -> 99 -> 16 -> 88
myLinkedList.remove(3)                  # 1 -> 10 -> 99 -> 88

myLinkedList.reverse()                  # 88 -> 99 -> 10 -> 1
print(myLinkedList)