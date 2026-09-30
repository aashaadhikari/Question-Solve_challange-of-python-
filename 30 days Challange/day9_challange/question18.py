"""
Given an array arr[], the task is to find whether the arr is palindrome or not.  An array is said to be palindrome if its reverse array matches the original array. 

Input: arr = [1, 2, 3, 2, 1]
Output: true
Explanation: If we reverse, we get [1, 2, 3, 2, 1] which is the same as before. So, the answer is true.
"""

"""

THIS IS SIMPLE AND USUALLY DONE PROGRAMM.
arr = [1, 2, 3, 2, 1]

start = len(arr) - 1
end = -1
step = -1

result = []

for i in range(start, end, step):
  result.append(arr[i])

  if result == arr:
    print ("This array is palindrome")

print(result)

"""
"""
TWO POINT METHODS TO SOLVE SAME PROBLEM.
"""
import copy
arr = [1, 2, 3, 2, 5]

i =0
j= len(arr) -1

arr1 = copy.deepcopy(arr)

while(i < j):
    arr1[i], arr1[j] = arr1[j], arr1[i]
    i+=1
    j-=1

if arr1 == arr:
    print( True)

else:
    print(False)



