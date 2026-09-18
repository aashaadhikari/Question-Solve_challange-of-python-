"""
Given an integer array arr[], return the sum of all elements of arr.

Examples:

Input: arr[] = [1, 2, 3, 4]
Output: 10
Explanation: 1 + 2 + 3 + 4 = 10.
Input: arr[] = [1, 3, 3]
Output: 7
Explanation: 1 + 3 + 3 = 7.
"""
arr= [1,2,3,4]
sum = 0
for i in arr:
    if arr == 0:
        continue
      
    else:
        sum += i
print(sum)
