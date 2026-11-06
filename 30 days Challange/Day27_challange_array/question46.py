"""
Given an array arr[] of integers and another integer target. Determine if there exist two distinct indices such that the sum of their elements is equal to the target.
"""

arr = [0, -1, 2, -3, 1]

target = -0
result = False

for i in range(len(arr)-1):
    if arr[i] + arr[i+1] == target:
        result = True
        break
print(result)
