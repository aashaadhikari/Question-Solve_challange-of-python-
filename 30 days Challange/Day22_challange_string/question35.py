"""
Given a string s, check if it is a "Panagram" or not.  A "Panagram" is a sentence containing every letter in the English Alphabet either in lowercase or Uppercase.
"""

s = "Bawds jog, flick quartz, vex nymph"

new_s = s.lower()
print(new_s)

arr = [0] * 26

for char in new_s:
    if char.isalpha():
        arr[ord(char)-97] += 1

for no in arr:
    if no == 0:
      print(False)
    
    else:
       continue

print(True)


      

