"""
Given a string s. Your task is to remove the vowels from the string.

Examples:

Input: s = "welcome to geeksforgeeks"
Output: "wlcm t gksfrgks"
Explanation: Vowels were ignored only consonents were returned in the same order.
Input: s = "what is your name ?"
Output: wht s yr nm ?
"""
s = "welcome to geeksforgeeks"

val = "aeiouAEIOU"
new_sring = ""

for char in s:
    if char in val:
        continue
    else:
        new_sring += char

print(new_sring)

"""
Given a string s, remove all the spaces from the string and return the modified string.
"""

s = "g eeks for ge eks"

val = " " # this show about space.
new = ""

for char in s:
    if val in char:
        continue
    else:
        new += char
print(new)