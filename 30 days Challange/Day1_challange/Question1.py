
"""
You are given an array arr[]. the task is to return a list element of arr in alternate order (starting from index 0.)
"""
arry = [1,2,3,4,5,6]
output = []

for i in range (len(arry)):
    if i % 2 == 0:
        output.append(arry[i])
    else:
        continue
print("This is my first day code")
print(output)