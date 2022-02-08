
class Stack():
    def __init__(self) -> None:
        self.data = []
        self.length = 0

    def __str__(self) -> str:
        return str(self.data)

    def peek(self):
        return self.data[self.length-1]

    def push(self,value):
        self.data.append(value)
        self.length += 1

    def pop(self):
        value2return = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return value2return




myStack = Stack()
myStack.push(2)
myStack.push(3)
myStack.push(5)
myStack.pop()
print(myStack.peek())
#myStack.pop()
print(myStack)