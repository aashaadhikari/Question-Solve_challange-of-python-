"""
Given a string s consisting of lowercase English letters, find the first character that repeats in the string.

Note: If the string contains no repeating characters, return '#'.

Examples :

Input: s = "geeksforgeeks"
Output: g
Explanation: g, e, k and s are the repeating characters. Out of these, g occurs first. 
Input: s = "abcde"
Output: '#'
Explanation: No repeating character present, so return '#'

"""
s = "geeksforgeeks"
dic = {}

for char in s:
    if char in dic:
        dic[char] +=1
    else:
        dic[char]=1


for key, value in dic.items():
    if value > 1:
        print (key)
    else:
        continue

print("#")


