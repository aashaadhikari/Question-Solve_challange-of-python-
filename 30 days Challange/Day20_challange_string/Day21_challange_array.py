"""
ou are given an array arr[] of size n - 1 that contains distinct integers in the range from 1 to n (inclusive).
This array represents a permutation of the integers from 1 to n with one element missing. 
Your task is to identify and return the missing element.
"""

"""
arr = [1,2,3,4,6]
miss = []

for i in range(len(arr)+1):
    if i+1 in arr:
        continue
    else:
        miss.append(i)
print(miss)

"""


"""
which is not shorted
"""
arr = [1,2,6,5,7,8,3]
sum = 0
for i in range(len(arr)):
    sum = sum + arr[i]

n = len(arr)+1

exact_sum = (n*(n+1))//2
res = exact_sum - sum

print(res)




"""
Given a sorted array arr[] of distinct integers and an integer k, return the 0-based index of k if it is present in the array. Otherwise, return -1.
"""

arr = [1,2,3,4,5,6]

k = 7

for i in arr:
    if k in arr:
        print(True)
    else:
        print(False)