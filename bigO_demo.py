import time

# nemo = ['dory', 'bruce', 'marlin','nemo', 
#         'gill', 'bloat', 'nigel', 'squirt',
#         'darla', 'hank']
# large = 100000 * ['nemo']

# def findNemo(array):
#     for i in range(len(array)):
#         if array[i] == 'nemo':
#             print('Found NEMO!')
# findNemo(large) # O(n) --> Linear Time

boxes = [1, 2, 3, 4, 5]

def log_pairs(array):
    for i in array:
        for j in array :
            if i != j:
                print(i,j)

log_pairs(boxes)