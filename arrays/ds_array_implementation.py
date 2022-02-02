
class MyArray():

    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1
    
    def pop(self):
        last_item = self.data[self.length-1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    def delete(self, index):
        item = self.data[index]

        #shift items to left
        for i in range(index,self.length-1):
            self.data[i] = self.data[i+1]

        del self.data[self.length-1]

        self.length -= 1
        return item

    def insert(self, index, item):

        #shift items to right
        for i in range(self.length, index-1,-1):
            self.data[i] = self.data[i-1]

        self.data[index] = item

        self.length += 1


    def __str__(self):
        output = {
            "length" : self.length,
            "data" : str(self.data)
        }
        return str(output)

newArray = MyArray()
newArray.push("hi")
newArray.push("you")
newArray.push("!")
newArray.push("are")
newArray.push("nice")

newArray.insert(3, "oscar")

# newArray.pop()
# newArray.pop()

#newArray.delete(1)

print(newArray)