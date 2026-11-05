"""
Given two non-empty strings s1 and s2, consisting only of lowercase English letters, determine whether they are anagrams of each other or not.
Two strings are considered anagrams if they contain the same characters with exactly the same frequencies, regardless of their order.


"""
s1 = "geeks" 
s2 = "kseega"

# s3 = ""
# for char in s1:
#     if char in s2:
#         s3 += 
#     else:
#         break
# # if s3 == s1 and len(s1) == len(s3):
# #     print(True)
# # else:
# #     print(False)
# print(s3)

# We create two separate lists because we want to count the characters in both strings.
s1_arr = [0]*26
s2_arr = [0]*26

#What is ord()?

# Python's ord() converts a character into its numerical Unicode value.
for char in s1:
    s1_arr[ord(char)-97]+= 1
for char in s2:
    s2_arr[ord(char)-97]+= 1

if s1_arr == s2_arr:
    print(True)

else:
    print(False)
