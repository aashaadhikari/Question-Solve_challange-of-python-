"""
Given a string s, consisting of lowercase alphabets. Remove consecutive duplicate characters from the string. 

"""

# s = "aabb"

# empty_list = []

# for char in s:
    
#     if char not in empty_list:
#         empty_list.append(char)
    
# print(empty_list)


s = "aabb"

string_s =""

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        continue
    else:
        string_s += s[i]
string_s = string_s + s[-1]
print(string_s)