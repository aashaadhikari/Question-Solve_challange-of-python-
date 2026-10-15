"""
Given an positive integer n, print numbers from 1 to n without using loops.

Implement the function printTillN() to print the numbers from 1 to n as space-separated integers.

Examples

Input: n = 5
Output: 1 2 3 4 5
Explanation: We have to print numbers from 1 to 5.
"""
# class Solution:

def printTillN( n):
    if n == 0:
        return
    printTillN(n-1)
    print(n, end=" ")

printTillN(5)
print()

"""
You are given an array arr[], the task is to return a list elements of arr in alternate order (starting from index 0).

Examples:

Input: arr[] = [1, 2, 3, 4]
Output: 1 3
Explanation:
Take first element: 1
Skip second element: 2
Take third element: 3
Skip fourth element: 4
"""
arr = [1, 2, 3, 4]
output=[]

for i in range(len(arr)):
    if i % 2 == 0:
        output.append(arr[i])
    else:
        continue
print("this is my result ", output,)