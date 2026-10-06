"""
Given an array arr[] of lower case English characters as strings, merge all of them into a string. Note that the size of every string in the input array is 1 only.

Examples:

Input: arr[] = ["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s"]
Output: geeksforgeeks
Explanation: combined all the characters to form a single string.
Input: arr[] = ["e", "e", "b", "a"]
Output: eeba
Explanation: combined all the characters to form a single string. 
"""

arr = ["e", "e", "b", "a"]

result = "". join(arr)

print(result)