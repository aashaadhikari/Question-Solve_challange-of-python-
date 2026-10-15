"""
Given two strings txt and pat, return the 0-based index of the first occurrence of the substring pat in txt. If pat is not found, return -1.

Examples :

Input: txt = "GeeksForGeeks", pat = "Fr"
Output: -1
Explanation: "Fr" is not present in the string "GeeksForGeeks" as substring.
Input: txt = "GeeksForGeeks", pat = "For"
Output: 5
Explanation: "For" is present as substring in "GeeksForGeeks" from index 5 (0 based indexing).
Input: txt = "GeeksForGeeks", pat = "gr"
Output: -1
Explanation: "gr" is not present in the string "GeeksForGeeks" as substring.
"""

# txt = "GeeksForGeeks"
# pat = "Fo"


# for i in range(len(txt)):
#     val2 = txt[i]
#     val = pat[0]
#     if pat[0] == val2:
#         search = txt[i:i+len(pat)]
#         if search == pat:
#             print(i)
#     else:
#         continue 


"""
Given a string s, the task is to create a string with the first letter of every word in the string. The string s contains lower case English alphabets and its words have a single space between them. 

Examples:

Input: s = "geeks for geeks"
Output: gfg
Explanation: 
First word starts at index 0, take 'g' 
After first space, next word starts with 'f'
After second space, next word starts with 'g'
Input: s = "bad is good"
Output: big
"""

s = "bad is good"

txt = s.split(" ")

# index = txt.index("bad")
# print(index)

for i in range(len(txt)):
    word = txt[i]
    word_sel = word[0]
    new_word = word_sel[0]
    print(new_word, end="")

