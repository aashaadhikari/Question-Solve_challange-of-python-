"""
Given an array arr[] of positive integers. The task is to return the count of the number of odd and even elements in the array.

Note: Return two elements where the first one in the count of odd & second one is the count of even.
"""
array = [1,2,3,4,5,6,7,8,9]

even_count = 0
odd_count = 0

for i in range(len(array)):
    if i % 2 == 0:
        even_count += 1

    else:
        odd_count += 1
print("Total even number in list ",even_count)
print("Total odd number in list",odd_count)