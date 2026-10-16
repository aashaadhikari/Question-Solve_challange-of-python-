"""
Given an array arr[], find the elements whose value is equal to the position where they appear.

Note: There can be more than one element in the array which have the same value as its position. You need to include the position of every such element.

Examples:

Input: arr[] = [15, 2, 45, 4, 7]
Output: [2, 4]
Explanation: Here, arr[2] = 2 exists here and arr[4] = 4 exists.
Input: arr[] = [1]
Output: [1]
Explanation: Here arr[1] = 1 exists.
"""
arr = [15, 2, 45, 4, 7]

list = []

for i in range(len(arr)):
    index= i+1
    if index == arr[i]:
        list.append(index)
    else:
        continue

print(list)

