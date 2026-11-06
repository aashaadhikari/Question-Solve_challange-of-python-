"""

You are given two strings s1 and s2. Your task is to identify the characters that appear in either string but not in both (i.e., characters that are unique to one of the strings). Return the result as a sorted string.
"""

s1 = "geeksforgeeks"
s2 = "geeksquiz"

store_string = ""

for char in s1:
    if char not in s2 and char not in store_string:
        store_string += char
for char1 in s2:
    if char1 not in s1 and char not in store_string:
        store_string += char1
store_string = "".join(sorted(store_string))
print(store_string)



"""
Given a string s of lowercase alphabets. The task is to find the maximum occurring character in the string s. If more than one character occurs the maximum number of times then print the lexicographically smaller character.
"""


s = "testsample"

s_dis = {}  # Empty dictionary

for char in s:
    if char in s_dis:
        s_dis[char] += 1
    else:
        s_dis[char] = 1

print(s_dis)

max_char = ""
max_count = 0

for key, value in s_dis.items():
    if value > max_count:
        max_count = value
        max_char = key

    elif value == max_count and key < max_char:
        max_char = key
print(max_char)
# e come first so output is e 