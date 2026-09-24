"""
Given an array arr[]. The task is to find the largest element and return it.

Examples:

Input: arr[] = [1, 8, 7, 56, 90]
Output: 90
Explanation: The largest element of the given array is 90.
Input: arr[] = [5, 5, 5, 5]
Output: 5
Explanation: The largest element of the given array is 5.
Input: arr[] = [10]
Output: 10
Explanation: There is only one element which is the largest.
"""
arr = [1, 8, 4, 56, 90]
store = 0

for i in range(len(arr)):
    if arr[i] > store:
        store = arr[i]
    else:
        continue
print("largest value is: ", store)
        

arr = [1, 8, 4, 56, 90]

store = 0

for num in arr:
    if num > store:
        store = num
    else:
        continue
print("largest value is:", store)

arr = [5,5,5,5,5]

store = 0

for num in arr:
    if num > store:
        store = num
    else:
        continue
print("largest value is:", store)