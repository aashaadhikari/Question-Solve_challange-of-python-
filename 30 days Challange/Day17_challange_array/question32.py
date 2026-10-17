"""
Given an unsorted array arr[]. Find the count of elements less than or equal to the given element x.

Examples:

Input: x = 9, arr[] = [10, 1, 2, 8, 4, 5] 
Output: 5
Explanation: The 5 elements are 1, 2, 8, 4 and 5.
Input: x = 2, arr[] = [1, 2, 2, 5, 7, 2, 9] 
Output: 4 
Explanation: The 4 elements are 1, 2, 2 and 2.
"""

arr = [10,1,2,8,4,5]
x = 9
count = 0
list = []

for i in range (len(arr)):
    if arr[i] < x:
        count += 1
        list.append(arr[i])
    else:
        continue
print(count)
print(list)

arr = [1,2,2,2,5,6,]
x = 5
count = 0
list = []

for char in arr:
    if char < x:
        count += 1
        list.append(char)
    else:
        continue
print(count)
print(list)