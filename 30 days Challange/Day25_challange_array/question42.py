"""
Given an array arr[] of size n that contains integers. Print the elements of the array in a single line with a space between them.

Note: Don't add a new line at the end.
"""

arr = [54, 43, 2, 1, 5]

for num in arr:
    print(num, end=" ")



print(" ".join(map(str, arr)), end="")

print(*arr, end="")

# *arr unpacks the array and prints elements separated by spaces.
# end="" prevents print() from adding a new line at the end.