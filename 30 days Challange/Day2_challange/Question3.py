"""
you are given an integer n. You need to convert all zeros of n to 5.

Iterating : to repeat a process or action
 in string we can do
"""

n = str(input("Enter the number: "))
result=''
for cher in n:
    if cher == '0':
        result += '5'

    else:
        result += cher
        
print (result)

"""
tala ko program mistake xa
"""

"""
str = "12345"
for i in range(len(n)): [0,2,3,4,5]
if i == 0: this is wrong
if str[i] == 0
    replace with 5
"""
"""
How to convert string into list
"""
num = 100004
num2 = str(num)
num_split = num2.split()
print(num_split)
results = ''
for i in range(len(num_split)):
    if num_split[i] == '0':
        results += '5'
    else:
        results += num_split[i]
print(results)

