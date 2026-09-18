"""
Given a string s, the task is to change the complete string to uppercase or lowercase depending on the case of the first character.

Examples:
Input: s = "abCD"
Output: "abcd"
Explanation: The first letter (a) is lowercase. Hence, the complete string is made lowercase.
Input: s = "Abcd"
Output: "ABCD"
Explanation: The first letter (A) is uppercase. Hence, the complete string is made uppercase.
"""

"""
/// simple and short

s = "abcd"
s1 = s.upper()
print(s1)

"""

"""
This code for uppercase
"""
alphabit = input("enter english alpha: ")

result = ""

for cher in alphabit:
    if 'a' <= cher <= 'z':
        result += chr(ord(cher)-32)
    else:
        result += cher 
print(result)



"""
This code for lowercase
"""
alphabit = input("enter english alpha: ")

result = ""

for cher in alphabit:
    if 'A' <= cher <= 'Z':
        result += chr(ord(cher)+32)
    else:
        result += cher 
print(result)