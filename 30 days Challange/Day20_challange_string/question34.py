"""
Given a binary string s, count the number of substrings that start and end with 1.
"""

s = "10101"
n = 5
count = 0

for i in range(n):
    if s[i] == '1':
        count += 1
            
print (count * (count-1) //2)



"""
Given a string s containing only lowercase English letters, convert all its characters to uppercase and return the resulting string.

Examples:

Input: s = "geeks"
Output: GEEKS
Explanation: All lowercase characters are converted to their corresponding uppercase characters.
Input: s = "geeksforgeeks"
Output: GEEKSFORGEEKS
Explanation: Each lowercase character in the string is converted to uppercase.

"""
s = "geeks"
# n = s.upper()
# print(n)

reslt = ""
for char in s:
    if 'a' <= char <= 'z': # # Subtract 32 from its ASCII value using ord() and chr()
        upper_case = chr(ord(char)-32) # Subtract 32 from its ASCII value using ord() and chr()
        reslt += upper_case
    else:
        reslt += char

print(reslt)