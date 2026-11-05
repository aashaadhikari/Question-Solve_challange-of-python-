"""
Given a string consisting of lowercase English alphabets, reverse only the vowels present in it and print the resulting string.

"""
s = "practice"

vow = "aeiou"

i = 0
j =len(s)-1

s = list(s)

while(i < j):
    if s[i] not in vow:
        i+=1
    elif s[j] not in vow:
        j-=1
    else:
        s[i], s[j] = s[j], s[i]

        i+=1
        j-=1
result = "".join(s)

print(result)
