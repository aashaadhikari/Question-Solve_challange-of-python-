"""
Given an unsorted array arr[] of size n, containing elements from the range 1 to n, it is known that one number in this range is missing, and another number occurs twice in the array, find the both numbers.
"""

# arr =  [4, 3, 6, 2, 1, 1]
# arr.sort()

# dic = {}
# empty_list = set()

# for char in arr:
#     if char in dic:
#         dic[char] += 1
#     else:
#         dic[char] = 1

# print(dic)

# for i in range(len(arr)):
#     if arr[i] in empty_list:
#         repeting = arr[i]
#     else:
#         empty_list.add(arr[i])
# actual_sum = sum(arr)
# total_sum = len(arr) *(len(arr)+1)// 2
# missing = total_sum -(actual_sum - repeting)
# print(missing, repeting)





arr =  [4, 3, 6, 2, 1, 1]
arr.sort()

dic = {}
empty_list = []

for char in arr:
    if char in dic:
        dic[char] += 1
    else:
        dic[char] = 1

# print(dic)

for keys, value in dic.items():
    if value > 1:
        empty_list.append(keys)
   
for i in range(1, len(arr) +1):
    if i not in dic:
        empty_list.append(i)


print(empty_list)