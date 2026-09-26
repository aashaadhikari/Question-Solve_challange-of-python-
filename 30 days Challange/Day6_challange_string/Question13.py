"""
Given a string s of lowercase alphabets, check if it is Isogram or not.  An Isogram is a string in which no letter occurs more than once.

Examples:

Input: s = "machine"
Output: true
Explanation: "machine" is an Isogram as no letter has appeared twice. so we return true.
Input: s = "geeks"
Output: false
Explanation: "geeks" is not an Isogram as 'e' appears twice. so we return false.
"""
"""

string_input = input(" Enter the name of you want to give: ")

result = {}
for char in string_input:
    if char in result:
        print(0)
        break
    else:
        result[char] = 1
else:
    print (1)
"""


"""

string_input = input(" Enter the name of you want to give: ")

for i in range(len(string_input)):
    val = string_input[i]
    for j in range(i+1, len(string_input)):
        val2 = string_input[j] 
        if val == val2:
            return 0
        else:
            continue
"""
string_input = input("Enter the word: ")

result = {}

for char in string_input:
    if char in result:
        print(0)
        break
    else:
        result[char] = 1
else:
    print(1)