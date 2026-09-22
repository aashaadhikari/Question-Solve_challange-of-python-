"""
use built in functoin to find upper, lower, numeric, and special
"""
S = "$dhjhGYJND%67?"
uppercass = 0
lower  = 0
numeric = 0
special = 0
for char in S:
    if char.isupper():
        uppercass+= 1
    elif char.islower():
        lower += 1
    elif char.isdigit():
        numeric += 1
    else:
        special += 1

print(uppercass, lower, numeric, special)