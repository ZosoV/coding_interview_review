class HashTable():
    def __init__(self, size):
        self.data = [None] * size
        self.size = size

        # buckets are
        # [['grapes',100000]]

    def _hash(self,key):
        # hash function -> smallest function
        # the function is a loop with few iteration
        # we consider this function O(1)
        hash = 0 
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % self.size
        return hash

    def set(self, key, value): # no loop -> O(1)
        address = self._hash(key)
        if not self.data[address]:
            self.data[address] = [] 
        self.data[address].append([key,value])

    def get(self, key): # if not collisions -> O(1)
                        # with collision, ocassionally -> O(n)
        address = self._hash(key)
        current_bucket = self.data[address]

        if current_bucket:
            for item in current_bucket:
                if item[0] == key:
                    return item[1]
        else:
            return None

    def keys(self): # downside when get keys-> O(n)
        keys_array = []

        for bucket in self.data:
            if bucket:
                if len(bucket) > 1:
                    for item in bucket:
                        keys_array.append(item[0])
                else:
                    keys_array.append(bucket[0][0])

        return keys_array

    def __str__(self):
        string = []
        for address, item in enumerate(self.data):
            string.append(str(address)+":"+ str(item))
        return str(string)


myHashTable = HashTable(50)

myHashTable.set('grapes', 10000)
myHashTable.set('apples', 54)
myHashTable.set('oranges', 2)

print(myHashTable)
print(myHashTable.get('grapes'))

print(myHashTable.keys())