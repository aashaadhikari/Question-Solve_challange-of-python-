"""
Given an array of arr[] positive integers where all numbers occur even number of times except one number which occurs odd number of times. Return that number.

Examples:

Input:arr[] = [1, 2, 3, 2, 3, 1, 3]
Output: 3
Explanation: 3 occurs three times.
Input:arr[] = [5, 7, 2, 7, 5, 2, 5]
Output: 5
Explanation: 5 occurs three times.
"""
arr =[5, 7, 2, 7, 5, 2, 5]

dic = {}

for i in range(0,len(arr)):
    if arr[i] in dic:
        dic[arr[i]] += 1
    else:
        dic[arr[i]] = 1 
for key,value in dic.items():
    if value % 2 == 0:
        continue
    else:
        print(key,"is even number type repated")
