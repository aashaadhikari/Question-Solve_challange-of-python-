"""
Given two strings s1 and s2. You have to check that s1 is a subsequence of s2 or not.
Note: A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.

Examples:

Input: s1 = "AXY", s2 = "YADXCP"
Output: false
Explanation: s1 is not a subsequence of s2 as 'Y' appears before 'A'.
Input: s1 = "gksrek", s2 = "geeksforgeeks"
Output: true
Explanation: If we combine the bold character of "geeksforgeeks", it equals to s1. So s1 is a subsequence of s2. 
"""

s1 = "DCP"
s2 = "YADXCP"
count = 0
start = 0

for char in s1:
    if start < len(s2):
        for i in range(start, len(s2)):
            if s2[i] == char:
                count += 1
                start = i+1
                break
            else:
                continue
if count == len(s1):
    print(True)
else:
    print(False)


