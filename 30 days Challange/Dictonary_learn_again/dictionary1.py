"""
Use of dictionary in real time:
A Python dictionary stores data in key-value pairs for fast lookups, updates, and association of related information.

Fast Lookups: Finding a value by a unique key (like a database ID or word definition) in constant time O(1).Counting & Frequency: Counting occurrences of items (e.g., counting word frequencies in text).Configuration Settings: Storing application settings or user preferences by setting parameter names as keys.JSON/Data Representation: Representing structured records or objects.

"""
"""

CREATE DICTIONARY
"""

DIC = {"seema": 500, "shisir": 400,
       "nirjals": 600, "manisha": 299}

"""
UPDATE DICTIONARY
"""
# from loguru import logger
DIC = {"seema": 500, "shisir": 400,
       "nirjals": 600, "manisha": 299}
DIC["aasha"] = 509
DIC["kusum"] = 1000
DIC["knan"] = 503
# for name in DIC:
#     print(name, DIC[name])

for key, value in DIC.items():
    print(key, value)
    

# DIC.keys()
# print(DIC)