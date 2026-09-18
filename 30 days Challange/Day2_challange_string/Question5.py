"""
You are given two strings s1 and s2 and your task is to concatenate both in s1 and print the final string.

Note: You may assume s1 will always have extra spaces to concatenate s2.

Examples:

Input: s1 = "Hello", s2 = "World"
Output: HelloWorld
Input: s1 = "abc", s2 = "def"
Output: abcdef
"""
s1 = str(input("Enter the first word: "))
s2 = str(input("Enter the second word: "))

result =s1+ " " + s2
print(result)

