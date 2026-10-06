"""
Given a string s, convert the first letter of each word in the string to uppercase. 

Examples:

Input: s = "gEEKs"
Output: "GEEKs"

Input: s = "i love programming"
Output: "I Love Programming"
"""
s = "i love programming"
new_list = s.split()
print("This is new list after split",new_list)



for i in range(len(new_list)):
    word = new_list[i]
    word_up = word[0].upper()
    new_word = word_up[0] + word[1:]
    new_list[i]= new_word

x = " ".join(new_list)

print(new_list)