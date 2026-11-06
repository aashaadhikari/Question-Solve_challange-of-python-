"""
You are given an array, arr[]. Find the minimum index based distance between two different elements of the array, x and y. Return -1, if either x or y does not exist in the array.
"""

arr =[1,2,3,2]

x= 1
y = 2

X_index = -1
y_index = -1

ans = float('inf')

for i in range(len(arr)):
    if x == arr[i]:
        X_index = i
    elif y == arr[i]:
        y_index = i
    else:
        continue

    if X_index!=-1 and y_index!= -1:

        ans =min(ans, abs(X_index - y_index))

if ans == float('inf'):
    print(-1)
else:
    print(ans)



