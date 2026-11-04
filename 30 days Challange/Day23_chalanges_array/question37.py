"""
Given an integer array arr, return all the unique pairs [arr[i], arr[j]] such that i != j and arr[i] + arr[j] == 0.

Note: The pairs must be returned in sorted order, the solution array should also be sorted, and the answer must not contain any duplicate pairs.

Examples:
"""

# arr = [-1, 6, 0, 1, 2, -1, -4, -6]

# arr.sort()
# empty_list = []

# i = 0
# j = len(arr)-1

# while(i<j):
#     total = arr[i] + arr[j]
#     if total == 0:
#         pair = [arr[i], arr[j]]
        
#         if pair not in empty_list:
#             empty_list.append(pair)
#         i+=1
#         j-=1

#     elif total < 0:
#         i+=1

#     else:
#         j-=1
# print(empty_list)


"""
Given an array arr[] of size n, containing elements from the range 1 to n, and each element appears at most twice, return an array of all the integers that appears twice.

Note: You can return the elements in any order but the driver code will print them in sorted order.
"""

arr = [2,3,1,2,3]

dic = {}
list = []

for char in arr:
    if char in dic:
        dic[char] += 1
    else:
        dic[char] = 1
print(dic)



for key, value in dic.items():
    
    if value == 2:
        list.append(key)
print(list) 

    