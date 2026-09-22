"""
Given a string. Count the number of Camel Case characters in it.

Example 1:

Input:
S = "ckjkUUYII"
Output: 5
Explanation: Camel Case characters present:
U, U, Y, I and I.

"""


S = "ckjkUUYII"
camal = 0
for char in S:
    if ord(char) >= 65 and ord(char) <= 90:
        camal += 1
    else:
        continue

print(camal)
