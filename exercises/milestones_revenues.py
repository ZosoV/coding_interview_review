# Revenue Milestones
# We keep track of the revenue Facebook makes every day, and we want to know on what days Facebook hits certain revenue milestones. Given an array of the revenue on each day, and an array of milestones Facebook wants to reach, return an array containing the days on which Facebook reached every milestone.
# 
# Signature
# int[] getMilestoneDays(int[] revenues, int[] milestones)
# 
# Input
# revenues is a length-N array representing how much revenue FB made on each day (from day 1 to day N). milestones is a length-K array of total revenue milestones.
# 
# Output
# Return a length-K array where K_i is the day on which FB first had milestones[i] total revenue. If the milestone is never met, return -1.
# 
# Example
# revenues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# milestones = [100, 200, 500]
# output = [4, 6, 10]
# 
# Explanation
# On days 4, 5, and 6, FB has total revenue of $100, $150, and $210 respectively. Day 6 is the first time that FB has >= $200 of total revenue.


from queue import PriorityQueue

def getMilestoneDays(revenues, milestones):
    # n: revenues
    # m: milestones

    # priority queque -> space O(n)
    queue = PriorityQueue() 

    for i in range(len(milestones)):   # time: O(nlog(n))
        queue.put((milestones[i], i))

    # zip and sort is also useful
    # zip_list = [ (val, idx) for idx, val in enumerate(milestones)] # time O(n)
    # zip_list.sort(key = lambda tup: tup[0]) # time O(nlog(n))

    i = 0 # i points revenues
    acum = 0
    res = [-1] * len(milestones)

    while(i < len(revenues) and not queue.empty()): # time: O(n + m)

        acum += revenues[i]

        while(not queue.empty() and acum >= queue.queue[0][0]):
            index = queue.get()[1]
            res[index] = i+1 # because iterator i start in 0

        i += 1

    # total time complexity: O(nlog(n)) + O(n + m) -> O(nlog(n))
    # NOTE: if I don't want to deal with repeated milestiones
    # I could use a hashmap with key:milestone val:idx
    # with space complexity: O(n) and time complexity: O(n)
    # Then my final complexity will be O(n + m)

    return res


revenues_1 = [100, 200, 300, 400, 500]
milestones_1 = [300, 800, 1000, 1400]
expected_1 = [2, 4, 4, 5]
print(getMilestoneDays(revenues_1, milestones_1))

revenues_2 = [700, 800, 600, 400, 600, 700]
milestones_2 = [3100, 2200, 800, 2100, 2100, 1000] 
expected_2 = [5, 4, 2, 3, 2]
print(getMilestoneDays(revenues_2, milestones_2))
