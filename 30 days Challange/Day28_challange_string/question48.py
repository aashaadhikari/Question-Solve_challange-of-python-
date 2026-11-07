""""
Given two strings s1 and s2, of equal lengths. The task is to check if s2 is a rotated version of the string s1.

Note: A string is a rotation of another if it can be formed by moving characters from the start to the end (or vice versa) without rearranging them.
"""

s1 = "abcd"
s2 = "cdab"
result = False

for i in range(len(s1)):
    if s1[i] == s2[0]:
        new_s1 = s1[i:] + s1[:i]
        if new_s1 == s2:
            result = True
        else:
            continue
    else:
        continue
print(result)


"""
Given two strings s1 and s2, remove every character from s1 that is present in s2. Return the resulting string. Both strings contain only lowercase English letters, and |s1| > |s2|.
"""

s1 = "computer"
s2 = "cat"

empy_string = ""

for char in s1:
    if char not in s2:
        empy_string += char
    else:
        continue
print(empy_string)
