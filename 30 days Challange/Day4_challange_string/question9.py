"""
Given a string s, count the occurrence of the following in it.

Lowercase characters
Uppercase characters
Special characters
Numeric Values
Note: There are no white spaces in the string.

Examples:

Input: s = "#GeeKs01fOr@gEEks07"
Output: [5, 8, 4, 2]
Explanation: There are 5 uppercase characters, 8 lowercase characters, 4 numeric characters and 2 special characters.
Input: s = "*GeEkS4GeEkS*"
Output: [6, 4, 1, 2]
Explanation: There are 6 uppercase characters, 4 lowercase characters, 1 numeric character and 2 special characters.
"""
# using ascii

s = "GeeKs01fOr@gEEks07"
lowercass = 0
uppercass = 0
numeric = 0
special = 0
for char in s:
    if ord(char) >= 65 and ord(char) <= 90:
        uppercass += 1
    elif ord(char) >= 97 and ord(char) <= 122:
        lowercass += 1
    elif ord(char) >= 48 and ord(char) <= 57:
        numeric += 1
    else:
          special += 1

print( lowercass, uppercass, numeric, special)