"""
You are given an array arr of positive integers. Your task is to find all the leaders in the array. An element is considered a leader if it is greater than or equal to all elements to its right. The rightmost element is always a leader.

"""

arr = [16, 17, 4, 3, 5, 2]

empty_list = []

max_right = 0

for i in range(len(arr) -1, -1, -1): # This loop moves from right to left.

    if arr[i] >= max_right:
        empty_list.append(arr[i])
        max_right = arr[i]

empty_list.reverse()
print(empty_list)
    




