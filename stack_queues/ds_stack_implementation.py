class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Stack():
    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.length = 0

    def __str__(self) -> str:
        string = ""
        current_element = self.top
        while current_element:
            string += str(current_element.value) + " -> "
            current_element = current_element.next
        return string

    def peek(self):
        return self.top.value

    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

        if self.length == 0:
            self.bottom = new_node

        self.length += 1

    def pop(self):
        if not self.top:
            return None
            
        value2return = self.top.value
        self.top = self.top.next

        self.length -= 1

        if self.length == 0:
            self.bottom = None
        return value2return




myStack = Stack()
myStack.push(2)
myStack.push(3)
myStack.push(5)
myStack.pop()
print(myStack.peek())
myStack.pop()
print(myStack)