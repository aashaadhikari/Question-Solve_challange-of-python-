"""
Given an array arr[]. Your task is to find the minimum and maximum elements in the array.

Examples:

Input: arr[] = [1, 4, 3, 5, 8, 6]
Output: [1, 8]
Explanation: minimum and maximum elements of array are 1 and 8.
"""

arr = [1,4,3,5,8,6]
# class solution:
#     def minMax(self, arr):

max_arr = arr[0]
min_arr = arr[0] 

for num in arr[1:]:
    if num < min_arr:
        min_arr = num
    elif num > max_arr:
        max_arr =num

print(max_arr)
print(min_arr)

"""
USING funcation
"""
def find_min_max(arr):
    if not arr:
        return None, None

    max_arr = arr[0]
    min_arr = arr[0] 

    for num in arr[1:]:
        if num < min_arr:
            min_arr = num
        elif num > max_arr:
            max_arr =num
    return max_arr,min_arr

arr = [12,3,5,6,1,87]
minimum, maximum = find_min_max(arr)

print(f"Minimum Value: {minimum}")  
print(f"Maximum Value: {maximum}")  
