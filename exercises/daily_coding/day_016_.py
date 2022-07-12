# Date: 03/07/2022

"""
Daily Coding Problem: Problem #16 [Easy]

You run an e-commerce website and want to record the last N order ids in a log. 
Implement a data structure to accomplish this, with the following API:
record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.
"""

"""
Sol: If you implement a circular array initialize with N spaces, you can push and get values with
     time complexity O(1) and space complexity O(N)
"""

class LogRercord():

    def __init__(self, N) -> None:
        # as you want to record the last N logs the data structure has a fixed memory
        self.orderIds = [None] * N

        # you have to keep a track of the current idx
        self.current_idx = 0

        # also could uselful to keep a track of the size
        self.size = N

    def record(self, order_id):
        
        # save the new record 
        self.orderIds[self.current_idx] = order_id

        # update the current idx
        self.current_idx = (self.current_idx + 1) % self.size


    def get_last(self,i):
        # always check that i must be least to N
        if i >= self.size:
            print("idx out of bounds")
            return None

        # to get the last ith element, I have to use another circular formula
        # try with different edges cases until find the correct
        # NOTE: that the current idx is one unit ahead

        # size = 7 elements
        # current_idx = 0, i = 2 ==>  7 - 2 + 0 = 5 % 7 = 5 correct
        # current_idx = 5, i = 2 ==>  7 - 2 + 5 = 10 % 7 = 3 correct

        idx = ( self.size - i + self.current_idx ) % self.size

        return self.orderIds[idx] # O(1)


ecommerceRecords = LogRercord(10)

for i in range(1,101):
    ecommerceRecords.record(i)

print(ecommerceRecords.orderIds)
print(ecommerceRecords.get_last(5))

print(ecommerceRecords.orderIds)
print(ecommerceRecords.get_last(70))

