# Implement Queue using Stacks

# Solution: https://leetcode.com/problems/implement-queue-using-stacks/solution/

# -> 1 2 3 

# -> 3
# 2
# -> 3 2

# 3 2 1 <-



# queue -> the first one element

# queue  -> one element in the queque at the last
#  

# Approach #1  enquee -> O(n) dequeue -> O(1)
class Queue:

    def __init__(self) -> None:
        self.stack1 = [] # pop from here == to dequeue
        self.stack2 = [] 
        self.length = 0

    def __str__(self) -> str:
        return str(self.stack1)

    def peek(self):
        return self.stack1[-1]

    def enquee(self,val):

        while(len(self.stack1) != 0):
            self.stack2.append(self.stack1.pop())

        self.stack2.append(val)

        while(len(self.stack2) != 0):
            self.stack1.append(self.stack2.pop())

        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        val2return = self.stack1.pop()
        self.length -= 1
        return val2return

myQueue = Queue()
myQueue.enquee('Joy')
myQueue.enquee('Matt')
myQueue.enquee('Pavel')
myQueue.enquee('Samir')
myQueue.dequeue()
myQueue.dequeue()
myQueue.enquee('Oscar')

print(myQueue)