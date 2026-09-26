"""
Given a string s as input. Delete the characters at odd indices of the string. Return the final string after deletion of characters at odd indices.

Examples :

Input: s = "Geeks"
Output: "Ges" 
Explanation: Deleted "e" at index 1 and "k" at index 3.
Input: s = "GeeksforGeeks"
Output: "GesoGes"
Explanation: Deleted e, k, f, r, e, k at index 1, 3, 5, 7, 9, 11.
"""
s = "geeks"
odd_count = ""

for i in range(len(s)):
    if i % 2 == 0:
         odd_count += s[i]
    
print(odd_count)


