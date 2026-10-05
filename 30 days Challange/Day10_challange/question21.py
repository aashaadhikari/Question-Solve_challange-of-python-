"""
Given a string s consisting of lowercase English Letters. return the first non-repeating character in s. If there is no non-repeating character, return '$'.

Examples:lowercase

Input: s = "geeksforgeeks"
Output: 'f'
Explanation: In the given string, 'f' is the first character in the string which does not repeat.
"""

s = "geeksforgeeks"

dic = {}

for char in s:
    if char in dic:
        dic[char] +=1
    else:
        dic[char]=1

for char in s:
    if dic[char] == 1:
        print(char)
        break
    else:
        print("$")