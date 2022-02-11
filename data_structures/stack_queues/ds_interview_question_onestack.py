#with one stack and recursion

class MyQueue(object):
    def __init__(self):
        self.stack = []

    def __str__(self) -> str:
        return str(self.stack)

    def push(self, x): #-> O(n)
        if len(self.stack) == 0:
            self.stack.append(x)
            return
        tmp = self.stack.pop()
        self.push(x)
        self.stack.append(tmp)

    def pop(self):
        return self.stack.pop(-1)

    def peek(self):
        return self.stack[-1]

    def empty(self):
        return len(self.stack) == 0

myQueue = MyQueue()
myQueue.push('Joy')
print(myQueue)
myQueue.push('Matt')
print(myQueue)
myQueue.push('Pavel')
print(myQueue)
myQueue.push('Samir')
print(myQueue)
myQueue.pop()
myQueue.pop()
myQueue.push('Oscar')

print(myQueue)