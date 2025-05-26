#Hashsets

s = set()
print(s)

#add item into set - O(1)
s.add(1)
s.add(2)
s.add(3)
print(s)

#Lookup if item in set - O(1)
if 1 in s:
    print(True)

#Remove item from set - O(1)
s.remove(3)
print(s)

string = "aaaaabbbbbccccceeee"
sett = set(string) #Set constructuion - O(S) - S is the length of the string

#Loop over items in set - O(n)
for x in s:
    print(x)

#Hashmaps - Dictionaries

d = {"greg":1, "steve":3, "rob":4}
print(d)

#add key:vall in dictionary - O(1)
d["arsh"]=4

print(d)

#Check for presence of key in dicitonary - O(1)
if 'greg' in d:
    print(True)

##Check the value corresponding to key in dict - O(1)
print(d['greg'])

#Loop over key:val pairs of dict - O(n)
for key, val in d.items():
    print(f'key {key}: val{val}')

#Defaultditc
from collections import defaultdict

default = defaultdict(int)

default[2]

#Counter
from collections import Counter

counter = Counter(string)
print(counter)