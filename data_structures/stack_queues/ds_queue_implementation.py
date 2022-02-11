class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Queue():
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self) -> str:
        string = ""
        current_element = self.first
        while current_element:
            string += str(current_element.value) + " -> "
            current_element = current_element.next
        return string

    def peek(self):
        return self.first.value

    def enquee(self,value):
        new_node = Node(value)
       
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self.length += 1

    def dequeue(self):
        if not self.first:
            return None
            
        value2return = self.first.value
        self.first = self.first.next

        self.length -= 1

        if self.length == 0:
            self.last = None
        return value2return




myQueue = Queue()
myQueue.enquee('Joy')
myQueue.enquee('Matt')
myQueue.enquee('Pavel')
myQueue.enquee('Samir')
myQueue.dequeue()
print(myQueue)