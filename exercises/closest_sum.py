def closest_sum_pair(arr1, arr2, target):
    #sort the arrays
    arr1.sort()
    arr2.sort()

    i = 0
    j = len(arr2) - 1
    closest_sum = float('inf')
    closest_pair = (0,len(arr2)-1)

    while(i < len(arr1) and j >= 0):
        current_sum = arr1[i] + arr2[j]
        if  abs(target - current_sum) < abs(target - closest_sum):
            closest_sum = current_sum
            closest_pair = (arr1[i],arr2[j])

        if current_sum == target:
            return closest_pair
        elif current_sum < target:
            i += 1
        else:
            j -= 1
        


    return closest_pair
        

# NOTE: You can use the following values to test this function.
a1 = [-1, 3, 8, 2, 9, 5]
a2 = [4, 1, 2, 10, 5, 20]
a_target = 24
print(closest_sum_pair(a1, a2, a_target)) #should return (5, 20) or (3, 20).

b1 = [7, 4, 1, 10]
b2 = [4, 5, 8, 7]
b_target = 13
print(closest_sum_pair(b1, b2, b_target)) #should return (4,8), (7, 7), (7, 5), or (10, 4).

c1 = [6, 8, -1, -8, -3]
c2 = [4, -6, 2, 9, -3]
c_target = 3
print(closest_sum_pair(c1, c2, c_target)) #should return (-1, 4) or (6, -3).

d1 = [19, 14, 6, 11, -16, 14, -16, -9, 16, 13]
d2 = [13, 9, -15, -2, -18, 16, 17, 2, -11, -7]
d_target = -15
print(closest_sum_pair(d1, d2, d_target)) #should return (-16, 2) or (-9, -7).



