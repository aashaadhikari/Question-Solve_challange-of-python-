"""
Given two strings s1 and s2, merge them alternatively i.e. the first character of s1 then the first character of s2 and so on till the strings end.
"""
s1 = "abc"
s2 = "defrtg"

empty_string = ""

for i in range(max(len(s1), len(s2))):
    if i < len(s1):
        empty_string+= s1[i]

    if i < len(s2):
        empty_string+= s2[i]
    




print(empty_string)

