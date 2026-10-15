"""
Given two strings, s1 and s2. The task is to remove all characters that are common in both strings and then combine the remaining characters from each string to form a new string.

The characters that are not shared between the two strings should appear in the result in the same order as they appear in their respective original strings.
If no characters are left after removing the common characters, return "-1"
"""

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

result =" "

for char in s1:
    if char not in s2:
        result += char
for char in s2:
    if char not in s1:
        result += char

if result:
    print(result)
             
else:
    print("-1")